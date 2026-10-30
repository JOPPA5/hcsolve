"""HCP 1477: decode work/transcription.txt with work/key.json; verify source hashes.
Run from repo root:  python3 -I ciphers/hcp-1477/work/decode.py"""
import hashlib, json, pathlib, sys
D = pathlib.Path(__file__).resolve().parent.parent
H = {"source/picture-large.jpg": "5963fb01036ddb43226b060d41d29cfdb6b92ad143cea3a481659f804f5bb715",
     "source/address-large.jpg": "2f2818f5d5532bbcd9389beb9f557c311376ecfac5c10d38f53d225a5bda77f9",
     "source/metadata.md": "3afcce1aa9546b694e365164b837ea96a15dc939dd107282511dae0ecc4f1343"}
for p, h in H.items():
    got = hashlib.sha256((D / p).read_bytes()).hexdigest()
    if got != h: sys.exit(f"HASH MISMATCH {p}")
print("source hashes OK")
key = json.loads((D / "work/key.json").read_text())
vow = set("aeiouåäö")
lines = [l for l in (D / "work/transcription.txt").read_text().splitlines() if l and not l.startswith("#")]
n = 0
for l in lines:
    out = []
    for w in l.split():
        s = ""
        for c in w:
            if c in vow: s += c
            elif c in key: s += key[c]
            else: sys.exit(f"unknown sign {c!r}")
            n += 1
        out.append(s)
    print(" ".join(out))
print(f"[{n} signs decoded, {len(lines)} lines]")
