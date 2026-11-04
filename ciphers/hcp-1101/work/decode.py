"""hcp-1101: verify source hashes, apply the 'red filter' (keep the R channel,
in which the red masking lattice turns near-white and the black ink stays dark),
save the filtered crop, and print the transcription read from it.
Run from the repo root:
  /Users/tomaspavuk/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 -I ciphers/hcp-1101/work/decode.py
"""
import hashlib, os, sys
D = os.path.join("ciphers", "hcp-1101")
HASHES = {
    "source/picture-large.jpg": "6e34d39d3870e18b1c1eb8debc1e50cb33b4cd4ec03afbca4427f0f7d10664cb",
    "source/address-large.jpg": "8efbb03fd7d28504cf2b00b165af1eab03bd729e236aba325211524190c92c1d",
    "work/hires/cpc_1898-02-11_CH_Basel_CH_Basel__pic.jpg": "db437831b0c3dc74f2f06256779f20c01ef29d1fe90a9b485b177df7aec47a87",
    "work/hires/cpc_1898-02-11_CH_Basel_CH_Basel__adr.jpg": "5bd193b00ce8818a75c61b3e7546e599aa19c86c91a211f5cfa5496c13c16a06",
}
ok = True
for p, h in HASHES.items():
    got = hashlib.sha256(open(os.path.join(D, p), "rb").read()).hexdigest()
    print(("OK  " if got == h else "BAD ") + p)
    ok &= got == h
if not ok:
    sys.exit("hash mismatch")
try:
    from PIL import Image
    im = Image.open(os.path.join(D, "work/hires/cpc_1898-02-11_CH_Basel_CH_Basel__pic.jpg"))
    im.crop((1860, 840, 3360, 1620)).split()[0].save(os.path.join(D, "work/redfilter.png"))
    print("wrote", os.path.join(D, "work/redfilter.png"), "(R channel = view through red glass)")
except ImportError:
    print("PIL missing: filtered image not written")

# Transcription read from work/redfilter.png (line by line, as written).
HIDDEN = [
    "Weñ der früche Morgen lächelt",
    "Weñ des Abends Kühle fächelt",
    "Immer-immer denk ich dein",
    "In der Mitternächte Hülle",
    "Selbst in meiner Träume Stille",
    "Mischt dein schönes Bild sich ein.",
]
OPEN = {"above": "das isch suber", "date": "11/II/98",
        "closing": "Mit freundl. Gruss", "signature": "H. B."}
print("\n[open] " + OPEN["date"] + "   " + OPEN["above"])
print("[hidden under red lattice]")
for l in HIDDEN:
    print("  " + l)
print("[open] " + OPEN["closing"] + "  " + OPEN["signature"])
print("\nnormalised: " + " / ".join(l.replace("ñ", "nn").replace("früche", "frühe") for l in HIDDEN))
