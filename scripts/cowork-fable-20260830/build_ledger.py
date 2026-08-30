#!/usr/bin/env python3
"""Build the Track 2 candidate evidence ledger (TSV)."""
import csv

COLS = ["id","axis","agent","class","mechanism","genotype_fit","best_evidence",
        "identifier","evidence_tier","stage_2026","cns_penetration","key_risk","verdict","notes"]

# Evidence tiers:
# E1 human clinical outcome in MVA | E2 human clinical data, other disease
# E3 in vivo, exact BubR1-insufficiency model | E4 in vivo, other model
# E5 patient-derived human cells | E6 cell lines / reporters | E7 mechanistic inference only

R = []
def add(**kw):
    row = {c: kw.get(c, "") for c in COLS}
    R.append(row)

# ---------------- AXIS A : restore BubR1 dosage ----------------
add(id="A01", axis="A-restore", agent="UGA suppressor tRNA (Leu), prime-editing-installed (PERT)",
    **{"class":"Genetic medicine"},
    mechanism="Prime editing converts a dispensable endogenous tRNA gene into a Leu-charged UGA suppressor tRNA; one-time, no overexpression",
    genotype_fit="OPTIMAL - restores wild-type Leu737; UGA-specific; no readthrough at natural stops reported",
    best_evidence="Rescued Batten/Tay-Sachs/CF cell models; corrected pathology in Hurler mouse in vivo; screened all 418 human tRNA genes; no transcriptomic/proteomic perturbation",
    identifier="PMID 41261131; DOI 10.1038/s41586-025-09732-2 (Nature 648:191-202, 2025)",
    evidence_tier="E4", stage_2026="Preclinical (published Nov 2025)", cns_penetration="Delivery-dependent",
    key_risk="Delivery to all affected tissues; permanence of edit; no human data",
    verdict="LEAD", notes="Only route that restores the exact wild-type residue")

add(id="A02", axis="A-restore", agent="AAV-delivered engineered UGA suppressor tRNA",
    **{"class":"Genetic medicine"},
    mechanism="rAAV-packaged engineered UGA suppressor tRNA gene; solves the UGA vector-production problem",
    genotype_fit="STRONG - UGA-specific; amino acid choice tunable; AAV is systemic and CNS-capable",
    best_evidence="Single dose restored enzyme activity to ~10% of normal in two lysosomal storage mouse models",
    identifier="PMID 41555020; DOI 10.1038/s41587-025-02982-5 (Nat Biotechnol 2026)",
    evidence_tier="E4", stage_2026="Preclinical", cns_penetration="Yes (serotype-dependent)",
    key_risk="AAV immunogenicity; redosing; durability",
    verdict="LEAD (alternate route)", notes="Closest published match to this genotype")

add(id="A03", axis="A-restore", agent="2,6-diaminopurine (DAP)",
    **{"class":"Small molecule TRID"},
    mechanism="Inhibits FTSJ1 -> loss of Cm34 in tRNA-Trp anticodon loop -> tRNA-Trp decodes UGA by A-C wobble; inserts Trp",
    genotype_fit="STRONG - UGA-exclusive; inserts Trp giving p.Leu737Trp, hydrophobic->hydrophobic in an unstructured linker",
    best_evidence="One of four compounds (with clitocine, SRI-41315, TLN468) identified as jointly most effective in the 2026 TRID head-to-head; UGA-exclusive (rescued UGA TP53 in Calu-6, not UAG/UAA). ABSTRACT-LEVEL ONLY, full text not retrieved: oral 29 mg/kg mouse; BBB penetrant with slower brain clearance than other tissues; non-genotoxic in micronucleus +/- S9; ~10 months daily dosing in dams without overt toxicity",
    identifier="PMID 32198346 (Nat Commun 11:1509); PMID 36641622 (Mol Ther 31:970); PMID 41917975 (J Transl Med 2026)",
    evidence_tier="E6", stage_2026="Preclinical; research chemical; no IND, no sponsor identified",
    cns_penetration="Yes - demonstrated; preferential brain retention",
    key_risk="FTSJ1 LoF causes X-linked intellectual disability (PMID 15342698); FTSJ1 depletion gives abnormal dendritic spines in human NPCs and memory deficits in Drosophila (PMID 36720500). Unevaluated neurodevelopmental risk in a child",
    verdict="BRIDGE - gated on juvenile neurodevelopmental tox study",
    notes="Does NOT inhibit NMD - must be paired (see A08/A09)")

add(id="A04", axis="A-restore", agent="Peh 2026 UGAA-selected readthrough hits",
    **{"class":"Small molecule TRID"},
    mechanism="Not disclosed in abstract; ~20,000-compound screen",
    genotype_fit="EXACT CONTEXT MATCH - hits reported as effective 'particularly on UGAA and UAAG premature stop codons'; this proband's tetranucleotide is UGAA",
    best_evidence="Outperformed both gentamicin and ataluren in a Nagashima-type PPK screen",
    identifier="PMID 42034525; DOI 10.1016/j.jdermsci.2026.02.001 (J Dermatol Sci 122:78-85, 2026)",
    evidence_tier="E6", stage_2026="Very early; compound identities not in abstract (full text paywalled)",
    cns_penetration="Unknown", key_risk="Unknown - uncharacterised",
    verdict="HIGHEST-YIELD ACTION - contact authors (Hokkaido/Tsukuba) for identities",
    notes="Only chemistry ever deliberately optimised against this termination context")

add(id="A05", axis="A-restore", agent="TLN468 (2-guanidino-quinazoline)",
    **{"class":"Small molecule TRID"},
    mechanism="Ribosome-targeting; strongly biases insertion toward one amino acid; does NOT read through normal termination codons",
    genotype_fit="MODERATE - broad codon activity",
    best_evidence="More efficient than gentamicin across the 40 most common DMD PTCs; one of four compounds identified as jointly most effective in the 2026 TRID head-to-head. Karri 2024 is an amino-acid-identity study across four CFTR PTCs, not an organoid ranking",
    identifier="PMID 35994666 (PNAS 119:e2122004119); PMID 39098506 (J Cyst Fibros 23:1185); PMID 41917975",
    evidence_tier="E6", stage_2026="Preclinical (I2BC/CEA Paris-Saclay)", cns_penetration="Not established",
    key_risk="Not characterised in vivo",
    verdict="SCREEN", notes="Best safety property in class - no readthrough at natural stops")

add(id="A06", axis="A-restore", agent="SRI-41315 (and SRI-37240)",
    **{"class":"Small molecule TRID"},
    mechanism="Reduces eRF1 abundance; prolonged ribosomal pause at stop codons; synergises with aminoglycosides",
    genotype_fit="MODERATE - not codon-selective",
    best_evidence="From a large HTS campaign; one of four compounds identified as jointly most effective in the 2026 TRID head-to-head (abstract level)",
    identifier="PMID 34272367; DOI 10.1038/s41467-021-24575-x (Nat Commun 12:4358)",
    evidence_tier="E6", stage_2026="Preclinical (Southern Research / UAB)", cns_penetration="Not established",
    key_risk="Global eRF1 depletion -> broad translational-fidelity effects",
    verdict="SCREEN", notes="Candidate combination partner for DAP")

add(id="A07", axis="A-restore", agent="NV848 (1,2,4-oxadiazole)",
    **{"class":"Small molecule TRID"},
    mechanism="Interferes with post-transcriptional tRNA modification (mechanism class shared with DAP)",
    genotype_fit="MODERATE - codon preference not fully mapped",
    best_evidence="Restored full-length LRBA from R1683X in patient fibroblasts, outperforming ataluren; cleanest proteomic profile of its series; NV848 + ETI + NMDI14 enhanced CFTR in W1282X organoids",
    identifier="PMID 41541268 (Mol Ther Nucleic Acids 37:102808); PMID 41492359 (Genet Med Open 4:103472)",
    evidence_tier="E5", stage_2026="Preclinical (Palermo)", cns_penetration="Not established",
    key_risk="Limited characterisation",
    verdict="SCREEN", notes="Only published readthrough + NMD-inhibitor combination result in this class")

add(id="A08", axis="A-restore", agent="NMDI14",
    **{"class":"NMD inhibitor"},
    mechanism="Disrupts the SMG7-UPF1 interaction; upregulates NMD targets at nanomolar concentrations",
    genotype_fit="REQUIRED PARTNER - PTC is in exon 17/23 with 6 downstream junctions, a canonical NMD substrate",
    best_evidence="Combined with a readthrough drug, restored full-length p53; used successfully in combination by Perriera 2025",
    identifier="PMID 24662918; DOI 10.1158/0008-5472.CAN-13-2235 (Cancer Res 74:3104)",
    evidence_tier="E6", stage_2026="Research reagent", cns_penetration="Not established",
    key_risk="POSSIBLE DOMINANT-NEGATIVE: stabilising the truncated protein (retains TPR, KEN, GLEBS, KARD; loses pseudokinase domain) may sequester Bub3/Cdc20. Must be tested alone with a functional readout",
    verdict="SCREEN - with mandatory NMD-alone safety arm", notes="Novel hazard identified in this report")

add(id="A09", axis="A-restore", agent="SMG1 inhibitor (SMG1i)",
    **{"class":"NMD inhibitor"},
    mechanism="Blocks the core NMD kinase SMG1 -> no UPF1 phosphorylation",
    genotype_fit="REQUIRED PARTNER (see A08)",
    best_evidence="In Cftr G542X mouse primary cells synergised with G418, gentamicin and paromomycin - but NOT with amikacin, tobramycin, PTC124, escin or amlexanox",
    identifier="PMID 33396210; DOI 10.3390/ijms22010344 (IJMS 22:344)",
    evidence_tier="E6", stage_2026="Research reagent; no SMG1 inhibitor found in any registered trial",
    cns_penetration="Not established",
    key_risk="Smg1 loss embryonic-lethal E8.5 in mice; depletion accumulates PTC variants from ~9% of genes (PMID 20566848). Chronic systemic NMD inhibition in a growing child is not benign",
    verdict="SCREEN - with mandatory NMD-alone safety arm", notes="Synergy is partner-specific")

add(id="A10", axis="A-restore", agent="Gentamicin (systemic IV)",
    **{"class":"Aminoglycoside TRID"},
    mechanism="Misreading at the ribosomal decoding site; inserts Trp/Arg/Cys at UGA",
    genotype_fit="MODERATE - context-dependent; the tetranucleotide is the primary determinant",
    best_evidence="Only human proof of systemic readthrough: 7.5 mg/kg/d IV x14d in 3 RDEB adults, of whom TWO continued 7.5 mg/kg twice weekly x12wk; restored type VII collagen at the DEJ persisting >6 months; >85% closure of monitored wounds; no oto/nephrotoxicity or anti-C7 antibodies observed",
    identifier="PMID 38366625; DOI 10.1093/bjd/ljae063 (Br J Dermatol 191:267)",
    evidence_tier="E2", stage_2026="Licensed antibiotic; readthrough use off-label; open-label n=3",
    cns_penetration="Poor - polycationic",
    key_risk="Cumulative and IRREVERSIBLE cochlear toxicity; nephrotoxicity. Different risk calculus in a child than in 3 adults over 14 weeks",
    verdict="PROOF-OF-MECHANISM ONLY - not a therapy recommendation",
    notes="Positive control for the ex vivo panel; a positive result would validate the whole readthrough strategy for this allele")

add(id="A11", axis="A-restore", agent="G418 / geneticin",
    **{"class":"Aminoglycoside TRID"},
    mechanism="Most potent readthrough aminoglycoside in vitro; partially inhibits NMD",
    genotype_fit="Benchmark", best_evidence="Universal positive control; among the most effective in patient organoids",
    identifier="PMID 41917975", evidence_tier="E6", stage_2026="Research reagent only",
    cns_penetration="n/a", key_risk="Too cytotoxic for systemic human use",
    verdict="POSITIVE CONTROL", notes="In vitro benchmark")

add(id="A12", axis="A-restore", agent="Ataluren (PTC124 / Translarna)",
    **{"class":"Small molecule TRID"},
    mechanism="Claimed promotion of near-cognate tRNA selection",
    genotype_fit="N/A - activity not replicated",
    best_evidence="NEGATIVE: original signal explained by PTC124-AMP being a firefly-luciferase adduct inhibitor (Kd 120 pM); no activity across a diverse reporter panel while G418 worked everywhere; no detectable readthrough in the 2026 head-to-head",
    identifier="PMID 20194791 (PNAS 107:4878); PMID 23824517 (PLoS Biol 11:e1001593); PMID 41917975",
    evidence_tier="E6",
    stage_2026="EU marketing authorisation NOT renewed, expired 28 Mar 2025 (CHMP: effectiveness not confirmed); US NDA resubmission withdrawn 12 Feb 2026. UK MHRA position not re-verified for 2026",
    cns_penetration="Not established", key_risk="Efficacy not established",
    verdict="REJECT", notes="ChEMBL CHEMBL256997 still shows withdrawn_flag=false and is STALE on the EU non-renewal")

add(id="A13", axis="A-restore", agent="ELX-02 / exaluren",
    **{"class":"Designer glycoside TRID"},
    mechanism="Eukaryotic-ribosome-selective glycoside from the NB124 series",
    genotype_fit="WRONG DISTRIBUTION - renally targeted by design",
    best_evidence="Ph2b EXACT in Alport recruiting from 30 Jun 2026, age >=12, 0.75 mg/kg SC daily x32wk. CF Ph2 did not meet its endpoints; the widely-cited insufficient-lung-exposure explanation could NOT be sourced to a primary reference (PMID 30650260 and PMID 33465285 are Phase 1 healthy-volunteer studies) - treat the exposure figures as UNCONFIRMED",
    identifier="NCT07523581; PMID 30650260; PMID 33465285",
    evidence_tier="E2", stage_2026="Phase 2b (Alport); CF programme abandoned", cns_penetration="No data",
    key_risk="Ototoxicity signal at 5.0 mg/kg MAD (confounded by placebo-arm threshold changes); parenteral only",
    verdict="REJECT for MVA", notes="Wrong tissue targeting, no CNS")

add(id="A14", axis="A-restore", agent="Clitocine",
    **{"class":"Nucleoside TRID"},
    mechanism="Incorporated into mRNA; induces readthrough when at position 3 of a PTC",
    genotype_fit="UNCERTAIN - codon preference not established in the primary reference we retrieved",
    best_evidence="Friesen 2017 shows readthrough requires clitocine at the third position of a PTC; it says nothing about UAA preference. NOTE: clitocine ranked in the SAME top tier as DAP, SRI-41315 and TLN468 in the 2026 head-to-head. It was de-prioritised by the DAP authors over toxicity, which is a general property of RNA incorporation rather than a measured result in the cited paper",
    identifier="PMID 28096517 (RNA 23:567); PMID 41917975", evidence_tier="E6", stage_2026="Preclinical, not advanced",
    cns_penetration="Not reported", key_risk="Mutagenic risk intrinsic to RNA incorporation",
    verdict="HOLD - reconsider if the DAP neurodevelopmental gate cannot be cleared",
    notes="Usually dismissed on weaker grounds than the evidence supports")

add(id="A15", axis="A-restore", agent="Escin",
    **{"class":"Small molecule TRID"},
    mechanism="Claimed readthrough + NMD inhibition", genotype_fit="N/A",
    best_evidence="NEGATIVE in two independent studies: no SMG1i synergy; no detectable readthrough, and the only compound failing to restore CFTR in every organoid genotype tested",
    identifier="PMID 33396210; PMID 41917975", evidence_tier="E6", stage_2026="n/a",
    cns_penetration="n/a", key_risk="Haemolytic", verdict="REJECT", notes="Discount it")

add(id="A16", axis="A-restore", agent="Amlexanox",
    **{"class":"Small molecule TRID"},
    mechanism="Readthrough + partial NMD inhibition; licensed topically",
    genotype_fit="UNCERTAIN - erratic, context-dependent",
    best_evidence="Best agent in aniridia PAX6 iPSC optic cups; INEFFECTIVE on F5 p.Arg1161Ter; no SMG1i synergy",
    identifier="PMID 37483273; PMID 37866515; PMID 33396210", evidence_tier="E5",
    stage_2026="Licensed topically; systemic use investigational", cns_penetration="Not established",
    key_risk="Low - good tolerability record", verdict="SCREEN (low priority)",
    notes="Cheap to include in the ex vivo panel")

add(id="A17", axis="A-restore", agent="CC-90009 / SJ6986 (GSPT1 degraders)",
    **{"class":"Molecular glue"},
    mechanism="Cereblon glue degrading GSPT1/eRF3a; secondarily lowers eRF1 and suppresses NMD",
    genotype_fit="MODERATE - not codon-selective; dual readthrough+NMD in one molecule",
    best_evidence="CC-90009 rescued W1282X-CFTR to ~20% of WT alone; SJ6986 4.6% alone, 13.7% with G418; G542X+G418 43.9%",
    identifier="PMID 33764477 (NAR 49:3692); DOI 10.1172/JCI154571 (JCI 132:e154571)",
    evidence_tier="E6", stage_2026="CC-90009 clinical-stage in AML only", cns_penetration="Not established",
    key_risk="Both substantially inhibit ENaC, linked to clinical hypotension; degrading a core termination factor systemically in a child",
    verdict="REJECT for paediatric chronic use", notes="Elegant mechanism, unacceptable profile here")

add(id="A18", axis="A-restore", agent="AP003 (Alltrna)",
    **{"class":"Suppressor tRNA"},
    mechanism="Engineered UGA suppressor tRNA inserting Arg, liver-directed LNP",
    genotype_fit="WRONG - would give p.Leu737Arg (charge into a hydrophobic stretch); liver-directed, no CNS",
    best_evidence="First tRNA therapeutic to enter the clinic; Ph1 SAD healthy volunteers, Australia (TGA CTN), announced 31 Mar 2026",
    identifier="Company announcement 31 Mar 2026; not registered on ClinicalTrials.gov",
    evidence_tier="E2", stage_2026="Phase 1", cns_penetration="No",
    key_risk="n/a for this use", verdict="REJECT for this genotype",
    notes="Matters as proof the modality reached humans")

add(id="A19", axis="A-restore", agent="Colistin",
    **{"class":"Claimed TRID"}, mechanism="Unverified",
    genotype_fit="n/a", best_evidence="NONE FOUND - PubMed returns zero results for colistin + readthrough / nonsense suppression",
    identifier="none", evidence_tier="unsupported", stage_2026="n/a", cns_penetration="n/a",
    key_risk="Nephrotoxic, neurotoxic", verdict="REJECT - unsupported claim",
    notes="Appears in some readthrough lists without primary evidence")

# ---------------- AXIS B : downstream of the checkpoint defect ----------------
add(id="B01", axis="B-downstream", agent="Low-dose paclitaxel (0.05-0.5 nM)",
    **{"class":"Microtubule agent"},
    mechanism="Dampens microtubule plus-end assembly rate, restoring spindle geometry and reducing lagging chromosomes",
    genotype_fit="POOR - wrong mechanism. Ertych's CIN driver is increased plus-end assembly from AURKA overexpression / CHK2 loss; MVA1's driver is SAC loss plus attachment defects from low BubR1",
    best_evidence="Restored assembly rates and karyotype stability in CIN cancer lines over 30 generations; BUT in the same study CIN suppression ACCELERATED xenograft growth, and sub-nanomolar nocodazole INDUCED CIN in stable cells",
    identifier="PMID 24976383; DOI 10.1038/ncb2994 (Nat Cell Biol 2014)",
    evidence_tier="E6", stage_2026="No in vivo drug experiment exists", cns_penetration="Poor",
    key_risk="Fully reversible on washout -> indefinite spindle-poison dosing in a SAC-weak child; narrow bidirectional dose window",
    verdict="REJECT", notes="")

add(id="B02", axis="B-downstream", agent="KIF18A inhibitors - FIVE clinical-stage compounds: VLS-1488; sovilnesib (formerly AMG 650 - one molecule, two NCTs); ATX-295; MEN2501; GenSci122",
    **{"class":"Kinesin inhibitor"},
    mechanism="Aneuploid/CIN cells depend on KIF18A; euploid cells do not",
    genotype_fit="INVERTED - designed to kill aneuploid cells; this child's NORMAL tissues are aneuploid",
    best_evidence="Cohen-Sharir 2021 (~1000 cell lines, CRISPR + drug screens). Company-disclosure only, NOT peer-reviewed: VLS-1488 Ph1/2 50-800 mg QD, no DLTs, MTD not reached",
    identifier="PMID 33505028; NCT05902988, NCT06084416, NCT04293094, NCT06799065, NCT07226427, NCT06772415",
    evidence_tier="E2", stage_2026="Phase 1/2, adults only", cns_penetration="Not established",
    key_risk="Therapeutic window may invert entirely; sponsor disclosures (company sources only) pair the class with taxanes and nominate p16 IHC as selection biomarker - both adverse here; KIF18A motor variants cause egg aneuploidy and diminished fertility (PMID 39475646)",
    verdict="REJECT as chronic therapy", notes="May be relevant to how a future tumour is treated")

add(id="B03", axis="B-downstream", agent="AICAR (AMPK/energy stress)",
    **{"class":"Metabolic"},
    mechanism="Exploits the metabolic burden of aneuploidy; induces p53-mediated apoptosis in trisomic MEFs",
    genotype_fit="INVERTED - would kill his own aneuploid tissues, including brain and marrow",
    best_evidence="Tang/Amon 2011", identifier="PMID 21315436; DOI 10.1016/j.cell.2011.01.017",
    evidence_tier="E6", stage_2026="No paediatric development", cns_penetration="Poor",
    key_risk="Marrow, muscle, CNS toxicity by design", verdict="REJECT", notes="")

add(id="B04", axis="B-downstream", agent="HSP90 inhibitors (17-AAG / tanespimycin)",
    **{"class":"Chaperone inhibitor"},
    mechanism="Aneuploidy compromises Hsp90 capacity and the proteasome -> proteotoxic stress",
    genotype_fit="INVERTED (as B03)", best_evidence="Tang/Amon 2011; Oromendia 2012",
    identifier="PMID 21315436; PMID 23222101", evidence_tier="E6",
    stage_2026="Development abandoned; ChEMBL109480 max_phase 3, never approved",
    cns_penetration="Poor", key_risk="Hepatotoxicity", verdict="REJECT", notes="")

add(id="B05", axis="B-downstream", agent="Chloroquine / hydroxychloroquine",
    **{"class":"Autophagy inhibitor"},
    mechanism="Aneuploid cells lean on autophagy",
    genotype_fit="HARMFUL - in NON-tumorigenic aneuploid human cells autophagy is protective; inhibiting it increased genomic instability, DNA damage and ROS",
    best_evidence="Ariyoshi 2016 directly contradicts the cancer-line result for the constitutional setting",
    identifier="PMID 27343755; DOI 10.1016/j.mrfmmm.2016.06.001", evidence_tier="E6",
    stage_2026="Licensed for other uses", cns_penetration="Yes",
    key_risk="Plausible route to MORE instability",
    verdict="AVOID - strong caution, not a proven contraindication",
    notes="Evidence is from microcell-transfer single-trisomy immortalised breast epithelial cells, not constitutional mosaic aneuploidy")

add(id="B06", axis="B-downstream", agent="STING inhibition (H-151)",
    **{"class":"Innate immune"},
    mechanism="Blocks micronuclei -> cGAS-STING -> chronic type-I IFN and NF-kB",
    genotype_fit="RATIONAL BUT UNTESTED - biology likely operative, never measured in an MVA patient",
    best_evidence="EVIDENCE CUTS BOTH WAYS. FOR: Li 2023 Nature reports that treatment with STING inhibitors REDUCES CIN-driven metastasis in melanoma, breast and colorectal models - direct in vivo evidence that STING blockade acts on chromosomal instability. AGAINST: Santaguida 2017 shows complex-karyotype cells recruit their own immune clearance via this pathway. No study in constitutional aneuploidy or MVA",
    identifier="PMID 29342134; PMID 37612508 (for); PMID 28633018 (against)", evidence_tier="E4 (cancer models) / E7 (MVA)",
    stage_2026="No clinical-stage STING antagonist", cns_penetration="Not established",
    key_risk="Blocking the pathway may preserve pre-malignant aneuploid clones in a cancer-predisposed child",
    verdict="NOT NOW - measure the interferon signature first",
    notes="Mechanism is not wrong; the risk/benefit in a constitutional setting is unknown and there is nothing to give him")

add(id="B07", axis="B-downstream", agent="JAK inhibition (tofacitinib / baricitinib)",
    **{"class":"Immunomodulator"},
    mechanism="Blunts chronic interferon signalling downstream of constitutional aneuploidy",
    genotype_fit="ANALOGOUS, IMPERFECT - Down syndrome drives IFN via chr21 gene dosage (4 IFN receptors), not via micronuclei",
    best_evidence="JAK1 inhibition rescued lethal immune hypersensitivity in a DS mouse model; Ph2 trials completed in DS",
    identifier="PMID 33207208; NCT04246372, NCT05662228, NCT07598643",
    evidence_tier="E2 (Down syndrome) / E7 (MVA)", stage_2026="Phase 2 in constitutional aneuploidy",
    cns_penetration="Limited", key_risk="Immunosuppression and class malignancy warnings in a cancer-predisposition syndrome",
    verdict="HYPOTHESIS - measure the interferon signature first", notes="Strongest symptom-modifying analogue available")

add(id="B08", axis="B-downstream", agent="MCAK/KIF2C modulation; CENP-E agonism; TUBB3 modulation",
    **{"class":"Mitotic"}, mechanism="Hypothesised error-correction enhancement",
    genotype_fit="n/a", best_evidence="NONE. No CENP-E agonist exists (all chemical matter is inhibitory); MCAK/Kif2b depletion and MCAK overexpression did not alter plus-end assembly rates",
    identifier="PMID 24976383", evidence_tier="none", stage_2026="n/a", cns_penetration="n/a",
    key_risk="n/a", verdict="REJECT - purely speculative", notes="Do not present as an option")

# ---------------- AXIS C : dosage-adjacent, ageing/senescence literature ----------------
add(id="C01", axis="C-adjacent", agent="NAD+ precursors (NMN, NR)",
    **{"class":"Supplement / metabolic"},
    mechanism="Raise NAD+ -> SIRT2 activity -> deacetylation of BubR1 K668 -> less ubiquitin-proteasome degradation -> more BubR1",
    genotype_fit="ATTRACTIVE ON PAPER, FAILS THE TUMOUR GATE",
    best_evidence="SIRT2 transgenic overexpression extended median lifespan in BubR1-H/H mice (reported +58% overall, +123% males), partially reversed the reduction in heart weight and LV dimensions, prevented J-point depression. BUT NMN itself was given only to WILD-TYPE mice (500 mg/kg/d i.p. x7d, BubR1 measured in testes, no lifespan data), and SIRT2 overexpression has no effect on lifespan in wild-type mice",
    identifier="PMID 24825348 (EMBO J 33:1438); PMID 38009412 (Aging Cell 22:e14027)",
    evidence_tier="E3 (SIRT2 genetic) / E4 (NMN, wrong genotype)", stage_2026="Widely sold supplement",
    cns_penetration="Limited", key_risk="NR increased cancer prevalence and brain metastasis in a TNBC model (PMID 36371959); NAM/NMN conferred chemoresistance and supported growth in pancreatic models in immunocompetent AND immunodeficient mice (PMID 41724424); NAMPT-NAD+ drives the pro-inflammatory SASP with an explicit precision-use warning (PMID 30778219)",
    verdict="REJECT in a cancer-predisposition child",
    notes="Mechanistic tension: SIRT2 deacetylates BubR1 at K668 (stabilising) AND K250 (removing the PCAF mark that protects BubR1 from APC/C proteolysis; K243R/+ mice develop tumours with massive missegregation, PMID 23878276)")

add(id="C02", axis="C-adjacent", agent="Senolytics - dasatinib + quercetin",
    **{"class":"Senolytic"},
    mechanism="Clear p16-positive senescent cells",
    genotype_fit="WEAKER THAN IT APPEARS",
    best_evidence="NEVER tested in a BubR1 mouse. The genetic analogue (INK-ATTAC, AP20187 0.2 ug/g i.p. q3d) delayed lordokyphosis and cataract and preserved fat and muscle in BubR1-H/H, but did NOT substantially extend survival and did NOT attenuate cardiac arrhythmia or arterial stiffening. D+Q evidence is in Ercc1-/D progeroid and naturally aged mice",
    identifier="PMID 22048312 (Nature 479); PMID 25754370; PMID 29988130",
    evidence_tier="E3 (genetic analogue) / E4 (drug, other models)", stage_2026="Investigational; multiple human trials in other indications",
    cns_penetration="Partial", key_risk="p16-Ink4a germline deletion extended BubR1-H/H median survival 25% but produced SIGNIFICANTLY MORE TUMOURS, 8 of 9 lung adenocarcinoma (PMID 18516091). Reducing p16 tone in a cancer-predisposition syndrome is unproven",
    verdict="REJECT pending direct evidence in a BubR1 model", notes="")

add(id="C03", axis="C-adjacent", agent="Fisetin",
    **{"class":"Senolytic / flavonoid supplement"},
    mechanism="Senolytic in aged mice; ALSO a direct Aurora B inhibitor and antimitotic",
    genotype_fit="ACTIVELY HARMFUL",
    best_evidence="Identified in a screen as an antimitotic that overrides mitotic arrest; caused premature chromosome segregation and mitotic exit without normal cytokinesis; Aurora B, Bub1, BubR1 and CENP-F rapidly lost kinetochore/centromere localisation",
    identifier="PMID 19395653; DOI 10.1093/carcin/bgp101 (Carcinogenesis 30:1032)",
    evidence_tier="E6", stage_2026="Widely sold supplement", cns_penetration="Yes",
    key_risk="Delocalises the very protein that is deficient, in a child with a constitutionally weakened SAC",
    verdict="CONTRAINDICATED", notes="")

add(id="C04", axis="C-adjacent", agent="SIRT2 inhibitors (e.g. SirReal2)",
    **{"class":"Epigenetic"}, mechanism="Selective SIRT2 inhibition",
    genotype_fit="OPPOSITE DIRECTION", best_evidence="Causes destabilisation of BubR1 in cells",
    identifier="PMID 25672491; DOI 10.1038/ncomms7263 (Nat Commun 6:6263)",
    evidence_tier="E6", stage_2026="Research", cns_penetration="n/a",
    key_risk="Lowers BubR1", verdict="CONTRAINDICATED", notes="")

add(id="C05", axis="C-adjacent", agent="Rapamycin / metformin / caloric restriction / antioxidants / exercise",
    **{"class":"Geroprotector"}, mechanism="Various",
    genotype_fit="UNKNOWN",
    best_evidence="NONE in any BubR1 model - PubMed returns zero. Nearest signal: monoallelic MVA carriers' sarcopenia predisposition correlated with mTORC1 hyperactivity, but no rapamycin was administered (PMID 31738183). Baker 2013 reportedly found no alteration in ROS in BubR1-overexpressing mice, weakening the antioxidant rationale (ABSTRACT-LEVEL ONLY, full text not retrieved)",
    identifier="PMID 31738183; PMID 23242215", evidence_tier="E7", stage_2026="n/a",
    cns_penetration="varies", key_risk="Unknown", verdict="NO EVIDENCE - do not recommend", notes="")

# ---------------- AXIS D : clinical care, actionable now ----------------
add(id="D01", axis="D-clinical", agent="Cardiac surveillance (ECG + echocardiography)",
    **{"class":"Monitoring"},
    mechanism="Detect the organ failure that the model literature identifies as terminal",
    genotype_fit="DIRECTLY SUPPORTED",
    best_evidence="Cardiac failure is reported as the presumed cause of death in BubR1-H/H mice and senescent-cell clearance reportedly failed to attenuate cardiac arrhythmia and arterial stiffening (Baker 2011, ABSTRACT-LEVEL ONLY); p16 deletion extended median but not maximum lifespan, authors state the condition causing death was not rescued; the one lifespan-extending intervention (SIRT2) partially reversed the reduction in heart weight and LV dimensions and prevented J-point depression; BubR1 insufficiency drives cardiac hypertrophy, fibrosis and senescence mirroring end-stage human heart failure. NOTE TENSION: the BubR1-H/H mouse has a REDUCED heart, Pun 2025 describes hypertrophy - measure, do not predict",
    identifier="PMID 22048312; PMID 18516091; PMID 24825348; PMID 40607964",
    evidence_tier="E3", stage_2026="Standard clinical tests", cns_penetration="n/a",
    key_risk="None - non-invasive",
    verdict="RECOMMEND NOW", notes="Absent from current MVA surveillance guidance, which is renal-only (SIOP-Europe HGWG / SIOP-RTSG: 3-monthly renal ultrasound until the 7th birthday)")

add(id="D02", axis="D-clinical", agent="Contraindication card",
    **{"class":"Clinical governance"},
    mechanism="Written record of agents to avoid or dose-reduce, held with the child's notes",
    genotype_fit="DIRECTLY SUPPORTED",
    best_evidence="Severe adverse reaction to dactinomycin preventing further chemotherapy in a 38-month-old with biallelic BUB1B and bilateral Wilms tumour; deliberate reduced-intensity VAC in an infant with PCS/MVA and vaginal embryonal rhabdomyosarcoma; fatal outcome after graft rejection following RIC HSCT in an 11-year-old with MVA1",
    identifier="PMID 31081598; PMID 31184400; PMID 31053147",
    evidence_tier="E1 (case-level, in MVA)", stage_2026="n/a", cns_penetration="n/a",
    key_risk="None - informational. Must not be used to withhold or override standard oncology care",
    verdict="RECOMMEND NOW", notes="Covers: dactinomycin/full-intensity chemo, HSCT conditioning and graft-failure risk, spindle poisons, CDK4/6 inhibitors, p53-attenuating agents, MPS1 and Aurora B inhibitors, SIRT2 inhibitors, fisetin, NAD+ precursors, chloroquine, growth hormone. The Aurora B row is mechanism-based (PMID 31264311), not from Cohen-Sharir; the Cohen-Sharir nuance (aneuploid cells LESS sensitive to short-term SAC inhibition) is stated in the card")

add(id="D03", axis="D-clinical", agent="Chemo/radiosensitivity panel on patient cells",
    **{"class":"Diagnostic"},
    mechanism="Clonogenic survival against vincristine, dactinomycin, doxorubicin and ionising radiation",
    genotype_fit="DIRECTLY SUPPORTED",
    best_evidence="NO published measurement of radiosensitivity or spindle-poison sensitivity in MVA patient cells exists, despite two independent chemotoxicity case reports",
    identifier="gap identified; see PMID 31081598, PMID 31184400",
    evidence_tier="n/a - proposed", stage_2026="n/a", cns_penetration="n/a",
    key_risk="None", verdict="RECOMMEND NOW - cheap, and the highest-value safety experiment for this population", notes="")

add(id="D04", axis="D-clinical", agent="Growth hormone",
    **{"class":"Endocrine"},
    mechanism="Listed for short stature in patient-facing MVA material",
    genotype_fit="HAZARDOUS",
    best_evidence="MVA1 is a high-penetrance embryonal-tumour predisposition syndrome; no MVA-specific GH safety data exists; growth restriction is partly developmental/mitotic (BubR1-null cortex shows shortened mitosis and apoptotic depletion of progenitors), so GH responsiveness is not assured",
    identifier="PMID 15475955; PMID 30668728",
    evidence_tier="E7", stage_2026="Licensed", cns_penetration="n/a",
    key_risk="Tumour predisposition", verdict="AVOID pending paediatric-endocrine and oncology review", notes="")

add(id="D05", axis="D-clinical", agent="Renal ultrasound surveillance",
    **{"class":"Monitoring"}, mechanism="Wilms tumour detection",
    genotype_fit="ESTABLISHED STANDARD",
    best_evidence="SIOP-Europe Host Genome Working Group / SIOP-RTSG Wilms tumour surveillance guideline: 3-monthly renal ultrasound for cytogenetically confirmed MVA until the 7th birthday",
    identifier="SIOP-E HGWG / SIOP-RTSG Wilms tumour surveillance guideline; mvasociety.org 2025",
    evidence_tier="expert consensus", stage_2026="Standard of care", cns_penetration="n/a",
    key_risk="None", verdict="CONTINUE", notes="Neither source addresses cardiac monitoring - see D01")

with open("/home/claude/track2_candidate_evidence_ledger.tsv", "w", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=COLS, delimiter="\t", quoting=csv.QUOTE_MINIMAL)
    w.writeheader()
    w.writerows(R)

from collections import Counter
print(f"rows: {len(R)}")
print("verdict spread:")
for k, v in Counter(r["verdict"].split(" -")[0].split(" (")[0] for r in R).most_common():
    print(f"  {v:>2}  {k}")
print("tier spread:", dict(Counter(r["evidence_tier"] for r in R)))
