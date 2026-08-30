#!/usr/bin/env python3
"""Finalize non-scientific Track 2 metadata from current authoritative sources.

This script is deliberately idempotent. It corrects two coordination defects:

1. The challenge dataset is the gated Hugging Face dataset
   ``SageBio/mva-hackathon-2026-data``; no current competition material names a
   Synapse project that must be cited.
2. The provider plan tiers are now known: OpenAI ChatGPT Pro and Anthropic Claude
   Max 20x (including Claude Code). The account-level training/retention settings
   remain participant-controlled and must still be verified.

It never changes scientific candidate rankings or experimental conclusions.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "reports" / "MarxistLeninist_track2_report.md"
METHODS = ROOT / "methods" / "MarxistLeninist_track2_methods_update_20260830.md"
README = ROOT / "README.md"
CHECKLIST = ROOT / "SUBMISSION_CHECKLIST.md"
STATUS = ROOT / "FINAL_STATUS.json"
MANIFEST = ROOT / "competition" / "CANONICAL.json"
VERSION = "2026-08-30.4"


def replace_once(text: str, old: str, new: str, label: str) -> str:
    if new in text:
        return text
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: expected one old block, found {count}")
    return text.replace(old, new, 1)


def write_text(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8")
    print(f"updated {path.relative_to(ROOT)}")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def update_report() -> None:
    text = REPORT.read_text(encoding="utf-8")
    text = replace_once(
        text,
        """OpenAI ChatGPT Pro (GPT-5.6 Pro) and Anthropic Claude Code/Claude models under a paid individual subscription were used for drafting, code review, candidate generation, and adversarial scientific review. **The exact account-level model-training and retention/data-control settings active during those sessions were not recorded in the repository and must be inserted by the participant before submission.** No claim of \"no training\" is made without that verification.""",
        """OpenAI ChatGPT Pro (GPT-5.6 Pro) and Anthropic Claude Max 20x, including Claude Code, were used for drafting, code review, candidate generation, and adversarial scientific review. **The exact account-level model-training, retention, and data-control settings active during those sessions were not recorded in the repository and must be verified by the participant before submission.** No claim of \"no training\" is made without that verification.""",
        "report AI disclosure",
    )
    text = replace_once(
        text,
        """# Dataset citation

**Participant action before submission:** insert the exact Synapse dataset citation supplied with the controlled Hackathon data-access record. The repository deliberately does not reproduce gated data.""",
        """# Dataset citation

Sage Bionetworks. *Rare Disease, Real Kid: MVA Hackathon 2026 - Dataset*. Hugging Face dataset `SageBio/mva-hackathon-2026-data`, accessed 30 August 2026. https://huggingface.co/datasets/SageBio/mva-hackathon-2026-data. Access is gated; the dataset is listed under CC BY 4.0 and remains subject to the Hackathon data-use conditions. The repository deliberately does not reproduce gated data.""",
        "official dataset citation",
    )
    write_text(REPORT, text)


def update_methods() -> None:
    text = METHODS.read_text(encoding="utf-8")
    text = replace_once(
        text,
        """OpenAI ChatGPT Pro (GPT-5.6 Pro) and Anthropic Claude Code/Claude models under a
paid individual subscription were used for drafting, code review, candidate
generation and adversarial scientific review.

**Participant action before submission:** confirm and insert the exact Anthropic
plan/tier and the account-level training, retention or data-control setting that
applied to both providers during the relevant sessions. No generic \"no training\"
claim should be made without verifying those settings.""",
        """OpenAI ChatGPT Pro (GPT-5.6 Pro) and Anthropic Claude Max 20x, including
Claude Code, were used for drafting, code review, candidate generation and
adversarial scientific review.

**Participant action before submission:** confirm and record the account-level
training, retention or data-control setting that applied to both providers during
the relevant sessions. No generic \"no training\" claim should be made without
verifying those settings.""",
        "methods AI disclosure",
    )
    dataset_sentence = (
        "\n\nThe controlled challenge data source is the gated Hugging Face dataset "
        "`SageBio/mva-hackathon-2026-data`, accessed 30 August 2026; gated data "
        "are not redistributed."
    )
    anchor = "Gated genomic and identifiable clinical data are\nnot redistributed."
    if dataset_sentence.strip() not in text:
        if text.count(anchor) != 1:
            raise RuntimeError("methods dataset anchor missing or duplicated")
        text = text.replace(anchor, anchor + dataset_sentence, 1)
    write_text(METHODS, text)


def update_readme() -> None:
    text = README.read_text(encoding="utf-8")
    text = replace_once(
        text,
        """The remaining participant-controlled requirements are:

- confirm the exact provider plan/tier and account-level data-handling setting
  for every AI assistant used;
- insert the exact Synapse dataset citation;
- host the reviewed MP4 on YouTube or Vimeo; and
- explicitly authorize the exact canonical version before a submission slot is
  used.""",
        """The remaining participant-controlled requirements are:

- confirm the exact account-level training, retention and data-handling settings
  that applied to the OpenAI ChatGPT Pro and Anthropic Claude Max 20x sessions;
- host the reviewed MP4 on YouTube or Vimeo; and
- explicitly authorize the exact canonical version before a submission slot is
  used.""",
        "README remaining requirements",
    )
    citation = (
        "\n\nThe controlled data source is the gated Hugging Face dataset "
        "`SageBio/mva-hackathon-2026-data`, accessed 30 August 2026."
    )
    anchor = "Run `make privacy` before\nevery public commit."
    if citation.strip() not in text:
        if text.count(anchor) != 1:
            raise RuntimeError("README data-boundary anchor missing or duplicated")
        text = text.replace(anchor, anchor + citation, 1)
    write_text(README, text)


def update_checklist() -> None:
    text = CHECKLIST.read_text(encoding="utf-8")
    text = replace_once(
        text,
        """- [ ] Insert the exact Synapse dataset citation supplied with the controlled
      Hackathon data-access record.
- [ ] Confirm the exact provider plan/tier used for each AI assistant.
- [ ] Confirm and record the relevant account-level training/retention/data-
      handling setting that applied during each AI-assisted session.""",
        """- [x] Provider plans verified: OpenAI ChatGPT Pro and Anthropic Claude Max
      20x, including Claude Code.
- [ ] Confirm and record the relevant account-level training/retention/data-
      handling setting that applied during each AI-assisted session.""",
        "checklist participant fields",
    )
    text = replace_once(
        text,
        "Confirm the AI disclosure and Synapse citation are complete.",
        "Confirm the AI account-level data-handling disclosure is complete.",
        "checklist authorization wording",
    )
    write_text(CHECKLIST, text)


def update_status_and_manifest() -> None:
    status = json.loads(STATUS.read_text(encoding="utf-8"))
    status["canonical_version"] = VERSION
    track2 = status.setdefault("track2", {})
    track2["ai_disclosure"] = (
        "plans verified as OpenAI ChatGPT Pro and Anthropic Claude Max 20x "
        "including Claude Code; exact account-level data-handling settings pending"
    )
    track2.pop("synapse_dataset_citation", None)
    track2["dataset_citation"] = (
        "SageBio/mva-hackathon-2026-data on Hugging Face; gated; accessed "
        "30 August 2026"
    )
    status["release"]["track2_hackathon_submission"] = (
        "not submitted; hosted video, verified AI account-level settings and "
        "explicit authorization remain"
    )
    STATUS.write_text(json.dumps(status, indent=2) + "\n", encoding="utf-8")
    print(f"updated {STATUS.relative_to(ROOT)}")

    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    manifest["canonical_version"] = VERSION
    report_spec = manifest["track2"]["report_markdown"]
    report_spec["status"] = "ready"
    report_spec["sha256"] = sha256(REPORT)
    manifest["open_blockers"] = [
        "Confirm exact account-level training, retention and data-control settings for OpenAI and Anthropic sessions",
        "Upload final video to YouTube or Vimeo",
        "Obtain explicit participant authorization before using a submission slot",
    ]
    MANIFEST.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(f"updated {MANIFEST.relative_to(ROOT)}")
    print(f"report markdown sha256={report_spec['sha256']}")


def main() -> int:
    update_report()
    update_methods()
    update_readme()
    update_checklist()
    update_status_and_manifest()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
