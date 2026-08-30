# Track 2 methods update — 30 August 2026

**Participant:** MarxistLeninist  
**Applies to:** `reports/MarxistLeninist_track2_report.md`  
**Status:** canonical methods narrative for the revised report

> The previously generated Excel form predates the final evidence reconciliation
> and contains conclusions that conflict with the revised report. Regenerate the
> spreadsheet from this update, or attach this Markdown methods description,
> before submission.

## 1. How candidates were generated

The analysis proceeded from **allele fate to drug class**, rather than from a
list of medicines:

1. `p.Leu737Ter` was classified as an NMD-competent premature stop with an exact
   `UGA-A` readthrough context.
2. `p.Asn1002Lys` was classified as an ultra-rare, full-length C-terminal
   missense VUS whose abundance and function are unmeasured.
3. Published BUB1B-MVA patient-cell work was used to define two possible primary
   mechanisms: insufficient transcript/protein from the stop allele and
   increased turnover or specific functional failure of the missense allele.
4. Downstream proteostasis, mitochondrial and redox consequences were separated
   from upstream BUBR1 rescue.
5. Approved medicines were mapped to those mechanisms, then filtered by human
   exposure, sequence dependence, paediatric safety, cancer-predisposition risk,
   and whether an apparent benefit could simply preserve aneuploid clones.

## 2. Automated and human-directed components

Candidate generation, literature discovery, repository inspection, consistency
checking, code review, and first-draft synthesis were AI-assisted and partly
parallel. The final decisions were not accepted from a generate-only pipeline.
Every major claim was independently rechecked against primary literature or an
official regulatory label, and contradictory or over-absolute audit claims were
rejected when the source did not support them.

Human-directed decisions included:

- retaining azithromycin only as an ex vivo readthrough lead;
- retaining arimoclomol only after a missense-instability entry gate;
- demoting sirolimus and acetylcysteine to downstream benchmarks;
- restricting gentamicin to a laboratory control;
- demoting prescription nicotinic acid;
- separating measured facts from scenario assumptions; and
- rejecting any inference that should change current oncology treatment.

## 3. Evidence hierarchy

Evidence was ranked in the following order:

1. direct functional evidence in the exact genotype;
2. patient-derived BUB1B-MVA cells;
3. drug-level evidence in a mechanistically close model;
4. drug-level evidence in another nonsense or protein-misfolding disease;
5. genetic or pathway-level evidence only.

No candidate has level-1 or level-2 drug evidence. Therefore, none is presented
as clinically actionable.

## 4. Variant-mechanism characterization

The working mechanism is a **candidate recessive BUBR1 dosage/function deficit**.
BUBR1 contributes to the spindle-assembly checkpoint and to stable kinetochore-
microtubule attachment. Published MVA cells with truncating and missense BUB1B
alleles show low BUBR1, weak checkpoint responses, alignment defects and
chromosome mis-segregation. Several previously studied C-terminal missense
proteins had increased turnover, and expression rescue restored checkpoint
function for selected variants.

Critical uncertainty: `p.Asn1002Lys` itself has never been functionally tested.
It may be unstable, stable but defective, or functionally neutral. The variants
are 10,911 bp apart and short reads do not establish trans phase. The report
therefore requires phasing, allele-specific RNA, protein abundance, half-life and
functional assays before treating the proposed mechanism as established.

## 5. Final candidate decisions

### Priority 1 — azithromycin

Role: exact-context readthrough screen for `p.Leu737Ter`.

Advance only if exposure-relevant treatment produces full-length stop-allele
BUBR1, identifies the residue-737-spanning peptide and inserted amino acid,
restores at least two orthogonal checkpoint/segregation outcomes, and does not
cause unacceptable normal-stop readthrough or clone expansion.

### Priority 2 — arimoclomol, conditional

Role: missense-stabilisation probe only after proving that `p.Asn1002Lys` is
short-lived, chaperone-responsive and functionally recoverable. Its labelled NPC
mechanism is unknown, and no BUBR1 rescue data exist.

### Downstream benchmark — sirolimus

Role: autophagy/proteostasis benchmark based on partial rapamycin rescue in a
2026 fly SAC-loss model. It is not an upstream BUBR1 rescue and carries major
immunosuppression concerns.

### Biomarker-gated comparator — acetylcysteine

Role: redox perturbation only if patient cells first show a reproducible
mitochondrial or glutathione abnormality. Acetylcysteine was not tested in the
MVA-like fly model.

### Laboratory control — gentamicin

Role: mechanistic positive comparator for readthrough. It is not proposed for
chronic administration because of renal and auditory toxicity.

## 6. Pre-registered experimental logic

Stage 0 establishes phase, allele-specific RNA, total and kinetochore BUBR1,
missense half-life/function, baseline checkpoint strength and existing mosaic
copy-number states.

The single-agent screen is randomized and image analysis is blinded. The primary
functional endpoint is the rate of **newly generated chromosome-segregation
errors**, confirmed by live imaging and single-cell copy-number profiling. A
candidate must improve at least two orthogonal functional outcomes in patient and
isogenic models, within an exposure ceiling derived from approved human
pharmacology.

A separate rescue-versus-clone-safety gate rejects any arm that preserves or
expands pre-existing aneuploid cells without reducing new mis-segregation,
weakens immune surveillance, increases micronuclei/DNA damage/checkpoint bypass,
or requires non-repurposable exposure.

## 7. Correction to the earlier dosage claim

Published inducible-cell work reported a steep BUBR1 response near approximately
6% versus 13% residual abundance. The earlier methods form treated a child-
specific 5-10% estimate and a 1.3-2.6-fold rescue target too strongly. Those
figures are now explicitly **scenario analysis**. This child's BUBR1 abundance
has not been measured, and the actual advancement threshold must be set from
patient cells and corrected isogenic controls.

## 8. Public data and reproducibility

Public sources used include PubMed/PMC primary literature, official FDA/DailyMed
labels, FDA and EMA regulatory records, gnomAD v4, ClinVar, Ensembl/UniProt, and
the 2026 Nature Communications SAC-loss model. The repository includes the
public analysis code, independent raw-read confirmation logic and counts,
readthrough-context code, dosage-scenario model, privacy checks, report source,
and pitch-video build materials. Gated genomic and identifiable clinical data are
not redistributed.

The controlled challenge data source is the gated Hugging Face dataset `SageBio/mva-hackathon-2026-data`, accessed 30 August 2026; gated data are not redistributed.

## 9. AI-assistance disclosure

OpenAI ChatGPT Pro (GPT-5.6 Pro) and Anthropic Claude Max 20x, including
Claude Code, were used for drafting, code review, candidate generation and
adversarial scientific review.

**Participant action before submission:** confirm and record the account-level
training, retention or data-control setting that applied to both providers during
the relevant sessions. No generic "no training" claim should be made without
verifying those settings.

## 10. Track 2 abstract (under 500 words)

We characterised a candidate biallelic BUB1B genotype — p.Leu737Ter plus the
ultra-rare p.Asn1002Lys VUS — as a testable dosage/function deficit rather than a
generic kinase defect. The stop allele is predicted to undergo nonsense-mediated
decay. The missense allele lies in the C-terminal pseudokinase region, where some
published MVA variants have increased turnover, but p.Asn1002Lys itself has not
been tested. Phase is inferred, not proven, and the child's BUBR1 abundance and
checkpoint function are unmeasured.

We propose a ranked ex vivo screen, not treatment. Azithromycin is the priority
allele-directed candidate because it has readthrough evidence in other nonsense-
disease patient cells and the exact BUB1B context is UGA-A. Advancement requires
full-length stop-allele BUBR1, identification of the residue-737 peptide and
inserted amino acid, functional checkpoint/segregation rescue near approved human
exposure, and acceptable termination fidelity. Gentamicin is a laboratory
comparator only.

Arimoclomol is retained conditionally: it is screened only if patient and
isogenic cells first prove that p.Asn1002Lys is unstable, chaperone-responsive
and functionally recoverable. Sirolimus is an autophagy benchmark based on
partial rapamycin rescue in a 2026 fly spindle-checkpoint-loss model, and
acetylcysteine is a biomarker-gated redox comparator; neither is presented as an
upstream cure.

The primary endpoint is the rate of newly generated chromosome-segregation
errors. Every candidate must show intended target engagement, improve at least
two orthogonal outcomes, remain within a predefined exposure ceiling and pass a
rescue-versus-clone-safety index. This index distinguishes prevention of new
aneuploidy from selective survival of pre-existing abnormal clones — essential in
a syndrome combining cellular fragility with cancer predisposition.

The earlier child-specific 5-10% BUBR1 estimate and 1.3-2.6-fold rescue target are
now labelled scenario analysis, not patient measurements. No approved medicine
has sufficient evidence for administration, no dose is proposed, and the report
recommends no change to current clinical or oncology care.
