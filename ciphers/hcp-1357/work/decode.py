#!/usr/bin/env python3
"""HCP 1357: verify capture hashes, apply Caesar -1, print the plaintext. Run from the repo root."""
import hashlib, json, pathlib, sys

BASE = pathlib.Path("ciphers/hcp-1357")
HASHES = {
    "source/picture-large.jpg": "0c3689af6fa50a7c3686c24eba179044e76c93b1776f0ecd94b7a4231b53dc75",
    "source/address-large.jpg": "1ac94f6183c57bcaa871a917f18c042e86ccfefb0e86706348be38daed1532b8",
    "work/hires/pc_hcp_38_pic.JPG": "cd414f196c8db63aa668b8857c11fc85543f911b597877b0c028b70171c1e154",
    "work/hires/pc_hcp_38_adr.JPG": "315ece753b346e5292c2ed96450161ede38bf050cb677023bc49742aad031f6b",
}
for name, want in HASHES.items():
    got = hashlib.sha256((BASE / name).read_bytes()).hexdigest()
    if got != want:
        sys.exit(f"HASH MISMATCH {name}: {got}")
print("source hashes OK")


def shift(ch):
    if not ch.isascii() or not ch.isalpha():
        return ch
    return chr((ord(ch.upper()) - 65 - 1) % 26 + 65)


data = json.loads((BASE / "work/transcription.json").read_text())
n = 0
for line in data["lines"]:
    n += sum(c.isalpha() for c in line)
    print(f"{line:26} {''.join(map(shift, line))}")
print("enciphered letters:", n)
print("clear:", " | ".join(data["clear_text"]))
