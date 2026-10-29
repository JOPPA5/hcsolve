"""Unretouched same-page controls for BB versus the older numeric 66 reading.

This is a manually selected comparison sheet, not a classifier or blind test.
Requires Pillow. No ink removal, sharpening, or reconstruction is applied.
"""
import hashlib
import json
from pathlib import Path

from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source/full/0004.jpg"
SPECS = [
    ("Disputed pair: preferred BB; 66 alternative", (2070, 2010, 2240, 2130)),
    ("Passage 1: 67", (1170, 1890, 1370, 2040)),
    ("Passage 1: 26", (1310, 2010, 1510, 2150)),
    ("Passage 2: 63", (1410, 2380, 1560, 2500)),
    ("Passage 2: 96 (partly overlapped by gloss)", (690, 2480, 880, 2620)),
    ("Earlier on the same page: 625", (1000, 900, 1260, 1030)),
]


def main():
    source = Image.open(SOURCE).convert("RGB")
    sheet = Image.new("RGB", (1260, 540), "white")
    draw = ImageDraw.Draw(sheet)
    metadata = {
        "source": str(SOURCE.relative_to(ROOT)),
        "source_sha256": hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
        "coordinate_convention": "Pillow left, top, right, bottom; original pixels",
        "operation": "rectangular crops at native pixel size on a white labelled sheet",
        "controls": [],
        "limitation": "Manual visual comparison; BB versus 66 remains unresolved. No support for PP=n is established.",
    }
    for i, (label, bounds) in enumerate(SPECS):
        x, y = (i % 3) * 420 + 12, (i // 3) * 250 + 12
        crop = source.crop(bounds)
        draw.text((x, y), label, fill="black")
        sheet.paste(crop, (x, y + 30))
        metadata["controls"].append({"label": label, "box": list(bounds)})
    draw.text((12, 515), "All six crops: original image 0004. Black annotations are preserved. No new reading is asserted.", fill="black")
    sheet.save(ROOT / "work/numeral-six-controls.png")
    (ROOT / "work/numeral-six-controls.json").write_text(json.dumps(metadata, indent=2) + "\n")


if __name__ == "__main__":
    main()
