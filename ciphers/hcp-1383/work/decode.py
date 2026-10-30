#!/usr/bin/env python3
"""Check source hashes, then decode the manual transcription (Caesar -1). Run from the repo root."""
import datetime, hashlib, json, re, string
from pathlib import Path
BASE = Path(__file__).resolve().parent.parent
EXPECTED = {
    "source/picture-large.jpg": "5591bb458c1bd997ae3107a7dbdeeb4eb5b665638259ea928ef4e13eff758990",
    "source/address-large.jpg": "2e1784d07eb22fd0c139c0ddc7303a2bc34b0e5b31b9889735f52f0a9bf8058c",
    "work/hires/pc_hcp_64_pic.JPG": "08a94e4e178da6e157397cf04bd9f69d072f1d5c4877ffdabdba3f13a9bd9133",
    "work/hires/pc_hcp_64_adr.JPG": "5e836859f12b01395bdba07f8082b26594c95811bf4df3b04ab25aa1ce261d07",
}
for name, want in EXPECTED.items():
    if hashlib.sha256((BASE / name).read_bytes()).hexdigest() != want:
        raise SystemExit("Source hash mismatch: " + name)
print("Source hashes OK")
assert datetime.date(1907, 9, 23).strftime("%A") == "Monday"
low, up = string.ascii_lowercase, string.ascii_uppercase
table = str.maketrans(low + up, up[-1] + up[:-1] + up[-1] + up[:-1])
data = json.loads((Path(__file__).resolve().parent / "transcription.json").read_text())
print("Heading (plain):", data["plain_heading"])
n = lit = 0
for line in data["lines"]:
    out = []
    for part in re.split(r"(\[[^\]]*\])", line):
        if part.startswith("["):
            out.append(part); lit += sum(c.isalpha() for c in part)
        else:
            out.append(part.translate(table)); n += sum(c.isalpha() for c in part)
    print(f"{line:32} -> {''.join(out)}")
print("Date (plain, before last word):", data["plain_date_before_last_word"])
print(f"Shifted letters: {n}; literal abbreviation letters: {lit}")
