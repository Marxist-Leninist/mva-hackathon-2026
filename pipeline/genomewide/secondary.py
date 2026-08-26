import json, sys, collections
sys.path.insert(0,'work')
events=json.load(open('work/events.json'))
gt=json.load(open('work/gt_map.json'))

NEPHRO = set("""CYP24A1 SLC34A1 SLC34A3 CLDN16 CLDN19 ATP6V1B1 ATP6V0A4 SLC4A1 AGXT GRHPR HOGA1
CASR SLC12A1 KCNJ1 CLCNKB BSND FAM20A VDR CA2 SLC9A3R1 CLCN5 OCRL SLC7A9 SLC3A1 AVPR2 AQP2
CYP27B1 GNA11 AP2S1 TRPM6 CNNM2 EGF FGF23 KL PHEX DMP1 ENPP1 SLC2A9 ABCG2 XDH APRT ADCY10
SLC26A1 SLC26A6 TRPV5 TRPV6 CLDN14 MAGED2 KCNJ16 NR3C2 SCNN1A SCNN1B SCNN1G HNF1B PAX2 UMOD REN
SLC12A3 CLDN10 SLC22A12 ATP6V1C2 WDR72 CTNS SLC7A7 SLC5A2""".split())

ACMG_SF = set("""ACTA2 ACTC1 ACVRL1 APC APOB ATP7B BAG3 BMPR1A BRCA1 BRCA2 BTD CACNA1S CALM1 CALM2 CALM3
CASQ2 COL3A1 DES DSC2 DSG2 DSP ENG FBN1 FLNC GAA GLA HFE HNF1A HHIP KCNH2 KCNQ1 LDLR LMNA MAX MEN1
MLH1 MSH2 MSH6 MUTYH MYBPC3 MYH7 MYH11 MYL2 MYL3 NF2 OTC PALB2 PCSK9 PKP2 PMS2 PRKAG2 PTEN RB1 RET
RPE65 RYR1 RYR2 SCN5A SDHAF2 SDHB SDHC SDHD SMAD3 SMAD4 STK11 TGFBR1 TGFBR2 TMEM127 TMEM43 TNNC1
TNNI3 TNNT2 TP53 TPM1 TRDN TSC1 TSC2 TTN TTR VHL WT1""".split())

CANCER_PRED = set("""TP53 DICER1 NF1 RB1 PTCH1 SUFU SMARCB1 SMARCA4 WT1 APC MSH2 MLH1 MSH6 PMS2 BRCA1 BRCA2
PALB2 ATM CHEK2 BLM NBN FANCA FANCC FANCD2 FANCG BRIP1 RAD51C RAD51D CDKN2A CDH1 STK11 PTEN VHL RET
MEN1 SDHB SDHC SDHD SDHA TSC1 TSC2 NF2 EXT1 EXT2 GPC3 REST CTR9 TRIM28 CDC73 DIS3L2 KDM3B BUB1B CEP57
TRIP13 MAD1L1 BUB1 CENPE ERCC6L2 SAMD9 SAMD9L RUNX1 GATA2 ETV6 ANKRD26 SBDS ELANE DKC1 TERT TERC RTEL1""".split())

groups=[("NEPHROCALCINOSIS / HYPERCALCIURIA / TUBULOPATHY PANEL",NEPHRO),
        ("ACMG SF v3.2 SECONDARY-FINDINGS GENES",ACMG_SF),
        ("CANCER PREDISPOSITION (incl. MVA/chromosome-instability)",CANCER_PRED)]

def d(c):
    if not c: return ''
    hp=(c.get('hgvsp') or '').split(':')[-1]
    hc=(c.get('hgvsc') or '').split(':')[-1]
    return (f"{c['chrom']}:{c['pos']} {c['ref']}>{c['alt']} {c['gt']} "
            f"DP{c['dp']} GQ{c['gq']} af={c['af']:.3g} {c['impact'][:4]} "
            f"{c['conseq'][:26]} {hc} {hp} CLN={c.get('clnsig','')[:34]}")

for title,panel in groups:
    print("="*118); print(title); print("="*118)
    hits=[e for e in events if e['gene'] in panel]
    if not hits: print("  (no qualifying events)"); continue
    for e in sorted(hits,key=lambda x:-x['score'])[:12]:
        print(f"  {e['gene']:<10} {e['model']:<14} score={e['score']:.2f} hpo={e['hpo']:.1f}")
        print(f"     v1: {d(e['v1'])}")
        if e['v2']: print(f"     v2: {d(e['v2'])}")
    print()

# Also: ANY ClinVar P/LP in the whole candidate set regardless of model
print("="*118); print("ALL ClinVar Pathogenic / Likely_pathogenic exact matches in coding candidate set"); print("="*118)
seen=set()
for e in events:
    for c in (e['v1'], e['v2']):
        if not c: continue
        sg=c.get('clnsig') or ''
        if ('Pathogenic' in sg or 'Likely_pathogenic' in sg) and 'Conflicting' not in sg:
            k=c['key']
            if k in seen: continue
            seen.add(k)
            print(f"  {c['gene']:<10} {d(c)}")
            print(f"     CLNDN: {(c.get('clndn') or '')[:150]}")
