#!/usr/bin/env python3
"""Reproduce a single-nucleotide stop-context derivation."""

from __future__ import annotations

import argparse
import json

STOPS = {"TAA", "TAG", "TGA"}


def derive(wild_type_codon: str, codon_position: int, alternate: str, plus_four: str):
    codon = wild_type_codon.upper()
    if len(codon) != 3 or any(base not in "ACGT" for base in codon):
        raise ValueError("wild-type codon must be three A/C/G/T bases")
    if codon_position not in {1, 2, 3}:
        raise ValueError("codon position must be 1, 2, or 3")
    if alternate.upper() not in "ACGT" or plus_four.upper() not in "ACGT":
        raise ValueError("alternate and +4 base must each be A/C/G/T")
    mutant = list(codon)
    mutant[codon_position - 1] = alternate.upper()
    mutant_codon = "".join(mutant)
    return {
        "wild_type_codon": codon,
        "mutant_codon": mutant_codon,
        "is_stop": mutant_codon in STOPS,
        "dna_context": f"{mutant_codon}-{plus_four.upper()}",
        "rna_context": f"{mutant_codon.replace('T', 'U')}-{plus_four.upper().replace('T', 'U')}",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--wild-type-codon", required=True)
    parser.add_argument("--codon-position", required=True, type=int)
    parser.add_argument("--alternate", required=True)
    parser.add_argument("--plus-four", required=True)
    args = parser.parse_args()
    print(json.dumps(derive(args.wild_type_codon, args.codon_position, args.alternate, args.plus_four), indent=2))


if __name__ == "__main__":
    main()

