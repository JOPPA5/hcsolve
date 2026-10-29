"""Original-sign controls for initial II/55 and terminal XX/[ff].

Crop coordinates and feature assessments are manual. No OCR, ink separation,
stroke reconstruction, language scoring, or independent review is performed.
"""
from pathlib import Path
import hashlib
import json
from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / "work"
SPECS = {
    "initial": ("0004", (900, 2360, 1140, 2540), "Initial pair: II / 55; nearby black gloss", 2),
    "500": ("0003", (1900, 1050, 2110, 1170), "Original 500: initial numeral 5", 2),
    "50": ("0004", (1000, 2460, 1200, 2640), "Original 50: initial 5; nearby gloss", 2),
    "625-p3": ("0003", (1620, 1140, 1820, 1260), "Original 625, image 0003", 2),
    "75": ("0004", (2015, 2370, 2200, 2495), "Original 75: previous control", 2),
    "85": ("0004", (1350, 1900, 1570, 2035), "Original 85: previous control", 2),
    "625-p4": ("0004", (1000, 900, 1260, 1030), "Original 625, image 0004", 2),
    "775": ("0003", (1520, 3070, 1930, 3270), "Original 775: black gloss above", 1),
    "576": ("0004", (1350, 670, 1710, 830), "Original 576: black gloss near upper 5", 1),
    "inverse-ii": ("key254", (1810, 3490, 2170, 3620), "Inverse key 254: II = g", 1),
    "inverse-55": ("key254", (650, 1350, 1000, 1540), "Inverse key 254: 55 = h", 1),
    "forward-g-h": ("key255", (710, 400, 950, 960), "Forward key 255: G/H columns", 1),
    "ihro": ("0003", (850, 1570, 1270, 1740), "I/J in Ihro: German-script variant", 1),
    "ihr": ("0003", (2000, 1460, 2480, 1660), "I/J in Ihr before Konigl.: German script", 1),
    "initial-context": ("0004", (520, 2280, 1500, 2540), "Initial pair in original line context", 1),
    "terminal": ("0004", (1420, 2430, 1790, 2620), "Terminal pair: two separate X-like forms", 2),
    "p1-xx": ("0004", (1650, 1890, 1940, 2050), "Original passage 1: XX = u under the key", 2),
    "key-ff": ("key255", (1010, 930, 1135, 1210), "Key 255: ff label and connected symbol", 2),
    "inverse-xx": ("key254", (2110, 2100, 2490, 2290), "Inverse key 254: XX = u; looped upper arms", 2),
    "forward-xx": ("key255", (2005, 790, 2110, 920), "Forward key 255: XX homophone", 2),
    "st": ("0004", (1940, 1890, 2095, 2030), "Original st symbol: upper connection retained", 2),
    "tt": ("0004", (1225, 2370, 1395, 2510), "Original tt symbol: lower connection retained", 2),
    "key-st": ("key255", (1915, 935, 2025, 1210), "Key 255: st symbol", 1),
    "key-tt": ("key255", (2015, 935, 2120, 1210), "Key 255: tt symbol", 1),
}


def main():
    manifest = json.loads((WORK / "source-sha256-2026-10-23-key1236.json").read_text())
    changed = [name for name, sha in manifest.items()
               if hashlib.sha256((ROOT / "source" / name).read_bytes()).hexdigest() != sha]
    if changed:
        raise SystemExit(f"Source preservation failure: {changed}")
    crops, records = {}, []
    for name, (page, box, label, scale) in SPECS.items():
        source = ROOT / f"source/full/{page}.jpg"
        original = Image.open(source).convert("RGB")
        assert 0 <= box[0] < box[2] <= original.width
        assert 0 <= box[1] < box[3] <= original.height
        crops[name] = original.crop(box)
        records.append({"name": name, "label": label, "box": box,
                        "source": str(source.relative_to(ROOT)),
                        "source_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
                        "display_scale": scale})

    def sheet(filename, names, columns, cell, lines):
        width, height = cell
        rows = (len(names) + columns - 1) // columns
        canvas = Image.new("RGB", (columns * width, rows * height + 25 * len(lines) + 20), "white")
        draw = ImageDraw.Draw(canvas)
        for i, name in enumerate(names):
            crop = crops[name]
            scale = SPECS[name][3]
            if scale != 1:
                crop = crop.resize((crop.width * scale, crop.height * scale), Image.Resampling.NEAREST)
            assert crop.width + 20 <= width and crop.height + 40 <= height, name
            x, y = i % columns * width + 10, i // columns * height + 30
            draw.text((x, y - 22), f"{SPECS[name][2]} ({scale}x)", fill="black")
            canvas.paste(crop, (x, y))
        for i, line in enumerate(lines):
            draw.text((10, rows * height + 5 + 25 * i), line, fill="black")
        canvas.save(WORK / filename)

    sheet("p2-initial-numeral-controls.png",
          ["initial", "500", "50", "625-p3", "75", "85", "625-p4", "775", "576"],
          3, (550, 405),
          ["Eight numeral-5 controls: visible bends/bowls contrast with the two long hooked target strokes.",
           "II is provisionally favored, not verified. Some controls have nearby or overlapping black glosses; no ink was removed."])
    sheet("p2-initial-letter-key-controls.png",
          ["inverse-ii", "inverse-55", "forward-g-h", "ihro", "ihr", "initial"],
          3, (550, 600),
          ["The key separates II=g from 55=h. The target's full upper loops/crossbars are not securely established.",
           "Ihr/Ihro are German-script variants, not exact matches or an independent cipher II. No recovered hidden strokes."])
    sheet("p2-terminal-original-controls.png", ["terminal", "p1-xx", "key-ff", "inverse-xx"],
          2, (800, 600),
          ["XX=u is provisionally favored by shape. A looped upper arm also occurs in the inverse key's XX.",
           "The key's ff symbol joins its staves with diagonal strokes; comparable links are not visible in the target.",
           "Simplified ff / a graphic collision remains a hypothesis. Neither an enciphering error nor a changed key is proved."])
    sheet("p2-connected-symbol-controls.png", ["st", "key-st", "tt", "key-tt", "forward-xx"],
          2, (460, 340),
          ["The original st/tt signs retain connecting curves. These two controls do not prove every ff must preserve its links.",
           "Original rectangles at native size or 2x pixel duplication only. Labels and judgments are manual."])
    sheet("p2-initial-original-context.png", ["initial-context"], 1, (1020, 310),
          ["The upper vicinity of the initial pair contains the black gott gloss; it is not used to choose II over 55."])

    result = {
        "status": "PARTIAL: initial II and terminal XX provisionally preferred by shape; neither verified",
        "prior_exposure": "Not blind. The Gott ... ablauff interpretation was already known from Bourdeau.",
        "scope": "Original three-page letter and existing keys 254/255 only; no new manuscript acquired.",
        "initial_pair": {
            "preferred_glyph": "II", "key_value": "g", "alternative": {"glyph": "55", "key_value": "h"},
            "new_numeral_controls": ["500", "50", "625-p3", "775", "576"],
            "previous_controls_rechecked": ["75", "85", "625-p4"],
            "observation": "The numeral controls have visible bends/rounded bowls, while both target signs are long hooked downstrokes. Initial-position 5 in 500/50 addresses the limitation of using final-position 5 alone.",
            "limits": "The key II forms have upper loops/crossbars not securely recovered in the target. The black gloss is near the target's upper parts. German-script Ihr/Ihro supplies variants, not a clean same-form control. No second unequivocal cipher II or numeric 55 was found in this letter.",
        },
        "terminal_pair": {
            "preferred_glyph": "XX", "key_value": "u", "alternative": {"glyph": "[ff]", "key_value": "ff"},
            "observation": "Two separate crossed forms resemble passage-1 XX. The inverse key XX=u also has looped upper arms, so the final sign's little upper loop does not distinguish ff. Key255 ff has two staves linked by diagonals; comparable links are not visible in the target.",
            "connector_controls": "Original st and tt preserve the key's connecting curves. This weakens a blanket connector-omission argument, but two different signs cannot prove how the writer would draw ff.",
            "limits": "There is no independent same-writer encrypted ff control. A simplified ff, homographic u/ff collision, copying error, or changed scheme is possible but unproved. Key254 confirms XX=u; its inspected sheet does not independently supply the ff symbol.",
        },
        "language_boundary": {
            "shape_preference_output": "<768>gottgebdasallwolablauu",
            "condition": "Also assumes the existing preferred ll and au identifications; not an accepted grammatical plaintext.",
            "language_candidate": "<768>gottgebdasallwolablauff",
            "extra_assumption": "The terminal X-like pair is intended as ff despite the visual preference for XX. No new ff reading is claimed from the black annotation.",
            "same_visible_family_models": [
                {"model": "Both X-like pairs are XX", "passage1_segment": "disgustirt", "passage2_ending": "ablauu", "status": "simplest shape assignment, linguistic problem retained"},
                {"model": "Writer's simplified ff collides with XX", "passage1_segment": "disgustirt", "passage2_ending": "ablauff", "status": "conditional local ambiguity, not an established writing rule"},
                {"model": "Both X-like pairs mean ff", "passage1_segment": "disgffstirt", "passage2_ending": "ablauff", "status": "unsupported global reassignment; not applied"},
            ],
        },
        "method": "Rectangular crops; native pixels or nearest-neighbor duplication. No thresholding, ink separation, interpolation, rotation, reconstruction, or numerical confidence estimate.",
        "crops": records,
        "source_preservation": {"checked": len(manifest), "changed": changed},
        "independent_review": False,
    }
    (WORK / "p2-original-controls.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"crop_count": len(records), "sheets": 5,
                      "source_preservation": result["source_preservation"],
                      "visual_preferences": ["II=g (provisional)", "XX=u (provisional)"]}, indent=2))


if __name__ == "__main__":
    main()
