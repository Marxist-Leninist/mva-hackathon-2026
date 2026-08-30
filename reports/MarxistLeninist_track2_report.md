---
title: "From genotype to a falsifiable rescue screen"
subtitle: "Allele-resolved drug repurposing for candidate BUB1B-associated Mosaic Variegated Aneuploidy type 1"
author: "MarxistLeninist"
date: "30 August 2026"
geometry: margin=0.75in
fontsize: 10pt
colorlinks: true
linkcolor: blue
urlcolor: blue
header-includes:
  - |
    ```{=latex}
    \usepackage{longtable}
    \usepackage{booktabs}
    \usepackage{array}
    \usepackage{microtype}
    \setlength{\parskip}{0.35em}
    \setlength{\parindent}{0pt}
    ```
---

# Track 2 proposal

**Participant:** MarxistLeninist  
**Submission type:** preclinical drug-repurposing proposal  
**Case interpretation:** candidate biallelic `BUB1B` disease; phase and the exact effect of the missense allele remain unconfirmed  
**Clinical status of this proposal:** no drug, dose, treatment change, or off-label use is recommended

> **Central claim.** The strongest immediately testable strategy is not a drug cocktail. It is an allele-resolved patient-cell screen that asks, in order: (1) can an approved medicine recover functional BUBR1 from the premature-stop allele, (2) is the missense BUBR1 protein actually unstable and pharmacologically stabilizable, and (3) can downstream mitochondrial or proteostatic injury be reduced without preserving genetically unstable clones?

# Executive summary

The case contains two high-quality heterozygous `BUB1B` variants on transcript `NM_001211.6`:

1. `c.2210T>G`, `p.Leu737Ter`, a premature termination variant expected to be loss-of-function through nonsense-mediated mRNA decay (NMD).
2. `c.3006T>G`, `p.Asn1002Lys`, an ultra-rare missense variant in the C-terminal pseudokinase region. It appears once in gnomAD v4 exomes and is absent from gnomAD genomes, but the exact allele is not established as pathogenic in isolation.

Both variants were independently confirmed from raw reads in the accompanying repository. They are 10,911 bp apart, beyond ordinary short-read phasing range. Therefore, **in trans is inferred, not demonstrated**, and `p.Asn1002Lys` remains a variant of uncertain significance until segregation or functional evidence is obtained.

The disease mechanism is best described as a **candidate recessive BUBR1 dosage and function deficit**, not simply a generic kinase defect. BUBR1 is required both for spindle-assembly checkpoint signalling and for stable kinetochore-microtubule attachment. Published MVA patient cells show low BUBR1, weak checkpoint responses, chromosome alignment defects, and chromosome mis-segregation. Several previously studied C-terminal MVA missense variants had increased turnover; raising two of those proteins back to wild-type-like abundance restored checkpoint activity. However, `p.Asn1002Lys` itself has never been tested, and a missense change in the same region cannot be assumed to behave like another one.[1-3]

No approved medicine currently has evidence sufficient to justify administration for this child's MVA. I therefore propose a **ranked ex vivo repurposing screen**:

| Priority | Approved medicine | Role in this proposal | Evidence level | Advancement condition |
|---|---|---|---|---|
| 1 | Azithromycin | Allele-directed readthrough screen for `p.Leu737Ter` | Readthrough shown in other nonsense-disease patient cells, not in BUB1B | Full-length stop-allele BUBR1, identified residue-737 peptide, and functional rescue at exposure-relevant concentrations |
| 2 | Arimoclomol | Conditional missense-stabilization probe | Indirect chaperone rationale; no BUB1B data | First prove that `p.Asn1002Lys` is unstable and chaperone-responsive |
| Benchmark | Sirolimus (rapamycin) | Downstream autophagy/proteostasis benchmark | Rapamycin partially rescued neural-stem-cell number in a 2026 fly SAC-loss model, but not progeny or brain size | Functional benefit without immunological harm or expansion of abnormal clones |
| Comparator | Acetylcysteine | Biomarker-gated redox comparator | Genetic ROS scavengers rescued parts of the fly phenotype; acetylcysteine itself was not tested | Measured mitochondrial oxidative stress plus functional benefit and clone safety |
| Laboratory control only | Gentamicin | Positive comparator for readthrough | Stronger historical readthrough precedent but highly context-dependent | Never promoted as a chronic clinical candidate; renal and auditory toxicity make it a mechanistic control only |

Each agent is tested alone before any combination. A combination advances only when both components independently show the intended target engagement, work within a predefined human-exposure ceiling, and do not increase survival or clonogenic expansion of aneuploid cells. The primary translational output is a **go/no-go map**, including useful negative results.

# 1. Genotype and uncertainty boundary

## 1.1 Variant evidence

The repository's genome-wide workflow ranked `BUB1B` first without supplying the disease name or a `BUB1B` gene-panel prior. Exact 31-mer counting from all eight raw FASTQ lanes independently confirmed both heterozygous calls:

| Variant | Reference reads | Alternate reads | Variant allele fraction |
|---|---:|---:|---:|
| `p.Leu737Ter` | 16 | 16 | 0.500 |
| `p.Asn1002Lys` | 11 | 13 | 0.542 |

This confirms the two sequence changes independently of the supplied variant caller. It does **not** establish that they are on opposite chromosomes.

## 1.2 What is known, inferred, and unknown

| Status | Statement |
|---|---|
| Measured in this case | Both variants are present at heterozygous read fractions; `p.Asn1002Lys` is extremely rare in population data. |
| Strongly predicted | `p.Leu737Ter` is NMD-competent and likely contributes little or no stable full-length protein. |
| Clinically plausible but unproven | The two variants are in trans and jointly explain MVA1. |
| Mechanistic hypothesis | `p.Asn1002Lys` lowers BUBR1 abundance through increased turnover. |
| Not measured | Allele-specific RNA, BUBR1 abundance, mutant protein half-life, checkpoint strength, or the child's position on any BUBR1 dose-response curve. |

This boundary is important because every proposed drug depends on one of the unmeasured quantities. The first experimental stage is therefore diagnostic as well as therapeutic.

# 2. Mechanism: loss of checkpoint and attachment fidelity

BUBR1 is a core part of the mitotic checkpoint complex and helps prevent anaphase until chromosomes are correctly attached. It also recruits PP2A-B56 through its KARD region to regulate kinetochore-microtubule attachment. Human BUBR1's C-terminal domain is an unusual pseudokinase: conventional catalytic activity is dispensable for accurate segregation, while nucleotide-interacting residues contribute to conformational stability.[2-4]

In published BUB1B-MVA patient cells, the combination of truncating and missense alleles produced:

- low overall BUBR1 abundance;
- impaired nocodazole-induced checkpoint arrest;
- shortened mitotic delay;
- chromosome alignment defects; and
- increased chromosome mis-segregation.

The 2010 study separated MVA variants into at least two mechanistic classes: variants causing specific functional defects and variants causing low protein abundance. Truncating alleles lacked stable transcript, while several missense proteins in or near the C-terminal domain had increased turnover. Overexpressing selected low-abundance missense proteins to wild-type-like levels restored checkpoint function.[1]

That result creates a plausible repurposing opportunity, but not a diagnosis of `p.Asn1002Lys`. The exact variant may be unstable, normally stable but functionally defective, or functionally neutral. The proposal has an explicit kill condition:

> **If `p.Asn1002Lys` has normal abundance and half-life but fails functional assays, the abundance-restoration arm is stopped. If it has normal abundance and normal function, the assumed biallelic mechanism must be re-examined.**

## 2.1 Downstream biological consequence

Repeated checkpoint and attachment failure produces chromosome mis-segregation and mosaic aneuploidy. Aneuploid cells carry imbalanced gene dosage, which can create proteotoxic stress, mitochondrial dysfunction, reactive oxygen species, altered proliferation, senescence, or cell loss. In a 2026 Drosophila neural-stem-cell model created by depleting spindle-checkpoint genes, complex aneuploidy caused proteostasis and mitochondrial defects. Genetic enhancement of autophagy, mitochondrial chaperones, or ROS-scavenging pathways rescued different parts of the phenotype. Rapamycin partially restored neural-stem-cell number, but did not restore progeny-cell number or brain size.[5]

This creates a second therapeutic axis: protecting vulnerable tissues from downstream stress. It also creates a major safety contradiction. A compound that helps aneuploid cells survive could preserve premalignant abnormal clones without reducing the production of new aneuploid cells. Therefore, **cell survival alone is not a successful endpoint**.

## 2.2 A dose-response hypothesis, not a patient measurement

An inducible BUBR1-depletion experiment in HeLa cells reported a steep response: approximately 6% residual BUBR1 was associated with mis-segregation in most cells, whereas approximately 13% had little detectable effect on segregation fidelity.[1] The prior repository converted this into a hypothetical 1.3- to 2.6-fold rescue target by assuming that this child's missense allele behaves like previously studied 5- to 10-fold destabilized variants.

That calculation is useful for planning but must not be presented as measured biology. In this report:

- 6% and 13% are published model-system observations;
- 5% to 10% for this child is a scenario assumption;
- 1.3- to 2.6-fold is a scenario-dependent planning range; and
- the actual advancement threshold will be set from measured patient-cell baseline, corrected isogenic control, and functional response.

# 3. Candidate 1: azithromycin for the premature-stop allele

## 3.1 Rationale

`p.Leu737Ter` changes the wild-type leucine codon `TTA` to `TGA`, followed by an adenine: an exact `UGA-A` termination context. Readthrough efficiency depends strongly on the stop codon and surrounding nucleotides. UGA is often more permissive than UAG or UAA, but the local sequence can dominate, and readthrough may insert tryptophan, cysteine, arginine, or another near-cognate amino acid rather than the original leucine.[6,7]

Azithromycin is a market-approved macrolide with experimental nonsense-readthrough evidence. Caspi and colleagues reported restoration of full-length proteins in patient-derived Rett and spinal muscular atrophy fibroblasts after azithromycin exposure, including effects at 0.1 to 5 micrograms/mL. The result establishes a disease-class signal, not a BUB1B signal.[8] The lowest experimental concentration is in the same order of magnitude as reported pediatric plasma Cmax after approved antibacterial dosing, but plasma Cmax is not equivalent to free intracellular exposure at the ribosome.[9]

Azithromycin is therefore the lead **screening candidate**, not a treatment recommendation.

## 3.2 Why the experiment can fail

Four barriers must all be crossed:

1. **NMD substrate barrier.** If the stop-allele transcript is nearly absent, the ribosome has little substrate to read through.
2. **Sequence barrier.** `UGA-A` may be poorly responsive despite UGA's average tendency.
3. **Protein-identity barrier.** A full-length band may contain a non-leucine residue at position 737 and may not function.
4. **Exposure and safety barrier.** A signal that appears only above clinically relevant exposure is not a repurposing hit.

Long-term noninfectious azithromycin would also raise antimicrobial-resistance and microbiome concerns. The current label warns about QT prolongation and torsades de pointes, hepatotoxicity, and hearing effects.[9] No dose is proposed.

## 3.3 Exact experiment

### Reporter stage

Construct dual-luciferase reporters containing at least 15 nucleotides on each side of the exact `UGA-A` context. Include:

- wild-type sense-codon control;
- premature-stop vehicle control;
- no-stop normalization control;
- an unrelated nonresponsive stop-context control;
- azithromycin concentration-response and time course; and
- gentamicin as a laboratory positive comparator, not as a clinical candidate.

### Patient-cell stage

In patient-derived fibroblasts and an isogenic compound-genotype line:

- quantify total and allele-specific `BUB1B` RNA by digital PCR;
- detect full-length BUBR1 by immunoblot;
- use targeted mass spectrometry to identify a peptide spanning residue 737 and determine the inserted amino acid;
- quantify kinetochore BUBR1;
- measure mitotic timing and nocodazole/STLC checkpoint response;
- measure chromosome alignment, lagging chromosomes, anaphase bridges, micronuclei, and new copy-number changes; and
- assess off-target readthrough at normal stop codons by a targeted termination-fidelity panel.

### Go/no-go rule

Azithromycin advances only if all of the following hold:

- full-length stop-allele protein is independently demonstrated;
- the inserted residue produces functional BUBR1;
- at least two orthogonal segregation/checkpoint endpoints improve;
- the effect appears within the predefined exposure ceiling derived from approved human pharmacology; and
- global termination errors, cytotoxicity, and clone expansion remain within preregistered bounds.

A reporter signal alone is not sufficient.

# 4. Candidate 2: arimoclomol, conditional on missense instability

## 4.1 Rationale

Arimoclomol is FDA-approved, with miglustat, for neurological manifestations of Niemann-Pick disease type C in adults and children aged two years and older. Its label states that the mechanism of clinical effect in NPC is unknown.[10] Experimental literature describes it as a stress-dependent amplifier of heat-shock responses, particularly HSP70-associated pathways. This makes it a plausible probe for a short-lived BUBR1 missense protein, but the bridge is indirect.

The relevant BUBR1 evidence is that previously studied C-terminal MVA missense proteins could be unstable and sensitive to HSP90 perturbation.[1] The relevant contradiction is that arimoclomol is not a selective HSP90 agonist, no publication shows that it stabilizes BUBR1, and a study of the misfolded NPC1-I1061T protein did not observe HSP70 induction or correction with arimoclomol under its tested conditions.[11] In July 2026, the EMA's CHMP issued a negative opinion for arimoclomol in NPC because clinical benefit had not been sufficiently demonstrated; this does not prove failure in MVA, but it lowers confidence in broad extrapolation.[12]

Arimoclomol is therefore retained only as a **conditional target-engagement experiment**.

## 4.2 Entry gate before drug testing

Do not screen arimoclomol until patient and isogenic cells demonstrate that `p.Asn1002Lys`:

- is expressed at the RNA level;
- produces a full-length protein;
- has lower steady-state abundance or a shorter half-life than wild type; and
- retains recoverable checkpoint or attachment function when experimentally expressed to a matched level.

If those conditions fail, arimoclomol is removed.

## 4.3 Experiment and kill conditions

Measure:

- allele-specific BUBR1 abundance;
- cycloheximide-chase half-life;
- cellular thermal-shift behaviour;
- HSP70 and HSP90 pathway engagement;
- BUBR1-chaperone co-immunoprecipitation;
- kinetochore localization and PP2A-B56 recruitment;
- checkpoint and chromosome-segregation outcomes; and
- broad heat-shock-response, proliferation, apoptosis, DNA-damage, and clonogenicity markers.

Arimoclomol advances only if it raises **functional** mutant BUBR1, not merely total protein or generic stress markers. It is rejected if it stabilizes abnormal clones, weakens surveillance, or requires exposure above approved human pharmacology.

# 5. Downstream benchmarks, not upstream cures

## 5.1 Sirolimus as an autophagy benchmark

Sirolimus is rapamycin, an approved mTOR inhibitor. Its relevance is unusually direct for a downstream candidate: rapamycin partially rescued neural-stem-cell number in the 2026 fly model of spindle-checkpoint-loss microcephaly. The same experiment did not restore progeny-cell number or brain size, so the result supports autophagy target engagement more strongly than organism-level rescue.[5]

Sirolimus does not restore BUBR1 or prevent a chromosome from being mis-segregated. It is immunosuppressive, and its label warns of increased susceptibility to infection, lymphoma, and other malignancies.[13] That is a serious contradiction in a cancer-predisposition syndrome.

Accordingly, sirolimus is a **phenotypic benchmark** for short ex vivo experiments. It does not advance toward clinical discussion unless it improves tissue-relevant function, reduces the generation of new abnormal cells, and does not expand existing aneuploid clones or impair immune surveillance in co-culture.

## 5.2 Acetylcysteine as a biomarker-gated redox comparator

Genetic expression of mitochondrial ROS-scavenging enzymes rescued parts of the 2026 fly phenotype, including additional aspects of brain growth.[5] Acetylcysteine is an approved medicine that replenishes cysteine/glutathione and can be used as a redox perturbation.[14] It was not tested in that MVA-like model, and generic antioxidant activity is not evidence of BUB1B rescue.

Acetylcysteine enters the screen only if patient cells show a reproducible mitochondrial ROS, glutathione, respiratory, or redox signature. It advances only if it improves a tissue-relevant or segregation-linked phenotype without simply keeping abnormal cells alive.

# 6. Rejected or demoted approaches

A rigorous repurposing result includes what should **not** be advanced.

| Approach | Decision | Reason |
|---|---|---|
| Gentamicin as chronic treatment | Control only | Context-dependent readthrough plus nephrotoxicity and often irreversible ototoxicity; unsuitable for empirical chronic use. |
| HSP90 inhibitors | Reject | Published C-terminal MVA missense proteins were further depleted when HSP90 was inhibited; this could remove the only productive allele.[1] |
| Proteasome inhibitors | Reject | May raise mutant protein experimentally but broadly disrupt proteostasis and are toxic oncologic drugs. |
| BUB1B, BUB1, TTK/MPS1 or APC/C checkpoint inhibitors | Reject | Directionally oppose restoration of chromosome-segregation fidelity. |
| Global NMD inhibition | Mechanistic control only | May increase stop-allele RNA but also stabilizes many abnormal transcripts. |
| Prescription nicotinic acid as a lead | Demote | SIRT2 overexpression and NMN increased BubR1 in mouse ageing models, but this is not evidence that nicotinic acid rescues `p.Asn1002Lys` or MVA.[15] |
| Aneuploidy-selective cytotoxic compounds | Reject | In cancer they exploit stress to kill aneuploid cells; in constitutional mosaic aneuploidy the same selectivity may damage the patient's affected tissues. |
| Senolytics | Reject for this proposal | Do not correct the primary segregation defect and could remove a tumour-suppressive arrest programme. |
| Altering current oncology treatment from this analysis | Reject | The report has no patient-specific chemotherapy-response data and must not change established cancer care. Any SAC-drug interaction is a separate laboratory hypothesis for the clinical team, not a treatment recommendation. |

# 7. Experimental programme

## Stage 0: establish the biological substrate

Before ranking any drug response:

1. Phase the two variants by parental testing or long-range/long-read methods.
2. Measure allele-specific `BUB1B` RNA and NMD sensitivity.
3. Measure total and kinetochore BUBR1 abundance.
4. Measure `p.Asn1002Lys` half-life and function in isogenic cells.
5. Quantify baseline checkpoint strength and chromosome-error rate.
6. Characterize existing mosaic copy-number states so later experiments can separate true rescue from selection of a surviving clone.

## Models

Use at minimum:

- two independently expanded patient-derived clones, if samples are available;
- a CRISPR isogenic panel: wild type, `p.Leu737Ter`, `p.Asn1002Lys`, compound genotype, and corrected compound genotype;
- fibroblasts for the first screen; and
- a neural-progenitor or organoid model only after a signal is reproducible, to test developmental relevance.

No experiment on identifiable patient material proceeds without the appropriate consent, governance, and ethics approval.

## Stage 1: blinded single-agent screen

Test vehicle, azithromycin, arimoclomol only if its entry gate is met, sirolimus, acetylcysteine only if its biomarker gate is met, and gentamicin as a readthrough control. Use randomized plate position, blinded image analysis, concentration-response, and time-course designs.

Concentrations are anchored to unbound exposure achievable in approved use. An arm that works only above the preregistered ceiling is recorded as mechanistically interesting but not repurposable.

## Stage 2: target engagement

| Agent | Required target-engagement evidence |
|---|---|
| Azithromycin | Exact-context reporter plus full-length stop-allele BUBR1 and a residue-737-spanning peptide |
| Arimoclomol | Longer `p.Asn1002Lys` half-life/greater abundance plus orthogonal chaperone or thermal-shift evidence |
| Sirolimus | Expected mTOR/autophagy-flux response; no claim of BUBR1 restoration |
| Acetylcysteine | Corrected glutathione/redox/mitochondrial biomarker in a cell line with a baseline abnormality |

## Stage 3: functional rescue

The primary functional outcome is the **rate of newly generated chromosome-segregation errors**, measured by live imaging and confirmed by single-cell copy-number profiling. Secondary outcomes are checkpoint arrest/mitotic timing, chromosome alignment, micronuclei, neural-progenitor maintenance, and mitochondrial function.

A candidate must improve at least two orthogonal outcomes in the same direction in patient and isogenic models. Cell number, reduced apoptosis, or a visually healthier culture alone is not sufficient.

## Stage 4: rescue-versus-clone-safety index

Reject any arm that:

- increases survival or clonogenicity of pre-existing aneuploid cells without reducing new mis-segregation;
- increases micronuclei, DNA damage, checkpoint bypass, or transformation-associated behaviour;
- weakens immune-cell recognition or killing in co-culture;
- causes broad normal-stop readthrough;
- has a narrow, irreproducible response window; or
- requires non-repurposable exposure.

Longitudinal barcoding and single-cell copy-number analysis distinguish prevention of new chromosome errors from selective expansion of one abnormal clone.

## Stage 5: combination only after single-agent proof

The only rational first combination is an allele-directed agent plus a validated stabilizer, for example azithromycin plus arimoclomol **only if both independently pass**. A downstream stress-buffering agent is evaluated separately before combination because it may hide continuing chromosome instability.

Synergy is not inferred from improved viability. It requires greater restoration of BUBR1/checkpoint function or a lower new-aneuploidy rate than either single agent, without a worse clone-safety index.

## Statistical design

- Pre-register one primary endpoint and the exposure ceiling for each arm.
- Use at least three independent biological repeats and two independent patient clones where possible.
- Treat cells as observations nested within clone and experiment, not as independent biological replicates.
- Analyze event counts with a mixed-effects count model and continuous protein/mitotic outcomes with hierarchical models appropriate to their distributions.
- Report effect sizes and confidence intervals, not only P values.
- Confirm the central result in a second laboratory from a frozen protocol before any translational claim.

# 8. Expected outcomes and decision tree

## Outcome A: azithromycin produces functional full-length BUBR1

This would be the strongest repurposing signal because it directly addresses a causal allele. The next steps would be independent replication, detailed termination-fidelity profiling, pharmacokinetic feasibility, and specialist toxicology. It would still not justify unsupervised or empirical use.

## Outcome B: the stop transcript is absent or readthrough is nonfunctional

This localizes the barrier to NMD, sequence context, inserted amino acid, or exposure. The approved-drug route is stopped. Research may shift to allele-specific RNA editing, antisense-mediated NMD escape, or gene replacement, none of which is claimed as an approved repurposing solution.

## Outcome C: `p.Asn1002Lys` is unstable and arimoclomol rescues function

This would support a dosage-restoration strategy. It would require a strict cancer/clone-safety programme because broad proteostasis support could affect abnormal cells beyond BUBR1.

## Outcome D: `p.Asn1002Lys` is stable but defective

The stabilization strategy is abandoned. The mechanistic focus shifts to localization, partner binding, or allele replacement.

## Outcome E: downstream agents improve stress markers but not segregation

They remain tissue-protection hypotheses, not disease-modifying candidates. The distinction is explicit in all reporting.

# 9. Innovation, impact, and scalability

## Scientific rigor

The proposal starts with molecular-fate validation, uses exact-context and allele-specific assays, anchors exposure to approved pharmacology, and requires orthogonal functional rescue. It is designed to falsify its own candidates.

## Potential impact

A modest restoration of functional BUBR1 could have disproportionate value if the published steep dose-response reproduces in patient cells. Even a negative result would prevent unsafe empirical repurposing and identify whether the dominant barrier is NMD, protein instability, intrinsic missense dysfunction, or downstream tissue stress.

## Innovation

The innovation is the combination of:

1. **allele-resolved repurposing** rather than a gene-level drug list;
2. **molecular-fate entry gates** before drug testing;
3. **an exposure-aware functional endpoint** rather than protein abundance alone; and
4. a **rescue-versus-clone-safety index** that asks whether a drug prevents new aneuploidy or merely preserves abnormal cells.

## Scalability

The workflow generalizes to other recessive disorders with a null allele plus a potentially unstable missense allele. The public code, exact-context reporter logic, dose-window model, and preregistered decision gates can be reused without publishing raw genomic data. The initial analysis runs on commodity CPU hardware; the expensive work is biological validation, not computation.

# 10. Limitations

1. Phase is inferred, not proven.
2. `p.Asn1002Lys` is an ultra-rare VUS; its exact abundance and function are unknown.
3. No proposed medicine has been tested in BUB1B-MVA patient cells for this genotype.
4. Azithromycin readthrough is sequence-dependent and may not restore leucine.
5. Arimoclomol's BUBR1 bridge is indirect, and its labelled NPC mechanism is unknown.
6. The 2026 downstream evidence is from a fly SAC-loss model, not this child's genotype or a human organoid.
7. The 6%/13% BUBR1 response window is from an inducible cell model; the child-specific 1.3- to 2.6-fold target is scenario analysis.
8. A downstream survival benefit could preserve premalignant aneuploid cells.
9. Pharmacokinetic feasibility, paediatric chronic safety, tissue penetration, and interactions with current care are unresolved.
10. The proposal does not establish clinical efficacy and must not alter current treatment.

# 11. Methods and reproducibility

## Sources and search strategy

The analysis used public sources available through 30 August 2026: PubMed/PMC primary literature, official FDA/DailyMed labels, FDA and EMA regulatory records, gnomAD v4, ClinVar, Ensembl/UniProt, and the 2026 Nature Communications MVA-like model. Candidate generation was followed by an independent adversarial review that was instructed to find contradictory evidence, failed trials, exposure mismatches, and genotype-specific safety problems.

Evidence was ranked in this order:

1. direct functional evidence in this exact genotype;
2. patient-derived BUB1B-MVA cells;
3. drug-level evidence in a mechanistically close disease model;
4. drug-level evidence in other nonsense or protein-misfolding diseases;
5. pathway-level or genetic evidence only.

No candidate is described as clinically actionable because levels 1 and 2 are absent.

## Repository

The public repository contains the genome-wide ranking workflow, independent raw-read confirmation code and counts, exact-context readthrough code, dosage-scenario model, report source, methods materials, privacy checks, and pitch-video source materials:

`https://github.com/Marxist-Leninist/mva-hackathon-2026`

Raw genomic files, genome-scale genotype tables, and identifiable clinical records are not redistributed.

## AI-assistance disclosure

OpenAI ChatGPT Pro (GPT-5.6 Pro) and Anthropic Claude Code/Claude models under a paid individual subscription were used for drafting, code review, candidate generation, and adversarial scientific review. **The exact account-level model-training and retention/data-control settings active during those sessions were not recorded in the repository and must be inserted by the participant before submission.** No claim of "no training" is made without that verification.

# 12. Patient-centred interpretation

This report proposes experiments, not medicines for administration. It does not replace genetics review, symptom-directed care, cancer surveillance, oncology treatment, or clinical judgement. No off-label use, dose, or treatment change follows from the analysis.

The immediate value is a small set of decisive experiments that can say:

- whether the nonsense allele can make functional protein;
- whether the missense allele is actually unstable;
- whether downstream stress is a modifiable contributor; and
- whether apparent rescue is safe for a child with constitutional chromosome instability.

# Acknowledgement

This work was made possible through the Hackathon, organized by Sage Bionetworks in partnership with the MVA Society, Hugging Face, and BEACON (The Benchmarking, Evaluation, and Assessment Consortium for Science), with prize sponsorship from AWS and Anthropic. We are deeply grateful to the child and their family who generously contributed their data and their story to advance research into this rare disease. We acknowledge their trust in making this Hackathon possible.

# Dataset citation

**Participant action before submission:** insert the exact Synapse dataset citation supplied with the controlled Hackathon data-access record. The repository deliberately does not reproduce gated data.

# References

1. Suijkerbuijk SJE, van Osch MHJ, Bos FL, Hanks S, Rahman N, Kops GJPL. Molecular causes for BUBR1 dysfunction in the human cancer predisposition syndrome mosaic variegated aneuploidy. *Cancer Research*. 2010;70(12):4891-4900. PMID 20516114. https://pubmed.ncbi.nlm.nih.gov/20516114/
2. Suijkerbuijk SJE, van Dam TJP, Karagoz GE, et al. The vertebrate mitotic checkpoint protein BUBR1 is an unusual pseudokinase. *Developmental Cell*. 2012;22(6):1321-1329. PMID 22698286. https://pubmed.ncbi.nlm.nih.gov/22698286/
3. Hanks S, Coleman K, Reid S, et al. Constitutional aneuploidy and cancer predisposition caused by biallelic mutations in BUB1B. *Nature Genetics*. 2004;36:1159-1161. PMID 15475955. https://pubmed.ncbi.nlm.nih.gov/15475955/
4. Suijkerbuijk SJE, Vleugel M, Teixeira A, Kops GJPL. Integration of kinase and phosphatase activities by BUBR1 ensures formation of stable kinetochore-microtubule attachments. *Developmental Cell*. 2012;23(4):745-755. PMID 23079597. https://pubmed.ncbi.nlm.nih.gov/23079597/
5. Gonzalez-Blanco A, Acuna-Higaki AR, Boettger D, Joy J, Milan M. Proteostasis failure and mitochondrial dysfunction contribute to chromosomal instability-induced microcephaly. *Nature Communications*. 2026. doi:10.1038/s41467-026-70521-0. https://doi.org/10.1038/s41467-026-70521-0
6. Wangen JR, Green R. Stop codon context influences genome-wide stimulation of termination codon readthrough by aminoglycosides. *eLife*. 2020;9:e52611. https://elifesciences.org/articles/52611
7. Dabrowski M, Bukowy-Bieryllo Z, Zietkiewicz E. Translational readthrough potential of natural termination codons in eucaryotes - the impact of RNA sequence. *RNA Biology*. 2015;12(9):950-958. https://pubmed.ncbi.nlm.nih.gov/26176195/
8. Caspi M, Firsow A, Rajkumar R, et al. A flow cytometry-based reporter assay identifies macrolide antibiotics as nonsense mutation read-through agents. *Journal of Molecular Medicine*. 2016;94(4):469-482. PMID 26620677. https://pubmed.ncbi.nlm.nih.gov/26620677/
9. Azithromycin prescribing information. DailyMed. Current label accessed 30 August 2026. https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=db52b91e-79f7-4cc1-9564-f2eee8e31c45
10. MIPLYFFA (arimoclomol) prescribing information. DailyMed. Current label accessed 30 August 2026. https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=5feffc0e-453d-47fa-91dd-38d4952309bc
11. Pipalia NH, Subramanian K, Mao S, Ralph H, Hutt DM, Scott SM, Balch WE, Maxfield FR. HSP90 inhibitors reduce cholesterol storage in Niemann-Pick type C1 mutant fibroblasts. *Journal of Lipid Research*. 2021;62:100114. PMCID PMC8517605. https://pmc.ncbi.nlm.nih.gov/articles/PMC8517605/
12. European Medicines Agency. Negative opinion for Aqneursa (arimoclomol), July 2026. https://www.ema.europa.eu/en/medicines/human/EPAR/aqneursa
13. Sirolimus prescribing information. DailyMed. Current label accessed 30 August 2026. https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=6a85ad01-8144-4d9c-e053-2991aa0a4f85
14. Acetylcysteine prescribing information. DailyMed. Current label accessed 30 August 2026. https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=5558a5f5-e821-473b-7d8a-5d33d09f0586
15. North BJ, Rosenberg MA, Jeganathan KB, et al. SIRT2 induces the checkpoint kinase BubR1 to increase lifespan. *EMBO Journal*. 2014;33(13):1438-1453. PMID 24825348. https://pubmed.ncbi.nlm.nih.gov/24825348/
16. Malik V, Rodino-Klapac LR, Viollet L, Wall C, King W, Al-Dahhak R, et al. Gentamicin-induced readthrough of stop codons in Duchenne muscular dystrophy. *Annals of Neurology*. 2010;67(6):771-780. PMID 20517938. https://pubmed.ncbi.nlm.nih.gov/20517938/
17. Gentamicin prescribing information. DailyMed. Current label accessed 30 August 2026. https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=84f5c763-1cd3-4d85-9afb-934db8666fbf
