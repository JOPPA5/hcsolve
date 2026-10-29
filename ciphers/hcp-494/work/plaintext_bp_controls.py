"""Original brown-text B/P controls; manual selections, no ink reconstruction."""
from pathlib import Path
import hashlib
import json
from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parents[1]
SPECS = [
    ("target", "0004", (2070, 2010, 2240, 2130), (10, 35), 2,
     "Cipher pair: BB or PP? (2x)"),
    ("proposition-initial", "0004", (575, 1350, 710, 1490), (370, 35), 2,
     "P in Proposition, original text (2x)"),
    ("brunsvicense-initial", "0004", (1370, 1160, 1520, 1300), (730, 35), 2,
     "B in Brunsvicense, original text (2x)"),
    ("breviat-initial", "0003", (1590, 1690, 1750, 1810), (1080, 35), 2,
     "b in breviat, original text (2x)"),
    ("proposition-word", "0004", (550, 1320, 1120, 1500), (10, 365), 1,
     "Word context: Proposition (1x)"),
    ("brunsvicense-word", "0004", (1360, 1130, 1980, 1310), (730, 365), 1,
     "Contrary control: Brunsvicense (1x)"),
    ("portrait-word", "0003", (840, 1400, 1280, 1570), (10, 620), 1,
     "Another P form: Portrait (1x)"),
    ("abfertigung-word", "0003", (660, 2880, 1240, 3070), (730, 620), 1,
     "Another b form: abfertigung (1x)"),
]


def main():
    out = Image.new("RGB", (1420, 980), "white")
    draw = ImageDraw.Draw(out)
    records = []
    for name, page, bounds, xy, scale, label in SPECS:
        source = ROOT / f"source/full/{page}.jpg"
        crop = Image.open(source).convert("RGB").crop(bounds)
        crop.save(ROOT / f"work/bp-{name}.png")
        if scale != 1:
            crop = crop.resize((crop.width * scale, crop.height * scale), Image.Resampling.NEAREST)
        x, y = xy
        draw.text((x, y - 25), label, fill="black")
        out.paste(crop, (x, y))
        records.append({"name": name, "source": str(source.relative_to(ROOT)),
                        "source_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
                        "box": bounds, "sheet_scale": scale,
                        "scaling": "nearest-neighbor duplication only" if scale != 1 else "native pixels"})
    draw.text((10, 865), "P in Proposition also has a small lower loop. B/b controls resemble the pair too: PP is possible, not established.", fill="black")
    draw.text((10, 895), "Plain-text letter forms need not equal cipher-capital forms. No contrast change, ink removal or reconstructed stroke.", fill="black")
    draw.text((10, 925), "Key 255 remains BB=z and PP=n. If PP is correct, the key gives undertanin; BB still gives undertazin.", fill="black")
    out.save(ROOT / "work/plaintext-bp-comparison.png")
    (ROOT / "work/plaintext-bp-controls.json").write_text(json.dumps({
        "status": "new visual comparison, not independent adjudication",
        "prior_exposure": "The proposed undertanin was already known; this is not blind discovery of that word.",
        "inference": "Proposition supplies an original-text P with a lower loop; similar original B/b forms prevent a unique classification.",
        "limits": "Manual palaeographic judgments; same letter body, not a proved repeated cipher PP; cipher-case conventions are not established.",
        "crops": records,
    }, indent=2) + "\n")


if __name__ == "__main__":
    main()
