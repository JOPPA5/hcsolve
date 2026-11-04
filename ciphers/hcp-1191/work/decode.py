"""hcp-1191: decode work/transcription.txt with work/key.tsv after checking source hashes.
Run from the repository root: python3 ciphers/hcp-1191/work/decode.py"""
import hashlib, os, sys
D = os.path.dirname(os.path.abspath(__file__))
C = os.path.dirname(D)
HASHES = {
    "source/picture-large.jpg": "f2002e66239f24a12dc0a1d6f6763a5f8cd5e92bcb8a101b75e3d3ad08d25573",
    "source/address-large.jpg": "a398feb963ce2dce3abbaeaba7fd8ece26d484b86ceb0dafd4de052213f59ece",
    "work/hires/cpc_1907-09-07_USA_Coshocton,-Ohio_USA_Canal,-Lewisville,-Ohio__pic.jpg":
        "912f949f61bcc18148927e5675bb328c292c4196cb6a7a7efb6c2f6e488ac589",
}
for rel, h in HASHES.items():
    got = hashlib.sha256(open(os.path.join(C, rel), "rb").read()).hexdigest()
    if got != h:
        sys.exit(f"HASH MISMATCH {rel}: {got}")
print("source hashes OK")
key = {}
for ln in open(os.path.join(D, "key.tsv"), encoding="utf-8"):
    if ln.startswith("#") or not ln.strip():
        continue
    code, plain = ln.split("\t")[:2]
    key[code] = plain
special = {"[I]": "I", "[#]": ""}
out = []
for ln in open(os.path.join(D, "transcription.txt"), encoding="utf-8"):
    if ln.startswith("#") or not ln.strip():
        continue
    words = []
    for w in ln.split(" / "):
        s = ""
        for t in w.split():
            if t in special:
                s += special[t]
            elif t.isdigit():
                s += (" " if s else "") + t
            else:
                s += key[t]  # KeyError = sign not in key
        words.append(s)
    out.append(" ".join(words))
print("\n".join(out))
