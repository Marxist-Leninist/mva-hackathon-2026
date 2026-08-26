# Allele-resolved rescue screening for BUB1B-associated MVA1

This repository contains the public, reproducible submission package for the
2026 **Rare Disease, Real Kid: MVA Hackathon**. It has two linked outputs:

1. A Track 1 prediction of a compound-heterozygous `BUB1B` pair.
2. A Track 2 proposal that tests upstream rescue of each allele before testing
   downstream protection from aneuploidy-induced stress.

The result is a research hypothesis, not a cure or a treatment recommendation.
No medicine should be given on the basis of this repository.

## Headline result

| Allele | GRCh38 | Transcript consequence | Evidence status |
|---|---|---|---|
| 1 | `chr15:40209701 T>G` | `NM_001211.6:c.2210T>G`, `p.Leu737Ter` | High-quality heterozygous call; ClinVar P/LP; predicted NMD |
| 2 | `chr15:40220612 T>G` | `NM_001211.6:c.3006T>G`, `p.Asn1002Lys` | High-quality heterozygous call; absent from gnomAD; exact allele is unclassified |

The alleles are 10,911 bp apart. Short reads do not establish phase and parental
data were not supplied, so **in trans is inferred, not proven**. The second
allele remains a VUS in isolation until segregation or functional evidence is
available.

The ready-to-upload Track 1 file is
[`results/MarxistLeninist_bub1b_compound_het.csv`](results/MarxistLeninist_bub1b_compound_het.csv).

## Track 2 concept

The proposal is an experimentally gated, three-axis screen:

- **Read through the nonsense allele:** gentamicin is an approved aminoglycoside
  with human proof-of-concept for premature-stop readthrough. The exact BUB1B
  context is `UGA-A`; it must be tested directly because NMD and the +4 base may
  sharply limit rescue.
- **Stabilize the missense allele:** arimoclomol is FDA-approved for NPC and
  amplifies a stress-induced heat-shock response. This is an indirect bridge,
  not evidence that it rescues `p.Asn1002Lys`.
- **Test an orthogonal abundance pathway:** prescription nicotinic acid is an
  approved NAD precursor, while NMN/SIRT2 increased BUBR1 abundance in mice.
  Niacin is not NMN, so this remains a biomarker-gated comparator.
- **Buffer downstream proteotoxic stress:** sirolimus (rapamycin) is the only
  approved candidate in the shortlist with drug-level rescue in a 2026 fly
  model of SAC-loss MVA-like microcephaly. It does not repair chromosome
  segregation and carries major immunosuppression and cancer-risk caveats.

Candidates advance only if they restore BUBR1 abundance or checkpoint function,
reduce *new* chromosome-segregation errors, work near approved human exposure,
and do not preferentially preserve premalignant aneuploid cells.

## Reproduce public checks

Python 3.11+ is sufficient; no patient data or third-party package is required.

```bash
make check

python scripts/readthrough_context.py \
  --wild-type-codon TTA --codon-position 2 --alternate G --plus-four A

python scripts/structure_context.py AF-O60566-F1-model_v6.pdb --residue 1002
```

The last command is optional and requires the public AlphaFold model linked in
the Track 2 report. Structural output is explicitly hypothesis-generating.

## Repository map

- `reports/MarxistLeninist_track1_report.md` - variant analysis and limitations
- `reports/MarxistLeninist_track2_report.md` - drug rationale and validation plan
- `reports/pitch_script.md` - approximately three-minute narration
- `results/` - submission CSV and public evidence/provenance records
- `scripts/` - submission validator, privacy gate, and reproducible context checks
- `tests/` - synthetic/unit tests only
- `DATA_GOVERNANCE.md` - release boundary and privacy safeguards

## Data boundary

The gated genome, phenotype document, read evidence, sample-wide annotations,
and intermediate files are deliberately absent. The repository publishes only
the minimum derived facts needed for the competition. Run `make privacy` before
every public commit.

## Acknowledgement

This work was made possible through the Hackathon, organized by Sage
Bionetworks in partnership with the MVA Society, Hugging Face, and BEACON (The
Benchmarking, Evaluation, and Assessment Consortium for Science), with prize
sponsorship from AWS and Anthropic. We are deeply grateful to the child and
their family who generously contributed their data and their story to advance
research into this rare disease. We acknowledge their trust in making this
Hackathon possible.

Released under [CC BY 4.0](LICENSE). The underlying gated dataset has separate,
more restrictive terms and is not redistributed here.
