"""Expanded B/P comparison from original pixels, not OCR or a classifier.

The feature descriptions and letter labels are manual visual judgments.
No annotation supplies a decoded value. Requires Pillow only to render sheets.
"""
from pathlib import Path
import hashlib
import json
from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / "work"
# Native pixel rectangles. No rotation, contrast adjustment, or ink removal.
SPECS = {
    "target": ("0004", (2050, 1980, 2270, 2160), "Cipher pair: PP / BB unresolved"),
    "proposition": ("0004", (575, 1330, 710, 1490), "P: Proposition"),
    "lit-b": ("0004", (675, 2650, 805, 2785), "B: isolated Lit. B"),
    "brunsvicense": ("0004", (1370, 1160, 1520, 1300), "B: Brunsvicense"),
    "berlin": ("0002", (1420, 2550, 1560, 2710), "B: Berlin"),
    "berlino": ("0002", (1570, 1240, 1725, 1390), "B: Berlino, different form"),
    "breviat": ("0003", (1590, 1690, 1750, 1810), "b/B: breviat, connected form"),
    "portrait": ("0003", (865, 1400, 1000, 1555), "P: Portrait, different form"),
    "key-pp": ("key255", (1300, 820, 1425, 925), "Key 255 PP = n; another hand"),
    "key-bb": ("key255", (2360, 790, 2495, 910), "Key 255 BB = z; another hand"),
    "proposition-word": ("0004", (550, 1320, 1120, 1500), "Proposition: word context"),
    "lit-b-word": ("0004", (530, 2640, 1010, 2800), "Lit. B: context"),
    "brunsvicense-word": ("0004", (1360, 1130, 1980, 1310), "Brunsvicense: word context"),
    "berlin-word": ("0002", (1390, 2550, 1900, 2730), "Berlin: word context"),
    "berlino-word": ("0002", (1560, 1235, 1940, 1400), "Berlino: word context"),
    "portrait-word": ("0003", (840, 1400, 1280, 1570), "Portrait: word context"),
    "breviat-word": ("0003", (1570, 1650, 2040, 1820), "breviat: word context"),
    "beylage-1": ("0004", (540, 1430, 1000, 1630), "b/B: beylage, German script"),
    "beylage-2": ("0004", (2010, 2550, 2370, 2690), "b/B: beylage, German script"),
    "burger": ("0004", (530, 2180, 1000, 2390), "B: Burger, German script"),
    "bauren": ("0004", (1010, 2170, 1440, 2350), "B: Bauren, German script"),
    "abfertigung": ("0003", (660, 2880, 1240, 3070), "b: abfertigung, German script"),
    "passato": ("0002", (1780, 1120, 2210, 1320), "p: passato, lower-case form"),
    "promissis": ("0002", (530, 2170, 1030, 2380), "p: promissis, lower-case form"),
    "plainten": ("0004", (2000, 2170, 2370, 2350), "p: plainten, lower-case form"),
    "ff-1": ("0004", (945, 1910, 1190, 2050), "Cipher FF: first passage"),
    "foedus": ("0004", (730, 1170, 1030, 1290), "Plain-text F: Foedus"),
    "ff-2": ("0004", (1790, 2380, 1950, 2520), "Cipher FF: second passage, gloss overlap"),
    "ll": ("0004", (2070, 1890, 2290, 2030), "Cipher LL: first passage"),
    "lit-l": ("0004", (530, 2650, 690, 2775), "Plain-text L: Lit."),
    "nn": ("0004", (825, 2450, 1060, 2610), "Cipher NN: second passage"),
}


def main():
    manifest = json.loads((WORK / "source-sha256-2026-10-23-key1236.json").read_text())
    changed = [name for name, sha in manifest.items()
               if hashlib.sha256((ROOT / "source" / name).read_bytes()).hexdigest() != sha]
    if changed:
        raise SystemExit(f"Source preservation failure: {changed}")
    crops, records = {}, []
    for name, (page, box, label) in SPECS.items():
        source = ROOT / f"source/full/{page}.jpg"
        original = Image.open(source).convert("RGB")
        assert 0 <= box[0] < box[2] <= original.width
        assert 0 <= box[1] < box[3] <= original.height
        crops[name] = original.crop(box)
        records.append({"name": name, "label": label, "box": box,
                        "source": str(source.relative_to(ROOT)),
                        "source_sha256": hashlib.sha256(source.read_bytes()).hexdigest()})

    def sheet(filename, names, columns, cell, scale, footer):
        width, height = cell
        rows = (len(names) + columns - 1) // columns
        canvas = Image.new("RGB", (columns * width, rows * height + 65), "white")
        draw = ImageDraw.Draw(canvas)
        for i, name in enumerate(names):
            crop = crops[name]
            if scale != 1:
                crop = crop.resize((crop.width * scale, crop.height * scale), Image.Resampling.NEAREST)
            assert crop.width + 20 <= width and crop.height + 40 <= height, name
            x, y = i % columns * width + 10, i // columns * height + 30
            draw.text((x, y - 22), SPECS[name][2], fill="black")
            canvas.paste(crop, (x, y))
        draw.text((10, rows * height + 5), footer, fill="black")
        draw.text((10, rows * height + 30),
                  f"Original rectangles; {scale}x nearest-neighbor pixels. No retouching. Labels/features are manual judgments.", fill="black")
        canvas.save(WORK / filename)

    sheet("expanded-bp-capitals.png",
          ["target", "proposition", "lit-b", "brunsvicense", "berlin", "berlino"],
          3, (470, 400), 2,
          "The B controls have a further right lower bow/return; no comparable extra bow is visible in either target sign.")
    sheet("expanded-bp-limits-and-key.png", ["breviat", "portrait", "key-pp", "key-bb"],
          2, (400, 370), 2,
          "The small lower stem loop is not diagnostic. P/b forms vary; the key is by a different hand. PP remains provisional.")
    sheet("expanded-bp-word-contexts.png",
          ["proposition-word", "lit-b-word", "brunsvicense-word", "berlin-word",
           "berlino-word", "portrait-word", "breviat-word"],
          2, (650, 235), 1,
          "These clear-word contexts identify control letters without using the black decipherment glosses.")
    sheet("expanded-bp-script-variants.png",
          ["beylage-1", "beylage-2", "burger", "bauren", "abfertigung", "passato", "promissis", "plainten"],
          2, (630, 250), 1,
          "German-script and lower-case forms are kept separate from the main capital-letter comparison.")
    sheet("expanded-bp-cipher-controls.png", ["ff-1", "foedus", "ff-2", "ll", "lit-l", "nn"],
          3, (620, 365), 2,
          "Cipher FF and LL resemble clear-text F and L on the same page; this supports, but does not prove, transfer for P/B.")

    rows = [line.split() for line in (ROOT / "source/bourdeau/ct.txt").read_text().splitlines()
            if line.strip() and not line.startswith("#")]
    pairs = [{"passage": p + 1, "index": i, "preserved_token": token}
             for p, row in enumerate(rows) for i, token in enumerate(row)
             if len(token) == 2 and token.isupper() and token[0] == token[1]]
    assert len(pairs) == 9
    assert sum(x["preserved_token"] == "BB" for x in pairs) == 1
    assert not any(x["preserved_token"] == "PP" for x in pairs)
    result = {
        "status": "PARTIAL; PP is now preferred provisionally over BB on visual grounds, not verified",
        "scope": "All three original letter pages visually inspected; selected controls from each. Not an exhaustive palaeographic edition.",
        "prior_exposure": "Not blind. Claude's undertanin and the earlier Proposition comparison were already known.",
        "feature_judgments": {
            "shared_nondiagnostic_feature": "A small loop at the foot of the stem occurs in P, B and connected b/B controls.",
            "new_discriminator": "Lit. B, Brunsvicense, Berlin and the variant Berlino have an additional lower right bow/return after the upper bow. Both target signs visibly end after the upper bow, closer to Proposition.",
            "strongest_added_control": "Lit. B is a detached capital in original brown ink on the same page; its lower right return cannot be attributed to joining the next letter.",
            "case_transfer_check": "Cipher FF and LL have counterparts in the original F of Foedus and L of Lit. This reduces, but does not eliminate, the uncertainty about comparing clear-text capitals with cipher letters.",
            "contrary_controls": "Connected b/B in breviat remains similar; Portrait shows a different P. German-script b/B and lower-case p vary and are not pooled as equivalent samples.",
        },
        "preferred_working_glyph": "PP",
        "retained_alternatives": {"BB": "live alternative; capital variation or simplified B is not excluded", "66": "older weaker numeric alternative; earlier numeral comparison remains available"},
        "conditional_outputs": {"PP": "disgustirtundertanin<634>", "BB": "disgustirtundertazin<634>", "66": "disgustirtundertadin<634>"},
        "unchanged_key_cells": {"PP": "n", "BB": "z", "66": "d"},
        "decoded_code_634": False,
        "repeated_cipher_control": "No second independently identified cipher PP or BB was found. No corroborating repeated cipher n is claimed.",
        "preserved_transcription_pair_inventory": pairs,
        "inventory_limitation": "Nine doubled-capital tokens in the two inherited transcriptions, including ambiguous terminal XX. Initial passage-2 55 is a separate II/55 hypothesis. This is not automatic recognition of the complete letter.",
        "method_limits": "Human-style visual interpretation by the solver; no classifier, statistical confidence, blind validation, or independent review. Missing lower bow is evidence, not a proof that a cursive B could never omit it.",
        "crops": records,
        "source_preservation": {"checked": len(manifest), "changed": changed},
    }
    (WORK / "expanded-bp-controls.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"source_preservation": result["source_preservation"],
                      "crop_count": len(records), "sheets": 5,
                      "preferred_working_glyph": "PP (provisional)"}, indent=2))


if __name__ == "__main__":
    main()
