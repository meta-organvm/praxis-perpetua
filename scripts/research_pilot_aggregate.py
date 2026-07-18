"""Deterministic evaluation for the four-run Perplexity research pilot."""

from __future__ import annotations

import hashlib
import json
import math
import re
from datetime import datetime
from pathlib import Path, PurePosixPath
from typing import Any, Mapping

import yaml
from jsonschema import Draft202012Validator, FormatChecker


PILOT_COMMISSION_ID = "INQ-2026-014"
PILOT_REQUEST_IDS = {
    "SGO-REQ-2026-PPLX-PILOT-01",
    "SGO-REQ-2026-PPLX-PILOT-02",
    "SGO-REQ-2026-PPLX-PILOT-03",
    "SGO-REQ-2026-PPLX-PILOT-04",
}
PILOT_STATES = {"continue", "switch", "wait_relay", "settled", "invalid"}
PILOT_VERDICTS = {"pass", "fail"}
_HEADING = re.compile(r"^#{1,6}\s+(.+?)\s*#*\s*$")
_HASH = re.compile(r"^sha256:[0-9a-f]{64}$")
_PLACEHOLDER_BODY = {"", "n/a", "none", "pending", "tbd"}


class PilotAggregateError(ValueError):
    """Raised when pilot owner inputs cannot support a trustworthy evaluation."""

    def __init__(self, code: str, message: str) -> None:
        super().__init__(f"{code}: {message}")
        self.code = code
        self.message = message


def canonical_json(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def canonical_hash(value: object) -> str:
    digest = hashlib.sha256(canonical_json(value).encode("utf-8")).hexdigest()
    return f"sha256:{digest}"


def raw_text_hash(value: str) -> str:
    digest = hashlib.sha256(value.encode("utf-8")).hexdigest()
    return f"sha256:{digest}"


def load_yaml(path: Path) -> dict[str, Any]:
    try:
        value = yaml.safe_load(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, yaml.YAMLError) as error:
        raise PilotAggregateError(
            "input.yaml", f"cannot read {path}: {error}"
        ) from error
    if not isinstance(value, dict):
        raise PilotAggregateError("input.yaml", f"{path} is not a YAML object")
    return value


def load_json(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as error:
        raise PilotAggregateError(
            "receipt.json", f"cannot read {path}: {error}"
        ) from error
    if not isinstance(value, dict):
        raise PilotAggregateError("receipt.json", f"{path} is not a JSON object")
    return value


def parse_owner_roots(values: list[str]) -> dict[str, Path]:
    roots: dict[str, Path] = {}
    for value in values:
        owner, separator, raw_path = value.partition("=")
        owner = owner.strip()
        if not separator or not owner or not raw_path:
            raise PilotAggregateError(
                "owner_root.syntax",
                f"expected OWNER_REPO=/absolute/path, got {value!r}",
            )
        if owner in roots:
            raise PilotAggregateError(
                "owner_root.duplicate", f"duplicate owner root {owner}"
            )
        path = Path(raw_path).expanduser()
        if not path.is_absolute():
            raise PilotAggregateError(
                "owner_root.relative",
                f"owner root for {owner} is not absolute",
            )
        roots[owner] = path.resolve()
    return roots


def _safe_owner_path(root: Path, relative: object, *, field_name: str) -> Path:
    if not isinstance(relative, str) or not relative:
        raise PilotAggregateError("owner_path.type", f"{field_name} is not a path")
    path = PurePosixPath(relative)
    if path.is_absolute() or ".." in path.parts or "." in path.parts:
        raise PilotAggregateError(
            "owner_path.unsafe", f"{field_name} is not owner-relative"
        )
    resolved_root = root.resolve()
    resolved = (resolved_root / Path(*path.parts)).resolve()
    try:
        resolved.relative_to(resolved_root)
    except ValueError as error:
        raise PilotAggregateError(
            "owner_path.escape",
            f"{field_name} escapes its owner root",
        ) from error
    return resolved


def _pilot_requests(praxis_root: Path) -> list[dict[str, Any]]:
    request_dir = (
        praxis_root
        / "commissions"
        / "2026-07-17-perplexity-research-pilot"
        / "requests"
    )
    requests = [load_yaml(path) for path in sorted(request_dir.glob("*.yaml"))]
    request_ids = {request.get("request_id") for request in requests}
    if request_ids != PILOT_REQUEST_IDS or len(requests) != len(PILOT_REQUEST_IDS):
        raise PilotAggregateError(
            "request.set",
            "pilot requests do not cover the canonical four request IDs",
        )
    return sorted(requests, key=lambda request: str(request["request_id"]))


def _receipt_validator(praxis_root: Path) -> Draft202012Validator:
    schema = load_json(praxis_root / "schemas" / "research-receipt.schema.json")
    Draft202012Validator.check_schema(schema)
    return Draft202012Validator(schema, format_checker=FormatChecker())


def _validate_receipt_schema(
    receipt: dict[str, Any],
    validator: Draft202012Validator,
    *,
    request_id: str,
) -> None:
    errors = sorted(
        validator.iter_errors(receipt),
        key=lambda error: tuple(str(part) for part in error.absolute_path),
    )
    if errors:
        error = errors[0]
        location = ".".join(str(part) for part in error.absolute_path) or "<root>"
        raise PilotAggregateError(
            "receipt.schema",
            f"{request_id} {location}: {error.message}",
        )


def _heading_key(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", value.strip().lower()).strip("_")


def _markdown_sections(report: str) -> dict[str, str]:
    sections: dict[str, list[str]] = {}
    current: str | None = None
    for line in report.splitlines():
        match = _HEADING.fullmatch(line.strip())
        if match:
            current = _heading_key(match.group(1))
            sections.setdefault(current, [])
        elif current is not None:
            sections[current].append(line)
    return {key: "\n".join(lines).strip() for key, lines in sections.items()}


def _validate_report(
    request: dict[str, Any],
    report: str,
    *,
    disposition: str,
) -> bool:
    if not report.strip():
        raise PilotAggregateError(
            "report.empty",
            f"{request['request_id']} report is empty",
        )
    if request["question"].strip() in report:
        raise PilotAggregateError(
            "report.prompt_body",
            f"{request['request_id']} report contains the private request question",
        )
    if disposition == "rejected":
        return False
    sections = _markdown_sections(report)
    for required in request["output_contract"]["required_sections"]:
        key = _heading_key(str(required))
        if key not in sections:
            raise PilotAggregateError(
                "report.section",
                f"{request['request_id']} report lacks section {required}",
            )
        if sections[key].strip().lower() in _PLACEHOLDER_BODY:
            raise PilotAggregateError(
                "report.section_empty",
                f"{request['request_id']} report section {required} is empty",
            )
    novelty = sections.get("novel_actionable_findings", "")
    return novelty.strip().lower() not in _PLACEHOLDER_BODY


def _validate_receipt_semantics(
    request: dict[str, Any],
    receipt: dict[str, Any],
    registry: dict[str, Any],
) -> str:
    request_id = str(request["request_id"])
    expected_output = request["output_contract"]
    if receipt["request_id"] != request_id:
        raise PilotAggregateError(
            "receipt.request_id",
            f"{request_id} receipt identifies {receipt['request_id']}",
        )
    if receipt["request_hash"] != canonical_hash(request):
        raise PilotAggregateError(
            "receipt.request_hash",
            f"{request_id} receipt does not bind the canonical request",
        )
    if receipt["catalog_hash"] != canonical_hash(registry):
        raise PilotAggregateError(
            "receipt.catalog_hash",
            f"{request_id} receipt does not bind the canonical catalog",
        )
    if receipt["selected_profile"] != "pro_research":
        raise PilotAggregateError(
            "receipt.profile",
            f"{request_id} did not use the attended pilot profile",
        )
    for field in ("owner_repo", "report_path", "receipt_path", "raw_export_ref"):
        if receipt["durable_output"].get(field) != expected_output.get(field):
            raise PilotAggregateError(
                "receipt.custody",
                f"{request_id} durable {field} diverges from its request",
            )
    privacy = receipt["privacy"]
    if privacy["preservation_tier"] != request["preservation_tier"]:
        raise PilotAggregateError(
            "receipt.preservation",
            f"{request_id} preservation tier diverges",
        )
    if privacy["external_transmission"] != request["external_transmission"]:
        raise PilotAggregateError(
            "receipt.transmission",
            f"{request_id} transmission authority diverges",
        )
    if privacy["tracked_output_safe"] is not True:
        raise PilotAggregateError(
            "receipt.tracked_output",
            f"{request_id} terminal tracked output is not marked safe",
        )
    if any(receipt["sanitization"].values()):
        raise PilotAggregateError(
            "receipt.sanitization",
            f"{request_id} terminal tracked output contains prohibited material",
        )

    verification = receipt["verification"]
    material = verification["material_claims"]
    supported = verification["supported_material_claims"]
    resolvable = verification["resolvable_citations"]
    citations = verification["total_citations"]
    primary = verification["primary_source_citations"]
    ratio = primary / citations if citations else 0.0
    if supported > material or resolvable > citations or primary > citations:
        raise PilotAggregateError(
            "receipt.counts",
            f"{request_id} verification counts are internally inconsistent",
        )
    if not math.isclose(
        verification["primary_source_ratio"],
        ratio,
        rel_tol=0,
        abs_tol=1e-9,
    ):
        raise PilotAggregateError(
            "receipt.primary_ratio",
            f"{request_id} primary-source ratio does not match its counts",
        )

    status = verification["status"]
    if status == "accepted":
        if receipt["outcome_type"] != "EvidencePacket":
            raise PilotAggregateError(
                "receipt.outcome",
                f"{request_id} accepted receipt is not an EvidencePacket",
            )
        if supported != material or resolvable != citations:
            raise PilotAggregateError(
                "receipt.accepted_evidence",
                f"{request_id} accepted receipt has unsupported claims or broken citations",
            )
        if material > 0 and citations == 0:
            raise PilotAggregateError(
                "receipt.accepted_evidence",
                f"{request_id} accepted material claims have no citations",
            )
        return "accepted"
    if status == "rejected":
        if receipt["outcome_type"] != "BlockedReceipt":
            raise PilotAggregateError(
                "receipt.outcome",
                f"{request_id} rejected receipt is not a BlockedReceipt",
            )
        if not verification.get("rejection_reasons"):
            raise PilotAggregateError(
                "receipt.rejection_reasons",
                f"{request_id} rejected receipt lacks a reason",
            )
        return "rejected"
    raise PilotAggregateError(
        "receipt.terminal_status",
        f"{request_id} owner receipt remains {status}",
    )


def _criterion(
    required: object, observed: object, passed: bool | None
) -> dict[str, Any]:
    return {"required": required, "observed": observed, "passed": passed}


def evaluate_pilot(
    praxis_root: Path,
    owner_roots: Mapping[str, Path],
) -> dict[str, Any]:
    """Evaluate live owner outputs without embedding local paths in the result."""

    praxis_root = praxis_root.resolve()
    requests = _pilot_requests(praxis_root)
    registry = load_yaml(praxis_root / "governance" / "research-backend-profiles.yaml")
    validator = _receipt_validator(praxis_root)
    required_owners = {
        str(request["output_contract"]["owner_repo"]) for request in requests
    }
    missing_roots = sorted(required_owners - set(owner_roots))
    if missing_roots:
        raise PilotAggregateError(
            "owner_root.missing",
            f"no explicit roots for {', '.join(missing_roots)}",
        )
    for owner in sorted(required_owners):
        root = Path(owner_roots[owner])
        if not root.is_absolute() or not root.is_dir():
            raise PilotAggregateError(
                "owner_root.unavailable",
                f"owner root for {owner} is not an available absolute directory",
            )

    runs: list[dict[str, Any]] = []
    missing_inputs: list[dict[str, str]] = []
    verified_times: list[str] = []
    for request in requests:
        request_id = str(request["request_id"])
        output = request["output_contract"]
        owner = str(output["owner_repo"])
        owner_root = Path(owner_roots[owner])
        report_path = _safe_owner_path(
            owner_root,
            output["report_path"],
            field_name=f"{request_id}.report_path",
        )
        receipt_path = _safe_owner_path(
            owner_root,
            output["receipt_path"],
            field_name=f"{request_id}.receipt_path",
        )
        missing = []
        for kind, path, reference in (
            ("report", report_path, str(output["report_path"])),
            ("receipt", receipt_path, str(output["receipt_path"])),
        ):
            if not path.is_file():
                missing.append(kind)
                missing_inputs.append(
                    {
                        "request_id": request_id,
                        "owner_repo": owner,
                        "kind": kind,
                        "path": reference,
                    }
                )
        if missing:
            runs.append(
                {
                    "request_id": request_id,
                    "owner_repo": owner,
                    "report_path": str(output["report_path"]),
                    "receipt_path": str(output["receipt_path"]),
                    "disposition": "missing",
                    "missing": missing,
                }
            )
            continue

        receipt = load_json(receipt_path)
        _validate_receipt_schema(receipt, validator, request_id=request_id)
        disposition = _validate_receipt_semantics(request, receipt, registry)
        try:
            report = report_path.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as error:
            raise PilotAggregateError(
                "report.read",
                f"cannot read {request_id} report: {error}",
            ) from error
        novel_finding = _validate_report(
            request,
            report,
            disposition=disposition,
        )
        verification = receipt["verification"]
        usage = receipt["usage"]
        verified_times.append(str(verification["verified_at"]))
        runs.append(
            {
                "request_id": request_id,
                "owner_repo": owner,
                "report_path": str(output["report_path"]),
                "receipt_path": str(output["receipt_path"]),
                "disposition": disposition,
                "report_hash": raw_text_hash(report),
                "receipt_hash": canonical_hash(receipt),
                "source_manifest_hash": receipt["source_manifest_hash"],
                "material_claims": verification["material_claims"],
                "supported_material_claims": verification["supported_material_claims"],
                "resolvable_citations": verification["resolvable_citations"],
                "total_citations": verification["total_citations"],
                "primary_source_citations": verification["primary_source_citations"],
                "novel_actionable_finding": novel_finding,
                "operator_handling_seconds": usage["operator_handling_seconds"],
                "variable_cost_usd": usage["variable_cost"],
                "verified_at": verification["verified_at"],
            }
        )

    catalog_hash = canonical_hash(registry)
    requests_hash = canonical_hash(requests)
    if missing_inputs:
        criteria = {
            "accepted_packets": _criterion(3, None, None),
            "material_claim_citation_resolution": _criterion(1.0, None, None),
            "primary_source_citation_ratio": _criterion(0.8, None, None),
            "durable_owner_outputs": _criterion(
                4,
                4 - len({item["request_id"] for item in missing_inputs}),
                None,
            ),
            "novel_actionable_findings": _criterion(True, None, None),
            "operator_handling_seconds_per_run": _criterion(1200, None, None),
            "variable_perplexity_spend_usd": _criterion(0, None, None),
        }
        result = {
            "schema_version": "1.0",
            "commission_id": PILOT_COMMISSION_ID,
            "state": "wait_relay",
            "verdict": None,
            "evaluated_at": None,
            "catalog_hash": catalog_hash,
            "requests_hash": requests_hash,
            "runs": runs,
            "missing_inputs": missing_inputs,
            "criteria": criteria,
        }
        validate_aggregate_record(result)
        return result

    accepted = [run for run in runs if run["disposition"] == "accepted"]
    total_citations = sum(run["total_citations"] for run in accepted)
    primary_citations = sum(run["primary_source_citations"] for run in accepted)
    primary_ratio = primary_citations / total_citations if total_citations else 0.0
    claim_resolution = 1.0 if accepted else 0.0
    accepted_count_passed = len(accepted) >= 3
    claim_resolution_passed = claim_resolution == 1.0
    primary_ratio_passed = primary_ratio >= 0.8
    durable_outputs_passed = len(runs) == 4
    novelty_passed = all(run["novel_actionable_finding"] for run in accepted)
    handling_passed = all(run["operator_handling_seconds"] <= 1200 for run in runs)
    total_cost = sum(float(run["variable_cost_usd"]) for run in runs)
    spend_passed = math.isclose(total_cost, 0.0, rel_tol=0, abs_tol=1e-9)
    criteria = {
        "accepted_packets": _criterion(3, len(accepted), accepted_count_passed),
        "material_claim_citation_resolution": _criterion(
            1.0,
            claim_resolution,
            claim_resolution_passed,
        ),
        "primary_source_citation_ratio": _criterion(
            0.8,
            primary_ratio,
            primary_ratio_passed,
        ),
        "durable_owner_outputs": _criterion(4, len(runs), durable_outputs_passed),
        "novel_actionable_findings": _criterion(
            True,
            novelty_passed,
            novelty_passed,
        ),
        "operator_handling_seconds_per_run": _criterion(
            1200,
            max(run["operator_handling_seconds"] for run in runs),
            handling_passed,
        ),
        "variable_perplexity_spend_usd": _criterion(
            0,
            total_cost,
            spend_passed,
        ),
    }
    passed = all(criterion["passed"] is True for criterion in criteria.values())
    result = {
        "schema_version": "1.0",
        "commission_id": PILOT_COMMISSION_ID,
        "state": "settled",
        "verdict": "pass" if passed else "fail",
        "evaluated_at": max(verified_times, key=datetime.fromisoformat),
        "catalog_hash": catalog_hash,
        "requests_hash": requests_hash,
        "runs": runs,
        "missing_inputs": [],
        "criteria": criteria,
    }
    validate_aggregate_record(result)
    return result


def validate_aggregate_record(record: Mapping[str, Any]) -> None:
    required = {
        "schema_version",
        "commission_id",
        "state",
        "verdict",
        "evaluated_at",
        "catalog_hash",
        "requests_hash",
        "runs",
        "missing_inputs",
        "criteria",
    }
    if set(record) != required:
        raise PilotAggregateError(
            "aggregate.fields",
            "aggregate record fields do not match the canonical contract",
        )
    if (
        record["schema_version"] != "1.0"
        or record["commission_id"] != PILOT_COMMISSION_ID
    ):
        raise PilotAggregateError("aggregate.identity", "aggregate identity is invalid")
    state = record["state"]
    if state not in {"wait_relay", "settled"}:
        raise PilotAggregateError(
            "aggregate.state", f"unsupported aggregate state {state}"
        )
    runs = record["runs"]
    missing = record["missing_inputs"]
    criteria = record["criteria"]
    if not isinstance(runs, list) or len(runs) != 4:
        raise PilotAggregateError("aggregate.runs", "aggregate must contain four runs")
    if not isinstance(missing, list) or not isinstance(criteria, dict):
        raise PilotAggregateError(
            "aggregate.types", "aggregate collections are invalid"
        )
    if any(not isinstance(run, dict) for run in runs):
        raise PilotAggregateError("aggregate.runs", "aggregate run is not an object")
    if {run.get("request_id") for run in runs} != PILOT_REQUEST_IDS:
        raise PilotAggregateError("aggregate.runs", "aggregate request IDs diverge")
    for run in runs:
        required_run_fields = {
            "request_id",
            "owner_repo",
            "report_path",
            "receipt_path",
            "disposition",
        }
        if not isinstance(run, dict) or not required_run_fields.issubset(run):
            raise PilotAggregateError("aggregate.runs", "aggregate run is incomplete")
        for field in ("report_path", "receipt_path"):
            path = PurePosixPath(str(run[field]))
            if path.is_absolute() or ".." in path.parts or "." in path.parts:
                raise PilotAggregateError(
                    "aggregate.runs",
                    f"aggregate run contains unsafe {field}",
                )
        if run["disposition"] in {"accepted", "rejected"}:
            for field in ("report_hash", "receipt_hash", "source_manifest_hash"):
                if not isinstance(run.get(field), str) or not _HASH.fullmatch(
                    run[field]
                ):
                    raise PilotAggregateError(
                        "aggregate.runs",
                        f"terminal aggregate run lacks a valid {field}",
                    )
    expected_criteria = {
        "accepted_packets",
        "material_claim_citation_resolution",
        "primary_source_citation_ratio",
        "durable_owner_outputs",
        "novel_actionable_findings",
        "operator_handling_seconds_per_run",
        "variable_perplexity_spend_usd",
    }
    if set(criteria) != expected_criteria:
        raise PilotAggregateError("aggregate.criteria", "aggregate criteria diverge")
    if any(
        not isinstance(value, dict) or set(value) != {"required", "observed", "passed"}
        for value in criteria.values()
    ):
        raise PilotAggregateError(
            "aggregate.criteria",
            "aggregate criterion fields diverge",
        )
    if state == "wait_relay":
        if record["verdict"] is not None or record["evaluated_at"] is not None:
            raise PilotAggregateError(
                "aggregate.wait_relay",
                "wait_relay cannot claim a verdict or evaluation time",
            )
        if not missing or any(
            value.get("passed") is not None for value in criteria.values()
        ):
            raise PilotAggregateError(
                "aggregate.wait_relay",
                "wait_relay must name missing inputs and defer every criterion",
            )
        return
    if record["verdict"] not in PILOT_VERDICTS or not isinstance(
        record["evaluated_at"], str
    ):
        raise PilotAggregateError(
            "aggregate.settled",
            "settled aggregate requires a verdict and evaluation time",
        )
    if missing or any(
        value.get("passed") not in {True, False} for value in criteria.values()
    ):
        raise PilotAggregateError(
            "aggregate.settled",
            "settled aggregate must resolve every input and criterion",
        )
    expected_verdict = (
        "pass"
        if all(value["passed"] is True for value in criteria.values())
        else "fail"
    )
    if record["verdict"] != expected_verdict:
        raise PilotAggregateError(
            "aggregate.verdict",
            "aggregate verdict diverges from its criteria",
        )
