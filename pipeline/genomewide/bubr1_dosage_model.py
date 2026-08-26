"""
BUBR1 dosage model for proband WGS_EX2312012 (BUB1B p.Leu737Ter / p.Asn1002Lys).

Anchored on measured quantities from Suijkerbuijk et al. 2010 (PMID 20516114):
  * BUBR1 shRNA titration: ~6% residual BUBR1 -> missegregation in the MAJORITY of
    cells; ~13% residual -> virtually NO effect on segregation fidelity.
    The dose-response is switch-like, not linear.
  * Pseudokinase-domain missense alleles (R727C, L844F, I909T, L1012P; and by
    structural class p.Asn1002Lys) show 5-10x lower steady-state protein and
    ~2x faster turnover, with UNAFFECTED mRNA -> a pure abundance defect.
  * PTC alleles (386X, 731X) give transcript undetectable in patient cells (NMD)
    -> functional null.  p.Leu737Ter is exon 17/23, upstream of the last EEJ.

Question the model answers: how large a fold-increase in the hypomorphic allele's
steady-state protein is needed to move this child from the failure regime into the
tolerant regime?  This sets the bar any candidate drug must clear.
"""
import numpy as np, json

WT_PER_ALLELE = 0.5           # each wild-type allele contributes 50% of normal BUBR1
NULL = 0.0                    # p.Leu737Ter: NMD, no protein
HYPO_FOLD_LOW, HYPO_FOLD_HIGH = 1/10, 1/5   # 5-10x reduction, measured

THRESH_FAIL, THRESH_SAFE = 0.06, 0.13       # measured switch-like thresholds

def residual(fold_rescue, hypo_fraction):
    """Total BUBR1 as a fraction of normal, given a drug that multiplies the
    hypomorphic allele's steady-state level by fold_rescue."""
    return NULL + WT_PER_ALLELE * hypo_fraction * fold_rescue

def needed_fold(target, hypo_fraction):
    return target / (WT_PER_ALLELE * hypo_fraction)

if __name__ == '__main__':
    res = {}
    for name, hf in (("worst case (10x reduction)", HYPO_FOLD_LOW),
                     ("best case (5x reduction)",  HYPO_FOLD_HIGH)):
        base = residual(1.0, hf)
        res[name] = dict(
            baseline_residual_pct = round(base*100, 2),
            regime = "FAILURE (<6%)" if base < THRESH_FAIL else ("MARGINAL" if base < THRESH_SAFE else "TOLERANT"),
            fold_to_reach_6pct  = round(needed_fold(THRESH_FAIL, hf), 2),
            fold_to_reach_13pct = round(needed_fold(THRESH_SAFE, hf), 2),
        )
    print(json.dumps(res, indent=2))

    print("\nTherapeutic window summary")
    lo = needed_fold(THRESH_SAFE, HYPO_FOLD_LOW)
    hi = needed_fold(THRESH_SAFE, HYPO_FOLD_HIGH)
    print(f"  Baseline residual BUBR1 in this proband: {residual(1,HYPO_FOLD_LOW)*100:.1f}% - {residual(1,HYPO_FOLD_HIGH)*100:.1f}% of normal")
    print(f"  Fold-increase in the p.Asn1002Lys allele's protein needed to reach the")
    print(f"  ~13% 'virtually no segregation defect' regime: {hi:.1f}x - {lo:.1f}x")
    print("\n  This is the key number. It is a MODEST target: a 1.3-2.6x increase in the")
    print("  steady-state level of one destabilised protein, not restoration to wild type.")
    print("  Gene therapy is not required to cross this threshold.")

    # figure
    try:
        import matplotlib; matplotlib.use('Agg')
        import matplotlib.pyplot as plt
        folds = np.linspace(1, 4, 400)
        fig, ax = plt.subplots(figsize=(8.6, 5.0))
        ax.axhspan(0, THRESH_FAIL*100, color='#b3261e', alpha=.14)
        ax.axhspan(THRESH_FAIL*100, THRESH_SAFE*100, color='#e08a00', alpha=.14)
        ax.axhspan(THRESH_SAFE*100, 40, color='#1e7d4f', alpha=.13)
        ax.plot(folds, [residual(f, HYPO_FOLD_HIGH)*100 for f in folds], lw=2.6,
                color='#1a4fa0', label='hypomorph at 1/5 of WT allele (best case)')
        ax.plot(folds, [residual(f, HYPO_FOLD_LOW)*100 for f in folds], lw=2.6,
                color='#1a4fa0', ls='--', label='hypomorph at 1/10 of WT allele (worst case)')
        ax.axhline(THRESH_FAIL*100, color='#b3261e', lw=1.1)
        ax.axhline(THRESH_SAFE*100, color='#1e7d4f', lw=1.1)
        ax.text(3.98, THRESH_SAFE*100+0.6, '13% — segregation essentially normal',
                ha='right', fontsize=9, color='#1e7d4f')
        ax.text(3.98, THRESH_FAIL*100-1.4, '6% — missegregation in most cells',
                ha='right', fontsize=9, color='#b3261e')
        ax.axvspan(hi, lo, color='#1a4fa0', alpha=.10)
        ax.text((hi+lo)/2, 33, f'target\n{hi:.1f}–{lo:.1f}×', ha='center', fontsize=10,
                color='#1a4fa0', fontweight='bold')
        ax.set_xlabel('Fold-increase in steady-state p.Asn1002Lys BUBR1 protein (drug effect)')
        ax.set_ylabel('Total residual BUBR1 (% of normal)')
        ax.set_title('BUBR1 dosage window — proband WGS_EX2312012 (p.Leu737Ter / p.Asn1002Lys)',
                     fontsize=11.5)
        ax.set_xlim(1, 4); ax.set_ylim(0, 40)
        ax.legend(loc='upper left', fontsize=9, frameon=False)
        ax.spines[['top','right']].set_visible(False)
        fig.tight_layout()
        fig.savefig('docs/bubr1_dosage_window.png', dpi=170)
        print("\n  figure -> docs/bubr1_dosage_window.png")
    except Exception as e:
        print("figure skipped:", e)
