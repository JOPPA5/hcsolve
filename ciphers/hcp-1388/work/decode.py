#!/usr/bin/env python3
"""Decode only frozen manual readings; verify immutable source bytes first."""
from pathlib import Path
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[1]
HASHES = {
    "address.jpg": "d3c26cd57ca7c97b7411a79c4bb4a541bfb3e1e01950955a5083428b2d85b210",
    "metadata.md": "0fe8e1bbfd37c67c15ca20121f0df054b5ffdd21fd43ecff4b8b3bef4a2b46f4",
    "picture.jpg": "69318983c3aa963477fc6b8786e0b171f67cbce47d146295bc5be3c359843215",
}
for name, digest in HASHES.items():
    assert hashlib.sha256((ROOT / "source" / name).read_bytes()).hexdigest() == digest, name

def shift(text):
    out = []
    for char in text:
        if "A" <= char <= "Z":
            out.append(chr((ord(char) - 65 - 1) % 26 + 65))
        elif "a" <= char <= "z":
            out.append(chr((ord(char) - 97 - 1) % 26 + 97))
        else:
            out.append(char)
    return "".join(out)

data = json.loads((ROOT / "work" / "transcript.json").read_text())
count = 0
for line in data["lines"]:
    chunks = re.split(r"(\{[^}]+\})", line)
    result = []
    for chunk in chunks:
        if chunk.startswith("{"):
            result.append(chunk)
        else:
            count += sum(c.isascii() and c.isalpha() for c in chunk)
            result.append(shift(chunk))
    print("".join(result))
print(f"\nFrozen cipher letters decoded: {count}")
print("Partial only: unresolved and cancelled ink remains on line 3.")
