"""Reproducible, unretouched crops for the terminal-component spacing check.

Only native-pixel crops and integer nearest-neighbour enlargement are used.
The geometric reading is manual and is not an image classifier result.
"""
from pathlib import Path
import hashlib
import json
import textwrap
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / "work"
SPECS = {
    "full-p2": ("full/0004.jpg", (890, 2290, 2400, 2680), 1, "Passage 2 in line context"),
    "table": ("full/key255.jpg", (130, 360, 2430, 1260), 1, "Comparison key alphabet and syllables"),
    "ff-detail": ("full/key255.jpg", (1018, 1050, 1118, 1210), 6, "Key 255: ff graphic, 6x native pixels"),
    "xx-detail": ("full/key255.jpg", (2005, 790, 2110, 920), 6, "Key 255: XX=u graphic, 6x native pixels"),
    "key-ff": ("full/key255.jpg", (1010, 930, 1135, 1210), 2, "Key 255 ff: label and graphic (2x)"),
    "key-xx": ("full/key255.jpg", (2005, 790, 2110, 920), 3, "Key 255 XX=u: glyph only (3x); full table saved separately"),
    "inverse-xx": ("full/key254.jpg", (2110, 2100, 2490, 2290), 2, "Inverse key 254 XX=u: label and looped forms (2x)"),
    "p2-terminal": ("full/0004.jpg", (1420, 2430, 1790, 2620), 2, "Passage 2 terminal pair: separated crossed forms (2x)"),
    "p1-xx": ("full/0004.jpg", (1650, 1890, 1940, 2050), 2, "Passage 1 XX control: separated crossed forms (2x)"),
    "ending-context": ("full/0004.jpg", (980, 2430, 1810, 2660), 1, "Ending: 50 32 110, looped sign, crossed pair (1x)"),
}


def main():
    manifest = json.loads((WORK / "source-sha256-2026-10-23-key1236.json").read_text())
    changed = [name for name, sha in manifest.items()
               if hashlib.sha256((ROOT / "source" / name).read_bytes()).hexdigest() != sha]
    if changed:
        raise SystemExit(f"Source preservation failure: {changed}")
    crops = {}
    records = []
    for name, (source, rect, scale, label) in SPECS.items():
        path = ROOT / "source" / source
        im = Image.open(path).convert("RGB")
        assert 0 <= rect[0] < rect[2] <= im.width
        assert 0 <= rect[1] < rect[3] <= im.height
        crop = im.crop(rect)
        if scale != 1:
            crop = crop.resize((crop.width * scale, crop.height * scale), Image.Resampling.NEAREST)
        crop.save(WORK / f"ending-alternative-{name}-2026-10-28.png")
        crops[name] = crop
        records.append({"name": name, "source": "source/" + source,
                        "rectangle_xyxy": rect, "integer_scale": scale,
                        "source_sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
                        "label": label})

    font_path = "/System/Library/Fonts/Supplemental/Arial.ttf"
    font = ImageFont.truetype(font_path, 23) if Path(font_path).exists() else ImageFont.load_default()
    canvas = Image.new("RGB", (1760, 2100), "white")
    draw = ImageDraw.Draw(canvas)
    names = ["key-ff", "key-xx", "p2-terminal", "p1-xx", "inverse-xx", "ending-context"]
    for index, name in enumerate(names):
        x, y = 10 + 880 * (index % 2), 10 + 650 * (index // 2)
        for offset, line in enumerate(textwrap.wrap(SPECS[name][3], 60)):
            draw.text((x, y + offset * 28), line, font=font, fill="black")
        canvas.paste(crops[name], (x, y + 70))
    footnote = (
        "Manual hypothesis: key ff may be two overlapping crossed components; separating them could remove their contact without deleting a distinct connector. "
        "No same-writer ff example proves this. XX=u remains directly compatible. No hidden ink reconstructed; no plaintext changed."
    )
    for offset, line in enumerate(textwrap.wrap(footnote, 140)):
        draw.text((10, 1970 + offset * 30), line, font=font, fill="black")
    canvas.save(WORK / "ending-alternative-spacing-board-2026-10-28.png")

    result = {
        "status": "Alternative geometric mechanism only; no new accepted plaintext",
        "new_question": "Does ff require omitted independent connectors, or can increased component spacing account for the target?",
        "manual_observation": "The ff graphic can be parsed as two near-vertical staves, each crossed by a rising diagonal. The diagonal arms contact the neighbouring stave. This permits, but does not prove, a spacing interpretation of the apparent connectors.",
        "hypothesis": "The writer could space the crossed components apart. This would resemble XX without requiring a global XX=ff key substitution.",
        "limits": [
            "A component decomposition is a manual geometric hypothesis, not a recovered ductus or writing rule.",
            "The target and passage-1 XX are also directly compatible with XX=u, including the inverse key's looped arms.",
            "No independent same-writer ff control is available.",
            "The complete key inventory and passage context supplied no well-supported third terminal sign or new segmentation.",
            "The top of the au/8 sign is obscured by black annotation; no hidden feature is reconstructed. Both prior branches remain live.",
            "Key253 and key266 ff graphics differ and provide no separated-cross corroboration.",
            "This revises a rationale for a known candidate; it is not a newly deciphered word."
        ],
        "crops": records,
        "source_preservation": {"checked": len(manifest), "changed": changed},
        "changed_key_cells": 0,
        "changed_plaintext_branches": 0,
        "independent_review": False,
    }
    (WORK / "ending-alternative-2026-10-28.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"source_preservation": result["source_preservation"], "crops": len(records), "new_plaintext": False}))


if __name__ == "__main__":
    main()
