#!/usr/bin/env python3
"""Validate the exact public Track 1 CSV contract without external packages."""

from __future__ import annotations

import argparse
import csv
import re
import sys
from pathlib import Path

COLUMNS = [
    "proband_id",
    "chrom_1",
    "pos_1",
    "ref_1",
    "alt_1",
    "chrom_2",
    "pos_2",
    "ref_2",
    "alt_2",
    "epcr",
    "finding_type",
    "notes",
]
CHROMOSOME = re.compile(r"^chr(?:[1-9]|1[0-9]|2[0-2]|X|Y|M|MT)$")
ALLELE = re.compile(r"^[ACGTN]+$")


def _positive_integer(value: str, field: str, row_number: int) -> int:
    try:
        parsed = int(value)
    except ValueError as exc:
        raise ValueError(f"row {row_number}: {field} must be an integer") from exc
    if parsed < 1:
        raise ValueError(f"row {row_number}: {field} must be positive")
    return parsed


def validate(path: Path) -> list[str]:
    errors: list[str] = []
    with path.open(newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != COLUMNS:
            return [f"header must be exactly: {','.join(COLUMNS)}"]
        rows = list(reader)

    if not 1 <= len(rows) <= 10:
        errors.append(f"submission must contain 1-10 rows; found {len(rows)}")

    previous_epcr = float("inf")
    seen: set[tuple[str, ...]] = set()
    for number, row in enumerate(rows, start=2):
        try:
            if not row["proband_id"].strip():
                raise ValueError(f"row {number}: proband_id is required")
            if not CHROMOSOME.fullmatch(row["chrom_1"]):
                raise ValueError(f"row {number}: invalid chrom_1")
            _positive_integer(row["pos_1"], "pos_1", number)
            for field in ("ref_1", "alt_1"):
                if not ALLELE.fullmatch(row[field]):
                    raise ValueError(f"row {number}: {field} must contain A/C/G/T/N only")

            second = [row[name].strip() for name in ("chrom_2", "pos_2", "ref_2", "alt_2")]
            if any(second) and not all(second):
                raise ValueError(f"row {number}: compound-pair fields must be all filled or all blank")
            if all(second):
                if not CHROMOSOME.fullmatch(row["chrom_2"]):
                    raise ValueError(f"row {number}: invalid chrom_2")
                _positive_integer(row["pos_2"], "pos_2", number)
                for field in ("ref_2", "alt_2"):
                    if not ALLELE.fullmatch(row[field]):
                        raise ValueError(f"row {number}: {field} must contain A/C/G/T/N only")

            epcr = float(row["epcr"])
            if not 0 < epcr <= 1:
                raise ValueError(f"row {number}: epcr must be in (0, 1]")
            if epcr > previous_epcr:
                raise ValueError(f"row {number}: rows must be ordered by non-increasing epcr")
            previous_epcr = epcr

            if row["finding_type"] not in {"primary", "secondary"}:
                raise ValueError(f"row {number}: finding_type must be primary or secondary")

            key = tuple(row[name] for name in COLUMNS[1:9])
            if key in seen:
                raise ValueError(f"row {number}: duplicate variant or pair")
            seen.add(key)
        except ValueError as exc:
            errors.append(str(exc))
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("csv_path", type=Path)
    args = parser.parse_args()
    errors = validate(args.csv_path)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print(f"PASS: {args.csv_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

