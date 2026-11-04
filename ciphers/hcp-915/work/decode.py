"""hcp-915: decode the Ogham transcription with the standard Ogham table and check source hashes.
Run from repo root:  python3 -I ciphers/hcp-915/work/decode.py"""
import hashlib, os, sys
D = os.path.dirname(os.path.abspath(__file__)); C = os.path.dirname(D)
H = {"source/picture-large.jpg": "18269f7abc1b9fb98e6a701250c7242d6111fd0a7d41c077f5e3db04fcb699ee",
     "source/address-large.jpg": "d185a780cd06a9c4faa40ed606c4e86a6bee841ed4e46b16c52a5c1a09a00bf0",
     "work/hires/cpc_--_IE_____pic.jpg": "dd2b3d0de3450e57267688992b1ff834228bb0131031b0494d4e9c08b7d7b186",
     "work/hires/cpc_--_IE_____adr.jpg": "1a6fcb4c4ae2a28c3a3e244b19e6dd52026b9805dadd952bb06b84f4d9852b3c"}
for p, h in H.items():
    got = hashlib.sha256(open(os.path.join(C, p), "rb").read()).hexdigest()
    if got != h: sys.exit("hash mismatch: " + p)
# standard Ogham aicmi (horizontal writing: B-aicme below, H-aicme above, M-aicme slanted across, vowels straight across)
T = {"B": "b l f s n".split(), "H": "h d t c q".split(), "M": "m g ng z r".split(), "X": "a o u e i".split()}
VOW = {"a": "á", "o": "ó", "u": "ú", "e": "é", "i": "í"}
line = [l for l in open(os.path.join(D, "transcription.txt"), encoding="utf-8") if not l.startswith("#")][0].split()
out, lit = "", ""
for g in line:
    if g == ":": out += " "; lit += " "; continue
    if g == ".": out += "."; lit += "."; continue
    base = g.rstrip("^'")
    ch = "p" if base == "P" else T[base[0]][int(base[1:]) - 1]
    lit += ch
    if g.endswith("^"): ch += "h"          # dot of lenition -> modern 'h' spelling
    if g.endswith("'"): ch = VOW[ch]
    out += ch
print("Ogham, letter for letter :", lit)
print("Ogham, with marks        :", out)
print("Ogham groups decoded     :", sum(1 for g in line if g not in ":."), "letters,", line.count(":"), "separators,", line.count("."), "final dot")
# The next line is NOT computed: it is the solver's manual reading of the unenciphered Gaelic-script line, kept for comparison.
print("Gaelic-script line (manual reading, plain writing, not computed): Taḃair ḋom póᵹ  = Tabhair dom póg")
print("Standard Irish           : Tabhair dom póg.  (Ogham first letter written as D = 2 H-strokes; T would be 3)")
