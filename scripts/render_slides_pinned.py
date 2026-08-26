#!/usr/bin/env python3
"""Re-render the pitch slides using the Chromium already present in the image.

The repo's make_slides.py calls p.chromium.launch() with no executable_path,
which makes Playwright look for the browser build matching whatever Playwright
version happens to be installed. In this environment those disagree (the image
ships build 1194; the pip-installed Playwright wants 1234), and the fix is NOT
to download a second browser — it is to point at the one already here.

This wrapper imports the repo's own CSS and SLIDES definitions so there is a
single source of truth for slide content: correcting make_slides.py corrects
this too, and this file holds no slide text of its own.
"""
import asyncio
import base64
import importlib.util
import os
import sys

CHROMIUM = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"


def load_repo_slides(path):
    """Import make_slides.py for CSS/SLIDES without running its asyncio main()."""
    src = open(path, encoding="utf-8").read()
    # Drop the module's own entrypoint so importing it has no side effects.
    marker = "async def main("
    if marker in src:
        src = src[: src.index(marker)]
    ns = {"__name__": "repo_slides"}
    exec(compile(src, path, "exec"), ns)
    return ns["CSS"], ns["SLIDES"]


async def render(css, slides, figpath, outdir):
    from playwright.async_api import async_playwright

    fig = base64.b64encode(open(figpath, "rb").read()).decode()
    os.makedirs(outdir, exist_ok=True)
    async with async_playwright() as p:
        browser = await p.chromium.launch(executable_path=CHROMIUM)
        page = await browser.new_page(viewport={"width": 1920, "height": 1080},
                                      device_scale_factor=1)
        for n, body in slides.items():
            html = (f"<html><head><meta charset='utf-8'><style>{css}</style></head>"
                    f"<body>{body.replace('FIGDATA', 'data:image/png;base64,' + fig)}</body></html>")
            await page.set_content(html, wait_until="load")
            await page.wait_for_timeout(300)
            out = os.path.join(outdir, f"slide{n}.png")
            await page.screenshot(path=out)
            print(f"rendered slide {n} -> {out}")
        await browser.close()


def main():
    repo = sys.argv[1] if len(sys.argv) > 1 else "."
    make_slides = os.path.join(repo, "pipeline/genomewide/make_slides.py")
    figpath = os.path.join(repo, "results/bubr1_dosage_window.png")
    outdir = os.path.join(repo, "video")

    if not os.path.exists(CHROMIUM):
        sys.exit(f"chromium not found at {CHROMIUM}")
    css, slides = load_repo_slides(make_slides)
    asyncio.run(render(css, slides, figpath, outdir))


if __name__ == "__main__":
    main()
