#!/usr/bin/env python3
"""hcp-1056: decode the digit groups with the vowel-digit key (partial reading).
Run from repo root:  python3 -I ciphers/hcp-1056/work/decode.py
Digits stand for letters; Kurrent letters written between digits are plaintext.
Transcription tokens: digits, or [x] for a plain Kurrent letter/ligature as read.
"""
import hashlib, pathlib, re

D = pathlib.Path(__file__).resolve().parent.parent
HASHES = {
    "source/picture-large.jpg": "6a6cc80ba7dafb6fb11341fd2eb527a15b8a8259f51f791958da894061b558e4",
    "source/address-large.jpg": "40baf7f55d64aad4be7003792d25b24b110c04a4b8ca86bd8b9658a1bc3718d0",
}
for p, h in HASHES.items():
    got = hashlib.sha256((D / p).read_bytes()).hexdigest()
    print(("OK  " if got == h else "BAD ") + p)

KEY = {"1": "a", "2": "e", "3": "i", "4": "o", "5": "u", "6": "l",
       "7": "n", "8": "m", "9": "r", "0": "s"}

GROUPS = [
    ("Habe diser Tage um", "[k]49[ch]50 59615[b]"),   # [ch]: tall double sign, read as Kurrent ch (uncertain)
    ("", "237[g]2[g]2[b]27"),
    ("und werde es Euch gleich mitteilen ... | Ich", "[w]19 [d]3029 [T]1[g]2"),
    ("", "15[f] [d]28 83370[t]29"),
    ("", "837[d]. {778} [stuf]27."),
]

def dec(s):
    out, i = [], 0
    for tok in re.findall(r"\{[^}]*\}|\[[^\]]*\]|\d|[^\d\[{]", s):
        if tok.startswith("{"):
            out.append(tok[1:-1])
        elif tok.startswith("["):
            out.append(tok[1:-1])
        elif tok.isdigit():
            out.append(KEY[tok])
        else:
            out.append(tok)
    return "".join(out)

for ctx, g in GROUPS:
    print(f"{ctx:45s} {g:40s} -> {dec(g)}")
