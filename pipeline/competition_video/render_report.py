#!/usr/bin/env python3
"""Render the canonical Track 2 Markdown report to a submission-ready PDF."""

from __future__ import annotations

import argparse
import hashlib
import html
import re
from pathlib import Path

import markdown
import yaml
from weasyprint import HTML


CSS = r"""
@page {
  size: A4;
  margin: 18mm 17mm 19mm 17mm;
  @bottom-left {
    content: "MVA Hackathon 2026 | MarxistLeninist | Track 2";
    font-family: DejaVu Sans, sans-serif;
    font-size: 8pt;
    color: #667085;
  }
  @bottom-right {
    content: "Page " counter(page) " of " counter(pages);
    font-family: DejaVu Sans, sans-serif;
    font-size: 8pt;
    color: #667085;
  }
}
@page:first {
  @bottom-left { content: none; }
  @bottom-right { content: none; }
}
html { font-family: DejaVu Sans, sans-serif; color: #172033; }
body { font-size: 9.3pt; line-height: 1.43; }
.title-page {
  min-height: 245mm;
  display: flex;
  flex-direction: column;
  justify-content: center;
  page-break-after: always;
  background: linear-gradient(145deg, #071226, #112442);
  color: #f7fbff;
  margin: -18mm -17mm -19mm -17mm;
  padding: 25mm 23mm;
  box-sizing: border-box;
}
.kicker { color: #42d6e6; font-weight: 700; letter-spacing: .12em; font-size: 10pt; }
h1.title { font-size: 30pt; line-height: 1.08; margin: 12mm 0 5mm; color: white; }
.subtitle { font-size: 16pt; line-height: 1.3; color: #c8d9f4; max-width: 150mm; }
.meta { margin-top: 22mm; font-size: 11pt; color: #d8e2f2; }
.scope {
  margin-top: 18mm; padding: 5mm 6mm; border: 1px solid #42d6e6;
  border-radius: 4mm; color: #dffcff; background: rgba(28, 54, 91, .65);
}
h1, h2, h3 { color: #10274a; page-break-after: avoid; }
h1 { font-size: 19pt; border-bottom: 2px solid #39b8ca; padding-bottom: 2mm; margin-top: 9mm; }
h2 { font-size: 14pt; margin-top: 7mm; }
h3 { font-size: 11.5pt; margin-top: 5mm; }
p { margin: 0 0 3mm; orphans: 3; widows: 3; }
ul, ol { margin: 2mm 0 4mm 6mm; padding-left: 5mm; }
li { margin-bottom: 1.2mm; }
blockquote {
  margin: 5mm 0; padding: 4mm 5mm; border-left: 4px solid #31baca;
  background: #edf8fa; color: #16324c; page-break-inside: avoid;
}
code { font-family: DejaVu Sans Mono, monospace; font-size: 8.5pt; background: #eef1f5; padding: .2mm .8mm; border-radius: 1mm; }
pre { white-space: pre-wrap; background: #101b2f; color: #edf7ff; padding: 4mm; border-radius: 2mm; page-break-inside: avoid; }
table { width: 100%; border-collapse: collapse; margin: 4mm 0 6mm; font-size: 8.2pt; page-break-inside: avoid; }
thead { display: table-header-group; }
th { background: #17355d; color: white; text-align: left; padding: 2.2mm; }
td { border: 0.4pt solid #c5cfdb; padding: 2.1mm; vertical-align: top; }
tr:nth-child(even) td { background: #f4f7fa; }
a { color: #075e91; text-decoration: none; overflow-wrap: anywhere; }
hr { border: 0; border-top: 1px solid #b7c4d2; margin: 7mm 0; }
strong { color: #10274a; }
.footnote, .references { font-size: 8.3pt; }
"""


def parse_front_matter(text: str) -> tuple[dict, str]:
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---\n", 4)
    if end < 0:
        return {}, text
    metadata = yaml.safe_load(text[4:end]) or {}
    return metadata, text[end + 5 :]


def normalise_markdown(text: str) -> str:
    # WeasyPrint handles ordinary ASCII punctuation most reliably. Preserve the
    # scientific symbols already used by the report while avoiding raw tab runs.
    return text.replace("\t", "    ").strip() + "\n"


def title_page(metadata: dict) -> str:
    title = html.escape(str(metadata.get("title", "Track 2 Drug-Repurposing Proposal")))
    subtitle = html.escape(str(metadata.get("subtitle", "Rare Disease, Real Kid: MVA Hackathon 2026")))
    author = html.escape(str(metadata.get("author", "MarxistLeninist")))
    date = html.escape(str(metadata.get("date", "30 August 2026")))
    return f"""
<section class="title-page">
  <div class="kicker">RARE DISEASE, REAL KID | TRACK 2</div>
  <h1 class="title">{title}</h1>
  <div class="subtitle">{subtitle}</div>
  <div class="meta"><strong style="color:white">Participant:</strong> {author}<br>
  <strong style="color:white">Report date:</strong> {date}</div>
  <div class="scope"><strong style="color:white">Preclinical scope:</strong>
  approved medicines proposed for controlled experimental testing. No drug, dose,
  off-label use, oncology change, or clinical efficacy claim follows from this report.</div>
</section>
"""


def render(source: Path, output: Path) -> None:
    raw = source.read_text(encoding="utf-8")
    metadata, body = parse_front_matter(raw)
    body = normalise_markdown(body)
    rendered = markdown.markdown(
        body,
        extensions=["tables", "fenced_code", "sane_lists", "toc"],
        output_format="html5",
    )
    document = f"""<!doctype html><html><head><meta charset="utf-8">
<style>{CSS}</style></head><body>{title_page(metadata)}{rendered}</body></html>"""
    output.parent.mkdir(parents=True, exist_ok=True)
    HTML(string=document, base_url=str(source.parent)).write_pdf(str(output))


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    render(args.source.resolve(), args.output.resolve())
    print(f"wrote {args.output} sha256={digest(args.output.resolve())}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
