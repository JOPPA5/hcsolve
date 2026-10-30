#!/usr/bin/env python3
"""hcp-1478: decode the transcription with the established key.

Run from the repo root:
    python3 -I ciphers/hcp-1478/work/decode.py

Key (plain -> cipher): letters e..x are swapped with the letter two places
away inside their block of four (efgh: e<->g, f<->h; ijkl; mnop; qrst; uvwx),
i.e. index XOR 2.  The block abcd is NOT XOR 2 on this card: it is a rotation
a->d, b->a, c->b, d->c (attested only by c->b in "sincerest" and by a,d in
"bathing", see SOLUTION.md).  y is unchanged; z is not attested.
"""
import hashlib, pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
HASHES = {
    "source/address-large.jpg": "ae612fe93d0e8a8717b8186229cac39f534c1473aba73099223258f5dba776c5",
    "source/picture-large.jpg": "9a950e0b4a81d222d019ed2944eba702abc6244f8ebfdf1d781bbe920574c194",
}
for rel, h in HASHES.items():
    got = hashlib.sha256((ROOT / rel).read_bytes()).hexdigest()
    if got != h:
        sys.exit(f"hash mismatch for {rel}: {got}")
print("source hashes OK")

# plain -> cipher
P2C = {"a": "d", "b": "a", "c": "b", "d": "c", "y": "y"}
A = "abcdefghijklmnopqrstuvwxyz"
for i in range(4, 24):
    P2C[A[i]] = A[i ^ 2]
C2P = {c: p for p, c in P2C.items()}
assert len(C2P) == len(P2C)

# Own transcription of the address side, line by line (lowercase = what the
# pen wrote; first glyph read as a capital R, see SOLUTION.md uncertainty 1;
# in line 6 the cursive w is written like "uo").
LINES = [
    "Rm oy mup",
    "adrfkpe",
    "ukrf",
    "qkpbgtgqr",
    "jmxg htmo",
    "rymwt",
    "jmxkpe",
]
SIGNATURE = "signature in clear, written 'Depgy'/'Pepgy'; interpreted as Peggy"


def dec(s):
    out = []
    for ch in s:
        lo = ch.lower()
        if lo in C2P:
            p = C2P[lo]
            out.append(p.upper() if ch.isupper() else p)
        elif lo.isalpha():
            out.append("?")
        else:
            out.append(ch)
    return "".join(out)


print("\nLiteral decryption, line by line:")
for l in LINES:
    print(f"  {l:12s} -> {dec(l)}")
print(f"  {'':12s}    {SIGNATURE}")

reading = " ".join(dec(l) for l in LINES)
# Line 6 has an extra leading glyph (r -> t) before 'ymwt' = 'your';
# shown in brackets in the reading.
reading = reading.replace("tyour", "[t]your")
# "bathing" depends on the abcd block, which is derived from this word itself
# (review 1, finding 1): mark it as tentative.
reading = reading.replace("bathing", "[bathing?]")
print("\nPlaintext:", reading, "- Peggy (signature as written: Depgy/Pepgy)")
