"""HCP 1800: decode the numbered-Pigpen transcription. Run from repo root:
python3 -I ciphers/hcp-1800/work/decode.py"""
import hashlib, pathlib, sys
D = pathlib.Path(__file__).resolve().parent.parent
HASHES = {
 "source/address-large.jpg": "35939ad6ea5f8dba7ecb619b85c57c0482d171bd41fa959ae6a9ec4bd553100d",
 "source/picture-large.jpg": "035ea6ea4c7bb2acbe0a696dd321cad9bc585b9983b5851cee067d7f3a81ad93",
}
for rel, h in HASHES.items():
    got = hashlib.sha256((D / rel).read_bytes()).hexdigest()
    if got != h:
        sys.exit(f"hash mismatch: {rel}")
ORDER = ["BR", "B", "BL", "R", "C", "L", "TR", "T", "TL"]
ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def dec(tok):
    tok = tok.rstrip("?")
    shape, n = tok[:-1], int(tok[-1])
    return ALPHA[(n - 1) * 9 + ORDER.index(shape)]
out = []
for line in (D / "work/transcription.txt").read_text().splitlines():
    if not line.strip() or line.startswith("#"):
        continue
    words = [w for w in line.split("  ") if w.strip()]
    out.append(" ".join("".join(dec(t) for t in w.split()) for w in words))
print("source hashes OK")
print("\n".join(out))
