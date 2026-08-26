#!/usr/bin/env python3
"""Fill the MVA Hackathon methods description form for Track 1 and Track 2.

Answers are written into column B, which the template marks with the "Answers"
header at B6. Column A (the questions) is left untouched, as are all existing
fonts, widths and the merged instruction block.
"""
import openpyxl
from openpyxl.styles import Alignment, Font

SRC = "methods_description_form.xlsx"
OUT = "MarxistLeninist_methods_description_form.xlsx"

TEAM = "MarxistLeninist"

TRACK1 = {
    "B7": TEAM,
    "B8": "Model 1 of 1 submitted. Submission file: "
          "model1_MarxistLeninist_bub1b_compound_het.csv",

    "B9": (
        "Gene-agnostic prioritisation of a single-proband GRCh38 WGS VCF. No gene panel, no "
        "candidate list and no disease name is supplied to any ranking step; the MVA gene set "
        "appears only afterwards, as a differential-diagnosis rule-out.\n\n"
        "Two independent lanes were run and converged on the same gene:\n\n"
        "LANE A — genome-wide knowledge screen. All 4,740,790 PASS records were intersected "
        "against 346,282 ClinVar Pathogenic/Likely_pathogenic records on EXACT "
        "chromosome/position/ref/alt match rather than positional overlap. Positional overlap "
        "alone gives 5,730 hits; exact-allele matching reduces this to 7 genome-wide. One is the "
        "BUB1B stop-gain whose ClinVar condition field names Mosaic variegated aneuploidy "
        "syndrome 1.\n\n"
        "LANE B — phenotype-driven ranking with no prior. PASS calls were restricted to GENCODE "
        "v47 CDS +/-8 bp (38.4 Mb, 27,896 variants), annotated through Ensembl VEP REST (MANE "
        "Select preference, gnomAD exome and genome AF, SIFT, PolyPhen-2), filtered to rare "
        "HIGH/MODERATE consequences, then scored per gene as genotype model x HPO phenotype "
        "similarity. The genotype model evaluates homozygous, two-hit (compound-heterozygous "
        "hypothesis) and rare-dominant-heterozygous architectures. The phenotype term is an "
        "asymmetric best-match-average Resnik similarity over the full HPO DAG with "
        "information-content weighting, computed against the proband's 8 HPO terms. BUB1B ranks "
        "first of the ranked candidate genes.\n\n"
        "The BUB1B locus was then re-extracted at EVERY filter level, including LowQual, so a "
        "genuine second allele lost to hard filtering could not be missed. It contains 14 "
        "non-reference calls in total; 12 are intronic MODIFIERs (9 of them common), and the "
        "only two coding-impact calls are the two submitted variants. Heterozygous calls are "
        "distributed across the whole gene, so there is no loss-of-heterozygosity block and "
        "therefore no large intragenic deletion concealing a third allele.\n\n"
        "Both alleles were then confirmed independently of the variant caller by exact 31-mer "
        "counting straight from all 8 raw FASTQ lanes (no aligner, no caller, files streamed and "
        "never written to disk): p.Leu737Ter 16 REF / 16 ALT, VAF 0.500; p.Asn1002Lys 11 REF / "
        "13 ALT, VAF 0.542. Both on both strands, no strand bias, both indistinguishable from "
        "0.5 by binomial test."
    ),

    "B10": (
        "AUTOMATED OUTPUT, with human-directed review of the final call.\n\n"
        "The ranked candidate list, the ClinVar exact-allele screen and the read-level "
        "confirmation are all direct programmatic output. The submitted CSV was assembled by "
        "code (04_build_submission.py in the pipeline) from that output, not hand-typed.\n\n"
        "What was not automated: the decision to report the pair as a single compound-het row, "
        "the wording of the notes field, the choice of which secondary findings to surface, and "
        "the exclusion of one automated hit as an artefact (see B11). We would rather state that "
        "plainly than claim a fully hands-off pipeline."
    ),

    "B11": (
        "Three review steps changed the output, and each is worth naming because each is a "
        "failure mode of the automated stage rather than a matter of taste.\n\n"
        "1. ARTEFACT EXCLUDED. The genome-wide ClinVar screen returned PRSS1 p.Ala16Val, a "
        "ClinVar Pathogenic assertion for hereditary pancreatitis, which has a gnomAD exome "
        "frequency of 0.202. A 20% allele cannot be a penetrant pathogenic variant; PRSS1 lies "
        "within the TRB locus and has close paralogs, so this is a mapping artefact. It was "
        "removed. A knowledge-based screen without a frequency sanity check would have reported "
        "it.\n\n"
        "2. FREQUENCY RE-VERIFICATION. Ensembl VEP REST returns no gnomAD record for a minority "
        "of alleles, and reading that silence as a frequency of zero makes a variant look "
        "maximally rare, which is exactly what promotes it in a rare-disease ranking. Every "
        "affected allele was re-queried directly against the gnomAD v4 API. Of 11,478 coding "
        "HIGH/MODERATE alleles, 36 (0.3%) had no VEP frequency, and 12 of those turned out to be "
        "COMMON, up to AF 0.93. Two of them had reached the top five of the ranking on a "
        "frequency that did not exist. Correcting this did not change the top candidate and "
        "widened its margin over the runner-up.\n\n"
        "3. PHASE LANGUAGE. The automated output asserted compound heterozygosity. Review "
        "downgraded this to 'candidate biallelic, phase undetermined', which is what the "
        "evidence supports (see B15)."
    ),

    "B12": "PUBLIC DATA ONLY. No proprietary data, no proprietary tools, no commercial API and "
           "no paid service was used at any stage. Everything is reproducible by anyone with "
           "approved access to the challenge dataset.",

    "B13": (
        "ClinVar GRCh38 (NCBI FTP, 2026 release) — 346,282 Pathogenic/Likely_pathogenic records, "
        "used for exact-allele matching and for the classification of both alleles.\n"
        "gnomAD v4 — allele frequencies, queried both through Ensembl VEP and directly against "
        "the gnomAD GraphQL API for verification of every top candidate.\n"
        "Ensembl VEP REST — consequence, MANE Select transcript, HGVS, exon/intron number, SIFT, "
        "PolyPhen-2.\n"
        "GENCODE v47 basic annotation — CDS interval set used to define the coding+splice search "
        "space.\n"
        "Human Phenotype Ontology (hp.obo and genes_to_phenotype) — 11,919 terms and 5,268 "
        "annotated genes, used for the information-content-weighted phenotype similarity.\n"
        "OMIM / ClinGen gene-disease validity — inheritance model and the established BUB1B-MVA1 "
        "genotype architecture.\n"
        "PubMed primary literature — mechanism, NMD competence, the BUBR1 dosage threshold "
        "series, and the published cryptic upstream regulatory second-allele architecture "
        "(PMID 15475955, 20516114, 22698286, 18932004, 16411201, 24344301, 40555658, 24981203)."
    ),

    "B14": "None. No proprietary data were used.",

    "B15": (
        "YES — the approach outputs compound-heterozygous PAIRS as first-class candidates, not "
        "single variants. The genotype model explicitly evaluates a two-hit architecture: for any "
        "gene carrying two or more rare heterozygous impactful variants it forms the pair and "
        "scores it as a recessive hypothesis alongside homozygous and dominant models. The "
        "submitted primary row uses the paired chrom_1/chrom_2 columns.\n\n"
        "IMPORTANT LIMITATION, stated deliberately: the pipeline proposes pairs, it does not "
        "PHASE them. The two variants are 10,911 bp apart, far beyond read-backed phasing range "
        "for short reads; GATK emitted no PGT/PID for either site, and no parental samples exist. "
        "Trans is therefore INFERRED from the clinical diagnosis plus the established MVA1 "
        "architecture (a null plus a hypomorph; biallelic complete null is embryonic lethal), not "
        "demonstrated. Under ClinGen SVI recessive scoring this is PM3_Supporting, not "
        "PM3_Moderate.\n\n"
        "We bounded rather than hand-waved this. Decomposed by the missense's origin: if de novo, "
        "P(cis) = 0.50 exactly; if inherited, cis requires a parent carrying a cis "
        "double-heterozygous haplotype, and gnomAD argues against one — the nonsense allele "
        "appears on ~115 exome chromosomes and zero carry the missense, where even 1% "
        "co-occurrence would predict ~1. Weighting de novo at 0.05-0.15 gives a prior P(cis) "
        "~0.07; conditioning on the confirmed MVA diagnosis gives a posterior P(cis) ~1.5%, "
        "defensible range 1-8%. Small, but not ignorable, because cis and trans imply different "
        "recurrence risks for the family. That is an argument for testing, not for quoting a "
        "probability. Parental testing settles it; failing that, long-range PCR plus Nanopore "
        "amplicon phasing is clinically validated across 5.8-21.4 kb and this 10,911 bp gap sits "
        "in that range."
    ),

    "B16": (
        "Secondary findings were generated by the same unbiased genome-wide ClinVar exact-allele "
        "screen that produced the primary call — they are a by-product of the method, not a "
        "separate hunt — then filtered by a frequency sanity check and by whether the finding is "
        "actionable or interpretable.\n\n"
        "The one we consider clinically noteworthy is LZTR1 chr22:20996720 C>G p.Tyr748Ter: a "
        "heterozygous nonsense in a tumour-suppressor, gnomAD 1.4e-06, ClinVar "
        "Pathogenic/Likely_pathogenic (schwannomatosis-2 / Noonan syndrome 10). It does not "
        "explain the MVA phenotype, but it is an independent germline tumour-suppressor "
        "loss-of-function in a child who already has rhabdomyosarcoma, so it is potentially "
        "relevant to cancer surveillance and to family cascade testing, and it warrants clinical "
        "confirmation and genetics review.\n\n"
        "Lower-value carrier-state findings were also identified and are reported with explicit "
        "interpretation rather than bare coordinates: RBM8A 5'UTR (low-penetrance; pathogenic for "
        "TAR only in trans with a 1q21.1 deletion, which is NOT present here), GNRHR p.Arg139His "
        "(heterozygous carrier for an AR condition, no second allele) and FLG p.Arg2447Ter (a "
        "common filaggrin null, unrelated).\n\n"
        "One automated hit was deliberately EXCLUDED rather than padded in: PRSS1 p.Ala16Val, "
        "ClinVar Pathogenic but gnomAD AF 0.202, a TRB-locus paralog mapping artefact.\n\n"
        "A deliberate negative is also reported: nephrocalcinosis present since birth is not an "
        "established BUB1B-MVA1 feature, so a recessive nephrocalcinosis/hypercalciuria/"
        "tubulopathy panel plus full ACMG SF v3.2 was screened for a possible second diagnosis. "
        "It returned ZERO qualifying variants. We report that clean negative rather than a VUS we "
        "do not believe; prematurity (32 weeks, ~1 kg) plausibly explains the nephrocalcinosis "
        "without a second locus."
    ),

    "B17": (
        "RUN TIME: under two hours end-to-end on commodity hardware, dominated by network I/O "
        "rather than compute.\n"
        "  Data download (315 MB VCF + clinical document): ~1 minute.\n"
        "  Reference downloads (GENCODE, ClinVar, HPO): ~30 seconds.\n"
        "  ClinVar genome-wide exact-allele screen over 4.74M PASS records: ~4 minutes.\n"
        "  VEP REST annotation of 27,963 alleles (140 batches of 200, 4 concurrent): ~10 minutes.\n"
        "  gnomAD API backfill and top-candidate verification: ~1 minute.\n"
        "  Prioritisation including full HPO DAG construction and IC weighting: ~30 seconds.\n"
        "  Mosaic-aneuploidy scan across all heterozygous SNVs: ~6 minutes.\n"
        "  Read-level 31-mer validation streaming all 8 FASTQ lanes (~85 GB) from the Hub: "
        "~40 minutes, network-bound.\n\n"
        "HARDWARE: 4 CPU cores, 15 GB RAM, ~30 GB disk. No GPU at any point. The FASTQ validation "
        "streams and never writes to disk, so the 85 GB dataset never needs local storage.\n\n"
        "COST: effectively zero. Every resource used is free and public — ClinVar, gnomAD, "
        "GENCODE, HPO and Ensembl VEP REST are all free; no commercial API, no paid inference, no "
        "cloud GPU. The dominant cost is bandwidth. This matters for the Scalability criterion: "
        "the method runs on a laptop and is affordable for any clinical genetics service, "
        "anywhere."
    ),

    "B18": (
        "We identified biallelic BUB1B (MVA1, MIM 257300) — NM_001211.6:c.2210T>G p.Leu737Ter "
        "with c.3006T>G p.Asn1002Lys — using a pipeline that is deliberately given no gene panel, "
        "no candidate list and no disease name.\n\n"
        "METHOD. Two independent lanes converge. Lane A intersects all 4,740,790 PASS calls "
        "against 346,282 ClinVar P/LP records on exact ref/alt match, yielding 7 hits "
        "genome-wide, one of which names MVA1. Lane B restricts to GENCODE v47 CDS+/-8bp, "
        "annotates via Ensembl VEP REST, and ranks every gene carrying a rare impactful variant "
        "by genotype model (homozygous / two-hit / rare dominant het) multiplied by "
        "information-content-weighted Resnik best-match-average HPO similarity over the full "
        "ontology DAG. BUB1B ranks first. Both alleles were then confirmed independently of the "
        "variant caller by exact 31-mer counting from all 8 raw FASTQ lanes, streamed and never "
        "written to disk: VAF 0.500 and 0.542, both strands, no strand bias.\n\n"
        "STRENGTHS. (1) The result does not rest on prior knowledge of the allele: ablating "
        "ClinVar entirely leaves BUB1B ranked first, and the phenotype axis alone also ranks it "
        "first, while the genotype axis alone leaves several genes tied and cannot discriminate. "
        "That is the property that would transfer to a genuinely novel gene, where no ClinVar "
        "assertion exists. (2) The differential is closed against the data, not by assertion: "
        "CEP57, TRIP13, CENATAC and every chromosomal-instability mimic (ESCO2, NBN, BLM, ATM, "
        "FANCA, FANCD2, TP53, DICER1) carry no qualifying rare coding variant. (3) Orthogonal "
        "read-level confirmation removes dependence on the caller. (4) Free, public, CPU-only, "
        "~2 hours.\n\n"
        "LIMITATIONS, stated plainly. (1) PHASE IS INFERRED, NOT DEMONSTRATED. 10,911 bp apart, "
        "no parental samples, no read-backed phase; ClinGen SVI scores this PM3_Supporting. We "
        "bound P(cis) at ~1.5% (range 1-8%) rather than dismissing it, and note the published "
        "architecture in which a cryptic regulatory allele ~44 kb upstream is the true second hit "
        "(PMID 16411201, 24344301) — we screened the 61 kb upstream window at all filter levels "
        "(88 calls, none matching ClinVar) and report that as a negative check, not a proof. "
        "(2) p.Asn1002Lys has no functional data; ACMG PM1 is explicitly NOT invoked, since the "
        "BUBR1 kinase domain shows no regional missense constraint and BUB1B is not a constrained "
        "gene. (3) Structural variants are out of scope — the callset is SNV/indel only. "
        "(4) Deep intronic variants were not systematically screened beyond +/-8 bp splice "
        "padding. (5) A VCF-only mosaic-aneuploidy scan was NEGATIVE and is reported as negative: "
        "the per-chromosome trend tracks GC content and chromosome size, i.e. coverage bias, and "
        "the statistic is too coarse at 44x depth. MVA is cell-mosaic and is not reliably "
        "diagnosed from bulk short-read depth.\n\n"
        "A frequency-handling defect found and fixed mid-analysis is documented in the repository "
        "because it generalises: treating a missing gnomAD annotation as a confirmed zero "
        "promoted 12 common variants (up to AF 0.93) into the rare pool, two into the top five."
    ),
}

TRACK2 = {
    "B7": TEAM,

    "B8": (
        "We went from genotype to candidates through molecular FATE rather than consequence "
        "label, and the route matters because it determines what is even druggable.\n\n"
        "STEP 1 — classify each allele by fate. p.Leu737Ter sits in exon 17 of 23 with the PTC "
        "745 nt upstream of the last exon-exon junction and six junctions downstream: robustly "
        "NMD-competent, contributing ZERO protein. p.Asn1002Lys sits in the FINAL exon and "
        "therefore ESCAPES NMD. Consequence: the mutant polypeptide is the ONLY BUBR1 species the "
        "child's cells can make. That reduces the problem to one protein species and one "
        "degradation pathway.\n\n"
        "STEP 2 — establish that this is a DOSAGE problem, not a broken-enzyme problem. Human "
        "BUBR1's C-terminal domain is a pseudokinase whose catalytic activity is dispensable for "
        "error-free segregation (PMID 22698286). MVA kinase-domain missense alleles do not "
        "abolish catalysis; they destabilise the fold and are proteasome-cleared, at 5-10x "
        "reduced abundance with ~2x faster turnover, and forced re-expression to wild-type levels "
        "FULLY restores the checkpoint (PMID 20516114).\n\n"
        "STEP 3 — quantify the target. The BUBR1 dose-response is switch-like: ~13% residual "
        "leaves segregation essentially normal, ~6% causes missegregation in most cells; mouse "
        "series puts ~5% at postnatal lethality and 0% at E3.5 (PMID 20516114, 18932004, "
        "15208629, 31738183). This proband sits at roughly 5-10% residual, so clearing the "
        "threshold requires raising one destabilised protein by approximately 1.3-2.6 fold. That "
        "converts every downstream candidate from 'did it go up' into a PRE-REGISTERED effect "
        "size decided before any experiment.\n\n"
        "STEP 4 — enumerate candidates per allele axis: PTC readthrough plus obligate NMD "
        "inhibition for allele 1; proteostasis/chaperone modulation for allele 2; the "
        "NAD+/SIRT2/BubR1-K668 stabilisation axis; aneuploidy-selective vulnerabilities; and "
        "oncological safety given the child's rhabdomyosarcoma.\n\n"
        "STEP 5 — run a HARD CONTRADICTION SCREEN BEFORE ranking, not after, asking of every "
        "candidate: would this further weaken the spindle assembly checkpoint, worsen aneuploidy, "
        "or add risk specific to a cancer-predisposed, growth-restricted child with congenital "
        "nephrocalcinosis?\n\n"
        "STEP 6 — hand every survivor to an INDEPENDENT ADVERSARIAL FACT-CHECK instructed to "
        "assume the claim is wrong, verify regulatory status against primary sources, pull the "
        "FULL TEXT of every cited paper to confirm it says what was claimed, and hunt for failed "
        "trials. This stage overturned our own top-ranked candidate (see B10)."
    ),

    "B9": (
        "BOTH, deliberately and in that order: automated multi-agent generation followed by "
        "independent adversarial verification, with human-directed scoping throughout.\n\n"
        "Candidate GENERATION was LLM-assisted and parallel — five independent mechanistic axes "
        "were explored concurrently, each querying ChEMBL, PubMed, bioRxiv and ClinicalTrials.gov "
        "programmatically via API.\n\n"
        "Candidate VERIFICATION was separate, adversarial and non-negotiable: each proposed "
        "candidate was handed to an independent agent that had NOT generated it, instructed to "
        "refute it, to check the regulatory claim against the actual FDA label / Drugs@FDA / "
        "EMA-CHMP record rather than a secondary summary, and to retrieve primary full text "
        "rather than abstracts.\n\n"
        "This is the methodological core of our submission rather than an implementation detail. "
        "A generate-only LLM pipeline produces confident, plausible, wrong drug lists; the "
        "verification stage is what makes the output trustworthy, and we can show it working "
        "because it demolished our own lead candidate."
    ),

    "B10": (
        "Verification changed the outcome materially. The single most important result is that "
        "OUR OWN TOP-RANKED CANDIDATE DID NOT SURVIVE IT.\n\n"
        "ARIMOCLOMOL was ranked first — FDA-approved September 2024 with paediatric labelling "
        "from age 2, which made it regulatorily the most attractive option available. Independent "
        "fact-check dropped it on four independent grounds:\n"
        "(1) DIRECTIONAL HARM. The plan was to chronically amplify HSF1-driven heat-shock "
        "signalling in a child whose defining risk is very-early-onset malignancy. Eliminating "
        "HSF1 is TUMOUR-PROTECTIVE in mice (PMID 17889646). We would be pushing, for years, the "
        "exact programme whose genetic removal protects against cancer.\n"
        "(2) WRONG CHAPERONE. The primary source implicates HSP90; arimoclomol co-induces HSP70. "
        "Our draft had bridged that gap with the vague phrase 'cytosolic chaperone capacity'.\n"
        "(3) DIRECT NEGATIVE. The closest head-to-head experiment in human patient fibroblasts "
        "found HSP90 inhibition rescued the folding defect while arimoclomol did nothing up to "
        "0.5 mM (PMID 34481829).\n"
        "(4) THE CLASS HAS FAILED. Phase 3 ALS p=0.62 (PMID 38782015); Phase 2/3 IBM p=0.12 "
        "(PMID 37739573); a target-tissue pharmacodynamic null; Gaucher Phase 2 terminated; "
        "negative CHMP opinion July 2026.\n\n"
        "Two citation errors in our own draft were also caught: PMID 15034571 is an efficacy "
        "study in SOD1 mice and does not establish the mechanistic claim attributed to it, and a "
        "secondary 'First Approval' summary had been mistaken for a regulator reframing the "
        "mechanism. The actual FDA label states the mechanism is UNKNOWN and never mentions "
        "HSP70.\n\n"
        "Expert curation also produced explicit CONTRAINDICATIONS, which we regard as a primary "
        "deliverable rather than a caveat list: HSP90 inhibitors are genotype-specifically "
        "catastrophic here (the surviving allele is the HSP90-dependent client — inhibition "
        "strips away the only working copy); amlexanox inhibits TBK1, a mitotic kinase; "
        "nicotinamide inhibits sirtuins; gentamicin is contraindicated by this child's congenital "
        "nephrocalcinosis and preterm birth; 2,6-diaminopurine acts via FTSJ1, whose loss causes "
        "intellectual disability; and the entire MPS1/TTK class directly inhibits the checkpoint "
        "at issue. 17 of 22 candidates were rejected."
    ),

    "B11": "PUBLIC SOURCES ONLY. No proprietary drug database, no commercial literature service, "
           "no paid API. Every regulatory claim is verifiable against a public FDA or EMA record "
           "and every mechanistic claim against a PubMed-indexed primary source.",

    "B12": (
        "ChEMBL (EMBL-EBI) — compound, target, mechanism-of-action and bioactivity queries.\n"
        "ClinicalTrials.gov API v2 — trial existence, phase, status, termination and results; "
        "used both to find evidence and to find its ABSENCE (there are zero registered MVA or "
        "BUB1B trials).\n"
        "PubMed / NCBI E-utilities — primary literature, retrieved as full text wherever "
        "available rather than abstracts.\n"
        "FDA DailyMed and Drugs@FDA — Structured Product Labels, verbatim indications, warnings, "
        "paediatric labelling (section 8.4) and mechanism sections (12.1), used to verify every "
        "approval claim at source.\n"
        "EMA / CHMP opinions and referrals — EU authorisation status, withdrawals and negative "
        "opinions.\n"
        "gnomAD v4 and ClinVar — allele frequency and clinical classification.\n"
        "UniProt and Ensembl — domain boundaries, transcript architecture, exon numbering and NMD "
        "competence.\n"
        "Human Phenotype Ontology, OMIM, ClinGen, Orphanet — disease definition, inheritance and "
        "gene-disease validity.\n"
        "bioRxiv/medRxiv — preprint coverage, treated as preprint and labelled as such."
    ),

    "B13": "None. No proprietary data sources were used.",

    "B14": (
        "LOSS OF FUNCTION, autosomal recessive — but the important characterisation is finer than "
        "that label, and getting it right is what redirected the search.\n\n"
        "NOT a broken-enzyme problem. Human BUBR1's C-terminal domain is a PSEUDOKINASE whose "
        "catalytic activity is dispensable for error-free chromosome segregation (PMID 22698286). "
        "MVA kinase-domain missense alleles do not abolish catalysis — they destabilise the fold "
        "and are cleared by the proteasome in an HSP90-dependent manner (PMID 20516114). So this "
        "is a PROTEIN-DOSAGE problem with a hard viability floor.\n\n"
        "ALLELE-RESOLVED. Allele 1 is NMD-competent and contributes zero protein. Allele 2 "
        "escapes NMD (final exon) and is the only species made. Whole-cell BUBR1 abundance "
        "therefore equals whatever fraction of the mutant survives turnover.\n\n"
        "PATHWAY. BUBR1 is a core component of the mitotic checkpoint complex with "
        "MAD2/BUB3/CDC20, inhibiting APC/C-CDC20 to sustain the spindle assembly checkpoint, and "
        "it scaffolds PP2A-B56 through its KARD motif to stabilise kinetochore-microtubule "
        "attachments. Note the scaffolding point has a therapeutic consequence: bulk PP2A "
        "activation cannot substitute, because what is missing is LOCALISATION, and unlocalised "
        "PP2A risks stabilising erroneous attachments.\n\n"
        "DOWNSTREAM CONSEQUENCE CHAIN. Weakened SAC leads to premature chromatid separation, then "
        "chromosome missegregation, then constitutional mosaic aneuploidy, which produces "
        "(a) intrauterine growth restriction and postnatal growth failure, (b) cancer "
        "predisposition with a characteristic embryonal spectrum — rhabdomyosarcoma, Wilms "
        "tumour, leukaemia — and (c) progeroid/senescence features. Parental recurrent "
        "miscarriage fits carrier parents producing aneuploid conceptuses (PMID 24981203).\n\n"
        "QUANTIFIED. ~13% residual BUBR1 leaves segregation essentially normal; ~6% causes "
        "missegregation in most cells; below ~5% is lethal. This proband sits at roughly 5-10%, "
        "which is why the therapeutic ask is a 1.3-2.6 fold increase in one destabilised protein "
        "rather than restoration of wild type."
    ),

    "B15": (
        "Approximately 6-8 hours of concentrated analysis, heavily parallelised, on CPU-only "
        "commodity hardware at effectively zero marginal cost.\n\n"
        "Roughly: 1 hour on allele-resolved mechanism characterisation and the dosage model; "
        "2 hours on the five parallel candidate-generation axes; 2 hours on independent "
        "adversarial verification, which was the single most expensive stage and the one that "
        "changed the answer; 1 hour on the contradiction screen and the oncology-safety review; "
        "1-2 hours on synthesis and writing.\n\n"
        "The verification stage cost roughly as much as generation. We consider that the correct "
        "ratio for this task and would not cut it: it is what caught a misattributed mechanism "
        "citation, a secondary source mistaken for a regulatory position, an FDA label that "
        "actually disclaims any known mechanism, four failed trials, and ultimately our own "
        "top-ranked candidate."
    ),

    "B16": (
        "We characterised biallelic BUB1B (p.Leu737Ter + p.Asn1002Lys) as a PROTEIN-DOSAGE "
        "disorder with a quantified viability window, screened 22 candidates across five "
        "mechanistic axes, and reached an honest negative: NO APPROVED DRUG CURRENTLY HAS A "
        "DEFENSIBLE DISEASE-MODIFYING RATIONALE FOR THIS CHILD.\n\n"
        "MECHANISM. BUBR1's C-terminal domain is a pseudokinase whose catalysis is dispensable; "
        "MVA missense alleles there destabilise the fold rather than break the enzyme, and forced "
        "re-expression fully restores checkpoint function. Allele 1 is NMD-competent (exon 17/23) "
        "and makes no protein; allele 2 escapes NMD (final exon) and is the only species present. "
        "The dose-response is switch-like — ~13% tolerated, ~6% fails, <5% lethal — placing this "
        "child at ~5-10%, so the target is a 1.3-2.6 fold increase in one protein.\n\n"
        "CENTRAL FINDING. Our two leading candidates failed for the SAME structural reason, and "
        "it generalises. MVA is simultaneously a cellular-FRAGILITY disorder and a "
        "CANCER-PREDISPOSITION syndrome (~37% malignancy, mostly under age 3), and pre-malignant "
        "aneuploid clones are constrained partly BY the proteotoxic stress aneuploidy imposes. So "
        "any therapy raising GENERAL cellular survival capacity — chaperone buffering "
        "(arimoclomol), NAD+ repletion (niacin) — is non-selective: it buffers the fragile cell "
        "you want to save AND the clone you need constrained. Neither can be aimed at BUBR1, and "
        "no biomarker monitors the off-target half. The screening question for this disease class "
        "is therefore: does this raise general cellular survival capacity? If yes, it is "
        "directionally suspect. The same inversion disqualifies the whole aneuploidy-selective "
        "literature: in a tumour inside a euploid host that selectivity is the therapy, but in MVA "
        "the HOST is the aneuploid organism, so the therapeutic index is not narrow — it is "
        "inverted.\n\n"
        "STRENGTHS. Allele-resolved rather than gene-level; a pre-registered effect size instead "
        "of 'did it go up'; a contradiction screen run BEFORE ranking that eliminated 17 of 22 "
        "candidates; independent adversarial verification that overturned our own top candidate, "
        "which we report rather than hide; and an explicit contraindications table — HSP90 "
        "inhibitors would strip away this child's only functional allele.\n\n"
        "CLINICAL HOOK. Vincristine, the backbone of curative rhabdomyosarcoma therapy, kills by "
        "sustaining a SAC-dependent mitotic arrest. This child's SAC is the lesion, and MVA cells "
        "slip such arrests within an hour. We state this as a FALSIFIABLE PREDICTION with a named "
        "one-plate experiment, graded D for mechanism and E for clinical inference, and say "
        "explicitly that it is NOT grounds to withhold or reduce vincristine — VAC is curative, "
        "and under-treating a curable cancer is the larger, better-characterised harm.\n\n"
        "LIMITATIONS. No agent here has been tested against BUB1B or in MVA. The load-bearing "
        "assumption — that p.Asn1002Lys is a destabilised hypomorph — is UNTESTED, with a "
        "counterexample in the same published series (Q921H, same domain, functionally normal). "
        "Phase is inferred, not demonstrated. We therefore state an explicit KILL CONDITION: if "
        "p.Asn1002Lys is not destabilised, the abundance-restoration thesis dies and should be "
        "abandoned, not rescued. The highest-value next steps are not pharmacological — phase the "
        "variants, and measure BUBR1 level and checkpoint function in the child's own cells."
    ),
}


def fill(ws, answers, body_font):
    for coord, text in answers.items():
        cell = ws[coord]
        cell.value = text
        cell.font = Font(name=body_font, size=10)
        cell.alignment = Alignment(wrap_text=True, vertical="top")
        # Approximate a sensible row height: column B is ~45 chars wide.
        lines = sum(max(1, len(seg) // 52 + 1) for seg in text.split("\n"))
        ws.row_dimensions[cell.row].height = min(max(15, lines * 12.0), 800)


def main():
    wb = openpyxl.load_workbook(SRC)
    t1, t2 = wb["Track 1 methods"], wb["Track 2 methods"]
    body_font = t1["A9"].font.name or "Arial"

    fill(t1, TRACK1, body_font)
    fill(t2, TRACK2, body_font)

    # Give the answer column room to breathe without disturbing the question column.
    t1.column_dimensions["B"].width = 92
    t2.column_dimensions["B"].width = 92

    wb.save(OUT)
    print(f"wrote {OUT}")
    for name, answers in (("Track 1 methods", TRACK1), ("Track 2 methods", TRACK2)):
        total = sum(len(v) for v in answers.values())
        print(f"  {name}: {len(answers)} answers, {total:,} characters")
        abstract = answers.get("B18") or answers.get("B16")
        print(f"    abstract: {len(abstract.split())} words (limit 500)")


if __name__ == "__main__":
    main()
