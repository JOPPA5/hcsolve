#!/usr/bin/env python3
"""HCP 1388: verify source hashes, decrypt the full manual transcription (Caesar, plain = cipher - 1)."""
from pathlib import Path
import hashlib, json, re

ROOT = Path(__file__).resolve().parents[1]
HASHES = {
    "address.jpg": "d3c26cd57ca7c97b7411a79c4bb4a541bfb3e1e01950955a5083428b2d85b210",
    "metadata.md": "0fe8e1bbfd37c67c15ca20121f0df054b5ffdd21fd43ecff4b8b3bef4a2b46f4",
    "picture.jpg": "69318983c3aa963477fc6b8786e0b171f67cbce47d146295bc5be3c359843215",
}
for name, digest in HASHES.items():
    got = hashlib.sha256((ROOT / "source" / name).read_bytes()).hexdigest()
    assert got == digest, f"hash mismatch: {name}"
print("source hashes OK")

def dec(s):
    out = []
    for part in re.split(r"(\[[^\]]*\])", s):
        if part.startswith("["):
            out.append(part); continue
        out.append("".join(chr((ord(c) - (65 if c.isupper() else 97) - 1) % 26 + (65 if c.isupper() else 97))
                           if c.isascii() and c.isalpha() else c for c in part))
    return "".join(out)

data = json.loads((ROOT / "work" / "transcript_full.json").read_text())
n = 0
for line, exp in zip(data["lines"], data["expected_plaintext"]):
    p = dec(line)
    assert p == exp, (p, exp)
    n += sum(c.isalpha() for c in re.sub(r"\[[^\]]*\]", "", line))
    print(f"{line:28s} -> {p}")
print(f"cipher letters decrypted: {n}")
print("Reading: My dearest, thanks for letter, it was fine. [**] M xx (kisses) from your own girl.")
