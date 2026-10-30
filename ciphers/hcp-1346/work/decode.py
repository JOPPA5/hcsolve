#!/usr/bin/env python3
"""HCP 1346: decode work/transcription.txt with work/key.json; verify source hashes. Run from repo root."""
import hashlib, json, pathlib, sys
D = pathlib.Path("ciphers/hcp-1346")
H = {"source/picture-large.jpg": "d50dd1b528d106e67a764a6d7909105e1d8cdb68a1e455cc948597f788a12746",
     "source/address-large.jpg": "02b0dfc727ef49e1e6ddfab72657eac8a0f94574f2ff617a7a1c207cf3268c0f",
     "work/hires/pc_hcp_27_pic.JPG": "9e5da7a3a352092fffd0cd13004eabc0143d9b5009c1cccf76357b6f0da825c0",
     "work/hires/pc_hcp_27_adr.JPG": "1dc83b44ccd5aaadf8c6dc8458ecada2d0b87556a65f8207cdb32803e8448fd1"}
for f, h in H.items():
    if hashlib.sha256((D / f).read_bytes()).hexdigest() != h:
        sys.exit("HASH MISMATCH " + f)
print("source hashes OK")
key = json.loads((D / "work/key.json").read_text())
n = doubt = emended = 0
notes = []
for line in (D / "work/transcription.txt").read_text().splitlines():
    if line.startswith("#") or not line.strip():
        continue
    tag, body = line.split(":", 1)
    words = []
    for w in body.split("|"):
        out = lit = ""
        for t in w.split():
            n += 1
            doubt += t.endswith("~")
            written, _, read = t.rstrip("~").partition("=")
            emended += bool(read)
            out += key[read or written].split("/")[0].lower()
            lit += key[written].split("/")[0].lower()
        words.append(out)
        if lit != out:
            notes.append(f"{tag} emended: card has {lit}, read {out}")
    print(tag, " ".join(words))
print(*notes, sep="\n")
print(f"{n} signs, {doubt} marked ~, {emended} emended, 0 unkeyed")
