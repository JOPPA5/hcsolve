"""Original-pixel punctuation microcheck; observations are manual, not OCR.

The unique outputs do not alter the transcription, key or plaintext branches.
"""
from pathlib import Path
import hashlib
import json
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / "work"
OUT = WORK / "terminal-punctuation-2026-10-28"
SPECS = {
    "p1": ("0004", (520, 1880, 2390, 2250), 1),
    "p2": ("0004", (520, 2330, 2400, 2660), 1),
    "terminal-detail": ("0004", (1390, 2400, 1810, 2680), 3),
    "p1xx-detail": ("0004", (1630, 1860, 1980, 2080), 3),
    "p2-768": ("0004", (510, 2370, 930, 2510), 3),
    "p4-625": ("0004", (950, 905, 1300, 1020), 3),
    "p3-625": ("0003", (1570, 1130, 1870, 1260), 3),
    "p4-upper": ("0004", (520, 580, 2420, 1170), 1),
    "p3-upper": ("0003", (610, 680, 2490, 1420), 1),
    "p3-lower": ("0003", (610, 2040, 2490, 3260), 1),
    "p4-lower": ("0004", (500, 2760, 2440, 3080), 1),
    "p2-630": ("0002", (1830, 2910, 2210, 3070), 3),
    "key-ff": ("key255", (1010, 930, 1135, 1210), 3),
    "key-xx": ("key255", (1980, 350, 2150, 930), 2),
    "inverse-xx": ("key254", (2110, 2100, 2490, 2290), 2),
    "p4-768-upper": ("0004", (1910, 665, 2160, 835), 3),
    "p3-630": ("0003", (2150, 2720, 2480, 2910), 3),
    "p4-601-mid": ("0004", (1750, 2090, 2070, 2230), 3),
}

# Code labels locate existing occurrences; their proposed meanings are not used.
# One = one securely visible adjacent trailing dot; small paper/bleedthrough
# specks are not counted as original punctuation. This is not a new transcription.
CODE_ROWS = [
    (2, "630", "one", "p2-630"),
    (3, "601", "one", "p3-upper"),
    (3, "651", "one", "p3-upper"),
    (3, "625", "one secure; possible upper mark uncertain", "p3-625"),
    (3, "653", "one", "p3-upper"),
    (3, "829", "one", "p3-lower"),
    (3, "651", "one", "p3-lower"),
    (3, "630", "obscured by annotation; not confidently counted", "p3-630"),
    (3, "774", "one", "p3-lower"),
    (3, "775", "one", "p3-lower"),
    (4, "601", "one", "p4-upper"),
    (4, "576", "one", "p4-upper"),
    (4, "768", "one", "p4-768-upper"),
    (4, "601", "one", "p4-upper"),
    (4, "625", "two vertical marks: upper short dash and lower dot", "p4-625"),
    (4, "829", "one", "p4-upper"),
    (4, "651", "one", "p4-upper"),
    (4, "634", "one", "p1"),
    (4, "601", "one", "p4-601-mid"),
    (4, "768", "one close dot plus two farther vertical marks", "p2-768"),
    (4, "427/447", "one", "p4-lower"),
    (4, "641", "one", "p4-lower"),
    (4, "303", "one", "p4-lower"),
    (4, "447", "one", "p4-lower"),
    (4, "602", "one", "p4-lower"),
    (4, "834", "one dot plus a separate lower comma-like stroke", "p4-lower"),
]


def main():
    OUT.mkdir(exist_ok=True)
    manifest = json.loads((WORK / "source-sha256-2026-10-23-key1236.json").read_text())
    changed = [name for name, sha in manifest.items()
               if hashlib.sha256((ROOT / "source" / name).read_bytes()).hexdigest() != sha]
    assert not changed, changed
    crops = {}
    records = []
    for name, (file, box, scale) in SPECS.items():
        path = ROOT / "source/full" / f"{file}.jpg"
        source = Image.open(path).convert("RGB")
        assert 0 <= box[0] < box[2] <= source.width
        assert 0 <= box[1] < box[3] <= source.height
        im = source.crop(box)
        im = im.resize((im.width * scale, im.height * scale), Image.Resampling.NEAREST)
        im.save(OUT / f"{name}.png")
        crops[name] = im
        records.append({"name": name, "source": str(path.relative_to(ROOT)),
                        "rectangle_xyxy": box, "integer_scale": scale,
                        "source_sha256": hashlib.sha256(path.read_bytes()).hexdigest()})

    # Show actual pixels at their native/previously declared integer scale.
    board = Image.new("RGB", (1370, 1980), "white")
    draw = ImageDraw.Draw(board)
    font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 24)
    entries = [
        ("p1xx-detail", "P1 crossed pair: one trailing dot", 10, 10),
        ("terminal-detail", "P2 terminal pair: two trailing dots; faint upper specks uncounted", 10, 730),
        ("p2-768", "P2 leading 768: close dot, then two vertical marks", 10, 1610),
    ]
    # Board uses dedicated tighter crops to keep the review sheet compact.
    tight = {
        "p1xx-detail": ("0004", (1650, 1890, 1940, 2050), 3),
        "terminal-detail": ("0004", (1460, 2460, 1770, 2620), 3),
        "p2-768": ("0004", (540, 2390, 875, 2500), 3),
    }
    board = Image.new("RGB", (1300, 1840), "white")
    draw = ImageDraw.Draw(board)
    for index, (name, label, _, _) in enumerate(entries):
        file, box, scale = tight[name]
        im = Image.open(ROOT / "source/full" / f"{file}.jpg").crop(box)
        im = im.resize((im.width*scale, im.height*scale), Image.Resampling.NEAREST)
        y = 10 + index * 600
        draw.text((10, y), label, fill="black", font=font)
        board.paste(im, (10, y+45))
        records.append({"name": name + "-board", "source": f"source/full/{file}.jpg",
                        "rectangle_xyxy": box, "integer_scale": scale})
    board.save(OUT / "punctuation-board.png")

    result = {
        "status": "No systematic dot-based ff/XX distinction established",
        "method": "Manual visual reading of original pixels; no OCR, enhancement, ink removal, inferred hidden strokes or guessed plaintext",
        "scope": "Both 20-token inserts, all 26 catalogued large-code occurrences in the original letter, plus forward ff/XX and inverse XX key controls",
        "letter_inserts": {
            "p1": {"tokens": 20, "observation": "One adjacent trailing dot visible after each group, including XX and final 634"},
            "p2": {"tokens": 20, "observation": "One adjacent trailing dot after each interior group; leading 768 has close dot plus farther vertical pair; terminal crossed pair has two approximately baseline dots"}
        },
        "key_controls": {
            "ff_forward": "No trailing two-dot distinction visible in the ff cell",
            "XX_forward": "No comparable two-dot distinction; faint isolated lower-right speck not identified as an encoded mark",
            "XX_inverse": "One visible dot between XX and u; table separation, not evidence of a mandatory ciphertext glyph component"
        },
        "code_occurrences": [dict(occurrence=i, page=p, code=c, visible_suffix=s, crop=n)
                             for i,(p,c,s,n) in enumerate(CODE_ROWS,1)],
        "inference": "Ordinary group separator plus additional punctuation is compatible with the terminal marks, but its exact function is not proved. Extra marks also occur after numeric codes; their existence cannot identify the terminal pair as ff.",
        "limits": [
            "Only two crossed-pair ciphertext examples are available, one internal and one terminal; sign identity and position are confounded.",
            "The numeric examples show extra punctuation, but not an exact repeated horizontal two-dot counterpart to the terminal pair.",
            "No independent same-writer ff occurrence or explicit dot-modification rule is available.",
            "All counts are manual and restricted to securely separable marks; bleedthrough and uncertain upper marks are retained as uncertainties.",
            "Ink chronology is not established from image colour."
        ],
        "crops": records,
        "source_preservation": {"checked": len(manifest), "changed": changed},
        "changed_key_cells": 0,
        "changed_plaintext_branches": 0,
        "independent_review": False,
    }
    (WORK / "terminal-punctuation-2026-10-28.json").write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({"source_preservation": result["source_preservation"], "code_occurrences": len(CODE_ROWS), "result": result["status"]}))


if __name__ == "__main__":
    main()
