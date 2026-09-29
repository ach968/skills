#!/usr/bin/env python3
"""Render every manual page and create a mechanical report and contact sheets."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pdf", type=Path)
    parser.add_argument("--out", required=True, type=Path)
    parser.add_argument("--scale", type=int, default=1600,
                        help="Longest rendered page edge in pixels (default: 1600)")
    args = parser.parse_args()
    if not args.pdf.is_file() or args.scale < 600:
        parser.error("Provide an existing PDF and a scale of at least 600 pixels.")
    try:
        from pypdf import PdfReader
        from PIL import Image, ImageDraw
    except ImportError as exc:
        print(f"Missing dependency: {exc}. Use the bundled runtime or install pypdf Pillow.", file=sys.stderr)
        return 2
    renderer = shutil.which("pdftoppm")
    if not renderer:
        print("pdftoppm is required. Use the bundled Poppler runtime or install Poppler.", file=sys.stderr)
        return 2

    pdf = args.pdf.resolve()
    out = args.out.resolve()
    out.mkdir(parents=True, exist_ok=True)
    digest = hashlib.sha256(pdf.read_bytes()).hexdigest()
    renders = out / ("pages-" + digest[:12])
    renders.mkdir(exist_ok=True)
    reader = PdfReader(pdf)
    report = {"pdf": str(pdf), "sha256": digest, "page_count": len(reader.pages),
              "checks": "Mechanical checks only; human/agent visual and evidence review still required.",
              "warnings": [], "pages": [], "contact_sheets": []}
    if not reader.pages:
        print("PDF has no pages.", file=sys.stderr)
        return 1

    for number, page in enumerate(reader.pages, 1):
        text = page.extract_text() or ""
        width, height = float(page.mediabox.width), float(page.mediabox.height)
        annotations = [ref.get_object() for ref in (page.get("/Annots") or [])]
        links = sum(a.get("/Subtype") == "/Link" for a in annotations)
        entry = {"page": number, "size_pt": [round(width, 2), round(height, 2)],
                 "text_characters": len(text.strip()), "links": links}
        if len(text.strip()) < 80:
            report["warnings"].append({"page": number, "issue": "Little searchable text; inspect for a blank or image-only page."})
        if abs(width - 612) > 2 or abs(height - 792) > 2:
            report["warnings"].append({"page": number, "issue": "Page is not US Letter; confirm this is intentional."})
        if "\ufffd" in text or "\u25a0" in text:
            report["warnings"].append({"page": number, "issue": "Possible replacement/missing glyph; inspect rendered page."})
        markers = sorted(set(re.findall(r"\b(?:TODO|TBD|REPLACE(?:_[A-Z]+)*|PLACEHOLDER)\b", text)))
        if markers:
            report["warnings"].append({"page": number, "issue": "Review possible unfinished markers: " + ", ".join(markers)})
        report["pages"].append(entry)

    command = [renderer, "-scale-to", str(args.scale), "-png", str(pdf), str(renders / "page")]
    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode:
        report["render_error"] = result.stderr[-4000:]
        (out / "report.json").write_text(json.dumps(report, indent=2) + "\n")
        print(result.stderr[-4000:], file=sys.stderr)
        return 1
    files = {}
    for path in renders.glob("page-*.png"):
        match = re.fullmatch(r"page-(\d+)\.png", path.name)
        if match:
            files[int(match.group(1))] = path
    expected = set(range(1, len(reader.pages) + 1))
    if set(files) != expected:
        print("Rendered page set does not match the PDF page set.", file=sys.stderr)
        return 1
    for entry in report["pages"]:
        entry["image"] = str(files[entry["page"]])

    columns, rows, cell_w, cell_h = 4, 3, 270, 380
    for start in range(1, len(reader.pages) + 1, columns * rows):
        stop = min(start + columns * rows - 1, len(reader.pages))
        sheet = Image.new("RGB", (columns * cell_w, rows * cell_h), "#dedbd5")
        draw = ImageDraw.Draw(sheet)
        for index, number in enumerate(range(start, stop + 1)):
            x, y = (index % columns) * cell_w, (index // columns) * cell_h
            with Image.open(files[number]) as page_image:
                thumb = page_image.convert("RGB")
                thumb.thumbnail((cell_w - 18, cell_h - 36))
                sheet.paste(thumb, (x + (cell_w - thumb.width) // 2, y + 8))
            draw.text((x + 12, y + cell_h - 20), f"PAGE {number}", fill="#1d1a17")
        destination = out / f"contact-{start:03d}-{stop:03d}.png"
        sheet.save(destination)
        report["contact_sheets"].append(str(destination))
    destination = out / "report.json"
    destination.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({"page_count": len(reader.pages), "warning_count": len(report["warnings"]),
                      "report": str(destination), "contact_sheets": report["contact_sheets"]}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
