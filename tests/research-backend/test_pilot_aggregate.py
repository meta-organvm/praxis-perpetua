"""Fixture-backed tests for the live Perplexity pilot aggregate predicate."""

from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from typing import Any

import yaml


ROOT = Path(__file__).resolve().parents[2]
SCRIPTS = ROOT / "scripts"
sys.path.insert(0, str(SCRIPTS))

from research_pilot_aggregate import (  # noqa: E402
    PilotAggregateError,
    canonical_hash,
    evaluate_pilot,
)


def _load_validator_module() -> Any:
    path = SCRIPTS / "validate-research-backend.py"
    spec = importlib.util.spec_from_file_location("validate_research_backend", path)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load owner validator")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


VALIDATOR = _load_validator_module()


class PilotAggregateFixtureTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        fixture_path = (
            ROOT
            / "tests"
            / "research-backend"
            / "fixtures"
            / "pilot-aggregate-cases.yaml"
        )
        cls.fixture = yaml.safe_load(fixture_path.read_text(encoding="utf-8"))
        request_dir = (
            ROOT / "commissions" / "2026-07-17-perplexity-research-pilot" / "requests"
        )
        cls.requests = {
            request["request_id"]: request
            for request in (
                yaml.safe_load(path.read_text(encoding="utf-8"))
                for path in sorted(request_dir.glob("*.yaml"))
            )
        }
        execution_catalog_receipt = json.loads(
            (
                ROOT
                / "commissions"
                / "2026-07-17-perplexity-research-pilot"
                / "execution-catalog-receipt.json"
            ).read_text(encoding="utf-8")
        )
        cls.catalog_hash = execution_catalog_receipt["catalog_hash"]

    def _owner_roots(self, base: Path) -> dict[str, Path]:
        owners = {
            request["output_contract"]["owner_repo"]
            for request in self.requests.values()
        }
        roots = {owner: base / owner.replace("/", "__") for owner in owners}
        for root in roots.values():
            root.mkdir(parents=True)
        return roots

    def _report(self, request: dict[str, Any], disposition: str) -> str:
        if disposition == "rejected":
            return "\n".join(
                [
                    "# Rejected pilot run",
                    "",
                    "The durable blocked report records why evidence was rejected.",
                    "",
                ]
            )
        lines = ["# Pilot fixture report", ""]
        for section in request["output_contract"]["required_sections"]:
            title = str(section).replace("_", " ").title()
            lines.extend(
                [
                    f"## {title}",
                    "",
                    (
                        f"Fixture evidence for {section}."
                        if disposition == "accepted"
                        else f"Run rejected with an owner-routed finding for {section}."
                    ),
                    "",
                ]
            )
        return "\n".join(lines)

    def _receipt(
        self,
        request: dict[str, Any],
        disposition: str,
    ) -> dict[str, Any]:
        accepted = disposition == "accepted"
        output = request["output_contract"]
        redactions = (
            ["sensitive_raw_material_omitted"]
            if request["external_transmission"] == "sanitized_only"
            else []
        )
        return {
            "schema_version": "1.0",
            "receipt_id": request["request_id"].replace("SGO-REQ", "SGO-RCT"),
            "request_id": request["request_id"],
            "request_hash": canonical_hash(request),
            "catalog_hash": self.catalog_hash,
            "selected_profile": "pro_research",
            "observed_provider": "Fixture attended surface",
            "observed_model": None,
            "retrieval_started_at": "2026-07-18T01:00:00Z",
            "retrieval_finished_at": "2026-07-18T01:10:00Z",
            "source_manifest_hash": f"sha256:{'1' * 64}",
            "outcome_type": "EvidencePacket" if accepted else "BlockedReceipt",
            "usage": {
                "currency": "USD",
                "variable_cost": 0,
                "requests": 1,
                "input_tokens": None,
                "output_tokens": None,
                "computer_credits": 0,
                "operator_handling_seconds": 600,
                "usage_source": "locally_observed",
            },
            "verification": {
                "status": "accepted" if accepted else "rejected",
                "verified_at": "2026-07-18T01:12:00Z",
                "verifier": (f"Studium Source Verifier attestation sha256:{'2' * 64}"),
                "material_claims": 1 if accepted else 0,
                "supported_material_claims": 1 if accepted else 0,
                "resolvable_citations": 1 if accepted else 0,
                "total_citations": 1 if accepted else 0,
                "primary_source_citations": 1 if accepted else 0,
                "primary_source_ratio": 1 if accepted else 0,
                "rejection_reasons": [] if accepted else ["verification_failed"],
            },
            "durable_output": {
                "owner_repo": output["owner_repo"],
                "report_path": output["report_path"],
                "receipt_path": output["receipt_path"],
                "raw_export_ref": output["raw_export_ref"],
            },
            "privacy": {
                "preservation_tier": request["preservation_tier"],
                "external_transmission": request["external_transmission"],
                "tracked_output_safe": True,
                "raw_export_disposition": "private_owner",
                "private_connected_sources_used": False,
                "redactions_applied": redactions,
            },
            "sanitization": {
                "contains_credentials": False,
                "contains_private_prompt_body": False,
                "contains_sensitive_raw_material": False,
            },
        }

    @staticmethod
    def _set_nested(value: dict[str, Any], field: str, replacement: Any) -> None:
        parts = field.split(".")
        target = value
        for part in parts[:-1]:
            target = target[part]
        target[parts[-1]] = replacement

    def _materialize(
        self,
        case: dict[str, Any],
        base: Path,
    ) -> dict[str, Path]:
        roots = self._owner_roots(base)
        omitted_reports = set(case.get("omit_reports", []))
        omitted_receipts = set(case.get("omit_receipts", []))
        mutation = case.get("receipt_mutation")
        for request_id, request in self.requests.items():
            disposition = case["dispositions"][request_id]
            output = request["output_contract"]
            owner_root = roots[output["owner_repo"]]
            report_path = owner_root / output["report_path"]
            receipt_path = owner_root / output["receipt_path"]
            if request_id not in omitted_reports:
                report_path.parent.mkdir(parents=True, exist_ok=True)
                report_path.write_text(
                    self._report(request, disposition),
                    encoding="utf-8",
                )
            if request_id not in omitted_receipts:
                receipt = self._receipt(request, disposition)
                receipt["usage"].update(
                    case.get("usage_overrides", {}).get(request_id, {})
                )
                if mutation and mutation["request_id"] == request_id:
                    self._set_nested(
                        receipt,
                        mutation["field"],
                        mutation["value"],
                    )
                receipt_path.parent.mkdir(parents=True, exist_ok=True)
                receipt_path.write_text(
                    json.dumps(receipt, indent=2, sort_keys=True) + "\n",
                    encoding="utf-8",
                )
        return roots

    def _materialize_status(
        self,
        synthetic_root: Path,
        result: dict[str, Any],
    ) -> None:
        pilot_root = (
            synthetic_root / "commissions" / "2026-07-17-perplexity-research-pilot"
        )
        pilot_root.mkdir(parents=True)
        request_dir = pilot_root / "requests"
        request_dir.mkdir()
        for index, request in enumerate(self.requests.values(), start=1):
            (request_dir / f"{index:02d}-fixture.yaml").write_text(
                yaml.safe_dump(request, sort_keys=False),
                encoding="utf-8",
            )
        governance_dir = synthetic_root / "governance"
        governance_dir.mkdir()
        (governance_dir / "research-backend-profiles.yaml").write_text(
            (ROOT / "governance" / "research-backend-profiles.yaml").read_text(
                encoding="utf-8"
            ),
            encoding="utf-8",
        )
        aggregate_ref = (
            "commissions/2026-07-17-perplexity-research-pilot/aggregate-evaluation.json"
        )
        (synthetic_root / aggregate_ref).write_text(
            json.dumps(result, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
        spend = result["criteria"]["variable_perplexity_spend_usd"]["observed"]
        (pilot_root / "status.md").write_text(
            "\n".join(
                [
                    "---",
                    'schema_version: "1.0"',
                    "commission_id: INQ-2026-014",
                    "state: settled",
                    f'observed_at: "{result["evaluated_at"]}"',
                    f"aggregate_evaluation_ref: {aggregate_ref}",
                    f"verdict: {result['verdict']}",
                    f"variable_spend_usd: {spend}",
                    "---",
                    "# Pilot status",
                    "",
                    "- **State:** `settled`",
                    f"- **Verdict:** `{result['verdict']}`",
                    "- **Profile:** `pro_research`",
                    f"- **Variable spend:** USD {float(spend):g}",
                    "",
                ]
            ),
            encoding="utf-8",
        )

    def test_aggregate_cases(self) -> None:
        for case in self.fixture["cases"]:
            with self.subTest(case=case["name"]), tempfile.TemporaryDirectory() as raw:
                roots = self._materialize(case, Path(raw))
                if "expected_error" in case:
                    with self.assertRaises(PilotAggregateError) as captured:
                        evaluate_pilot(ROOT, roots)
                    self.assertEqual(captured.exception.code, case["expected_error"])
                    continue
                result = evaluate_pilot(ROOT, roots)
                self.assertEqual(result["state"], case["expected_state"])
                self.assertEqual(result["verdict"], case["expected_verdict"])
                self.assertEqual(
                    len(result["missing_inputs"]),
                    case["expected_missing_inputs"],
                )
                if "expected_failed_criteria" in case:
                    failed = sorted(
                        name
                        for name, criterion in result["criteria"].items()
                        if criterion["passed"] is False
                    )
                    self.assertEqual(failed, case["expected_failed_criteria"])
                if "expected_missing_kinds" in case:
                    self.assertEqual(
                        sorted(item["kind"] for item in result["missing_inputs"]),
                        case["expected_missing_kinds"],
                    )

    def test_current_terminal_status(self) -> None:
        self.assertEqual(VALIDATOR.validate_pilot_status(ROOT), "settled")

    def test_settled_status_accepts_terminal_aggregate(self) -> None:
        case = next(
            item for item in self.fixture["cases"] if item["name"] == "terminal_pass"
        )
        with (
            tempfile.TemporaryDirectory() as owner_raw,
            tempfile.TemporaryDirectory() as root_raw,
        ):
            result = evaluate_pilot(
                ROOT,
                self._materialize(case, Path(owner_raw)),
            )
            synthetic_root = Path(root_raw)
            self._materialize_status(synthetic_root, result)
            self.assertEqual(
                VALIDATOR.validate_pilot_status(synthetic_root),
                "settled",
            )

    def test_settled_fail_status_records_nonzero_spend_truthfully(self) -> None:
        case = next(
            item
            for item in self.fixture["cases"]
            if item["name"] == "terminal_fail_nonzero_spend"
        )
        with (
            tempfile.TemporaryDirectory() as owner_raw,
            tempfile.TemporaryDirectory() as root_raw,
        ):
            result = evaluate_pilot(
                ROOT,
                self._materialize(case, Path(owner_raw)),
            )
            self.assertEqual(result["verdict"], "fail")
            synthetic_root = Path(root_raw)
            self._materialize_status(synthetic_root, result)
            self.assertEqual(
                VALIDATOR.validate_pilot_status(synthetic_root),
                "settled",
            )

    def test_require_settled_does_not_write_wait_relay_artifact(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            base = Path(raw)
            roots = self._owner_roots(base / "owners")
            output = base / "aggregate-evaluation.json"
            command = [
                sys.executable,
                str(SCRIPTS / "evaluate-research-pilot.py"),
                "--root",
                str(ROOT),
            ]
            for owner, path in sorted(roots.items()):
                command.extend(["--owner-root", f"{owner}={path}"])
            command.extend(["--output", str(output), "--require-settled"])
            completed = subprocess.run(
                command,
                cwd=ROOT,
                check=False,
                capture_output=True,
                text=True,
            )
            self.assertEqual(completed.returncode, 3)
            self.assertEqual(json.loads(completed.stdout)["state"], "wait_relay")
            self.assertFalse(output.exists())


if __name__ == "__main__":
    unittest.main()
