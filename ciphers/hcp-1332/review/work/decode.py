#!/usr/bin/env python3
"""Reviewer's independent decoder for hcp-1332. Own table, no import from work/decipher.py.
Prints the decode of the solver's transcription, then with the reviewer's two pixel corrections.
Run from the repo root: python3 -I ciphers/hcp-1332/review/work/decode.py"""
import pathlib, re
D = pathlib.Path(__file__).resolve().parents[2]
T = {"M":"a","D":"b","T":"c","L":"d","B":"e","F":"f","S":"h","Q":"i","Z":"j","V":"l","P":"m","H":"n",
     "X":"o","9":"p","R":"r","C":"s","A":"t","O":"u","W":"v","5":"z"}
def word(w):
    o = ""
    for i, c in enumerate(w):
        if c == "U":
            o += "q" if w[i+1:i+2] == "O" and w[i+2:i+3] in ("B","Q","M") else "g"
        elif c in T: o += T[c]
        elif c == "^": o += "'"
        elif c == "~": o += "~"
        else: o += c
    return o
L = [l.split(" ",1) for l in (D/"work/transcription.txt").read_text().splitlines() if l and l[0] != "#"]
def show(rows):
    n = sum(ch.isalnum() for _, b in rows for ch in b)
    print(n, "signs"); print("\n".join(f"{t:4}{' '.join(word(w) for w in b.split())}" for t, b in rows))
show(L)
FIX = {"A7": ("M AXRRB,", "M AXRRBC,"), "P1": ("SM TMDBTM", "M PQHSM TMDBTM")}
L2 = [[t, b.replace(*FIX[t]) if t in FIX else b] for t, b in L]
print("\nwith corrections A7, P1:"); show(L2)
