#!/usr/bin/env python3
"""hcp-1340: verify source hashes, decode work/transcription.txt with work/key.json.
Run from the repo root: python3 -I ciphers/hcp-1340/work/decode.py"""
import hashlib, json, pathlib, sys, collections
d = pathlib.Path("ciphers/hcp-1340")
H = {"source/picture-large.jpg":"c9353991a24dc0ae4ca265efa338b53e859afb7911039b895aaab0a78ddbda41",
     "source/address-large.jpg":"39cb06bedd76c1dbf92f3f1bd8a679b28f8e0dee8fab944578886584051f2a1e",
     "work/hires/pc_hcp_21_pic.JPG":"2e135e720737677722770ce6e31b5f10d7d54a2d4cd9fffdaf05b7974c95c60c",
     "work/hires/pc_hcp_21_adr.JPG":"07e003861ef301492bbe26c0a6d9504a9a65bd5e422c4b1f74dfddceb0588e8a"}
for f, h in H.items():
    if hashlib.sha256((d/f).read_bytes()).hexdigest() != h:
        sys.exit("HASH MISMATCH " + f)
print("source hashes OK")
key = json.loads((d/"work/key.json").read_text())
# D is one sign for two sounds. This table only chooses d or t for each D in a word, in order;
# it cannot change any other letter. Any word with D that is missing is an error.
T = {"LIBSDE":"t","HASD":"t","DU":"d","KARDE":"t","GED":"t","DIR":"d","BISD":"t","WIDER":"d","GESUND":"d",
     "SCHADZ":"t","KELDED":"tt","UND":"d","MACHD":"t","NICHDS":"t","DOCH":"d","NEDZ":"t","BREUDCHEN":"t",
     "FREIDAG":"t","ISD":"t","NICHD":"t","DA":"d","DRIBERG":"t","DINSDAG":"dt","UNARDIG":"t","FESD":"t",
     "GEKU:SSD":"t","DEINEM":"d","DREUEN":"t","DEIN":"d"}
# Editorial step, kept apart from the decoding: reading of literal forms, also listed in SOLUTION.md.
EDIT = {"hae":"ha[b]e","keltet":"kältet","netz":"nett","breutchen":"bräutchen"}
n = collections.Counter()
lit, read = [], []
for line in (d/"work/transcription.txt").read_text().splitlines():
    if not line.strip() or line.startswith("#"): continue
    side, rest = line.split(" ", 1)
    out = []
    for w in rest.split():
        w, _, p = w.partition("|")
        s = w.split(".")
        n.update(s)
        for t in s:
            if t not in key: sys.exit("no key for " + t)
        j = "".join(s)
        choice = iter(T[j]) if "D" in s else None
        plain = "".join(next(choice) if t == "D" else key[t] for t in s)
        if choice is not None and next(choice, None) is not None: sys.exit("bad d/t choice for " + j)
        out.append((plain, p))
    lit.append(f"{side:11s} " + " ".join(w + p for w, p in out))
    read.append(f"{side:11s} " + " ".join(EDIT.get(w, w) + p for w, p in out))
print("LITERAL (key plus d/t choice only)")
print("\n".join(lit))
print("EDITED READING (only change: " + ", ".join(f"{k} > {v}" for k, v in EDIT.items()) + ")")
print("\n".join(read))
print("signs:", sum(n.values()), "distinct:", len(n))
print(dict(n.most_common()))
