# Track 1 report: biallelic BUB1B in Mosaic Variegated Aneuploidy

**Participant:** MarxistLeninist  
**Reference:** GRCh38  
**Proband:** PROBAND01  
**Submission file:** `results/MarxistLeninist_bub1b_compound_het.csv`

## Result

The top causal model is **BUB1B-associated MVA1** with two heterozygous variants:

1. `chr15:40209701 T>G`; `NM_001211.6:c.2210T>G`; `p.Leu737Ter`
2. `chr15:40220612 T>G`; `NM_001211.6:c.3006T>G`; `p.Asn1002Lys`

The predicted architecture is a loss-of-function allele plus a full-length
missense/hypomorphic allele. This fits the established autosomal-recessive
BUB1B-MVA1 mechanism. The pair is submitted as one primary row.

This conclusion is strong, but one part remains unresolved: the two sites are
10,911 bp apart and are not read-phased. There is no parental dataset. Therefore,
**compound heterozygosity (in trans) is inferred rather than demonstrated**.

## Analysis strategy

The gated data were handled only in an authorized private environment. The
public repository contains derived allowlisted facts, code, and reports; it does
not contain the genome, clinical source document, read evidence, or sample-wide
annotations.

The primary discovery lane was gene-agnostic:

1. Retain the 4,740,790 `PASS` records from the supplied singleton WGS VCF.
2. Normalize representation conceptually to GRCh38 coordinates and require an
   exact chromosome-position-reference-alternate match.
3. Intersect against 346,282 ClinVar Pathogenic/Likely pathogenic records. This
   produced seven exact matches genome-wide; one was the BUB1B stop-gain already
   associated with MVA1.
4. Annotate coding consequences, population frequency, disease mechanism, and
   computational predictions.
5. Search the complete BUB1B locus for a second allele rather than stopping at
   the ClinVar hit.
6. Rank complete recessive pairs against phenotype and gene-disease validity.
7. Cross-check the resulting pair against the public live scorer only after the
   private derivation.

The locus contained 14 non-reference calls at any filter level. Twelve were
intronic modifier calls, mostly common. The only two coding-impact calls were
the two submitted variants. Distributed heterozygous sites across the locus did
not suggest a large intragenic loss-of-heterozygosity block. A separate simple
VCF depth/heterozygous-allele-balance screen did not yield convincing evidence
of mosaic whole-chromosome imbalance in this bulk sample; chromosome-level
shifts tracked known coverage/GC behavior. This negative result does not argue
against MVA, which is tissue- and cell-mosaic and is not reliably diagnosed from
bulk short-read WGS depth.

## Variant-level evidence

### Allele 1: p.Leu737Ter

- `FILTER=PASS`, `QUAL=708.77`
- genotype `0/1`, allele depths `21,25`, total depth `46`, genotype quality `99`
- alternate-allele balance `0.54`
- ClinVar Allele ID 529272, Pathogenic/Likely pathogenic, multiple submitters,
  no conflicts
- reported gnomAD frequency approximately `7.87e-05` in exomes and `3.29e-05`
  in genomes
- stop gained in exon 17 of 23

The premature stop is well upstream of the final exon junction and is expected
to trigger nonsense-mediated decay. Transcript-level NMD was not measured, so
the report uses “NMD-competent/expected,” not “experimentally proven absent.”

The exact coding change is reproducible: wild-type codon `TTA` (Leu), with the
second base changed from `T` to `G`, becomes `TGA` (UGA stop). The following
base is `A`, giving `TGA-A` in DNA or `UGA-A` in RNA.

### Allele 2: p.Asn1002Lys

- `FILTER=PASS`, `QUAL=344.77`
- genotype `0/1`, allele depths `15,13`, total depth `28`, genotype quality `99`
- alternate-allele balance `0.46`
- absent from the queried gnomAD exome and genome datasets
- predicted deleterious by SIFT and probably damaging by PolyPhen
- located in exon 23, the final exon, within the C-terminal kinase/pseudokinase
  region

The exact `T>G` allele is not classified in ClinVar. Other substitutions at the
same genomic position do not determine the classification of this one. It must
therefore remain a **VUS in isolation**. Rarity, in-silico predictions, domain
location, the second BUB1B loss-of-function allele, and the highly specific MVA
phenotype provide strong case-level support, but segregation or functional data
are needed for formal reclassification.

An AlphaFold DB v6 model places residue 1002 in a high-confidence local region
(mean per-atom pLDDT 91.06). Predicted Asn side-chain contacts to backbone atoms
near residues 978 and 998 suggest a plausible local structural role. This is
hypothesis-generating only: a predicted model cannot establish destabilization,
pathogenicity, or druggability.

## Gene and inheritance fit

ClinGen classifies the relationship between biallelic BUB1B variants and MVA1 as
Definitive. The founding study identified constitutional aneuploidy and cancer
predisposition with biallelic BUB1B variants. Functional work in MVA patient
cells showed low BUBR1 abundance, impaired spindle-checkpoint activity, and
chromosome-alignment defects; restoring BUBR1 restored checkpoint activity.

Viable reported patients often retain residual BUBR1 function through a
hypomorphic/hypomorphic or truncating-plus-missense combination. It would be
too strong to claim that human biallelic null is proven embryonic lethal; the
defensible observation is that complete loss is lethal in mouse models and
viable human cases generally preserve residual function.

The main gene-level alternatives were considered:

- **TRIP13:** particularly important in a Wilms-tumor-heavy presentation.
- **CEP57:** important with relative head sparing, rhizomelia, hypothyroidism,
  and the original series' limited cancer history; manual indel review matters.
- **CENATAC:** limited human evidence and a generally milder reported phenotype.
- **MAD1L1, SLF2, SMC5, and other chromosome-segregation genes:** retained in
  the broader MVA lane.

No alternative explains the gene-agnostic pathogenic ClinVar hit plus the second
rare coding BUB1B allele as directly as the submitted pair.

## Confirmation required

Before clinical use or publication as a solved genotype:

1. Inspect both sites in the alignment for mapping, strand, read-position, and
   local sequence artifacts; independently re-call if raw data are available.
2. Orthogonally confirm each allele.
3. Establish trans through parental testing or targeted long-molecule phasing.
   Ordinary short reads cannot bridge 10.9 kb; validating each site by Sanger
   sequencing alone does not phase them.
4. Measure allele-specific BUB1B RNA and BUBR1 protein abundance in patient cells.
5. Test p.Asn1002Lys in an isogenic system for half-life, kinetochore recruitment,
   spindle-checkpoint arrest, chromosome alignment, and missegregation.
6. Apply ACMG/AMP and ClinGen PVS1/PM3 guidance conservatively after segregation
   and functional evidence are available.

## Incidental findings and privacy

Additional candidate records from an automated ClinVar screen are intentionally
not published. Automated annotation is not clinical confirmation, and an open
competition is not an appropriate return-of-results pathway. A qualified clinical
genetics team may review such records under the governing protocol.

## Limitations

- Singleton WGS cannot prove inheritance phase.
- The missense allele has no exact ClinVar classification and no direct functional
  assay in this child.
- Bulk WGS is not a sensitive substitute for cytogenetic assessment of mosaic
  aneuploidy across relevant tissues.
- In-silico predictors and AlphaFold contacts are supporting hypotheses, not
  independent proof.
- The public report cannot expose restricted read-level material, sample-wide
  findings, or phenotype source files.

## References

1. Hanks S, et al. *Nat Genet.* 2004. https://pubmed.ncbi.nlm.nih.gov/15475955/
2. Suijkerbuijk SJE, et al. *Cancer Res.* 2010. https://pmc.ncbi.nlm.nih.gov/articles/PMC2887387/
3. ClinGen BUB1B-MVA1 gene validity. https://search.clinicalgenome.org/kb/gene-validity/CGGV:assertion_59147f27-d5a3-4760-ba8d-0429bae3c906-2019-11-22T14:53:26.352Z
4. ClinGen variant-interpretation guidance. https://www.clinicalgenome.org/tools/clingen-variant-classification-guidance/
5. AlphaFold DB, BUB1B/O60566. https://alphafold.ebi.ac.uk/entry/O60566

