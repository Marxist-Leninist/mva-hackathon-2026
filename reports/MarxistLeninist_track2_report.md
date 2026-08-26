# Track 2 report: an allele-resolved rescue screen for BUB1B-associated MVA1

**Participant:** MarxistLeninist  
**Status:** preclinical repurposing hypothesis  
**Scope:** approved medicines proposed for controlled experimental testing, not for administration

## Executive proposal

This case is best explained by a `BUB1B` null-plus-missense pair:

- `p.Leu737Ter` is an NMD-competent premature stop (`UGA-A`).
- `p.Asn1002Lys` is a full-length, gnomAD-absent missense change in the
  C-terminal kinase/pseudokinase region.

That architecture creates two distinct therapeutic opportunities. The first is
to recover full-length protein from the nonsense allele. The second is to
increase the abundance or function of the missense protein. A third, downstream
arm can buffer the proteotoxic and mitochondrial stress caused by cells that
remain aneuploid.

I propose a **factorial patient-cell rescue screen**, not an empirical cocktail:

1. **Gentamicin** for allele-specific premature-stop readthrough.
2. **Arimoclomol** for stress-gated chaperone amplification and stabilization of
   the full-length missense protein.
3. **Prescription nicotinic acid** as an orthogonal, biomarker-gated
   NAD/SIRT2/BUBR1-abundance hypothesis.
4. **Sirolimus (rapamycin)** as a downstream autophagy/proteostasis benchmark
   with direct drug-level rescue evidence in a 2026 MVA-like fly model.

Each agent is tested alone first. A readthrough-plus-stabilization combination
advances only if both single-agent arms show allele-specific target engagement without a
genotoxic, survival, or checkpoint penalty. Sirolimus advances separately only
if it reduces functional harm without masking continued chromosome
missegregation. This is a route to identify a credible rescue signal; it is not
evidence that any of these medicines will help the child.

## Mechanism anchored to this genotype

BUBR1 is a core component of the spindle assembly checkpoint and kinetochore-
microtubule attachment machinery. It helps delay anaphase until chromosomes are
properly attached. In BUB1B-MVA1 patient cells, low BUBR1 abundance and impaired
checkpoint activity drive chromosome alignment and segregation defects.

The 2010 patient-cell study by Suijkerbuijk and colleagues is unusually useful
for repurposing. It found that truncating alleles produced no stable transcript,
while several missense proteins in or near the kinase region had increased
turnover. HSP90 inhibition further depleted the missense proteins; proteasome
inhibition blocked that loss. Raising two poorly expressed mutants to wild-type-
like abundance restored nocodazole checkpoint response. The therapeutic lesson
is specific: for some kinase-region BUBR1 substitutions, **quantity rather than
irreversible catalytic failure may be the limiting variable**. That has not yet
been shown for p.Asn1002Lys and must be tested.

The nonsense allele supplies a complementary route. `c.2210T>G` converts the
wild-type `TTA` leucine codon into `TGA`, followed by `A`. UGA is often more
readthrough-responsive than other stop classes, but the +4 base is not the
favorable +4C context. More importantly, the transcript is predicted to undergo
NMD. A readthrough drug has little substrate if the RNA is almost absent.
Allele-specific RNA abundance is therefore the first gate, not an afterthought.

## Candidate 1: gentamicin - rescue the premature-stop allele

### Rationale

Gentamicin is an approved aminoglycoside antibiotic that can reduce decoding
fidelity and permit translation across some premature termination codons. Human
nonsense-disease studies establish proof of mechanism but also show strong
context dependence. A two-week Duchenne study in four patients did not detect
full-length dystrophin. A later six-month study reported a significant group-level
increase, with a few participants reaching 13-15% of normal dystrophin; stable
pretreatment transcript predicted response. The latter observation is directly
relevant to an NMD-competent BUB1B stop.

Readthrough does not necessarily restore leucine: near-cognate decoding at UGA
commonly inserts tryptophan, cysteine, or arginine. A full-length band is therefore
not proof of a functional BUBR1 molecule. Aminoglycosides can also increase
readthrough at normal stop codons, so global translation-termination effects are
part of the safety screen.

### Why it is only an ex-vivo lead

The approved label carries serious nephrotoxicity, often irreversible
ototoxicity, and neurotoxicity warnings; risk rises with exposure and duration.
The label also warns that certain `MT-RNR1` variants can confer hearing-loss risk
even at usual serum levels. Chronic use for a noninfectious pediatric indication
cannot be inferred from antibiotic approval. No dose is proposed here.

### First experiment

Build a dual-luciferase reporter containing at least 12 nucleotides on each side
of the exact `UGA-A` context, then test exposure-matched gentamicin alongside a
no-stop control and a non-readthrough negative control. In patient-derived cells:

- quantify allele-specific BUB1B RNA before and after treatment;
- detect full-length BUBR1 by immunoblot and targeted mass spectrometry;
- identify the amino acid inserted at residue 737 by peptide mass spectrometry;
- test checkpoint arrest, mitotic timing, chromosome alignment, and new
  missegregation events.

If the stop-allele transcript is nearly absent or full-length protein cannot be
detected near tolerated human exposure, gentamicin is rejected. NMD inhibitors
may be used as short mechanistic controls in vitro, but global NMD suppression is
not promoted as a treatment because it can stabilize many abnormal transcripts.

## Candidate 2: arimoclomol - test stabilization of p.Asn1002Lys

### Rationale

Arimoclomol is FDA-approved, in combination with miglustat, for neurological
manifestations of Niemann-Pick disease type C in adults and children aged two
years and older. It is described in clinical literature as a stress-dependent
heat-shock-response/HSP70 co-inducer. The BUB1B bridge is plausible but indirect:
MVA kinase-region missense mutants can be unstable and chaperone-dependent, but
the published dependency was specifically demonstrated with HSP90 perturbation.
Arimoclomol is not a selective HSP90 activator, and no published experiment shows
that it stabilizes BUBR1 or p.Asn1002Lys. The nearby published p.Leu1012Pro
result strengthens the domain hypothesis but cannot be transferred to a different
amino-acid substitution ten residues away.

The current label describes pediatric steady-state exposure in the low-micromolar
range and states that the NPC mechanism is unknown. Hypersensitivity, creatinine
elevation, gastrointestinal/weight effects, and broad stabilization of oncogenic
chaperone clients are relevant counter-screens.

### First experiment

Use CRISPR-edited isogenic cells carrying wild-type BUB1B, p.Leu737Ter,
p.Asn1002Lys, and the compound genotype, alongside patient cells if available.
Measure:

- total and allele-specific BUBR1 abundance;
- cycloheximide-chase protein half-life;
- cellular thermal-shift behavior;
- HSP70/HSP90 induction and BUBR1-chaperone co-immunoprecipitation;
- kinetochore localization and binding partners;
- spindle-checkpoint and chromosome-segregation phenotypes.

An AlphaFold v6 model places Asn1002 in a locally high-confidence region and
predicts side-chain contacts to backbone atoms near residues 978 and 998. Lysine
could disturb that local polar network, but this is a structural hypothesis, not
evidence of instability. Arimoclomol advances only if it raises the mutant
protein's functional abundance rather than merely inducing a generic stress
response.

## Candidate 3: prescription nicotinic acid - orthogonal BUBR1 abundance test

### Rationale

SIRT2 deacetylates BUBR1 at Lys668 and can increase its stability. In mouse
experiments, SIRT2 expression and the NAD precursor NMN raised BubR1 abundance
and partially improved phenotypes in BubR1-hypomorphic animals. Prescription
nicotinic acid is an approved NAD precursor, and high-dose niacin has raised
tissue NAD in adults with mitochondrial myopathy.

This bridge is deliberately labeled indirect. The BUBR1 experiments used NMN or
SIRT2, not nicotinic acid; no patient MVA cell or p.Asn1002Lys rescue has been
shown. Niacin will also fail if p.Asn1002Lys produces a stable but intrinsically
nonfunctional protein.

### First experiment

At exposure-matched concentrations, measure NAD metabolites, SIRT2 activity,
BUBR1 Lys668 acetylation, p.Asn1002Lys half-life, and the same checkpoint and
segregation endpoints used for arimoclomol. SIRT2 overexpression and NMN serve as
non-drug pathway controls. NAD elevation without BUBR1/SAC rescue is a no-go.
Hepatotoxicity, flushing, glucose intolerance, hyperuricemia, hypotension,
arrhythmia, limited pediatric evidence, and possible support of tumor metabolism
make long-term abnormal-clone counter-screening mandatory.

## Candidate 4: sirolimus - downstream proteostasis benchmark

### Rationale

A 2026 *Nature Communications* study created a fly model of MVA-like
microcephaly by depleting spindle-checkpoint genes in neural stem cells. Complex
aneuploidies caused proteostasis failure, mitochondrial dysfunction, and loss of
stemness. Increasing autophagy genetically rescued neural stem-cell counts, and
feeding rapamycin partially rescued neural stem-cell number, but not progeny
count or brain size. Genetic ROS scavengers and mitochondrial chaperones restored
additional aspects of brain growth; those were genetic interventions, not drugs.

Sirolimus is rapamycin and is an approved mTOR inhibitor. This is the shortlist's
most direct drug-to-MVA-model link, but it is downstream: it may help cells cope
with aneuploidy without correcting BUBR1 or preventing new aneuploid cells.

### Contradiction and safety gate

Sirolimus is immunosuppressive. Its current label warns of serious infection and
possible lymphoma or other malignancy. That is a major contradiction in a child
with cancer-predisposition syndrome. A drug that simply keeps abnormal cells
alive could also preserve premalignant clones. Sirolimus is therefore a
phenotypic benchmark and conditional candidate, not a clinical recommendation.

It advances only if longitudinal single-cell DNA analysis shows fewer newly
generated aneuploid cells or improved tissue function **without** expansion of
pre-existing abnormal clones, loss of tumor-suppressive surveillance, or reduced
immune competence in co-culture.

## Exploratory comparator: N-acetylcysteine

N-acetylcysteine is an approved medicine in specific indications and a useful
redox perturbation. The 2026 fly study supports ROS-scavenger biology through
genetic overexpression, not through N-acetylcysteine itself. It is therefore an
exploratory downstream comparator, not a co-lead. It advances only after a
patient-cell ROS/mitochondrial signature is demonstrated and only if it improves
function without protecting genetically unstable cells.

## Factorial experiment and pre-registered gates

### Models

Use at least two independent patient-derived clones and a CRISPR isogenic panel:

- wild type;
- p.Leu737Ter alone;
- p.Asn1002Lys alone;
- compound genotype;
- corrected compound-genotype control.

Fibroblasts give a practical first screen. A neural progenitor model is added for
developmental relevance. Experiments are randomized, blinded at image analysis,
and repeated by a second laboratory before any translational claim.

### Treatment matrix

Test vehicle, gentamicin, arimoclomol, nicotinic acid, sirolimus,
N-acetylcysteine, and readthrough-plus-stabilizer combinations. Use
concentration-response and time-course designs anchored to unbound exposure
achieved in approved use. Add research-only
controls where informative: an NMD-blockade control, a nonclinical readthrough
positive control, an autophagy-flux control, and a chaperone-dependency control.

The numerical thresholds below are prospective screening rules, not clinical
efficacy cutoffs.

### Gate G0 - target engagement

- Gentamicin: at least a two-fold reporter signal plus independently detected
  full-length stop-allele protein.
- Arimoclomol: at least a 25% increase in p.Asn1002Lys half-life or abundance,
  with an orthogonal chaperone/thermal-shift signal.
- Nicotinic acid: NAD/SIRT2 pathway engagement, reduced BUBR1 Lys668 acetylation,
  and increased variant-protein abundance.
- Sirolimus: expected mTOR/autophagy target engagement and improved proteostasis
  markers, without claiming BUBR1 restoration.

Failure at clinically reachable exposure stops that arm.

### Gate G1 - causal functional rescue

Require a pre-specified improvement in at least two orthogonal primary outcomes:

1. spindle-checkpoint arrest or mitotic timing;
2. chromosome alignment and lagging-chromosome rate;
3. micronucleus/new-aneuploidy rate by live imaging and single-cell DNA profiling.

Illustrative advancement thresholds are checkpoint activity approaching at least
50% of corrected control, at least a 30% reduction in spontaneous segregation
errors, and less than a 10% reduction in proliferation/viability across two
independent clones. These are study-design thresholds, not known therapeutic
targets. The same direction must reproduce in patient and isogenic models. Generic cell
growth, reduced apoptosis, or a prettier morphology is not sufficient.

### Gate G2 - rescue-versus-cancer safety index

Reject any arm that:

- increases survival or clonogenic expansion of pre-existing aneuploid cells
  without reducing new missegregation;
- weakens p53-independent or immune surveillance;
- increases DNA damage, micronuclei, transformation, or checkpoint bypass;
- requires exposure far above approved human pharmacology;
- shows a narrow or irreproducible window.

Longitudinal barcoding and single-cell copy-number profiling distinguish true
prevention of new errors from mere selection of a surviving abnormal clone.

### Gate G3 - external confirmation

An independent laboratory repeats the central result from a frozen protocol and
pre-specified analysis. Only then would medicinal-chemistry, formulation,
pharmacokinetic, toxicology, and specialist clinical discussions be justified.

## Contradiction screen and rejected approaches

| Approach | Why it is not a treatment candidate here |
|---|---|
| BUB1B/BUB1 kinase inhibitors | Developed to weaken checkpoints or kill cancer cells; mechanistically opposed to restoring segregation fidelity |
| HSP90 inhibitors | Published MVA missense proteins fell further when HSP90 was inhibited |
| Proteasome inhibitors | May raise mutant protein experimentally but are toxic, oncologic agents and broadly disrupt proteostasis |
| Antimitotics/TTK or APC/C interference | Can intensify chromosome instability or arrest rather than restore a deficient checkpoint |
| Global NMD inhibition | May increase the stop-allele substrate but also stabilizes many abnormal transcripts; mechanistic control only |
| Senolytics | Could alter later progeroid features but do not repair the child's core segregation defect and may interfere with tumor surveillance |

ChEMBL records provide useful direct-target controls, not therapies. TG101209
(`CHEMBL1995703`) and BAY-1816032 (`CHEMBL5084426`) increased BUB1B thermal
resistance in a 20 micromolar cellular assay while showing weak recombinant
BUB1B inhibition. Both are preclinical, and the source program developed BUB1B
inhibitors for renal cancer. Conversely, related molecules destabilized BUB1B.
These compounds can help validate a cellular thermal-shift assay, but they fail
the approved-drug and direction-of-effect requirements.

The NAD+/SIRT2 literature is a mechanistic bridge rather than efficacy evidence.
NMN is not an approved medicine, and prescription nicotinic acid is not assumed
to reproduce NMN pharmacology. That is why niacin remains an orthogonal,
biomarker-gated stabilization arm rather than a treatment claim.

## Innovation and scalability

The innovation is not a longer drug list. It is the **allele-resolved rescue
logic plus a rescue-versus-cancer safety index**:

- classify each allele by RNA, protein, and pathway failure;
- demand direct target engagement for each matching repurposing strategy;
- distinguish prevention of new aneuploidy from survival of existing abnormal
  clones;
- test downstream tissue protection only after measuring whether upstream
  chromosome segregation is fixed;
- publish a privacy-preserving, pre-registered workflow that can be reused for
  other null-plus-unstable-missense recessive diseases.

This makes negative results useful. Failure of gentamicin localizes the barrier
to NMD/context or toxicity. Failure of arimoclomol distinguishes an unstable
protein from a stable but functionally defective one. Failure of sirolimus shows
that downstream proteostasis buffering is insufficient or unsafe. The framework
can then redirect effort toward antisense NMD escape, allele-specific RNA editing,
or gene replacement without pretending that an approved drug already works.

## Patient-centered interpretation

No established disease-modifying treatment for BUB1B-MVA1 follows from the
current evidence. The proposed experiments do not replace symptom-directed care,
cancer surveillance, genetics review, or clinical judgment. No off-label use is
recommended. The immediate contribution is a falsifiable route from this child's
two alleles to a small, safety-aware experimental shortlist.

## References

1. Hanks S, et al. *Nat Genet.* 2004. https://pubmed.ncbi.nlm.nih.gov/15475955/
2. Suijkerbuijk SJE, et al. *Cancer Res.* 2010. https://pmc.ncbi.nlm.nih.gov/articles/PMC2887387/
3. Malik V, et al. *Ann Neurol.* 2010. https://pubmed.ncbi.nlm.nih.gov/20517938/
4. Wagner KR, et al. *Ann Neurol.* 2001. https://pubmed.ncbi.nlm.nih.gov/11409421/
5. Gentamicin prescribing information. https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=84f5c763-1cd3-4d85-9afb-934db8666fbf
6. FDA approval letter, Miplyffa (arimoclomol), NDA 214927. https://www.accessdata.fda.gov/drugsatfda_docs/appletter/2024/214927Orig1s000ltr.pdf
7. González-Blanco A, et al. *Nat Commun.* 2026. https://www.nature.com/articles/s41467-026-70521-0
8. Sirolimus prescribing information. https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=9f64692d-2a18-ffcb-c572-0f218a71ca67
9. North BJ, et al. *Nat Cell Biol.* 2014. https://pmc.ncbi.nlm.nih.gov/articles/PMC4194088/
10. El Hafi M, et al. *Eur J Med Chem.* 2025. https://pubmed.ncbi.nlm.nih.gov/39818011/
11. ChEMBL BUB1B target `CHEMBL4295998`. https://www.ebi.ac.uk/chembl/explore/target/CHEMBL4295998
12. AlphaFold DB BUB1B model. https://alphafold.ebi.ac.uk/entry/O60566
13. Wangen JR, Green R. *eLife.* 2020. https://elifesciences.org/articles/52611
14. Pirinen E, et al. *Cell Metab.* 2020. https://pubmed.ncbi.nlm.nih.gov/32386566/
15. Miplyffa prescribing information. https://dailymed.nlm.nih.gov/dailymed/fda/fdaDrugXsl.cfm?setid=5feffc0e-453d-47fa-91dd-38d4952309bc&type=display
