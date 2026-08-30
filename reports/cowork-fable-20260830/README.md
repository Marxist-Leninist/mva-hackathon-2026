# Track 2 — Cowork lane, 30 August 2026

Independent Track 2 report produced in the Cowork/Claude lane. **This is an additional
report, not a replacement.** `reports/MarxistLeninist_track2_report.md` at the repository
root was claimed by another agent lane and has not been modified by this lane.

## Contents

| File | What it is |
|---|---|
| `MarxistLeninist_track2_report.md` / `.pdf` | The report, 16 pages, ~12,000 words |
| `track2_candidate_evidence_ledger.tsv` | 37 evaluated candidates with evidence tiers and verdicts |
| `figure1_gates.svg` | Development plan and go/no-go gates |
| `figure2_strategies.png` | Monte Carlo: probability each strategy restores enough BubR1 |
| `figure3_sensitivity.png` | Which unknown decides the outcome |
| `dosage_results.json` | Raw model output |
| `../../scripts/cowork-fable-20260830/` | Everything needed to reproduce the computation |

## What is new in this lane

1. **BUB1B exon 17 is a clean in-frame skip.** 141 nt, phase 1/1, and the junction codon
   after skipping reconstitutes wild-type Gly762 exactly — so skipping deletes residues
   715–761 with no novel amino acid, removes the premature stop, and removes the NMD
   substrate. Verified against GRCh38 reference sequence; splice sites confirmed canonical.
2. **Four designed splice-switching oligonucleotides**, including an allele-selective
   candidate (ASO-4) carrying a single central mismatch against the wild-type allele.
3. **A 400,000-draw dosage model** which demotes small-molecule readthrough (2,6-DAP class)
   at this UGA-A context and promotes ACE-tRNA-Leu + gene-specific NMD ASO.
4. **AlphaFold analysis** showing p.Asn1002Lys is buried in the pseudokinase aromatic core
   (pLDDT 91, 27 neighbours within 8 Å) — consistent with a destabilising, turnover-limited
   allele — and that the exon-17 segment is not a free linker (113 long-range contacts).
5. **Two clinically actionable outputs requiring no new drug**: a cardiac surveillance gap
   in current MVA guidance, and a written contraindication card.
6. **Adversarial review**, logged in §B.10, including a risk none of the four reports had
   raised: partial correction may move the child from a tumour-suppressive high-missegregation
   regime into the tumour-promoting intermediate regime (Silk 2013, PMID 24133140).

## Reproduce

```
python3 scripts/cowork-fable-20260830/bubr1_dosage_sim.py
python3 scripts/cowork-fable-20260830/aso_design.py
python3 scripts/cowork-fable-20260830/build_ledger.py
```

No credentials are stored in this directory or anywhere in this repository.
