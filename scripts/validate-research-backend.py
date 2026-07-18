#!/usr/bin/env python3
"""Validate SGO research-backend schemas, fixtures, registry, and invariants."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import math
import re
from datetime import date, datetime
from pathlib import Path, PurePosixPath
from typing import Any
from urllib.parse import urlparse

import yaml
from jsonschema import Draft202012Validator, FormatChecker

from research_pilot_aggregate import (
    PILOT_STATES,
    PilotAggregateError,
    validate_aggregate_record,
)


PRESERVATION_TIERS = {
    "public_facing",
    "operational_internal",
    "client_private",
    "essence_private",
}
TRANSMISSION_MODES = {"public_only", "sanitized_only", "forbidden"}
VERIFICATION_STRENGTH = {
    "basic": 0,
    "corroborated": 1,
    "primary_source": 2,
    "systematic": 3,
}
PROFILE_STATES = {"enabled", "disabled", "dormant", "available"}
SENSITIVE_VALUE_PATTERNS = (
    re.compile(r"\bsk-[A-Za-z0-9_-]{8,}\b", re.IGNORECASE),
    re.compile(
        r"\b(?:api[_-]?key|access[_-]?token|client[_-]?secret|password)"
        r"\s*[:=]\s*\S+",
        re.IGNORECASE,
    ),
    re.compile(r"\bauthorization\s*:\s*bearer\s+\S+", re.IGNORECASE),
    re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
)
LOCAL_ABSOLUTE_PATH_PATTERNS = (
    re.compile(r"(?<![A-Za-z0-9:])/(?:Users|home|tmp|Volumes|var/folders)/\S+"),
    re.compile(r"(?<![A-Za-z0-9])~/\S+"),
    re.compile(r"\b[A-Za-z]:\\[^\s]+"),
    re.compile(r"\bfile:///", re.IGNORECASE),
)
PILOT_REQUEST_IDS = {
    "SGO-REQ-2026-PPLX-PILOT-01",
    "SGO-REQ-2026-PPLX-PILOT-02",
    "SGO-REQ-2026-PPLX-PILOT-03",
    "SGO-REQ-2026-PPLX-PILOT-04",
}
MODEL_POLICY_KEYS = {
    "fixed_model_ids_forbidden",
    "model_ids_allowed_in_registry",
    "no_model_choice",
    "no_model_selection",
}
CATALOG_POLICY_KEYS = {
    "live_catalog_required",
    "provider_catalog",
}
PROVIDER_ORDER_POLICY_KEYS = {
    "fixed_provider_order_forbidden",
}
FROZEN_PROVIDER_KEYS = {
    "adapter_ids",
    "adapter_order",
    "adapter_priority",
    "adapters",
    "preferred_provider",
    "provider_ids",
    "provider_priority",
    "providers",
}
TRUE_PROHIBITION_KEYS = {
    "fixed_model_ids_forbidden",
    "fixed_provider_order_forbidden",
    "no_model_choice",
    "no_model_selection",
}
PROFILE_FIELDS = {
    "state",
    "activation",
    "execution_kind",
    "outcome_type",
    "verification_strength",
    "preservation_tiers",
    "external_transmission",
    "variable_cost_usd",
    "provider_surface",
    "capabilities",
    "guardrails",
    "health",
    "execution_timeout_seconds",
    "subscription_policy",
}
REGISTRY_FIELDS = {
    "schema_version",
    "registry_id",
    "updated",
    "owner",
    "startup",
    "selection",
    "profiles",
    "observed_current",
}
SELECTION_FIELDS = {
    "basis",
    "provider_catalog",
    "insufficient_metadata_behavior",
    "model_ids_allowed_in_registry",
    "silent_fallback",
    "unavailable_outcomes",
}


class ContractError(RuntimeError):
    """A stable semantic or schema failure."""

    def __init__(self, code: str, message: str):
        super().__init__(f"{code}: {message}")
        self.code = code
        self.message = message


def fail(code: str, message: str) -> None:
    raise ContractError(code, message)


def load_data(path: Path) -> Any:
    with path.open(encoding="utf-8") as handle:
        if path.suffix == ".json":
            return json.load(handle)
        return yaml.safe_load(handle)


def canonical_hash(value: Any) -> str:
    payload = json.dumps(
        value,
        ensure_ascii=False,
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")
    return f"sha256:{hashlib.sha256(payload).hexdigest()}"


def raw_text_hash(value: str) -> str:
    return f"sha256:{hashlib.sha256(value.encode('utf-8')).hexdigest()}"


def parse_datetime(value: str, field: str) -> datetime:
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except (TypeError, ValueError) as exc:
        fail("timestamps.format", f"{field} is not an ISO-8601 timestamp: {exc}")
    if parsed.tzinfo is None:
        fail("timestamps.format", f"{field} must include a timezone")
    return parsed


def parse_date(value: str, field: str) -> date:
    try:
        return date.fromisoformat(value)
    except (TypeError, ValueError) as exc:
        fail("freshness.format", f"{field} is not an ISO-8601 date: {exc}")


def assert_relative_path(value: str, field: str) -> None:
    path = PurePosixPath(value)
    if (
        not value
        or value.startswith(("/", "~"))
        or "\\" in value
        or "://" in value
        or path.is_absolute()
        or ".." in path.parts
    ):
        fail("path.relative", f"{field} must be a safe repository-relative path")


def schema_validators(root: Path) -> dict[str, Draft202012Validator]:
    checker = FormatChecker()
    validators: dict[str, Draft202012Validator] = {}
    schema_paths = {
        "request": root / "schemas" / "research-request.schema.json",
        "outcome": root / "schemas" / "research-outcome.schema.json",
        "receipt": root / "schemas" / "research-receipt.schema.json",
        "attestation": (root / "schemas" / "source-verifier-attestation.schema.json"),
        "sanitization_attestation": (
            root / "schemas" / "output-sanitization-attestation.schema.json"
        ),
    }
    for kind, path in schema_paths.items():
        schema = load_data(path)
        Draft202012Validator.check_schema(schema)
        validators[kind] = Draft202012Validator(
            schema,
            format_checker=checker,
        )
    return validators


def validate_schema(
    validators: dict[str, Draft202012Validator],
    kind: str,
    value: Any,
) -> None:
    errors = sorted(
        validators[kind].iter_errors(value),
        key=lambda error: [str(part) for part in error.absolute_path],
    )
    if not errors:
        return
    error = errors[0]
    location = ".".join(str(part) for part in error.absolute_path) or "<root>"
    fail(f"schema.{kind}", f"{location}: {error.message}")


def validate_dynamic_registry_keys(value: Any, path: tuple[str, ...] = ()) -> None:
    """Reject frozen provider/model choices regardless of nesting."""

    if isinstance(value, dict):
        for raw_key, child in value.items():
            key = str(raw_key).strip().lower().replace("-", "_")
            location = ".".join((*path, key))
            if "model" in key and key not in MODEL_POLICY_KEYS:
                fail(
                    "registry.fixed_model",
                    f"{location} encodes a model field",
                )
            if "catalog" in key and key not in CATALOG_POLICY_KEYS:
                fail(
                    "registry.fixed_catalog",
                    f"{location} encodes a catalog snapshot",
                )
            if "fallback" in key and key != "silent_fallback":
                fail(
                    "registry.silent_fallback",
                    f"{location} encodes a fallback table",
                )
            if "provider_order" in key and key not in PROVIDER_ORDER_POLICY_KEYS:
                fail(
                    "registry.fixed_catalog",
                    f"{location} encodes a fixed provider order",
                )
            if key in FROZEN_PROVIDER_KEYS:
                fail(
                    "registry.fixed_catalog",
                    f"{location} encodes a fixed provider list",
                )
            if key in TRUE_PROHIBITION_KEYS and child is not True:
                fail(
                    "registry.prohibition",
                    f"{location} must remain true",
                )
            validate_dynamic_registry_keys(child, (*path, key))
    elif isinstance(value, list):
        for index, child in enumerate(value):
            validate_dynamic_registry_keys(child, (*path, str(index)))


def validate_registry(registry: dict[str, Any]) -> None:
    validate_dynamic_registry_keys(registry)
    registry_extras = set(registry) - REGISTRY_FIELDS
    if registry_extras:
        fail(
            "registry.fields",
            f"registry has unknown fields {sorted(registry_extras)}",
        )
    profiles = registry.get("profiles")
    if not isinstance(profiles, dict) or not profiles:
        fail("registry.profiles", "registry must contain profiles")

    startup = registry.get("startup", {})
    for field in (
        "open_provider_surfaces",
        "background_execution",
        "scheduled_execution",
        "automatic_refill_allowed",
    ):
        if startup.get(field) is not False:
            fail("registry.startup", f"startup.{field} must be false")

    selection = registry.get("selection")
    if not isinstance(selection, dict):
        fail("registry.selection", "registry must contain structured selection")
    selection_extras = set(selection) - SELECTION_FIELDS
    if selection_extras:
        fail(
            "registry.selection",
            f"selection has unknown fields {sorted(selection_extras)}",
        )
    expected_selection = {
        "provider_catalog": "discover_live",
        "insufficient_metadata_behavior": "provider_auto",
        "model_ids_allowed_in_registry": False,
        "silent_fallback": "forbidden",
    }
    for field, expected in expected_selection.items():
        if selection.get(field) != expected:
            fail(
                "registry.selection",
                f"selection.{field} must be {expected!r}",
            )

    required = {
        "state",
        "activation",
        "execution_kind",
        "outcome_type",
        "verification_strength",
        "preservation_tiers",
        "external_transmission",
        "variable_cost_usd",
        "provider_surface",
        "capabilities",
        "guardrails",
        "health",
    }
    provider_profiles = {"pro_research", "pro_computer", "api_search", "api_synthesis"}
    for name, profile in profiles.items():
        missing = required - set(profile)
        if missing:
            fail("registry.fields", f"{name} missing {sorted(missing)}")
        extras = set(profile) - PROFILE_FIELDS
        if extras:
            fail("registry.fields", f"{name} has unknown fields {sorted(extras)}")
        if profile["state"] not in PROFILE_STATES:
            fail("registry.state", f"{name} has invalid state {profile['state']!r}")
        if profile["verification_strength"] not in VERIFICATION_STRENGTH:
            fail("registry.verification", f"{name} has invalid verification strength")
        if not set(profile["preservation_tiers"]) <= PRESERVATION_TIERS:
            fail("registry.preservation", f"{name} has an unknown preservation tier")
        if not set(profile["external_transmission"]) <= TRANSMISSION_MODES:
            fail("registry.transmission", f"{name} has an unknown transmission mode")
        cost = profile["variable_cost_usd"]
        if cost is not None and (
            isinstance(cost, bool) or not isinstance(cost, (int, float)) or cost < 0
        ):
            fail("registry.cost", f"{name} cost must be non-negative or null")
        guardrails = profile["guardrails"]
        if guardrails.get("private_connected_sources_allowed") is not False:
            fail("registry.private_sources", f"{name} must forbid private sources")
        health = profile["health"]
        if not isinstance(health.get("machine"), dict):
            fail("registry.health", f"{name} needs structured machine health")
        attended = health.get("attended")
        if not isinstance(attended, dict):
            fail("registry.health", f"{name} needs structured attended health")
        if attended.get("live_authentication_asserted") is not False:
            fail("registry.auth_claim", f"{name} must not assert live authentication")
        if "executable_when" in health:
            fail("registry.health", f"{name} retains prose-only executable_when")

        if name in provider_profiles or name == "provider_auto":
            if not set(profile["preservation_tiers"]) <= {
                "public_facing",
                "operational_internal",
            }:
                fail("registry.private_profile", f"{name} accepts C/E preservation")
            if not set(profile["external_transmission"]) <= {
                "public_only",
                "sanitized_only",
            }:
                fail(
                    "registry.private_profile", f"{name} accepts forbidden transmission"
                )

    pro = profiles.get("pro_research")
    if not pro:
        fail("registry.pro_research", "pro_research profile is required")
    if pro.get("execution_timeout_seconds") != 3600:
        fail("registry.timeout", "pro_research timeout must be 3600 seconds")
    pro_guardrails = pro["guardrails"]
    expected_handoff = {
        "project_name": "Limen Research",
        "required_export_format": "markdown",
        "standing_instructions_ref": (
            ".claude/skills/sgo-commission-research/templates/"
            "perplexity-project-standing-instructions.md"
        ),
        "launch_url": "https://www.perplexity.ai/",
    }
    for field, expected in expected_handoff.items():
        if pro_guardrails.get(field) != expected:
            fail("registry.handoff", f"pro_research guardrails.{field} drifted")
    if pro["health"]["machine"].get("enforce_execution_timeout") is not True:
        fail("registry.timeout", "pro_research timeout is not machine-enforced")
    if pro["health"]["attended"].get("disposition") != "defer_to_manual_handoff":
        fail("registry.handoff", "pro_research attended checks are not deferred")
    for name in ("api_search", "api_synthesis"):
        if profiles.get(name, {}).get("state") != "dormant":
            fail("registry.api_state", f"{name} must begin dormant")


def validate_request_semantics(request: dict[str, Any]) -> None:
    output = request["output_contract"]
    assert_relative_path(output["report_path"], "output_contract.report_path")
    assert_relative_path(output["receipt_path"], "output_contract.receipt_path")
    for index, context in enumerate(request.get("context_refs", [])):
        assert_relative_path(context["path"], f"context_refs[{index}].path")

    tier = request["preservation_tier"]
    transmission = request["external_transmission"]
    if tier in {"client_private", "essence_private"} and transmission != "forbidden":
        fail("privacy.private_transmission", f"{tier} requires forbidden transmission")
    raw_ref = output.get("raw_export_ref")
    if (
        tier in {"client_private", "essence_private"}
        and raw_ref
        and not raw_ref.startswith("private-owner://")
    ):
        fail("privacy.private_custody", f"{tier} raw exports require a private owner")

    freshness = request.get("freshness", {})
    published_after = freshness.get("published_after")
    published_before = freshness.get("published_before")
    if published_after and published_before:
        if parse_date(published_after, "freshness.published_after") > parse_date(
            published_before,
            "freshness.published_before",
        ):
            fail("freshness.order", "published_after exceeds published_before")


def validate_profile_compatibility(
    request: dict[str, Any],
    profile_name: str,
    registry: dict[str, Any],
) -> None:
    profile = registry["profiles"].get(profile_name)
    if profile is None:
        fail("profile.unknown", f"selected profile {profile_name!r} is not registered")
    if request["preservation_tier"] not in profile["preservation_tiers"]:
        fail(
            "profile.preservation",
            f"{profile_name} rejects {request['preservation_tier']}",
        )
    if request["external_transmission"] not in profile["external_transmission"]:
        fail(
            "profile.transmission",
            f"{profile_name} rejects {request['external_transmission']}",
        )
    missing_capabilities = set(request["required_capabilities"]) - set(
        profile["capabilities"]
    )
    if missing_capabilities:
        fail(
            "profile.capability",
            f"{profile_name} lacks {sorted(missing_capabilities)}",
        )
    requested_strength = VERIFICATION_STRENGTH[request["verification_strength"]]
    profile_strength = VERIFICATION_STRENGTH[profile["verification_strength"]]
    if profile_strength < requested_strength:
        fail("profile.verification", f"{profile_name} verification is too weak")
    timeout = profile.get("execution_timeout_seconds")
    if timeout is not None and timeout > request["latency_ceiling_seconds"]:
        fail("profile.latency", f"{profile_name} timeout exceeds request ceiling")
    profile_cost = profile["variable_cost_usd"]
    if profile_cost is None:
        fail("profile.cost_unknown", f"{profile_name} cost is not projected")
    if profile_cost > request["spend_ceiling"]["variable_cost"]:
        fail("profile.cost", f"{profile_name} cost exceeds request ceiling")
    required_state = profile["health"]["machine"].get("required_profile_state")
    if required_state and profile["state"] != required_state:
        fail(
            "profile.health",
            f"{profile_name} state {profile['state']} is not {required_state}",
        )


def validate_attestation(
    request: dict[str, Any],
    outcome: dict[str, Any],
    receipt: dict[str, Any],
    attestation: dict[str, Any],
    validators: dict[str, Draft202012Validator],
) -> None:
    validate_schema(validators, "attestation", attestation)
    if attestation["request_id"] != request["request_id"]:
        fail("attestation.request_id", "attestation request ID diverges")
    if attestation["verdict"] != "accepted":
        fail(
            "attestation.verdict",
            "accepted EvidencePacket requires an accepted attestation",
        )

    claims = attestation["claims"]
    sources = attestation["sources"]
    claim_ids = [claim["claim_id"] for claim in claims]
    source_ids = [source["source_id"] for source in sources]
    if len(claim_ids) != len(set(claim_ids)):
        fail("attestation.claims_duplicate", "attestation claim IDs must be unique")
    if len(source_ids) != len(set(source_ids)):
        fail("attestation.sources_duplicate", "attestation source IDs must be unique")

    outcome_claims = {claim["claim_id"]: claim for claim in outcome["claims"]}
    outcome_sources = {source["source_id"]: source for source in outcome["sources"]}
    attested_claims = {claim["claim_id"]: claim for claim in claims}
    attested_sources = {source["source_id"]: source for source in sources}
    if set(attested_claims) != set(outcome_claims):
        fail("attestation.claim_set", "attestation claim set diverges from packet")
    if set(attested_sources) != set(outcome_sources):
        fail("attestation.source_set", "attestation source set diverges from packet")

    for claim_id, claim in attested_claims.items():
        packet_claim = outcome_claims[claim_id]
        if set(claim["source_ids"]) != set(packet_claim["source_ids"]):
            fail(
                "attestation.claim_edges",
                f"{claim_id} source edges diverge from packet",
            )
        if claim["verification_status"] != packet_claim["verification_status"]:
            fail(
                "attestation.claim_status",
                f"{claim_id} status diverges from packet",
            )
        for source_id in claim["source_ids"]:
            if source_id not in attested_sources:
                fail(
                    "attestation.source_ref",
                    f"{claim_id} references missing {source_id}",
                )

    for source_id, source in attested_sources.items():
        packet_source = outcome_sources[source_id]
        parsed_source_url = urlparse(source["url"])
        if (
            parsed_source_url.username is not None
            or parsed_source_url.password is not None
        ):
            fail(
                "attestation.source_url_credentials",
                f"{source_id} URL contains forbidden userinfo",
            )
        if source["url"] != packet_source["url"]:
            fail(
                "attestation.source_url",
                f"{source_id} URL diverges from packet",
            )
        if source["resolvable"] is not True:
            fail(
                "attestation.source_resolution",
                f"{source_id} is not resolvable",
            )
        for field in ("source_type", "primary_source", "quality_tier"):
            if source[field] != packet_source[field]:
                fail(
                    "attestation.source_grading",
                    f"{source_id} {field} diverges from packet",
                )

    verification = receipt["verification"]
    if verification["verified_at"] != attestation["verified_at"]:
        fail(
            "attestation.verified_at",
            "receipt verification time diverges from attestation",
        )
    expected_verifier = (
        f"{attestation['verifier']} attestation {canonical_hash(attestation)}"
    )
    if verification["verifier"] != expected_verifier:
        fail(
            "attestation.receipt_verifier",
            "receipt does not bind the canonical attestation hash",
        )


def validate_output_sanitization(
    request: dict[str, Any],
    receipt: dict[str, Any],
    attestation: dict[str, Any],
    raw_export: str,
    validators: dict[str, Draft202012Validator],
) -> None:
    validate_schema(validators, "sanitization_attestation", attestation)
    if attestation["request_id"] != request["request_id"]:
        fail(
            "sanitization.request_id",
            "sanitization attestation request ID diverges",
        )
    for pattern in SENSITIVE_VALUE_PATTERNS:
        if pattern.search(attestation["attestor"]):
            fail(
                "sanitization.attestor",
                "sanitization attestor contains a credential-shaped value",
            )
    if attestation["preservation_tier"] != request["preservation_tier"]:
        fail(
            "sanitization.preservation",
            "sanitization attestation preservation tier diverges",
        )
    if attestation["external_transmission"] != request["external_transmission"]:
        fail(
            "sanitization.transmission",
            "sanitization attestation transmission authority diverges",
        )
    if attestation["export_hash"] != raw_text_hash(raw_export):
        fail(
            "sanitization.export_hash",
            "sanitization attestation does not bind the exact Markdown export",
        )
    question = request["question"].strip()
    raw_contains_private_material = bool(question and question in raw_export) or any(
        pattern.search(raw_export) for pattern in SENSITIVE_VALUE_PATTERNS
    )
    raw_export_ref = request["output_contract"].get("raw_export_ref")
    if raw_contains_private_material and not (
        isinstance(raw_export_ref, str)
        and raw_export_ref.startswith("private-owner://")
    ):
        fail(
            "sanitization.raw_export_custody",
            "raw prompt or credential material requires private-owner custody",
        )

    attested_at = parse_datetime(
        attestation["attested_at"],
        "sanitization_attestation.attested_at",
    )
    retrieval_finished_at = parse_datetime(
        receipt["retrieval_finished_at"],
        "receipt.retrieval_finished_at",
    )
    if attested_at < retrieval_finished_at:
        fail(
            "sanitization.timestamp",
            "sanitization attestation predates the retrieval interval",
        )
    if (
        request["external_transmission"] == "sanitized_only"
        and not attestation["redactions_applied"]
    ):
        fail(
            "sanitization.redactions",
            "sanitized_only output requires a redaction record",
        )

    receipt_privacy = receipt["privacy"]
    if receipt_privacy["tracked_output_safe"] != attestation["tracked_output_safe"]:
        fail(
            "sanitization.receipt",
            "receipt tracked-output safety diverges from attestation",
        )
    if receipt_privacy["redactions_applied"] != attestation["redactions_applied"]:
        fail(
            "sanitization.receipt",
            "receipt redaction record diverges from attestation",
        )
    receipt_sanitization = receipt["sanitization"]
    for field in (
        "contains_credentials",
        "contains_private_prompt_body",
        "contains_sensitive_raw_material",
    ):
        if receipt_sanitization[field] != attestation[field]:
            fail(
                "sanitization.receipt",
                f"receipt {field} diverges from attestation",
            )


def domain_matches(host: str, candidate: str) -> bool:
    normalized = candidate.lower().strip().lstrip(".")
    return host == normalized or host.endswith("." + normalized)


def validate_source_constraints(
    request: dict[str, Any],
    outcome: dict[str, Any],
    attestation: dict[str, Any],
) -> None:
    constraints = request.get("domain_constraints", {})
    freshness = request.get("freshness", {})
    after_text = freshness.get("published_after")
    before_text = freshness.get("published_before")
    after = parse_date(after_text, "freshness.published_after") if after_text else None
    before = (
        parse_date(before_text, "freshness.published_before") if before_text else None
    )
    retrieved_after_text = freshness.get("retrieved_after")
    retrieved_after = (
        parse_date(retrieved_after_text, "freshness.retrieved_after")
        if retrieved_after_text
        else None
    )
    as_of_text = freshness.get("as_of")
    as_of = parse_datetime(as_of_text, "freshness.as_of") if as_of_text else None
    maximum_age = freshness.get("max_source_age_days")
    allow_domains = tuple(
        str(value).lower() for value in constraints.get("allow_domains", [])
    )
    deny_domains = tuple(
        str(value).lower() for value in constraints.get("deny_domains", [])
    )
    source_types = set(str(value) for value in constraints.get("source_types", []))
    languages = set(str(value).lower() for value in constraints.get("languages", []))
    jurisdictions = set(
        str(value).lower() for value in constraints.get("jurisdictions", [])
    )
    verified_sources = {
        source["source_id"]: source for source in attestation["sources"]
    }

    for source in outcome["sources"]:
        source_id = source["source_id"]
        verified_source = verified_sources[source_id]
        parsed_url = urlparse(source["url"])
        host = (parsed_url.hostname or "").lower()
        if parsed_url.scheme not in {"http", "https"} or not host:
            fail("domain.url", f"{source_id} does not use a public-web URL")
        if allow_domains and not any(
            domain_matches(host, domain) for domain in allow_domains
        ):
            fail("domain.not_allowed", f"{source_id} host {host} is not allowed")
        if any(domain_matches(host, domain) for domain in deny_domains):
            fail("domain.denied", f"{source_id} host {host} is denied")
        if source_types and source["source_type"] not in source_types:
            fail(
                "domain.source_type",
                f"{source_id} source type is not allowed",
            )

        published_text = source["published_at"]
        if (after or before or maximum_age is not None) and published_text is None:
            fail(
                "freshness.missing_publication_date",
                f"{source_id} cannot satisfy a source-age constraint",
            )
        published = (
            parse_date(
                published_text,
                f"sources.{source_id}.published_at",
            )
            if published_text
            else None
        )
        if after and published and published < after:
            fail("freshness.source_before", f"{source_id} predates bound")
        if before and published and published > before:
            fail("freshness.source_after", f"{source_id} exceeds bound")

        retrieved = parse_datetime(
            source["retrieved_at"],
            f"sources.{source_id}.retrieved_at",
        )
        if retrieved_after and retrieved.date() < retrieved_after:
            fail(
                "freshness.retrieved_before",
                f"{source_id} retrieval predates bound",
            )
        if as_of and retrieved < as_of:
            fail(
                "freshness.retrieved_before_as_of",
                f"{source_id} retrieval predates as_of",
            )
        if maximum_age is not None and published:
            age_days = (retrieved.date() - published).days
            if age_days < 0:
                fail(
                    "freshness.publication_after_retrieval",
                    f"{source_id} publication follows retrieval",
                )
            if age_days > maximum_age:
                fail(
                    "freshness.source_too_old",
                    f"{source_id} exceeds max_source_age_days",
                )

        language = str(verified_source.get("language") or "").lower()
        if languages and language not in languages:
            fail(
                "domain.language",
                f"{source_id} language is not verified as allowed",
            )
        verified_jurisdictions = {
            str(value).lower() for value in verified_source.get("jurisdictions", [])
        }
        if jurisdictions and not jurisdictions.intersection(verified_jurisdictions):
            fail(
                "domain.jurisdiction",
                f"{source_id} jurisdiction is not verified as allowed",
            )


def validate_timestamps(
    request: dict[str, Any],
    outcome: dict[str, Any],
    receipt: dict[str, Any],
) -> None:
    requested = parse_datetime(request["requested_at"], "request.requested_at")
    started = parse_datetime(
        receipt["retrieval_started_at"],
        "receipt.retrieval_started_at",
    )
    finished = parse_datetime(
        receipt["retrieval_finished_at"],
        "receipt.retrieval_finished_at",
    )
    retrieved = parse_datetime(outcome["retrieved_at"], "outcome.retrieved_at")
    verified = parse_datetime(
        receipt["verification"]["verified_at"],
        "receipt.verification.verified_at",
    )
    if not requested <= started <= finished <= verified:
        fail(
            "timestamps.order", "request, retrieval, and verification are out of order"
        )
    if not started <= retrieved <= finished:
        fail("timestamps.order", "outcome retrieval is outside the retrieval interval")
    for source in outcome["sources"]:
        source_time = parse_datetime(
            source["retrieved_at"],
            f"sources.{source['source_id']}.retrieved_at",
        )
        if not started <= source_time <= finished:
            fail("timestamps.order", f"{source['source_id']} retrieval is out of range")
    for index, search in enumerate(outcome["negative_searches"]):
        search_time = parse_datetime(
            search["searched_at"],
            f"negative_searches[{index}].searched_at",
        )
        if not started <= search_time <= finished:
            fail("timestamps.order", f"negative search {index} is out of range")


def validate_claims_and_counts(
    outcome: dict[str, Any],
    receipt: dict[str, Any],
) -> None:
    claims = outcome["claims"]
    sources = outcome["sources"]
    source_ids = [source["source_id"] for source in sources]
    claim_ids = [claim["claim_id"] for claim in claims]
    if len(source_ids) != len(set(source_ids)):
        fail("sources.duplicate", "source IDs must be unique")
    if len(claim_ids) != len(set(claim_ids)):
        fail("claims.duplicate", "claim IDs must be unique")
    source_map = {source["source_id"]: source for source in sources}

    material_claims = [claim for claim in claims if claim["material"]]
    supported_material = [
        claim
        for claim in material_claims
        if claim["verification_status"] == "supported"
    ]
    for claim in material_claims:
        if not claim["source_ids"] or claim["verification_status"] != "supported":
            fail("claims.material", f"{claim['claim_id']} is not supported")
    citation_ids: list[str] = []
    for claim in claims:
        for source_id in claim["source_ids"]:
            if source_id not in source_map:
                fail(
                    "claims.source_ref",
                    f"{claim['claim_id']} references missing {source_id}",
                )
            citation_ids.append(source_id)

    total_citations = len(citation_ids)
    resolvable_citations = len(citation_ids)
    primary_citations = sum(
        1 for source_id in citation_ids if source_map[source_id]["primary_source"]
    )
    ratio = primary_citations / total_citations if total_citations else 0.0
    verification = receipt["verification"]
    if verification["supported_material_claims"] > verification["material_claims"]:
        fail("counts.material", "supported material claims exceed material claims")
    if verification["resolvable_citations"] > verification["total_citations"]:
        fail("counts.citations", "resolvable citations exceed total citations")
    if verification["primary_source_citations"] > verification["total_citations"]:
        fail("counts.citations", "primary citations exceed total citations")
    if verification["material_claims"] != len(material_claims):
        fail("counts.material_exact", "material claim count does not match packet")
    if verification["supported_material_claims"] != len(supported_material):
        fail("counts.material_exact", "supported material count does not match packet")
    if verification["total_citations"] != total_citations:
        fail("counts.citation_exact", "citation count does not match packet")
    if verification["resolvable_citations"] != resolvable_citations:
        fail("counts.citation_exact", "resolvable count does not match packet")
    if verification["primary_source_citations"] != primary_citations:
        fail("counts.primary_exact", "primary citation count does not match packet")
    if not math.isclose(
        verification["primary_source_ratio"],
        ratio,
        rel_tol=0,
        abs_tol=1e-9,
    ):
        fail("counts.primary_ratio", "primary-source ratio does not match counts")


def validate_custody(
    request: dict[str, Any],
    outcome: dict[str, Any],
    receipt: dict[str, Any],
) -> None:
    requested_output = request["output_contract"]
    outcome_output = outcome["durable_output_ref"]
    receipt_output = receipt["durable_output"]
    for field in ("owner_repo", "report_path", "receipt_path", "raw_export_ref"):
        expected = requested_output.get(field)
        if (
            outcome_output.get(field) != expected
            or receipt_output.get(field) != expected
        ):
            fail("custody.output", f"{field} diverges across request/outcome/receipt")

    privacy = receipt["privacy"]
    if privacy["preservation_tier"] != request["preservation_tier"]:
        fail("custody.preservation", "receipt preservation tier diverges")
    if privacy["external_transmission"] != request["external_transmission"]:
        fail("custody.transmission", "receipt transmission authority diverges")
    if privacy["tracked_output_safe"] is not True:
        fail(
            "custody.tracked_output", "sanitized report and receipt are not track-safe"
        )

    raw_ref = requested_output.get("raw_export_ref")
    expected_disposition = "not_retained"
    if raw_ref:
        expected_disposition = (
            "private_owner"
            if raw_ref.startswith("private-owner://")
            else "tracked_owner_repo"
        )
        if expected_disposition == "tracked_owner_repo":
            assert_relative_path(raw_ref, "output_contract.raw_export_ref")
    if privacy["raw_export_disposition"] != expected_disposition:
        fail("custody.raw_export", "raw-export disposition does not match its owner")
    if (
        request["external_transmission"] == "sanitized_only"
        and not privacy["redactions_applied"]
    ):
        fail("custody.sanitization", "sanitized transmission lacks a redaction record")


def validate_hashes(
    request: dict[str, Any],
    outcome: dict[str, Any],
    receipt: dict[str, Any],
    registry: dict[str, Any],
) -> None:
    if receipt["request_hash"] != canonical_hash(request):
        fail("hashes.request", "request hash does not match canonical request")
    if receipt["catalog_hash"] != canonical_hash(registry):
        fail(
            "hashes.catalog", "catalog hash does not match canonical registry snapshot"
        )
    manifest = sorted(outcome["sources"], key=lambda source: source["source_id"])
    manifest_hash = canonical_hash(manifest)
    if outcome["source_manifest_hash"] != manifest_hash:
        fail("hashes.sources", "outcome source-manifest hash does not match sources")
    if receipt["source_manifest_hash"] != manifest_hash:
        fail("hashes.sources", "receipt source-manifest hash does not match sources")


def validate_sanitization(
    request: dict[str, Any],
    outcome: dict[str, Any],
    receipt: dict[str, Any],
    tracked_report: str,
) -> None:
    question = request["question"].strip()
    tracked_derivatives = {
        "EvidencePacket": json.dumps(outcome, ensure_ascii=False, sort_keys=True),
        "report": tracked_report,
        "receipt": json.dumps(receipt, ensure_ascii=False, sort_keys=True),
    }
    for label, serialized in tracked_derivatives.items():
        if question and question in serialized:
            fail(
                "sanitization.prompt_body",
                f"tracked {label} contains the request question",
            )
        for pattern in SENSITIVE_VALUE_PATTERNS:
            if pattern.search(serialized):
                fail(
                    "sanitization.secret",
                    f"tracked {label} contains a credential-shaped value",
                )


def validate_bundle(
    bundle: dict[str, Any],
    validators: dict[str, Draft202012Validator],
    registry: dict[str, Any],
) -> None:
    request = bundle["request"]
    outcome = bundle["outcome"]
    receipt = bundle["receipt"]
    attestation = bundle.get("attestation")
    if not isinstance(attestation, dict):
        fail(
            "attestation.required",
            "complete EvidencePacket bundles require SourceVerifierAttestation",
        )
    sanitization_attestation = bundle.get("sanitization_attestation")
    if not isinstance(sanitization_attestation, dict):
        fail(
            "sanitization.required",
            "complete bundles require OutputSanitizationAttestation",
        )
    raw_export = bundle.get("raw_export")
    if not isinstance(raw_export, str):
        fail(
            "sanitization.raw_export_required",
            "complete bundles require the exact raw Markdown export",
        )
    tracked_report = bundle.get("tracked_report")
    if not isinstance(tracked_report, str):
        fail(
            "sanitization.tracked_report_required",
            "complete bundles require the normalized tracked report",
        )
    validate_schema(validators, "request", request)
    validate_schema(validators, "outcome", outcome)
    validate_schema(validators, "receipt", receipt)
    validate_request_semantics(request)
    validate_profile_compatibility(request, receipt["selected_profile"], registry)

    if outcome["outcome_type"] != "EvidencePacket":
        fail("bundle.outcome", "complete bundles require EvidencePacket")
    if not request["request_id"] == outcome["request_id"] == receipt["request_id"]:
        fail("bundle.request_id", "request IDs diverge")
    if receipt["outcome_type"] != outcome["outcome_type"]:
        fail("bundle.outcome", "receipt outcome type diverges")
    if receipt["verification"]["status"] != "accepted":
        fail("bundle.verification", "accepted packet receipt is not accepted")
    if receipt["usage"]["variable_cost"] > request["spend_ceiling"]["variable_cost"]:
        fail("cost.ceiling", "observed variable cost exceeds request ceiling")

    validate_timestamps(request, outcome, receipt)
    validate_claims_and_counts(outcome, receipt)
    validate_attestation(request, outcome, receipt, attestation, validators)
    validate_output_sanitization(
        request,
        receipt,
        sanitization_attestation,
        raw_export,
        validators,
    )
    validate_source_constraints(request, outcome, attestation)
    validate_custody(request, outcome, receipt)
    validate_sanitization(request, outcome, receipt, tracked_report)
    validate_hashes(request, outcome, receipt, registry)

    if bundle.get("pilot_run"):
        if not outcome["novel_actionable_findings"]:
            fail("pilot.novel_finding", "accepted pilot packet lacks a novel finding")
        if receipt["usage"]["operator_handling_seconds"] > 1200:
            fail("pilot.handling", "operator handling exceeds 20 minutes")
        if receipt["usage"]["variable_cost"] != 0:
            fail("pilot.cost", "pilot variable cost is not zero")


def validate_standalone_outcomes(
    outcomes: list[dict[str, Any]],
    validators: dict[str, Draft202012Validator],
    registry: dict[str, Any],
) -> None:
    for outcome in outcomes:
        validate_schema(validators, "outcome", outcome)
        if outcome["outcome_type"] == "EvidencePacket":
            manifest = sorted(
                outcome["sources"],
                key=lambda source: source["source_id"],
            )
            if outcome["source_manifest_hash"] != canonical_hash(manifest):
                fail(
                    "hashes.sources",
                    "standalone outcome source-manifest hash does not match sources",
                )
            continue
        if outcome["outcome_type"] != "ManualHandoff":
            continue
        profile = registry["profiles"].get(outcome["selected_profile"])
        if profile is None:
            fail("handoff.profile", "manual handoff selected an unknown profile")
        if outcome["preservation_tier"] not in profile["preservation_tiers"]:
            fail("handoff.preservation", "manual handoff preservation is incompatible")
        if outcome["external_transmission"] not in profile["external_transmission"]:
            fail("handoff.transmission", "manual handoff transmission is incompatible")
        guardrails = profile["guardrails"]
        expected = {
            "project_name": guardrails["project_name"],
            "launch_url": guardrails["launch_url"],
            "standing_instructions_ref": guardrails["standing_instructions_ref"],
            "required_export_format": guardrails["required_export_format"],
            "execution_timeout_seconds": profile["execution_timeout_seconds"],
        }
        for field, value in expected.items():
            if outcome[field] != value:
                fail("handoff.metadata", f"ManualHandoff {field} drifted from profile")


def pointer_parts(pointer: str) -> list[str]:
    if not pointer.startswith("/"):
        fail("fixtures.pointer", f"invalid JSON pointer {pointer!r}")
    return [
        part.replace("~1", "/").replace("~0", "~")
        for part in pointer.lstrip("/").split("/")
    ]


def pointer_parent(document: Any, pointer: str) -> tuple[Any, str]:
    parts = pointer_parts(pointer)
    current = document
    for part in parts[:-1]:
        current = current[int(part)] if isinstance(current, list) else current[part]
    return current, parts[-1]


def apply_case(bundle: dict[str, Any], case: dict[str, Any]) -> dict[str, Any]:
    mutated = copy.deepcopy(bundle)
    for pointer, value in case.get("set", {}).items():
        parent, key = pointer_parent(mutated, pointer)
        if isinstance(parent, list):
            parent[int(key)] = value
        else:
            parent[key] = value
    for pointer in case.get("remove", []):
        parent, key = pointer_parent(mutated, pointer)
        if isinstance(parent, list):
            del parent[int(key)]
        else:
            del parent[key]
    return mutated


def validate_negative_cases(
    base: dict[str, Any],
    cases: list[dict[str, Any]],
    validators: dict[str, Draft202012Validator],
    registry: dict[str, Any],
) -> None:
    names: set[str] = set()
    for case in cases:
        name = case["name"]
        if name in names:
            fail("fixtures.duplicate", f"duplicate negative case {name}")
        names.add(name)
        expected = case["expected_error"]
        try:
            validate_bundle(apply_case(base, case), validators, registry)
        except ContractError as error:
            if error.code != expected:
                fail(
                    "fixtures.wrong_error",
                    f"{name} expected {expected}, got {error.code}: {error.message}",
                )
        else:
            fail("fixtures.false_negative", f"{name} unexpectedly passed")


def validate_negative_outcome_cases(
    outcomes: list[dict[str, Any]],
    cases: list[dict[str, Any]],
    validators: dict[str, Draft202012Validator],
    registry: dict[str, Any],
) -> None:
    for case in cases:
        index = case["outcome_index"]
        wrapper = {"outcome": copy.deepcopy(outcomes[index])}
        wrapped_case = {
            "set": {
                f"/outcome{pointer}": value
                for pointer, value in case.get("set", {}).items()
            },
            "remove": [f"/outcome{pointer}" for pointer in case.get("remove", [])],
        }
        mutated = apply_case(wrapper, wrapped_case)["outcome"]
        try:
            validate_standalone_outcomes([mutated], validators, registry)
        except ContractError as error:
            if error.code != case["expected_error"]:
                fail(
                    "fixtures.wrong_error",
                    f"{case['name']} expected {case['expected_error']}, "
                    f"got {error.code}: {error.message}",
                )
        else:
            fail("fixtures.false_negative", f"{case['name']} unexpectedly passed")


def validate_negative_registry_cases(
    registry: dict[str, Any],
    cases: list[dict[str, Any]],
) -> None:
    for case in cases:
        try:
            validate_registry(apply_case(registry, case))
        except ContractError as error:
            if error.code != case["expected_error"]:
                fail(
                    "fixtures.wrong_error",
                    f"{case['name']} expected {case['expected_error']}, "
                    f"got {error.code}: {error.message}",
                )
        else:
            fail("fixtures.false_negative", f"{case['name']} unexpectedly passed")


def validate_pilot_requests(
    root: Path,
    validators: dict[str, Draft202012Validator],
    registry: dict[str, Any],
) -> int:
    request_dir = (
        root / "commissions" / "2026-07-17-perplexity-research-pilot" / "requests"
    )
    request_ids: set[str] = set()
    count = 0
    for path in sorted(request_dir.glob("*.yaml")):
        request = load_data(path)
        validate_schema(validators, "request", request)
        validate_request_semantics(request)
        validate_profile_compatibility(request, "pro_research", registry)
        if request["request_id"] in request_ids:
            fail("pilot.request_id", f"duplicate request ID in {path}")
        request_ids.add(request["request_id"])
        if request["spend_ceiling"]["variable_cost"] != 0:
            fail("pilot.cost", f"{path} permits variable spend")
        count += 1
    if count != 4:
        fail("pilot.count", f"expected 4 pilot requests, found {count}")
    return count


def validate_portable_sanitized_material(label: str, text: str) -> None:
    for pattern in SENSITIVE_VALUE_PATTERNS:
        if pattern.search(text):
            fail(
                "handoff.sanitization",
                f"{label} contains credential-shaped material",
            )
    for pattern in LOCAL_ABSOLUTE_PATH_PATTERNS:
        if pattern.search(text):
            fail(
                "handoff.absolute_path",
                f"{label} contains a local absolute path",
            )


def validate_generated_handoffs(
    root: Path,
    validators: dict[str, Draft202012Validator],
    registry: dict[str, Any],
    execution_catalog_hash: str,
) -> int:
    pilot_root = root / "commissions" / "2026-07-17-perplexity-research-pilot"
    request_dir = pilot_root / "requests"
    handoff_dir = pilot_root / "handoffs"
    requests = {
        request["request_id"]: request
        for request in (load_data(path) for path in sorted(request_dir.glob("*.yaml")))
    }
    if set(requests) != PILOT_REQUEST_IDS:
        fail(
            "handoff.request_ids",
            "generated handoffs require the exact four pilot request IDs",
        )

    artifact_suffixes = {
        "outcome": ".outcome.json",
        "receipt": ".receipt.json",
        "prompt": ".prompt.md",
    }
    artifacts: dict[str, dict[str, Path]] = {}
    for kind, suffix in artifact_suffixes.items():
        paths = sorted(handoff_dir.glob(f"*{suffix}"))
        artifacts[kind] = {path.name.removesuffix(suffix): path for path in paths}
        if set(artifacts[kind]) != PILOT_REQUEST_IDS:
            fail(
                "handoff.artifact_ids",
                f"{kind} artifacts do not cover the exact pilot request IDs",
            )

    empty_manifest_hash = canonical_hash([])
    for request_id in sorted(PILOT_REQUEST_IDS):
        request = requests[request_id]
        outcome = load_data(artifacts["outcome"][request_id])
        receipt = load_data(artifacts["receipt"][request_id])
        validate_schema(validators, "outcome", outcome)
        validate_schema(validators, "receipt", receipt)
        validate_standalone_outcomes([outcome], validators, registry)

        if outcome["request_id"] != request_id or receipt["request_id"] != request_id:
            fail("handoff.request_id", f"{request_id} artifact IDs diverge")
        if (
            outcome["selected_profile"] != "pro_research"
            or receipt["selected_profile"] != "pro_research"
        ):
            fail("handoff.profile", f"{request_id} did not select pro_research")
        if outcome["outcome_type"] != "ManualHandoff":
            fail("handoff.outcome", f"{request_id} is not a ManualHandoff")
        if outcome["status"] != "ready":
            fail("handoff.status", f"{request_id} handoff is not ready")
        if receipt["outcome_type"] != "ManualHandoff":
            fail("handoff.receipt_outcome", f"{request_id} receipt type diverges")
        if receipt["verification"]["status"] != "manual_pending":
            fail("handoff.verification", f"{request_id} is not manual_pending")
        if receipt["usage"]["variable_cost"] != 0:
            fail("handoff.cost", f"{request_id} permits variable spend")
        if receipt["privacy"]["tracked_output_safe"] is not False:
            fail(
                "handoff.tracked_output",
                f"{request_id} claims a tracked report exists",
            )

        if receipt["request_hash"] != canonical_hash(request):
            fail("handoff.request_hash", f"{request_id} request hash diverges")
        if receipt["catalog_hash"] != execution_catalog_hash:
            fail("handoff.catalog_hash", f"{request_id} catalog hash diverges")
        if receipt["source_manifest_hash"] != empty_manifest_hash:
            fail(
                "handoff.source_manifest",
                f"{request_id} preliminary source manifest is not empty",
            )
        verification = receipt["verification"]
        for field in (
            "material_claims",
            "supported_material_claims",
            "resolvable_citations",
            "total_citations",
            "primary_source_citations",
        ):
            if verification[field] != 0:
                fail(
                    "handoff.verification_counts",
                    f"{request_id} preliminary {field} is not zero",
                )
        if verification["primary_source_ratio"] != 0:
            fail(
                "handoff.verification_counts",
                f"{request_id} preliminary primary-source ratio is not zero",
            )

        requested_output = request["output_contract"]
        durable_output = receipt["durable_output"]
        for field in ("owner_repo", "report_path", "receipt_path", "raw_export_ref"):
            if durable_output.get(field) != requested_output.get(field):
                fail(
                    "handoff.custody",
                    f"{request_id} durable {field} diverges from request",
                )
        if (
            outcome["preservation_tier"] != request["preservation_tier"]
            or receipt["privacy"]["preservation_tier"] != request["preservation_tier"]
        ):
            fail("handoff.preservation", f"{request_id} preservation diverges")
        if (
            outcome["external_transmission"] != request["external_transmission"]
            or receipt["privacy"]["external_transmission"]
            != request["external_transmission"]
        ):
            fail("handoff.transmission", f"{request_id} transmission diverges")
        if outcome["ingest_destination"] != requested_output.get("raw_export_ref"):
            fail("handoff.ingest", f"{request_id} ingest destination diverges")

        prompt_ref = outcome["prompt_ref"]
        assert_relative_path(prompt_ref, f"{request_id}.prompt_ref")
        expected_prompt_ref = f"{request_id}.prompt.md"
        if prompt_ref != expected_prompt_ref:
            fail("handoff.prompt_ref", f"{request_id} prompt reference diverges")
        prompt_path = handoff_dir / prompt_ref
        if (
            prompt_path.resolve().parent != handoff_dir.resolve()
            or not prompt_path.is_file()
            or prompt_path != artifacts["prompt"][request_id]
        ):
            fail("handoff.prompt_file", f"{request_id} prompt file is missing")
        prompt = prompt_path.read_text(encoding="utf-8")
        if (
            request["question"] not in prompt
            or f"# Limen Research commission: {request_id}" not in prompt
        ):
            fail("handoff.prompt_content", f"{request_id} prompt is not ready")

        instructions_ref = outcome["standing_instructions_ref"]
        assert_relative_path(
            instructions_ref,
            f"{request_id}.standing_instructions_ref",
        )
        if not (root / instructions_ref).is_file():
            fail(
                "handoff.instructions",
                f"{request_id} standing instructions are missing",
            )

        requested_at = parse_datetime(request["requested_at"], "request.requested_at")
        started_at = parse_datetime(
            receipt["retrieval_started_at"],
            f"{request_id}.retrieval_started_at",
        )
        finished_at = parse_datetime(
            receipt["retrieval_finished_at"],
            f"{request_id}.retrieval_finished_at",
        )
        verified_at = parse_datetime(
            verification["verified_at"],
            f"{request_id}.verification.verified_at",
        )
        if not requested_at <= started_at <= finished_at <= verified_at:
            fail("handoff.timestamps", f"{request_id} timestamps are out of order")

        serialized = json.dumps(
            {"outcome": outcome, "receipt": receipt},
            ensure_ascii=False,
            sort_keys=True,
        )
        validate_portable_sanitized_material(
            f"{request_id} outcome and receipt",
            serialized,
        )
        validate_portable_sanitized_material(f"{request_id} prompt", prompt)

    return len(PILOT_REQUEST_IDS)


def validate_execution_catalog_receipt(root: Path) -> str:
    path = (
        root
        / "commissions"
        / "2026-07-17-perplexity-research-pilot"
        / "execution-catalog-receipt.json"
    )
    receipt = load_data(path)
    expected_fields = {
        "schema_version",
        "owner_repo",
        "git_commit",
        "catalog_path",
        "catalog_hash",
        "profile_state_at_execution",
        "captured_at",
    }
    if not isinstance(receipt, dict) or set(receipt) != expected_fields:
        fail(
            "execution_catalog.fields",
            "execution catalog receipt fields diverge",
        )
    if (
        receipt["schema_version"] != "1.0"
        or receipt["owner_repo"] != "organvm/praxis-perpetua"
        or receipt["catalog_path"] != "governance/research-backend-profiles.yaml"
        or receipt["profile_state_at_execution"] != "enabled"
    ):
        fail(
            "execution_catalog.identity",
            "execution catalog receipt identity diverges",
        )
    if not isinstance(receipt["git_commit"], str) or not re.fullmatch(
        r"[0-9a-f]{40}",
        receipt["git_commit"],
    ):
        fail(
            "execution_catalog.commit",
            "execution catalog receipt lacks an exact Git commit",
        )
    catalog_hash = receipt["catalog_hash"]
    if not isinstance(catalog_hash, str) or not re.fullmatch(
        r"sha256:[0-9a-f]{64}",
        catalog_hash,
    ):
        fail(
            "execution_catalog.hash",
            "execution catalog receipt lacks a valid catalog hash",
        )
    if not isinstance(receipt["captured_at"], str):
        fail(
            "execution_catalog.timestamp",
            "execution catalog receipt timestamp is invalid",
        )
    parse_datetime(receipt["captured_at"], "execution_catalog.captured_at")
    validate_portable_sanitized_material(
        "execution catalog receipt",
        json.dumps(receipt, sort_keys=True),
    )
    return catalog_hash


def validate_pilot_status(root: Path) -> str:
    pilot_root = root / "commissions" / "2026-07-17-perplexity-research-pilot"
    status_path = pilot_root / "status.md"
    if not status_path.is_file():
        fail("pilot.status_file", "pilot status.md is missing")
    status = status_path.read_text(encoding="utf-8")
    if not status.startswith("---\n") or "\n---\n" not in status[4:]:
        fail("pilot.status_frontmatter", "pilot status lacks YAML frontmatter")
    frontmatter_text, body = status[4:].split("\n---\n", maxsplit=1)
    try:
        frontmatter = yaml.safe_load(frontmatter_text)
    except yaml.YAMLError as error:
        fail("pilot.status_frontmatter", f"pilot status YAML is invalid: {error}")
    expected_fields = {
        "schema_version",
        "commission_id",
        "state",
        "observed_at",
        "aggregate_evaluation_ref",
        "verdict",
        "variable_spend_usd",
    }
    if not isinstance(frontmatter, dict) or set(frontmatter) != expected_fields:
        fail(
            "pilot.status_frontmatter",
            "pilot status fields do not match the phase contract",
        )
    if (
        frontmatter["schema_version"] != "1.0"
        or frontmatter["commission_id"] != "INQ-2026-014"
    ):
        fail("pilot.status_identity", "pilot status identity is invalid")
    state = frontmatter["state"]
    if state not in PILOT_STATES:
        fail("pilot.status_state", f"unsupported pilot state {state!r}")
    observed_at = frontmatter["observed_at"]
    if not isinstance(observed_at, str):
        fail("pilot.status_timestamp", "pilot observed_at must be a string")
    parse_datetime(observed_at, "pilot.status.observed_at")
    for required in (
        f"- **State:** `{state}`",
        "- **Profile:** `pro_research`",
    ):
        if required not in body:
            fail("pilot.status_body", f"pilot status lacks {required!r}")

    aggregate_ref = frontmatter["aggregate_evaluation_ref"]
    verdict = frontmatter["verdict"]
    variable_spend = frontmatter["variable_spend_usd"]
    if (
        not isinstance(variable_spend, (int, float))
        or isinstance(variable_spend, bool)
        or variable_spend < 0
    ):
        fail("pilot.status_spend", "pilot variable spend is invalid")
    if state == "settled":
        if not isinstance(aggregate_ref, str) or not aggregate_ref:
            fail(
                "pilot.status_aggregate",
                "settled pilot status lacks an aggregate evaluation reference",
            )
        assert_relative_path(aggregate_ref, "pilot.status.aggregate_evaluation_ref")
        aggregate_path = root / aggregate_ref
        if not aggregate_path.is_file():
            fail(
                "pilot.status_aggregate",
                "settled pilot aggregate evaluation is missing",
            )
        aggregate = load_data(aggregate_path)
        try:
            validate_aggregate_record(aggregate)
        except PilotAggregateError as error:
            fail(
                "pilot.status_aggregate",
                f"aggregate evaluation is invalid: {error}",
            )
        if aggregate["state"] != "settled":
            fail(
                "pilot.status_aggregate",
                "settled pilot status points to a non-terminal aggregate",
            )
        if verdict != aggregate["verdict"]:
            fail(
                "pilot.status_verdict",
                "pilot status verdict diverges from its aggregate",
            )
        aggregate_spend = aggregate["criteria"]["variable_perplexity_spend_usd"][
            "observed"
        ]
        if not math.isclose(
            float(variable_spend),
            float(aggregate_spend),
            rel_tol=0,
            abs_tol=1e-9,
        ):
            fail(
                "pilot.status_spend",
                "pilot status spend diverges from its aggregate",
            )
        registry = load_data(root / "governance" / "research-backend-profiles.yaml")
        request_dir = pilot_root / "requests"
        requests = sorted(
            (load_data(path) for path in request_dir.glob("*.yaml")),
            key=lambda request: request["request_id"],
        )
        if aggregate["catalog_hash"] != canonical_hash(registry):
            fail(
                "pilot.status_aggregate",
                "aggregate catalog hash diverges from the canonical registry",
            )
        if aggregate["requests_hash"] != canonical_hash(requests):
            fail(
                "pilot.status_aggregate",
                "aggregate request-set hash diverges",
            )
        request_map = {request["request_id"]: request for request in requests}
        for run in aggregate["runs"]:
            expected = request_map[run["request_id"]]["output_contract"]
            for field in ("owner_repo", "report_path", "receipt_path"):
                if run[field] != expected[field]:
                    fail(
                        "pilot.status_aggregate",
                        f"{run['request_id']} aggregate {field} diverges",
                    )
        if parse_datetime(
            aggregate["evaluated_at"],
            "pilot.aggregate.evaluated_at",
        ) > parse_datetime(observed_at, "pilot.status.observed_at"):
            fail(
                "pilot.status_timestamp",
                "pilot status predates its aggregate evaluation",
            )
    else:
        if aggregate_ref is not None:
            fail(
                "pilot.status_aggregate",
                f"{state} pilot status cannot claim a terminal aggregate",
            )
        if verdict is not None:
            fail(
                "pilot.status_verdict",
                f"{state} pilot status cannot claim a terminal verdict",
            )
        if not math.isclose(
            float(variable_spend),
            0.0,
            rel_tol=0,
            abs_tol=1e-9,
        ):
            fail(
                "pilot.status_spend",
                f"{state} pilot status must retain the zero-spend pre-run fact",
            )
    rendered_verdict = verdict if verdict is not None else "pending"
    rendered_spend = f"{float(variable_spend):g}"
    for required in (
        f"- **Verdict:** `{rendered_verdict}`",
        f"- **Variable spend:** USD {rendered_spend}",
    ):
        if required not in body:
            fail("pilot.status_body", f"pilot status lacks {required!r}")
    validate_portable_sanitized_material("pilot status", status)
    return str(state)


def run(root: Path) -> None:
    validators = schema_validators(root)
    registry = load_data(root / "governance" / "research-backend-profiles.yaml")
    validate_registry(registry)

    fixture_dir = root / "tests" / "research-backend" / "fixtures"
    bundle = load_data(fixture_dir / "valid-bundle.json")
    bundle["attestation"] = load_data(
        fixture_dir / "valid-source-verifier-attestation.json"
    )
    bundle["sanitization_attestation"] = load_data(
        fixture_dir / "valid-output-sanitization-attestation.json"
    )
    bundle["raw_export"] = (fixture_dir / "valid-export.md").read_text(encoding="utf-8")
    bundle["tracked_report"] = (fixture_dir / "valid-tracked-report.md").read_text(
        encoding="utf-8"
    )
    validate_bundle(bundle, validators, registry)
    standalone = load_data(fixture_dir / "valid-standalone-outcomes.json")
    validate_standalone_outcomes(standalone["outcomes"], validators, registry)
    negative = load_data(fixture_dir / "negative-cases.yaml")
    validate_negative_cases(bundle, negative["cases"], validators, registry)
    validate_negative_outcome_cases(
        standalone["outcomes"],
        negative["outcome_cases"],
        validators,
        registry,
    )
    validate_negative_registry_cases(registry, negative["registry_cases"])
    request_count = validate_pilot_requests(root, validators, registry)
    execution_catalog_hash = validate_execution_catalog_receipt(root)
    handoff_count = validate_generated_handoffs(
        root,
        validators,
        registry,
        execution_catalog_hash,
    )
    pilot_state = validate_pilot_status(root)

    print("OK research schemas: 5")
    print("OK SourceVerifierAttestation contract: 1")
    print("OK OutputSanitizationAttestation contract: 1")
    print(f"OK profile registry: {len(registry['profiles'])} profiles")
    print(f"OK pilot requests: {request_count}")
    print(f"OK generated ManualHandoffs: {handoff_count}")
    print(f"OK phase-aware pilot status: {pilot_state}")
    print(f"OK standalone outcomes: {len(standalone['outcomes'])}")
    negative_count = (
        len(negative["cases"])
        + len(negative["outcome_cases"])
        + len(negative["registry_cases"])
    )
    print(f"OK negative semantic fixtures: {negative_count}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="Praxis repository root",
    )
    args = parser.parse_args()
    try:
        run(args.root.resolve())
    except ContractError as error:
        print(f"FAIL {error}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
