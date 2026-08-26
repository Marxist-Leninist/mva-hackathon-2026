#!/usr/bin/env python3
"""Correct the 'absent from gnomAD' claim about BUB1B p.Asn1002Lys.

The claim is false and checkable in under a minute by anyone on the judging
panel. gnomAD v4 exomes report 15-40220612-T-G at AC=1, AN=1,461,878
(AF 6.84e-07). It is absent from gnomAD *genomes* only.

The error's origin is worth stating because it is a general trap: Ensembl VEP
REST returns no frequency record for this allele, and a pipeline that reads a
missing annotation as a confirmed zero will report it as absent. Missing and
zero are different claims.

Rarity evidence is unaffected in substance — one allele in 1.46 million is
still ultra-rare and still supports ACMG PM2 — but at Supporting strength per
ClinGen SVI 2020, not Moderate.

Each replacement below is exact-match and asserted, so this fails loudly rather
than silently no-op'ing if the surrounding text has moved.
"""
import sys

REPLACEMENTS = [
    (
        "README.md",
        "High-quality heterozygous call; absent from gnomAD; exact allele is unclassified",
        "High-quality heterozygous call; gnomAD v4 exomes AC=1 / AN=1,461,878 "
        "(AF 6.8e-07), absent from gnomAD genomes; exact allele is unclassified",
    ),
    (
        "results/public_evidence_matrix.tsv",
        "Absent from gnomAD; deleterious in silico; final-exon kinase-domain location",
        "gnomAD v4 exomes AF 6.8e-07 (AC=1/AN=1461878), absent from genomes; "
        "deleterious in silico; final-exon kinase-domain location",
    ),
    (
        "reports/pitch_script_3min_opus5.md",
        "> and a novel missense at asparagine 1002, absent from gnomAD, sitting in the\n"
        "> pseudokinase domain.",
        "> and a novel missense at asparagine 1002 — one allele in one and a half million —\n"
        "> sitting in the pseudokinase domain.",
    ),
    (
        "reports/MarxistLeninist_track2_report.md",
        "- `p.Asn1002Lys` is a full-length, gnomAD-absent missense change in the\n"
        "  C-terminal kinase/pseudokinase region.",
        "- `p.Asn1002Lys` is a full-length missense change in the C-terminal\n"
        "  kinase/pseudokinase region, at gnomAD v4 exome AF 6.8e-07 (AC=1 / AN=1,461,878)\n"
        "  and absent from gnomAD genomes.",
    ),
]


def main():
    failures = []
    for path, old, new in REPLACEMENTS:
        text = open(path, encoding="utf-8").read()
        if old not in text:
            failures.append(f"{path}: expected text not found (already fixed, or moved)")
            continue
        if text.count(old) != 1:
            failures.append(f"{path}: expected exactly 1 occurrence, found {text.count(old)}")
            continue
        open(path, "w", encoding="utf-8").write(text.replace(old, new))
        print(f"fixed {path}")
    if failures:
        print("\nNOT APPLIED:", file=sys.stderr)
        for f in failures:
            print("  " + f, file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
