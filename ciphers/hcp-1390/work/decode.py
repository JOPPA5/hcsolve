#!/usr/bin/env python3
"""Hash immutable sources; decode the manual transcription of the message body (Caesar -1)."""
import hashlib
import json
from pathlib import Path
import string

HERE = Path(__file__).resolve().parent
BASE = HERE.parent
EXPECTED = {
    "address.jpg": "433535388d513e07064ac4e210a19ccb9133a293b1f305dafc59ad3031dfb6d9",
    "metadata.md": "480089de07074e297c34abe280e6aecb3181db23fddb8009fe2f6fa0d3ef80ad",
    "picture.jpg": "3864dfdae8e00b501b85d9e494022a727d18f3f610f0a1f02c1d486cb474deda",
}
for name, expected in EXPECTED.items():
    actual = hashlib.sha256((BASE / "source" / name).read_bytes()).hexdigest()
    if actual != expected:
        raise SystemExit(f"Source hash mismatch: {name}")

alpha = string.ascii_lowercase
key = dict(zip(alpha + alpha.upper(), (alpha[-1:] + alpha[:-1]) + (alpha[-1:] + alpha[:-1]).upper()))
inverse = {plain: cipher for cipher, plain in key.items()}
data = json.loads((HERE / "transcription.json").read_text())
count = 0
print("Body text complete (two closing groups unread); source hashes verified; manual transcript, not image recognition")
print("Cipher alphabet: ABCDEFGHIJKLMNOPQRSTUVWXYZ")
print("Plain alphabet:  ZABCDEFGHIJKLMNOPQRSTUVWXY")
for line in data["lines"]:
    raw = line["cipher"]
    decoded = ''.join(key.get(c, c) for c in raw)
    assert ''.join(inverse.get(c, c) for c in decoded) == raw
    count += sum(c in key for c in raw)
    print(f"{line['id']}: {raw} -> {decoded}")
    if "unresolved_before" in line:
        print("  UNRESOLVED BEFORE: " + line["unresolved_before"])
    if "unresolved_after" in line:
        print("  UNRESOLVED AFTER: " + line["unresolved_after"])
print(f"Confirmed alphabetic positions: {count}")
print("This command reproduces the deciphered body only; the two closing groups are printed as notes, not decoded.")
