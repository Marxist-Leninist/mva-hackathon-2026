# Rare Disease, Real Kid: The MVA Hackathon 2026

Submission repository for the **MVA Hackathon 2026** (Sage Bionetworks, MVA Society, Hugging Face, BEACON), covering:

- **Track 1 - Variant Prediction:** identification of the causal variant(s) underlying the proband's Mosaic Variegated Aneuploidy (MVA), from the challenge WGS VCF and clinical HPO phenotype.
- **Track 2 - Drug Repurposing:** mechanism-characterised, approved-drug repurposing hypotheses for follow-up investigation.

Challenge space: https://sagebio-rare-disease-real-kid-mva-hackathon-2026.hf.space/

## Result summary

**Primary finding (independently verified against the gated WGS VCF):** a compound heterozygous pair in **BUB1B** (MVA1, OMIM 602860), GRCh38:

| # | Variant | HGVS (NM_001211.6) | Protein | VCF evidence |
|---|---|---|---|---|
| 1 | chr15:40209701 T>G | c.2210T>G | p.Leu737Ter (UGA; NMD-competent null) | PASS, GT 0/1, AD 21,25, DP 46, GQ 99, MQ 60 |
| 2 | chr15:40220612 T>G | c.3006T>G | p.Asn1002Lys (C-terminal pseudokinase domain) | PASS, GT 0/1, AD 15,13, DP 28, GQ 99, MQ 60 |

Biallelic BUB1B loss is the established cause of MVA1; ClinGen classifies BUB1B-MVA1 as Definitive autosomal recessive. The architecture (null + missense/hypomorph) matches the viable-MVA model, since complete BUBR1 loss is not compatible with life in human reports and BubR1-null mice are embryonic lethal.

## Repository layout

- `submissions/` - Track 1 prediction CSVs and reports as submitted
- `track2/` - Track 2 repurposing report and pitch materials
- `methods/` - full methods write-up
- `code/` - reproducible analysis code (sanitised; no patient data)

## Data governance

This repository contains **no patient genomic data and no identifying clinical information**, in accordance with the challenge data-use terms (WCG IRB protocol 20252010). Only derived variant coordinates and method descriptions are published. Raw challenge data remain gated on Hugging Face under `SageBio/mva-hackathon-2026-data` and will be deleted from local compute environments after the hackathon, with deletion notified to MVAHackathon2026@synapse.org as required.

## License and acknowledgements

All submission materials in this repository are licensed **CC-BY-4.0**, as required by the hackathon rules.

We thank the child and family who shared their genome and clinical story with the research community, and the MVA Society, Sage Bionetworks, Hugging Face, BEACON, AWS and Anthropic for organising and sponsoring this challenge.
