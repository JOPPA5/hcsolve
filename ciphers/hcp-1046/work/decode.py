"""Decode hcp-1046 (number substitution, A=2 ... Z=26 without J). Run from repo root: python3 -I ciphers/hcp-1046/work/decode.py"""
import hashlib, pathlib, re, sys
base = pathlib.Path(__file__).resolve().parent.parent
HASHES = {
    "source/picture-large.jpg": "974e81789905fdd15891b8ab4de74e72cfbffd37d555cac0ca434f1ea2dc8768",
    "source/address-large.jpg": "93c8352dc4d4a454eaadd82d0175cecca9584df61aa461b6acb554439856d0a7",
    "work/hires/cpc_1909-07-13_DE_-(Schlesien)_DE_Hier_fritzlehmann-04_adr.jpg": "a9562e5fc276a605d5cca4084d536ebbfd651e2539f8b8b8a29c4c36e8fc5161",
}
for rel, h in HASHES.items():
    got = hashlib.sha256((base / rel).read_bytes()).hexdigest()
    if got != h:
        sys.exit(f"hash mismatch: {rel}")
print("source hashes OK")
alpha = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # no J
KEY = {str(i + 2): c for i, c in enumerate(alpha)}
UML = {"A": "Ä", "O": "Ö", "U": "Ü"}
words = []
for line in (base / "work/transcription.txt").read_text().splitlines():
    if line.startswith("#") or not line.strip():
        continue
    for w in line.split("-"):
        toks = [t for t in w.strip().split(".") if t.strip()]
        if not toks:
            continue
        out = ""
        for t in toks:
            t = t.strip()
            m = re.fullmatch(r"(\d+)(x?)(:?)", t)
            if not m:
                sys.exit(f"bad token {t!r}")
            c = KEY[m.group(1)]
            if m.group(3):
                c = UML[c]
            out += c
        words.append(out)
print(" ".join(words))
