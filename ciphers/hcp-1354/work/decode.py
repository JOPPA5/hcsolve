#!/usr/bin/env python3
"""hcp-1354: verify source hashes, then decode work/transcription.json with Caesar -1."""
import hashlib, json, pathlib, sys
base = pathlib.Path(__file__).resolve().parent.parent
for line in (base / "work/source-sha256.txt").read_text().splitlines():
    digest, rel = line.split(None, 1)
    rel = rel.replace("ciphers/hcp-1354/", "")
    if hashlib.sha256((base / rel).read_bytes()).hexdigest() != digest:
        sys.exit("HASH MISMATCH: " + rel)
print("source hashes OK")
def dec(s):
    return "".join(chr((ord(c.upper()) - 65 - 1) % 26 + 65) if c.isalpha() else c for c in s)
t = json.loads((base / "work/transcription.json").read_text())
n = 0
for line in t["lines"]:
    print(" ".join(line).ljust(30), "=>", " ".join(dec(w) for w in line))
    n += sum(c.isalpha() for w in line for c in w)
print("plain, not enciphered:", t["plain_not_enciphered"])
print(n, "cipher letters, all decoded by one key (Caesar -1)")
