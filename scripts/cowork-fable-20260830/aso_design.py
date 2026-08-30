region = ("CCATTTTAAGCATTAGGGTTTTTTTGGTGATATATTTTCACCTTTCCCTCCCACTGGCAG"
          "AAAACCCTACTCAGTCACCATGGTGTTCACAGTATCGCAGACAGCTACTGAAGTCCCTACCAGAGTTAAGTGCCTCTGCAGAGTTGTGTATAGAAGACAGACCAATGCCTAAGTTGGAAATTGAGAAGGAAATTGAATTAG"
          "GTAAGTACCATTGAACTCATGTCCTCTGGTTCATGACAGTATACAAATAAGTGATTATTT")
GSTART = 40209575                      # genomic coord of region[0]
EX_S, EX_E = 40209635, 40209775        # exon 17
i_s, i_e = EX_S-GSTART, EX_E-GSTART    # 60, 200 inclusive
exon = region[i_s:i_e+1]
print(f"region {len(region)} nt | exon 17 = {len(exon)} nt (expect 141): {len(exon)==141}")
print(f"3' splice acceptor ...{region[i_s-8:i_s]}|{exon[:10]}...   (acceptor must end AG: {region[i_s-2:i_s]})")
print(f"5' splice donor     ...{exon[-10:]}|{region[i_e+1:i_e+9]}...  (donor must start GT: {region[i_e+1:i_e+3]})")
print(f"exon starts 'AA' -> codon715 = G+{exon[:2]} = G{exon[:2]} = Glu : {('G'+exon[:2])=='GAA'}")
print(f"exon ends '{exon[-1]}'  -> codon762 = {exon[-1]}+GT = {exon[-1]}GT = Gly : {(exon[-1]+'GT')=='GGT'}")

# mutation position
c2210_off = 66                          # 0-based offset into exon 17
mut_idx = i_s + c2210_off
print(f"\nc.2210 at region index {mut_idx} = genomic {GSTART+mut_idx} (expect 40209701): {GSTART+mut_idx==40209701}")
print(f"  WT base here = '{region[mut_idx]}' (expect T): {region[mut_idx]=='T'}")
print(f"  WT codon 737 = {region[mut_idx-1:mut_idx+2]}  -> mutant {region[mut_idx-1]}G{region[mut_idx+1]}")

comp = str.maketrans("ACGT","TGCA")
def rc(s): return s.translate(comp)[::-1]
def gc(s): return 100*sum(c in "GC" for c in s)/len(s)
def tm(s):  # nearest-neighbour-free approximation for 2'-MOE gapmer-length oligos
    return 64.9 + 41*(sum(c in "GC" for c in s)-16.4)/len(s)

def design(name, start, length, note, mutant=False):
    target = region[start:start+length]
    if mutant:
        target = target[:mut_idx-start] + "G" + target[mut_idx-start+1:]
    aso = rc(target)
    print(f"\n{name}")
    print(f"  genomic target   chr15:{GSTART+start}-{GSTART+start+length-1} (+)")
    print(f"  pre-mRNA target  5'-{target}-3'")
    print(f"  ASO (RNA, 5'->3') {aso.replace('T','U')}")
    print(f"  ASO (DNA-style)   5'-{aso}-3'   len {length}  GC {gc(aso):.0f}%  Tm~{tm(aso):.0f}C")
    print(f"  rationale: {note}")

print("\n" + "="*76)
print("CANDIDATE EXON-17 SKIPPING OLIGONUCLEOTIDES (BUB1B, GRCh38)")
print("="*76)
design("ASO-1  acceptor-site blocker", i_s-18, 25,
       "spans the intron16/exon17 3' splice acceptor (-18 to +7); blocks U2AF/SF1 recognition. Not allele-selective.")
design("ASO-2  donor-site blocker", i_e-16, 25,
       "spans the exon17/intron17 5' splice donor (-16 to +9); blocks U1 snRNP base-pairing. Not allele-selective.")
design("ASO-3  ESE blocker, mutation-centred (WT-matched)", mut_idx-12, 25,
       "centred on c.2210; targets the exonic splicing enhancer region. Perfect match to the WILD-TYPE allele.")
design("ASO-4  ESE blocker, mutation-centred (MUTANT-matched)  <-- ALLELE-SELECTIVE CANDIDATE", mut_idx-12, 25,
       "identical position to ASO-3 but complementary to the c.2210G MUTANT allele. Central mismatch to the "
       "wild-type allele destabilises the WT duplex, giving allele-selective skipping of the nonsense allele only.",
       mutant=True)

# show the single-base discrimination
t_wt  = region[mut_idx-12:mut_idx+13]
t_mut = t_wt[:12]+"G"+t_wt[13:]
print(f"\nAllele discrimination for ASO-4:")
print(f"  WT     target 5'-{t_wt}-3'")
print(f"  MUTANT target 5'-{t_mut}-3'")
print(f"  ASO-4 is a perfect 25-mer duplex with the mutant and carries ONE CENTRAL MISMATCH (position 13/25)")
print(f"  against wild type - the position of maximum thermodynamic penalty for splice-switching ASOs.")

print("\nProtein consequence of successful skipping:")
print("  BubR1 residues 1-714 :: Gly (= wild-type Gly762) :: residues 763-1050")
print("  = clean in-frame deletion of residues 715-761 (47 aa), product 1003 aa,")
print("    premature stop removed, transcript no longer an NMD substrate.")
