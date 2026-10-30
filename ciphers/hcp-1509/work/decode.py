"""Decode hcp-1509 (pc_hcp_190). Run from the repo root:
    python3 -I ciphers/hcp-1509/work/decode.py
Checks source hashes, then decodes work/transcription.txt with work/key.json."""
import hashlib, json, os, sys
D = os.path.join("ciphers", "hcp-1509")
HASHES = {
    "source/address-large.jpg": "349b300f023739875cb7eb004d4569ca86bbe28970d5ff9da1f1d469d0419a1c",
    "source/picture-large.jpg": "f0fb5c3dd8d00c2bf0b9cfb4050f12f582f3319c9686c7f02bf5c57eede79588",
    "source/metadata.md": "222e61fe670a6eec2f6f11a388e23a08abb9411859846a2d2fcb06056c8303c4",
}
ok = True
for rel, h in HASHES.items():
    got = hashlib.sha256(open(os.path.join(D, rel), "rb").read()).hexdigest()
    print(("OK  " if got == h else "BAD ") + rel)
    ok &= got == h
if not ok:
    sys.exit("source hash mismatch")
key = json.load(open(os.path.join(D, "work", "key.json"), encoding="utf-8"))
n = 0
unknown = []
print()
for line in open(os.path.join(D, "work", "transcription.txt"), encoding="utf-8"):
    line = line.rstrip("\n")
    if line.startswith("# PLAIN"):
        print("[plain] " + line.split(":", 1)[1].strip())
        continue
    if not line.strip() or line.startswith("#"):
        continue
    out = []
    for t in line.split():
        if t == "x":
            out.append(" ")
        elif t.startswith("#"):
            out.append(t[1:])
        elif t in key:
            out.append(key[t]); n += 1
        else:
            out.append("?"); unknown.append(t)
    print("".join(out).strip().upper())
print()
print(f"cipher signs decoded: {n}; unknown tokens: {unknown or 'none'}")
