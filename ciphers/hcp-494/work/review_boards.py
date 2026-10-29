"""Compact neutral boards for user inspection; existing original rectangles only."""
from pathlib import Path
import hashlib
import json
from PIL import Image, ImageDraw, ImageFont
from expanded_bp_controls import SPECS as BP
from p2_original_controls import SPECS as P2

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / "work"
FONT_PATH = Path("/System/Library/Fonts/Supplemental/Arial.ttf")
FONT = ImageFont.truetype(str(FONT_PATH), 20) if FONT_PATH.exists() else ImageFont.load_default()


def board(filename, selections, columns, width, height):
    rows = (len(selections) + columns - 1) // columns
    canvas = Image.new("RGB", (columns * width, rows * height), "white")
    draw = ImageDraw.Draw(canvas)
    records = []
    for i, (specs, name, label, scale) in enumerate(selections):
        page, box = specs[name][:2]
        source = ROOT / f"source/full/{page}.jpg"
        crop = Image.open(source).convert("RGB").crop(box)
        crop = crop.resize((crop.width * scale, crop.height * scale), Image.Resampling.NEAREST)
        assert crop.width + 20 <= width and crop.height + 50 <= height, name
        x, y = i % columns * width + 10, i // columns * height + 45
        draw.text((x, y - 35), label + f" ({scale}x)", font=FONT, fill="black")
        canvas.paste(crop, (x, y))
        records.append({"source": str(source.relative_to(ROOT)), "box": box, "scale": scale,
                        "label": label, "source_sha256": hashlib.sha256(source.read_bytes()).hexdigest()})
    canvas.save(WORK / filename)
    return records


def main():
    records = {}
    records["review-pp-bb.png"] = board("review-pp-bb.png", [
        (BP, "target", "Target pair", 2),
        (BP, "proposition", "P in Proposition", 2),
        (BP, "lit-b", "B in Lit. B", 2),
        (BP, "breviat", "b/B in breviat: contrary control", 2),
        (BP, "key-pp", "Key: PP = n", 2),
        (BP, "key-bb", "Key: BB = z", 2),
    ], 3, 470, 420)
    records["review-ii-55.png"] = board("review-ii-55.png", [
        (P2, "initial", "Target pair; black gloss above", 2),
        (P2, "500", "Original 500", 2),
        (P2, "50", "Original 50", 2),
        (P2, "inverse-ii", "Key: II = g", 1),
        (P2, "inverse-55", "Key: 55 = h", 1),
        (P2, "ihro", "I/J in Ihro: different script", 1),
    ], 3, 510, 420)
    records["review-terminal.png"] = board("review-terminal.png", [
        (P2, "terminal", "Target at end of passage 2", 2),
        (P2, "p1-xx", "XX in passage 1", 2),
        (P2, "key-ff", "Key: ff and its connected symbol", 2),
        (P2, "inverse-xx", "Inverse key: XX = u", 2),
    ], 2, 800, 620)
    (WORK / "review-boards.json").write_text(json.dumps({
        "purpose": "User inspection of existing evidence, not a new decipherment experiment",
        "operation": "Existing original rectangles; nearest-neighbor 1x/2x only. No marks added to source pixels.",
        "boards": records,
    }, indent=2) + "\n")
    print("Three review boards created from previously checked rectangles.")


if __name__ == "__main__":
    main()
