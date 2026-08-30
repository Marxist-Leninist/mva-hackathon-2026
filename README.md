# Allele-resolved rescue screening for candidate BUB1B-associated MVA1

This repository contains the public, reproducible submission package for the
2026 **Rare Disease, Real Kid: The MVA Hackathon**. It has two linked outputs:

1. A Track 1 prediction of a candidate biallelic `BUB1B` pair.
2. A Track 2 proposal for a falsifiable, exposure-aware patient-cell drug screen.

The result is a research hypothesis, not a cure or a treatment recommendation.
No medicine, dose, off-label use, or change to current oncology care follows
from this repository.

## Headline result

| Allele | GRCh38 | Transcript consequence | Evidence status |
|---|---|---|---|
| 1 | `chr15:40209701 T>G` | `NM_001211.6:c.2210T>G`, `p.Leu737Ter` | High-quality heterozygous call; ClinVar P/LP; predicted NMD |
| 2 | `chr15:40220612 T>G` | `NM_001211.6:c.3006T>G`, `p.Asn1002Lys` | High-quality heterozygous call; gnomAD v4 exomes AC=1 / AN=1,461,878 (AF 6.8e-07), absent from gnomAD genomes; exact allele unclassified |

Both variants were independently confirmed from all eight raw FASTQ lanes by
exact 31-mer counting, without using the supplied variant caller. They are
10,911 bp apart. Short reads do not establish phase and parental data were not
supplied, so **in trans is inferred, not proven**. The second allele remains a
VUS in isolation until segregation or functional evidence is available.

The ready-to-upload Track 1 file is
[`results/MarxistLeninist_bub1b_compound_het.csv`](results/MarxistLeninist_bub1b_compound_het.csv).

## One canonical Track 2 submission

The source of truth is [`competition/CANONICAL.json`](competition/CANONICAL.json),
currently version `2026-08-30.4`. Every human or agent must read that manifest
and [`competition/coordination/AGENT_PROTOCOL.md`](competition/coordination/AGENT_PROTOCOL.md)
before editing competition material.

There is exactly one editable Track 2 report:

`reports/MarxistLeninist_track2_report.md`

The PDF is generated from that Markdown source. Addenda and older pitch scripts
are supporting or historical files, not alternate reports. `make check` fails if
someone creates another filename resembling a Track 2 report. Apparently the
robots did, eventually, learn not to produce `final_v3_really_final.md`.

## Track 2 conclusion

No approved medicine currently has evidence sufficient to justify administration
for this child's MVA. The proposal is therefore a **ranked ex vivo rescue screen**,
not an empirical cocktail:

1. **Azithromycin - priority allele-directed screen.** Test the exact `UGA-A`
   context of `p.Leu737Ter`, then require full-length stop-allele BUBR1, an
   identified residue-737 peptide, and functional checkpoint/segregation rescue
   near exposure achieved in approved use.
2. **Arimoclomol - conditional missense-stabilisation probe.** Do not screen it
   until `p.Asn1002Lys` is shown to be unstable, chaperone-responsive, and still
   functionally recoverable. No published experiment shows arimoclomol rescues
   BUBR1.
3. **Sirolimus - downstream autophagy benchmark only.** Rapamycin partially
   rescued neural-stem-cell number in a 2026 fly SAC-loss model, but did not
   restore progeny or brain size and carries major immunosuppression concerns.
4. **Acetylcysteine - biomarker-gated redox comparator.** It enters only if
   patient cells first show a reproducible mitochondrial/redox abnormality; it
   was not tested in the MVA-like fly study.
5. **Gentamicin - laboratory readthrough control only.** Its renal and auditory
   toxicity make it unsuitable as an empirical chronic treatment proposal.

Candidates advance only if they show the intended molecular target engagement,
reduce **new** chromosome-segregation errors, work within a predefined human-
exposure ceiling, and do not preferentially preserve premalignant aneuploid
clones.

## Important uncertainty correction

Published inducible-cell experiments reported a steep BUBR1 response around
approximately 6% versus 13% residual abundance. The earlier repository converted
this into a child-specific 5-10% estimate and a 1.3-2.6-fold rescue target. Those
numbers are now explicitly labelled as **scenario analysis**, not measurements
from this child. The real threshold must be set from patient-cell BUBR1 abundance,
corrected isogenic controls, and functional response.

## Current Track 2 candidate artifacts

Canonical version `2026-08-30.4` contains a newly built report and pitch video.
They are candidates for a later authorized submission update and remain
**built but unreviewed**:

- `competition/artifacts/MarxistLeninist_track2_report.pdf`
  - SHA-256 `dc434c332670c7f5df9296d95b8576366386a4da094375ff36f04d205941b65e`
- `competition/artifacts/MarxistLeninist_track2_pitch.mp4`
  - 177.267 seconds
  - 1920x1080 H.264, AAC 48 kHz
  - SHA-256 `83d6df1c74f3615d5c65306d664946a5cfe943def4eb698737b217d6cbbf20be`

Before another submission, both exact artifacts must be reviewed, the current
video must be hosted and watched after platform processing, the AI
data-handling disclosure must be verified, and the participant must explicitly
authorize use of a remaining slot.

## Track 2 submission history

Submission 1 was received and is preserved under
`competition/history/submission-01/`. Its exact supplied report and pitch are
historical and do not overwrite the current canonical v4 artifacts.

The form permits three Track 2 submissions. One has been used, **two remain**,
and the judging panel reviews only the latest entry. The Submission 1 YouTube
URL is historical; it is not the hosting URL for the current canonical video.
No later submission is authorized by this repository.

## Dedicated SG competition MCP

The competition-specific `SG MVA Hackathon 2026` MCP is deployed and verified
on SG1 and SG2 with identical 12-tool surfaces. The artifact-specific
`mva_report` and `mva_video` tools are strictly read-only and expose the
canonical artifacts, Submission 1 archive and remaining quota.

GitHub PR #1 and issue #2 remain the shared workboard. SG1 is the single
coordination writer and SG2 is a fenced standby, preventing node-local claims
from diverging. The MCP deliberately has no Hackathon submission capability.

## Reproduce public checks

Python 3.11+ is sufficient for the public, synthetic checks; no gated patient
data are required.

```bash
make check

python scripts/readthrough_context.py \
  --wild-type-codon TTA --codon-position 2 --alternate G --plus-four A

python scripts/structure_context.py AF-O60566-F1-model_v6.pdb --residue 1002
```

The last command is optional and requires the public AlphaFold model linked in
the Track 2 report. Structural output is explicitly hypothesis-generating.

## Repository map

- `competition/CANONICAL.json` - machine-readable source of truth
- `competition/artifacts/` - current candidate PDF and MP4
- `competition/history/` - immutable prior-submission receipts and supplied artifacts
- `competition/review/` - contact sheet, captions and build evidence
- `competition/coordination/` - mandatory multi-agent protocol
- `reports/MarxistLeninist_track1_report.md` - variant analysis and limitations
- `reports/MarxistLeninist_track2_report.md` - the only canonical Track 2 report source
- `methods/MarxistLeninist_track2_methods_update_20260830.md` - methods/disclosure update
- `reports/pitch_script_track2_revised_20260830.md` - canonical report-aligned pitch source
- `reports/pitch_script_3min_opus5.md` - superseded historical pitch source
- `pipeline/competition_video/` - deterministic report and video builders
- `SUBMISSION_CHECKLIST.md` - current form fields and action-time safety gates
- `results/` - submission CSV and public evidence/provenance records
- `scripts/` - submission, privacy and canonical-manifest validators
- `tests/` - synthetic/unit tests only
- `DATA_GOVERNANCE.md` - release boundary and privacy safeguards

## Data boundary

The gated genome, phenotype document, read evidence, sample-wide annotations,
and intermediate files are deliberately absent. The repository publishes only
the minimum derived facts needed for the competition. Run `make privacy` before
every public commit.

The controlled data source is the gated Hugging Face dataset `SageBio/mva-hackathon-2026-data`, accessed 30 August 2026.

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
