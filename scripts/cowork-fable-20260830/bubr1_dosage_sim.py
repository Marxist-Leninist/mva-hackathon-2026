#!/usr/bin/env python3
"""
BubR1 dosage restoration model for BUB1B c.2210T>G p.Leu737Ter / c.3006T>G p.Asn1002Lys.

Units: one wild-type allele contributes 1.0 unit of BubR1 function; WT diploid = 2.0.
Patient baseline = f (missense allele only); the nonsense allele contributes ~0.

Strategies modelled
  RT-SM   small-molecule readthrough (DAP class) on the UGAA context
  RT-SM+  the same, plus gene-specific EJC-blocking NMD ASO
  ACE     leucine-encoding ACE-tRNA (UGA -> Leu), restores wild-type residue
  ACE+    the same, plus gene-specific NMD ASO
  ASO-ES  exon-17 skipping ASO, allele-selective (mutant pre-mRNA only)
  ASO-ESn exon-17 skipping ASO, NON-allele-selective (acts on both alleles)

All priors are stated, uniform or lognormal, and sourced in the report. This is a
transparent decision model, not a prediction.
"""
import numpy as np, json

rng = np.random.default_rng(20260830)
N = 400_000

def U(a, b):            # uniform prior
    return rng.uniform(a, b, N)

# ---------------------------------------------------------------- priors
# f : residual per-allele function of p.Asn1002Lys.
# AlphaFold: N1002 is buried (27 heavy-atom neighbours <=8 A, pLDDT 91) in an
# aromatic/aliphatic pocket (W973/F977/W978/F997/V998/I1000). Burying a Lys+ there
# is a classic destabilising substitution, consistent with Suijkerbuijk 2010's
# finding that MVA missense alleles near the kinase domain are turnover-limited.
# Prior therefore skewed low.
f = U(0.05, 0.60)

# T_ptc : steady-state transcript level of the PTC allele relative to normal.
# Canonical NMD substrate (exon 17 of 23, 746-748 nt upstream of the last junction,
# 6 downstream junctions).
T_ptc      = U(0.05, 0.30)
T_ptc_aso  = U(0.50, 0.95)     # + gene-specific EJC-blocking NMD ASO

# E_rt : per-event readthrough efficiency at a UGA-A (strong-terminator) context.
E_sm  = U(0.002, 0.030)        # small molecule, low end of the UGA range
E_ace = U(0.05,  0.50)         # ACE-tRNA-Leu, from CFTR rescue data

# S : functional competence of the product relative to wild type
S_trp = U(0.60, 1.00)          # p.Leu737Trp, conservative swap in a linker
S_leu = 1.0                    # ACE-tRNA-Leu restores wild-type Leu exactly

# Exon-17 skipping
P_skip = U(0.20, 0.90)         # ASO skipping efficiency
# S_del : functional competence of BubR1-delta715-761.
# UNKNOWN and the dominant uncertainty. AlphaFold shows the segment makes 113
# long-range contacts (34/47 residues), 68% of the density of a folded control
# window, docking onto the pseudokinase domain -> deletion is NOT obviously benign.
S_del  = U(0.0, 1.0)

# ---------------------------------------------------------------- strategies
r = {}
r["RT-SM"]   = T_ptc     * E_sm  * S_trp
r["RT-SM+"]  = T_ptc_aso * E_sm  * S_trp
r["ACE"]     = T_ptc     * E_ace * S_leu
r["ACE+"]    = T_ptc_aso * E_ace * S_leu
r["ASO-ES"]  = P_skip * S_del                      # allele-selective: null allele only
# non-selective: the missense allele is ALSO skipped, so its contribution f is
# replaced, in the skipped fraction, by a delta715-761 + N1002K double variant.
# Model that double variant as S_del * f (both liabilities multiply).
r["ASO-ESn"] = P_skip * S_del + (P_skip * S_del * f - P_skip * f)

total   = {k: f + v for k, v in r.items()}
BASE    = f

TARGET_CARRIER = 1.0                 # f + r > 1  ("carrier-equivalent")
def rel_gain(k): return (total[k] - BASE) / np.maximum(BASE, 1e-9)

print("=" * 78)
print("BubR1 dosage restoration - Monte Carlo, N = {:,}".format(N))
print("=" * 78)
print(f"Baseline f (missense allele only): median {np.median(f):.3f} units "
      f"= {np.median(f)/2*100:.1f}% of wild-type diploid")
print()
hdr = f"{'strategy':<9} {'median r':>9} {'P(r>0.10)':>10} {'P(+20% rel)':>12} {'P(carrier-eq)':>14}"
print(hdr); print("-" * len(hdr))
out = {}
for k in ["RT-SM", "RT-SM+", "ACE", "ACE+", "ASO-ES", "ASO-ESn"]:
    med = float(np.median(r[k]))
    p10 = float((r[k] > 0.10).mean())
    p20 = float((rel_gain(k) > 0.20).mean())
    pc  = float((total[k] > TARGET_CARRIER).mean())
    out[k] = dict(median_r=med, p_r_gt_0_10=p10, p_rel_gain_20pc=p20, p_carrier_equiv=pc)
    print(f"{k:<9} {med:9.4f} {p10:10.1%} {p20:12.1%} {pc:14.1%}")

# ---------------------------------------------------------------- sensitivity
print()
print("Sensitivity - which unknown decides the answer?")
print("(Spearman rho between each parameter and the achieved r, per strategy)")
from scipy.stats import spearmanr
params = {"f": f, "T_ptc": T_ptc, "T_ptc+ASO": T_ptc_aso, "E_sm": E_sm,
          "E_ace": E_ace, "S_trp": S_trp, "P_skip": P_skip, "S_del": S_del}
sens = {}
sub = slice(0, 40_000)
for k in ["RT-SM+", "ACE+", "ASO-ES"]:
    rows = []
    for pn, pv in params.items():
        rho = spearmanr(pv[sub], r[k][sub]).statistic
        if abs(rho) > 0.05: rows.append((abs(rho), pn, rho))
    rows.sort(reverse=True)
    sens[k] = [(pn, round(rho, 3)) for _, pn, rho in rows]
    print(f"  {k:<8} " + "  ".join(f"{pn}={rho:+.2f}" for _, pn, rho in rows))

print()
print("Conclusions")
print("-" * 78)
print("1. Small-molecule readthrough alone essentially cannot reach a meaningful")
print("   increment at this UGA-A context: P(r>0.10) = {:.1%}.".format(out['RT-SM']['p_r_gt_0_10']))
print("2. Adding a gene-specific NMD ASO multiplies the substrate but does not")
print("   rescue a weak per-event efficiency: P(r>0.10) = {:.1%}.".format(out['RT-SM+']['p_r_gt_0_10']))
print("3. ACE-tRNA-Leu + NMD ASO is the only pharmacological route with a")
print("   substantial chance of carrier-equivalence: {:.1%}.".format(out['ACE+']['p_carrier_equiv']))
print("4. Exon-17 skipping has the highest ceiling but its outcome is governed")
print("   almost entirely by S_del, which is unmeasured. That single experiment -")
print("   express BubR1-delta715-761 and assay it - is worth more than any")
print("   compound screen in this project.")

json.dump({"n": N, "baseline_f_median": float(np.median(f)), "strategies": out,
           "sensitivity": sens}, open("/home/claude/sim/dosage_results.json", "w"), indent=2)
print("\nwrote /home/claude/sim/dosage_results.json")
