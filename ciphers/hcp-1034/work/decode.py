#!/usr/bin/env python3
"""hcp-1034: decode the invented-symbol cipher on the picture side.
Run from repo root: python3 -I ciphers/hcp-1034/work/decode.py
Sign names are descriptive labels for the drawn glyphs (see SOLUTION.md)."""
import hashlib, os, sys
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
HASHES = {
 "source/picture-large.jpg": "447e7c60b4fe29eee505250a5aba5456948b4f8ae432004de6881ca59f0ae33b",
 "source/address-large.jpg": "df7b1be1ee5d8473f162ccd09a743a46df675bfa38b5b2c772298262c026f964",
 "work/hires/cpc_1904-09-05_DE_Munster_DE_Bremen__pic.jpg": "0306fa46f9af2250d23649cde9684f58437d494286c398e81516378c14e09c54",
 "work/hires/cpc_1904-09-05_DE_Munster_DE_Bremen__adr.jpg": "3fe4aa98e9663c012d82478e99429bd23437b14dc6749873f289052c074a54ec",
}
ok = True
for p, h in HASHES.items():
    got = hashlib.sha256(open(os.path.join(D, p), "rb").read()).hexdigest()
    print(("OK  " if got == h else "BAD ") + p); ok &= got == h
if not ok: sys.exit("hash mismatch")

KEY = {
 "TRI": "I",      # open triangle, no dot (capital I)
 "TRId": "i",     # triangle with dot
 "VTRd": "i",     # downward triangle with dot
 "H2": "n",       # two verticals + crossbar
 "H3": "m",       # three verticals + crossbar
 "SQ": "d",       # square / flat-bottomed box
 "D": "e",        # D-shape (hollow or inked-in)
 "OV": "c",       # narrow oval 0
 "L": "h",        # L / b-shape
 "XL": "f",       # crossed looped X
 "U": "u",        # u-shape (with or without mark above)
 "R": "r",        # r-shape
 "P": "l",        # P-shape
 "N": "b",        # N / V-with-hook zigzag
 "X": "a",        # small x / crossed loop
 "XG": "G",       # tall X (capital G)
 "S": "s",        # k-like sign (long s; S+Z = ß as in Kurrent)
 "Z8": "z",       # 8 / Kurrent z
 "THk": "k",      # circle or c with bar and hook mark
 "CX": "t",       # circle struck through diagonally
 "DAG": "v",      # double-dagger cross
}
# reading order; '/' word gap, '.' ',' and '-' punctuation as drawn
ROWS = [
 ("A", "TRI H2 SQ D H3 / TRId OV L / H3 TRId OV L / XL U R / SQ D TRId H2 D P TRId D N D"),
 ("B", "X OV* XL / H3 D R THk / S X H3 / THk D TRId CX / L D R Z8 P TRId OV L - N D SQ X H2 ."),
 ("orphan", "[THk]"),
 ("C", "THk D , / DAG D R / N P D TRId N D / VTRd OV L / H3 TRId CX / XG R U S Z8 / U H2 SQ"),
 ("D", "THk U S Z8"),
 ("E", "SQ D TRId H2 / CX R . / XL R TRId CX Z8 ."),
]
out = []
for name, row in ROWS:
    s = ""
    for t in row.split():
        if t == "/": s += " "
        elif t in ".,-": s += t   # '-' = joining dash drawn between herzlich and bedan. (review 1, finding 1)
        elif t == "[THk]": s += "[k]"
        elif t == "OV*": s += "u"   # same oval glyph as c; read u by word sense (Aufmerksamkeit)
        else: s += KEY[t]
    print(f"{name:7s} {s}")
    if name != "orphan": out.append(s)
plain = " ".join(out)
print("\nPLAINTEXT:", plain)
print("NORMALISED: Indem ich mich für deine liebe Aufmerksamkeit herzlich bedanke, verbleibe ich mit Gruß und Kuß dein tr[euer] Fritz.")
