#!/usr/bin/env python3
"""Validate the single-source-of-truth manifest for the MVA competition."""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / "competition" / "CANONICAL.json"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def safe_path(value: str) -> Path:
    candidate = Path(value)
    if candidate.is_absolute() or ".." in candidate.parts:
        raise ValueError(f"unsafe manifest path: {value}")
    resolved = (ROOT / candidate).resolve()
    if ROOT not in resolved.parents and resolved != ROOT:
        raise ValueError(f"path escapes repository: {value}")
    return resolved


def check_artifact(label: str, spec: object, errors: list[str]) -> None:
    if isinstance(spec, str):
        path = safe_path(spec)
        if not path.exists():
            errors.append(f"missing {label}: {spec}")
        return

    if not isinstance(spec, dict) or not isinstance(spec.get("path"), str):
        errors.append(f"invalid {label} manifest entry")
        return

    path = safe_path(spec["path"])
    status = spec.get("status", "ready")
    expected = spec.get("sha256")

    if status == "ready" and not path.exists():
        errors.append(f"ready {label} is missing: {spec['path']}")
        return
    if not path.exists():
        return

    if expected:
        actual = sha256(path)
        if actual != expected:
            errors.append(
                f"{label} sha256 mismatch: expected {expected}, got {actual}"
            )
    elif status == "ready":
        errors.append(f"ready {label} has no sha256: {spec['path']}")


def main() -> int:
    errors: list[str] = []

    if not MANIFEST_PATH.exists():
        print("ERROR: missing competition/CANONICAL.json", file=sys.stderr)
        return 1

    try:
        data = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"ERROR: cannot parse canonical manifest: {exc}", file=sys.stderr)
        return 1

    if data.get("schema_version") != 1:
        errors.append("unsupported or missing schema_version")
    if data.get("team") != "MarxistLeninist":
        errors.append("unexpected team value")

    rules = data.get("rules", {})
    required_true = (
        "single_track2_report",
        "alternate_reports_forbidden",
        "all_agents_must_read_manifest_first",
        "all_changes_must_target_the_canonical_paths",
        "submission_requires_explicit_participant_authorization",
    )
    for rule in required_true:
        if rules.get(rule) is not True:
            errors.append(f"required rule is not true: {rule}")

    track2 = data.get("track2")
    if not isinstance(track2, dict):
        errors.append("missing track2 object")
        track2 = {}

    report_spec = track2.get("report_markdown")
    if not isinstance(report_spec, dict) or not isinstance(report_spec.get("path"), str):
        errors.append("track2.report_markdown must contain path and sha256")
        canonical_report = None
    else:
        canonical_report = safe_path(report_spec["path"])
        check_artifact("Track 2 Markdown report", report_spec, errors)

    for key, label in (
        ("report_pdf", "Track 2 PDF report"),
        ("pitch_video", "Track 2 pitch video"),
        ("methods", "Track 2 methods"),
        ("pitch_source", "Track 2 pitch source"),
        ("submission_checklist", "submission checklist"),
    ):
        if key not in track2:
            errors.append(f"missing track2.{key}")
        else:
            check_artifact(label, track2[key], errors)

    # Enforce one editable Track 2 report source. Supporting addenda and pitch
    # scripts may exist, but a second *track2*report*.md is a hard failure.
    report_candidates = {
        path.resolve()
        for base in (ROOT / "reports", ROOT / "competition")
        if base.exists()
        for path in base.rglob("*.md")
        if "track2" in path.name.lower() and "report" in path.name.lower()
    }
    if canonical_report:
        unexpected = sorted(path for path in report_candidates if path != canonical_report)
        for path in unexpected:
            errors.append(
                "alternate Track 2 report source forbidden: "
                + str(path.relative_to(ROOT))
            )

    if canonical_report and canonical_report.exists():
        text = canonical_report.read_text(encoding="utf-8")
        required_phrases = (
            "phase and the exact effect of the missense allele remain unconfirmed",
            "no drug, dose, treatment change, or off-label use is recommended",
            "scenario analysis",
            "rescue-versus-clone-safety",
        )
        for phrase in required_phrases:
            if phrase.lower() not in text.lower():
                errors.append(f"canonical report missing safety phrase: {phrase}")

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print("PASS: one canonical MVA competition submission")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
