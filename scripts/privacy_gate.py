#!/usr/bin/env python3
"""Fail closed when likely gated genomic data or secrets enter the public tree."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

from validate_submission import validate

BANNED_DIRECTORIES = {"data", "raw", "private", "work", "logs", "tmp"}
BANNED_SUFFIXES = {
    ".vcf", ".bcf", ".tbi", ".csi", ".bam", ".bai", ".cram", ".crai",
    ".fastq", ".fq", ".gvcf", ".ped", ".fam", ".docx",
}
SECRET_PATTERNS = {
    "Hugging Face token": re.compile(r"hf_[A-Za-z0-9]{20,}"),
    "GitHub token": re.compile(r"gh[opsu]_[A-Za-z0-9]{20,}"),
    "private key": re.compile(r"BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY"),
}
MAX_PUBLIC_FILE_BYTES = 5 * 1024 * 1024


def iter_public_files(root: Path):
    for path in sorted(root.rglob("*")):
        if not path.is_file() or ".git" in path.parts or "__pycache__" in path.parts:
            continue
        yield path


def check(root: Path) -> list[str]:
    errors: list[str] = []
    for path in iter_public_files(root):
        relative = path.relative_to(root)
        if any(part in BANNED_DIRECTORIES for part in relative.parts[:-1]):
            errors.append(f"banned directory: {relative}")
        suffixes = "".join(path.suffixes).lower()
        if path.suffix.lower() in BANNED_SUFFIXES or any(
            suffixes.endswith(item + ".gz") for item in BANNED_SUFFIXES
        ):
            errors.append(f"banned genomic/private extension: {relative}")
        if path.stat().st_size > MAX_PUBLIC_FILE_BYTES:
            errors.append(f"file exceeds 5 MiB public limit: {relative}")

        if relative.as_posix() == "scripts/privacy_gate.py":
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            errors.append(f"unexpected binary file: {relative}")
            continue
        for label, pattern in SECRET_PATTERNS.items():
            if pattern.search(text):
                errors.append(f"possible {label}: {relative}")

    prediction = root / "results" / "MarxistLeninist_bub1b_compound_het.csv"
    if prediction.exists():
        errors.extend(f"submission: {item}" for item in validate(prediction))
    else:
        errors.append("missing public Track 1 prediction CSV")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", nargs="?", default=".", type=Path)
    args = parser.parse_args()
    errors = check(args.root.resolve())
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print("PASS: public-release privacy gate")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

