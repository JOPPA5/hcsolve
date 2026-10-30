#!/usr/bin/env python3
"""Validate immutable source hashes, then decode manually frozen excerpts only."""
from pathlib import Path
import hashlib
import json
import string

ROOT = Path(__file__).resolve().parents[1]
HASHES = {
    "address.jpg": "1a63d151325acfc141d27e2fe6a57ef12d4eb25ec432de4669feab6a0835453f",
    "metadata.md": "59e661cada67d8171fe904dee8827909659b3c3042314f53a1a6460abb174576",
    "picture.jpg": "95dd2ce6bbd091bca21ce96e2754622309f8d8e6448d5cb57a8f51e95403dbee",
}
for name, digest in HASHES.items():
    assert hashlib.sha256((ROOT / "source" / name).read_bytes()).hexdigest() == digest, name

def decrypt(text):
    result = []
    for ch in text:
        alphabet = string.ascii_uppercase if ch.isupper() else string.ascii_lowercase
        result.append(alphabet[(alphabet.index(ch) - 1) % 26] if ch in string.ascii_letters else ch)
    return "".join(result)

data = json.loads((ROOT / "work/transcription.json").read_text())
count = 0
for row in data["excerpts"]:
    plain = decrypt(row["ciphertext"])
    assert plain == row["plaintext"], row
    count += sum(ch in string.ascii_letters for ch in row["ciphertext"])
    print(f"L{row['line']}: {plain}")
assert count == 44
print(f"PARTIAL: {count} frozen letters; several groups in message lines 3-7 are unresolved (see transcription.json unfrozen).")
print("This command validates a manual transcript, not image pixels or a whole-card solution.")
