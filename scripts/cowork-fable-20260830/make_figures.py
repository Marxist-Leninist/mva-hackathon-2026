#!/usr/bin/env python3
"""Figures 2 and 3 for the MVA Track 2 extension appendix."""
import json
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

R = json.load(open("/home/claude/sim/dosage_results.json"))
S = R["strategies"]

SURFACE   = "#fcfcfb"
INK       = "#0b0b0b"
INK2      = "#52514e"
INK3      = "#8a8880"
GRID      = "#e4e3dd"
# categorical slots 1-3 (validated all-pairs, light mode)
FAM = {"readthrough": "#2a78d6", "acetrna": "#eb6834", "skipping": "#1baf7a"}

ORDER = [
    ("RT-SM",   "Small-molecule readthrough",              "readthrough"),
    ("RT-SM+",  "…+ gene-specific NMD ASO",                "readthrough"),
    ("ACE",     "ACE-tRNA-Leu",                            "acetrna"),
    ("ACE+",    "…+ gene-specific NMD ASO",                "acetrna"),
    ("ASO-ES",  "Exon-17 skip, allele-selective",          "skipping"),
    ("ASO-ESn", "Exon-17 skip, non-selective",             "skipping"),
]
PANELS = [
    ("p_r_gt_0_10",     "Recovers >0.10 units of BubR1"),
    ("p_rel_gain_20pc", "Raises this child's BubR1 by >20%"),
    ("p_carrier_equiv", "Reaches carrier-equivalent level"),
]

def rbar(ax, y, w, color, h=0.62, r=0.018):
    """Bar with rounded data-end, anchored at x=0."""
    if w <= 0:
        return
    r = min(r, w / 2)
    ax.add_patch(FancyBboxPatch(
        (0, y - h / 2), max(w - r, 1e-9), h,
        boxstyle=f"round,pad=0,rounding_size={r}",
        mutation_aspect=1, linewidth=0, facecolor=color, clip_on=False, zorder=3))

# ---------------------------------------------------------------- Figure 2
fig, axes = plt.subplots(1, 3, figsize=(12.4, 3.5), sharey=True)
fig.patch.set_facecolor(SURFACE)

for ax, (key, title) in zip(axes, PANELS):
    ax.set_facecolor(SURFACE)
    for i, (sid, label, fam) in enumerate(ORDER):
        y = len(ORDER) - 1 - i
        v = S[sid][key]
        rbar(ax, y, v, FAM[fam])
        txt = "<0.1%" if v < 0.001 else f"{v*100:.0f}%"
        ax.text(v + 0.022, y, txt, va="center", ha="left",
                fontsize=8.5, color=INK2, zorder=4)
    ax.set_xlim(0, 1.0); ax.set_ylim(-0.65, len(ORDER) - 0.35)
    ax.set_xticks([0, 0.25, 0.5, 0.75, 1.0])
    ax.set_xticklabels(["0", "25%", "50%", "75%", "100%"], fontsize=8, color=INK3)
    ax.set_title(title, fontsize=9.5, color=INK, loc="left", pad=9)
    ax.xaxis.grid(True, color=GRID, linewidth=0.8, zorder=0)
    ax.set_axisbelow(True)
    for s in ("top", "right", "left"): ax.spines[s].set_visible(False)
    ax.spines["bottom"].set_color(GRID); ax.spines["bottom"].set_linewidth(0.8)
    ax.tick_params(axis="both", length=0)

axes[0].set_yticks(range(len(ORDER)))
axes[0].set_yticklabels([lbl for _, lbl, _ in reversed(ORDER)], fontsize=8.5, color=INK)

handles = [plt.Line2D([], [], marker="s", linestyle="", markersize=7.5,
                      markerfacecolor=c, markeredgecolor="none", label=n)
           for n, c in [("Small-molecule readthrough", FAM["readthrough"]),
                        ("ACE-tRNA (UGA→Leu)",         FAM["acetrna"]),
                        ("Exon-17 skipping ASO",       FAM["skipping"])]]
fig.legend(handles=handles, loc="lower left", bbox_to_anchor=(0.008, -0.035),
           ncol=3, frameon=False, fontsize=8.5, handletextpad=0.5,
           columnspacing=1.8, labelcolor=INK2)
fig.suptitle("Probability each strategy restores enough BubR1 — 400,000-draw Monte Carlo",
             fontsize=11, color=INK, x=0.008, ha="left", y=1.10, fontweight="bold")
fig.text(0.008, 1.00,
         "Priors stated in the model script. One wild-type allele = 1.0 unit; this child's baseline is a median 0.33 units "
         "(16% of wild-type diploid).",
         fontsize=8, color=INK3, ha="left")
fig.tight_layout(rect=[0, 0.045, 1, 0.94])
fig.savefig("/home/claude/sim/figure2_strategies.png", dpi=220,
            facecolor=SURFACE, bbox_inches="tight")
print("wrote figure2_strategies.png")

# ---------------------------------------------------------------- Figure 3
sens = R["sensitivity"]
names = {"RT-SM+": ("Small-molecule readthrough + NMD ASO", "readthrough"),
         "ACE+":   ("ACE-tRNA-Leu + NMD ASO", "acetrna"),
         "ASO-ES": ("Exon-17 skipping ASO", "skipping")}
PRETTY = {"E_sm": "readthrough efficiency at UGAA", "E_ace": "ACE-tRNA suppression efficiency",
          "T_ptc+ASO": "transcript rescued from NMD", "S_trp": "function of p.Leu737Trp product",
          "S_del": "function of BubR1-Δ715–761", "P_skip": "exon-skipping efficiency",
          "T_ptc": "PTC transcript level", "f": "residual function of p.Asn1002Lys"}

fig, axes = plt.subplots(1, 3, figsize=(12.4, 2.35))
fig.patch.set_facecolor(SURFACE)
for ax, k in zip(axes, ["RT-SM+", "ACE+", "ASO-ES"]):
    ax.set_facecolor(SURFACE)
    rows = sens[k][:3]
    for i, (pn, rho) in enumerate(rows):
        y = len(rows) - 1 - i
        rbar(ax, y, abs(rho), FAM[names[k][1]], h=0.5)
        ax.text(abs(rho) + 0.022, y, f"{abs(rho):.2f}", va="center", ha="left",
                fontsize=8.5, color=INK2)
        ax.text(-0.03, y, PRETTY.get(pn, pn), va="center", ha="right",
                fontsize=8.2, color=INK)
    ax.set_xlim(0, 1.0); ax.set_ylim(-0.6, len(rows) - 0.4)
    ax.set_xticks([0, 0.5, 1.0]); ax.set_xticklabels(["0", "0.5", "1.0"], fontsize=8, color=INK3)
    ax.set_yticks([])
    ax.set_title(names[k][0], fontsize=9.5, color=INK, loc="left", pad=8)
    ax.xaxis.grid(True, color=GRID, linewidth=0.8); ax.set_axisbelow(True)
    for s in ("top", "right", "left"): ax.spines[s].set_visible(False)
    ax.spines["bottom"].set_color(GRID); ax.spines["bottom"].set_linewidth(0.8)
    ax.tick_params(axis="both", length=0)
fig.suptitle("Which unknown decides the outcome — rank correlation with recovered BubR1",
             fontsize=11, color=INK, x=0.008, ha="left", y=1.14, fontweight="bold")
fig.text(0.008, 1.02,
         "The tallest bar in each panel names the experiment worth running first.",
         fontsize=8, color=INK3, ha="left")
fig.tight_layout(rect=[0, 0, 1, 0.94])
fig.savefig("/home/claude/sim/figure3_sensitivity.png", dpi=220,
            facecolor=SURFACE, bbox_inches="tight")
print("wrote figure3_sensitivity.png")
