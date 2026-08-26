import asyncio, base64, os
from playwright.async_api import async_playwright

CSS = """
*{margin:0;padding:0;box-sizing:border-box}
:root{--ink:#12131a;--mut:#5b6070;--line:#dfe2ea;--blue:#1a4fa0;--red:#b3261e;--grn:#1e7d4f;--amb:#b06a00}
html,body{width:1920px;height:1080px;background:#fbfbfd;
 font-family:'Inter','Helvetica Neue',Helvetica,Arial,'DejaVu Sans',sans-serif;color:var(--ink);
 -webkit-font-smoothing:antialiased}
.s{width:1920px;height:1080px;padding:92px 118px 210px;display:flex;flex-direction:column;position:relative}
.kicker{font-size:26px;letter-spacing:.16em;text-transform:uppercase;color:var(--mut);font-weight:600;margin-bottom:26px}
h1{font-size:74px;line-height:1.1;font-weight:750;letter-spacing:-.02em}
h2{font-size:58px;line-height:1.15;font-weight:700;letter-spacing:-.015em}
.big{font-size:104px;font-weight:800;letter-spacing:-.03em;line-height:1.05}
.mono{font-family:'DejaVu Sans Mono',ui-monospace,Menlo,monospace}
.sub{font-size:32px;color:var(--mut);line-height:1.45}
.rule{height:5px;width:132px;background:var(--blue);border-radius:3px;margin:0 0 34px}
.foot{position:absolute;left:118px;bottom:172px;font-size:21px;color:#8b90a0}
/* slide 1 */
.vt{display:flex;flex-direction:column;gap:40px;margin-top:58px;justify-content:center;flex:1}
.v{border-left:9px solid var(--blue);padding:22px 0 22px 34px}
.v.alt{border-left-color:#7d9ad0}
.v .c{font-size:52px;font-weight:700;letter-spacing:-.01em}
.v .p{font-size:37px;color:#2c303c;margin-top:9px}
.v .n{font-size:27px;color:var(--mut);margin-top:11px}
.pill{display:inline-block;font-size:23px;font-weight:700;padding:7px 17px;border-radius:999px;
 background:#e7efff;color:var(--blue);margin-left:14px;vertical-align:middle;letter-spacing:.02em}
.pill.g{background:#e3f3ea;color:var(--grn)} .pill.r{background:#fdeaea;color:var(--red)}
/* slide 2 */
.flow{display:flex;align-items:center;gap:52px;margin-top:60px}
.box{flex:1;border:3px solid var(--line);border-radius:20px;padding:38px 40px;background:#fff}
.box .t{font-size:31px;color:var(--mut);font-weight:600}
.box .n{font-size:82px;font-weight:800;margin-top:12px;letter-spacing:-.03em}
.box .d{font-size:26px;color:var(--mut);margin-top:10px}
.arrow{font-size:66px;color:#b9bfcd}
.punch{margin-top:78px;font-size:60px;font-weight:750;line-height:1.2;letter-spacing:-.02em}
.punch em{font-style:normal;color:var(--blue)}
/* slide 4 */
.cols{display:flex;gap:56px;margin-top:52px}
.col{flex:1;border-radius:20px;padding:40px 42px;border:3px solid var(--line);background:#fff}
.col.bad{border-color:#f0c4c0;background:#fffafa}
.col h3{font-size:38px;font-weight:750;margin-bottom:8px}
.col .lead{font-size:26px;color:var(--mut);margin-bottom:26px}
.col ul{list-style:none;font-size:31px;line-height:1.85}
.col li:before{content:"•";color:#b9bfcd;margin-right:14px}
.verdict{margin-top:30px;font-size:34px;font-weight:750}
/* slide 5 */
.center{flex:1;display:flex;flex-direction:column;justify-content:center}
/* slide 6 */
.steps{display:flex;gap:44px;margin-top:56px}
.step{flex:1;border-top:6px solid var(--blue);padding-top:26px}
.step .k{font-size:24px;color:var(--mut);font-weight:700;letter-spacing:.1em;text-transform:uppercase}
.step .b{font-size:38px;font-weight:700;margin-top:12px;line-height:1.25}
.step .s2{font-size:25px;color:var(--mut);margin-top:12px;line-height:1.4}
.gate{margin-top:66px;border:3px solid var(--blue);border-radius:18px;background:#f2f6ff;
 padding:30px 38px;font-size:40px;font-weight:750;color:var(--blue)}
img.fig{width:100%;max-height:668px;object-fit:contain;margin-top:16px}
"""

SLIDES = {
1: """<div class="s">
 <div class="kicker">Track 1 · the answer</div>
 <h1>Mosaic Variegated Aneuploidy type 1<span class="pill">BUB1B · candidate biallelic</span></h1>
 <div class="vt">
  <div class="v"><div class="c mono">chr15:40,209,701 T&gt;G</div>
   <div class="p">c.2210T&gt;G &nbsp;<b>p.Leu737Ter</b> — premature stop <span class="pill r">null allele</span></div>
   <div class="n">ClinVar: Pathogenic / Likely pathogenic — “Mosaic variegated aneuploidy syndrome 1”</div></div>
  <div class="v alt"><div class="c mono">chr15:40,220,612 T&gt;G</div>
   <div class="p">c.3006T&gt;G &nbsp;<b>p.Asn1002Lys</b> — pseudokinase domain <span class="pill">predicted hypomorph</span></div>
   <div class="n">gnomAD v4 exomes: 1 in 1,461,878 (AF 6.8&times;10<sup>-7</sup>) · unreported in ClinVar</div></div>
 </div>
 <div class="foot">Ranked #1 genome-wide with no gene-panel prior · confirmed at read level from the raw FASTQs · research findings only, not medical advice</div>
</div>""",

2: """<div class="s">
 <div class="kicker">Mechanism</div><div class="rule"></div>
 <h2>Two alleles, one surviving supply of BUBR1</h2>
 <div class="flow">
  <div class="box"><div class="t">p.Leu737Ter</div><div class="n" style="color:var(--red)">0%</div>
   <div class="d">nonsense-mediated decay · no protein</div></div>
  <div class="arrow">+</div>
  <div class="box"><div class="t">p.Asn1002Lys</div><div class="n" style="color:var(--amb)">5–10%</div>
   <div class="d">same mRNA · 5–10× less protein · 2× turnover</div></div>
  <div class="arrow">→</div>
  <div class="box" style="border-color:var(--blue);background:#f2f6ff">
   <div class="t">Total residual BUBR1</div><div class="n" style="color:var(--blue)">5–10%</div>
   <div class="d">restore the level and the checkpoint works</div></div>
 </div>
 <div class="punch">Not a broken protein.<br>A <em>scarce</em> one.</div>
</div>""",

3: """<div class="s" style="padding-bottom:150px">
 <div class="kicker">The target, as a number</div><div class="rule"></div>
 <h2 style="font-size:50px">Raise one destabilised protein <span style="color:var(--blue)">1.3–2.6×</span> — not restore it</h2>
 <img class="fig" src="FIGDATA">
</div>""",

4: """<div class="s">
 <div class="kicker">The framing error</div><div class="rule"></div>
 <h2>The same drugs. The opposite verdict.</h2>
 <div class="cols">
  <div class="col"><h3>In cancer</h3><div class="lead">aneuploid tumour · euploid host</div>
   <ul><li>HSP90 inhibitors</li><li>AMPK activators</li><li>Autophagy blockade</li></ul>
   <div class="verdict" style="color:var(--grn)">Selectivity = the therapeutic window</div></div>
  <div class="col bad"><h3>In MVA</h3><div class="lead">the patient <i>is</i> the aneuploid organism</div>
   <ul><li>Brain</li><li>Muscle</li><li>Marrow</li></ul>
   <div class="verdict" style="color:var(--red)">Selectivity = pointed at the child</div></div>
 </div>
 <div class="punch" style="margin-top:52px;font-size:52px">The therapeutic index isn’t narrow. It’s <em>inverted</em>.</div>
</div>""",

5: """<div class="s">
 <div class="kicker">The question nobody has asked</div><div class="rule"></div>
 <div class="center">
  <div class="big">Vincristine needs<br>the checkpoint.</div>
  <div class="big" style="color:var(--red);margin-top:26px">He doesn’t have one.</div>
  <div class="sub" style="margin-top:52px;max-width:1450px">
   Vinca alkaloids kill by holding cells in a spindle-checkpoint-dependent mitotic arrest.
   MVA1 cells exit that arrest in <b>68–114 minutes</b>; controls hold indefinitely.
   Prediction: they slip rather than die — escaping with a wrecked genome.</div>
 </div>
 <div class="foot">A falsifiable prediction for patient cells, not a treatment recommendation. No MVA line has been tested with vinca alkaloids.</div>
</div>""",

6: """<div class="s">
 <div class="kicker">What we would run</div><div class="rule"></div>
 <h2>One cell system. Three readouts. One threshold, set in advance.</h2>
 <div class="steps">
  <div class="step"><div class="k">Readout 1</div><div class="b">BUBR1 immunoblot</div>
   <div class="s2">total protein as % of isogenic wild type</div></div>
  <div class="step"><div class="k">Readout 2</div><div class="b">Checkpoint strength</div>
   <div class="s2">time to mitotic exit vs the 68–114 min patient baseline</div></div>
  <div class="step"><div class="k">Readout 3</div><div class="b">Genome integrity</div>
   <div class="s2">micronucleus frequency and PCS rate</div></div>
 </div>
 <div class="gate">Pre-registered gate: ≥1.3× BUBR1 <i>and</i> fewer micronuclei — or it is not a hit.</div>
 <div class="foot">Code, data-handling and full reports: github.com/Marxist-Leninist/mva-hackathon-2026 · CC-BY 4.0</div>
</div>"""
}

async def main():
    fig = base64.b64encode(open('slides/fig_dosage.png','rb').read()).decode()
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={'width':1920,'height':1080}, device_scale_factor=1)
        for n, body in SLIDES.items():
            html = f"<html><head><meta charset='utf-8'><style>{CSS}</style></head><body>{body.replace('FIGDATA','data:image/png;base64,'+fig)}</body></html>"
            await pg.set_content(html, wait_until='load')
            await pg.wait_for_timeout(250)
            await pg.screenshot(path=f'slides/slide{n}.png')
            print("rendered slide", n)
        await b.close()

asyncio.run(main())
