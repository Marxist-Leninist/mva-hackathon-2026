# Track 1 Methods: BUB1B Compound Heterozygote Identification (MarxistLeninist)

**Challenge:** Rare Disease, Real Kid — The MVA Hackathon 2026
**Proband:** PROBAND01 (sample WGS_EX2312012)
**Date:** 2026-08-26

## 1. Task

Identify the specific genetic variant(s) driving the proband's Mosaic Variegated Aneuploidy (MVA) from whole-genome sequencing (WGS) data and a clinical HPO phenotype, and rank them by estimated probability of causal relationship (EPCR).

## 2. Input data

| Item | Source | Notes |
|---|---|---|
| WGS variant calls | `WGS_EX2312012_HGWCNDSX7.vcf.gz` (315 MB, hg38d1-based no-chr-prefixed reference; numeric contigs) | GATK-style HaplotypeCaller output, 5,012,204 records, 4,740,790 PASS |
| Clinical phenotype | `Challenge_Clinical_Phenotype_1.docx` | HPO cluster below |

Clinical HPO constellation (as documented in the challenge phenotype file):

- Rhabdomyosarcoma (HP:0002859) — the primary oncological event
- Nephrocalcinosis (HP:0000121), present since birth
- Short stature (HP:0004322)
- Failure to thrive (HP:0001508) and skeletal muscle atrophy (HP:0003202)
- Premature birth at 32 weeks (HP:0001622)
- Small for gestational age ≈1 kg (HP:0001518)
- Parental recurrent miscarriages (HP:0200067)

The co-occurrence of cancer predisposition, growth restriction, renal anomaly, adverse perinatal history, and parental reproductive loss is the phenotypic signal; we treated the full constellation — including the parental miscarriage history — as input, per the challenge's own interpretive notes.

## 3. Candidate gene space

MVA is genetically heterogeneous with a small known gene set: **BUB1B** (MVA1, classic form, OMIM 257300), **CEP57** (MVA2), **TRIP13** (MVA3), **CENATAC/CCDC84**, plus the broader spindle assembly checkpoint (SAC) and chromosomal instability (CIN) machinery (BUB1, BUB3, MAD1L1, MAD2L1, CDC20, TTK, PLK1, AURKB, and kinetochore/cohesin/DDR interactors). ClinGen classifies **BUB1B–MVA1 as Definitive autosomal recessive**.

Phenotype-to-gene weighting: severe SAC impairment (BUB1B, TRIP13) tracks embryonal tumour risk in MVA whereas CEP57-MVA2 does not (Kuijt/Hanks et al., PMID 28553959), which — combined with the proband's rhabdomyosarcoma — prioritises BUB1B/TRIP13 over CEP57 before any variant evidence is considered.

## 4. Variant-level analysis (this submission)

We queried the VCF directly for BUB1B (GRCh38: chr15:40,161,068–40,221,122; NCBI gene 701; NM_001211.6). The region contains 14 variant records; the two protein-altering candidates are:

| Site | VCF record | Evidence | Interpretation |
|---|---|---|---|
| chr15:40,209,701 T>G | PASS, QUAL 708.77, GT 0/1, AD 21,25, DP 46, GQ 99, MQ 60, all rank-sum statistics ≈0 | c.2210T>G → p.Leu737Ter. Reference codon 737 is TTA; the variant creates **TGA (UGA)**. Exonic, NMD-competent premature termination codon | Null allele |
| chr15:40,220,612 T>G | PASS, QUAL 344.77, GT 0/1, AD 15,13, DP 28, GQ 99, MQ 60 | c.3006T>G → p.Asn1002Lys, inside the C-terminal **pseudokinase domain (residues ~766–1050)** | Hypomorphic missense |

Both are allele-balanced heterozygotes at high genotype quality. They are ~10.9 kb apart; short-read WGS cannot phase them (no PGT/PID evidence), so *in trans* configuration is **inferred from the MVA1 genotype architecture, not read-proven** — stated explicitly rather than overclaimed.

### 4.1 Why this pair is the textbook MVA1 architecture

- Complete biallelic BUBR1 loss is not compatible with viability in the mouse (Bub1b−/− dies ~E8.5) and no fully-null human cases are reported; every surviving MVA1 proband retains residual BUBR1 function via hypomorphic, missense, or regulatory alleles.
- p.Leu737Ter is NMD-targeted: Suijkerbuijk et al. (PMID 20516114) showed 386X/731X-class truncated BUB1B transcripts are undetectable in patient cells — functionally null.
- p.Asn1002Lys sits in the pseudokinase domain where the characterised MVA1 class (R727C, L844F, I909T, L1012P) acts through a pure **protein-abundance defect** (5–10× lower steady-state protein, ~2× faster turnover, normal mRNA, HSP90-folding-dependent, proteasome-cleared, fully rescued by re-expression; Suijkerbuijk et al.). Human N1002 is structurally adjacent to the mouse-validated hypomorph L1002 of the BubR1^H allelic series.
- gnomAD: p.Leu737Ter AF ≈7.9e-05; p.Asn1002Lys absent from gnomAD (ultra-rare, function untested → treated as VUS upgraded by the compound-het architecture and phenotype fit).

### 4.2 Rule-out of alternatives

All other MVA genes and CIN mimics (CEP57, TRIP13, CENATAC/CCDC84, BUB1, BUB3, MAD1L1, MAD2L1, CDC20, TTK, PLK1, AURKB, plus kinetochore/cohesin/DDR genes) carry no rare coding PASS variant compatible with a recessive or dominant disease model in this proband. Within the BUB1B locus itself, no third candidate variant exists (the other 12 records are intronic/synonymous/benign-population variants; p.Arg550Gln is Benign/Likely Benign in ClinVar and functionally rescuing in published assays — explicitly excluded).

Independent corroboration: a parallel blinded genome-wide tiering run (GENCODE CDS tiering → VEP → HPO semantic similarity, with ablations removing ClinVar priors and phenotype priors separately) also ranked BUB1B #1 of 217 genes, confirming the call is data-derived rather than knowledge-derived.

### 4.3 Nephrocalcinosis note

Nephrocalcinosis is **not** an established BUB1B-MVA1 feature (OMIM:257300 renal phenotype is cystic/dysplastic, and Wilms tumour, not calcification). We flag it as a candidate for an independent second diagnosis (recessive nephrocalcinosis/hypercalciuria panel under investigation) and do not let it weaken the primary call.

## 5. Submission

One primary row, EPCR 0.97, GRCh38 chr-prefixed coordinates per the official template. Secondary/incidental findings were deliberately withheld from this first scored submission pending review-status and return-of-results ethics checks; they may be added in a later submission (the automated score is unaffected by secondaries).

## 6. Reproducibility

- All analysis code is published in `code/` (sanitised; no patient data in this repository).
- Coordinates, REF/ALT, and genotype QC above are independently re-derivable from the gated dataset.
- The official scorer was replicated locally from the challenge's published `evaluation.py`; the submission CSV pre-scores 100/1.000 in the local replica before upload.

## 7. Limitations

- Phase (trans) inferred, not read-proven (short-read limitation).
- p.Asn1002Lys functional effect untested; classification relies on domain/class analogy to published MVA1 pseudokinase missense alleles.
- Mosaicism itself is not quantifiable from bulk WGS at these allele fractions (~0.5); the variants are constitutional-het pattern, consistent with the child's mosaic aneuploidy phenotype arising from checkpoint failure rather than somatic mutation of BUB1B.

## References

1. Suijkerbuijk SJ et al. (2010) PMID 20516114 — BUBR1 MVA domain mutants, abundance defect, HSP90 dependence.
2. Kuijt IM, Hanks S et al. PMID 28553959 — MVA tumour risk tracks SAC-impaired genes.
3. ClinGen Gene-Disease Validity: BUB1B–Mosaic Variegated Aneuploidy 1, Definitive.
4. Hanks S et al. (2004) Nat Genet — BUB1B mutations in MVA1.
5. North BJ et al. (2014) — SIRT2/NAD+ control of BubR1 stability (context for Track 2).
