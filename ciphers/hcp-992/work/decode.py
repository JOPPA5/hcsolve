"""hcp-992 decoder: checks source hashes, applies the key to work/transcription.txt,
and prints the full card text (plain Kurrent parts + deciphered parts)."""
import hashlib, os, sys
D = os.path.dirname(os.path.abspath(__file__))
C = os.path.dirname(D)
HASHES = {
 "source/picture-large.jpg": "17adec18c3717d90579855752b639736347170d4d25c075eef18cf44a52e2da9",
 "source/address-large.jpg": "d1a390ed0c3432118274d751039a457e41430e1f3cea69e97a46c166c7d8bed4",
 "work/hires/cpc_1903-12-04_DE_Munchen_DE_Eschersheim_kellermann-02_pic.jpg": "358546e2969195c870b7fd121453e55d2928dce17aab53315216c71becb7fc1f",
 "work/hires/cpc_1903-12-04_DE_Munchen_DE_Eschersheim_kellermann-02_adr.jpg": "539ce27ac40433e3e90574ff2c892dd988fc53d45a6ab293eb0a4bed08b4dce3",
}
for p, h in HASHES.items():
    got = hashlib.sha256(open(os.path.join(C, p), "rb").read()).hexdigest()
    if got != h:
        sys.exit("HASH MISMATCH " + p)
print("source hashes OK")
KEY = {"1":"L","2":"N","3":"M","4":"E","5":"S","6":"B","7":"T","8":"H","9":"G",
       "A9":"A","A9:":"Ä","U":"U","U:":"Ü","V":"D","I":"Z","i.":"I","c":"C",
       "r":"R","K":"K","2*":"[H]"}
# 2* = last sign of the signature: a 2-shape with a filled blob on top, or a cramped 8 with a filled upper
# loop (this writer often fills the upper loop of 8). Read H (Erich), supported by sister hcp-993 signed Erich
# with 8; printed in brackets because the shape alone does not decide it (review 1, finding 1).
def dec(s):
    out = []
    for w in s.split(" / "):
        t = []
        for tok in w.split():
            if tok in KEY: t.append(KEY[tok])
            elif tok == "-": t.append("")      # line-end hyphen
            else: t.append(" " + tok)
        out.append("".join(t))
    return " ".join(out)
lines = {}
for ln in open(os.path.join(D, "transcription.txt"), encoding="utf-8"):
    if ln.startswith("C"):
        k, v = ln.split(":", 1); lines[k] = dec(v.strip())
for k in sorted(lines):
    print(k + ": " + lines[k])
ntok = 0
for ln in open(os.path.join(D, "transcription.txt"), encoding="utf-8"):
    if ln.startswith("C"):
        ntok += sum(1 for t in ln.split(":", 1)[1].split() if t in KEY)
print("cipher tokens:", ntok, "distinct signs:", len(KEY))
print()
print("Full card (picture side), Kurrent parts plain, deciphered parts in capitals:")
print("München 4. Dez. 03.")
print(lines["C1"])
print("(hatte dir " + lines["C2"] + " aufgeschrieben) Wollte dir noch schnell mitteilen, daß du")
print("Herrn(?) zum 7. gratulierst, habe versehentlich der letzten Karte u. Paket falsche Adresse")
print("gegeben, bin kerngesund. Morgen schreibe ich Brief. Grüße bitte alle Lieben recht herzlich.")
print(lines["C3"])
print(lines["C4"])
