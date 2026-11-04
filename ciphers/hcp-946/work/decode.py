"""hcp-946: Roman numeral = position in the 25-letter German alphabet without J (I/J share 9)."""
import hashlib, sys, os
here = os.path.dirname(os.path.abspath(__file__)); root = os.path.dirname(here)
H = {"source/address-large.jpg": "e7969eecac1b85f6ea59a4b0cef6046b47c731cc63c846718e232a501f9d639a",
     "work/hires/cpc_1909-04-02_DE_Doberan_DE_Reddelich_ernagarbe-01_adr.jpg": "617fb88ed6a14921b6c090a4474a73a9ca06b5fd628ca4f308659e0a79e93f96"}
for p, h in H.items():
    d = hashlib.sha256(open(os.path.join(root, p), "rb").read()).hexdigest()
    if d != h: sys.exit("hash mismatch " + p)
ALPH = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
def rom(s):
    v = {"I": 1, "V": 5, "X": 10}; t = 0
    for i, c in enumerate(s):
        t += -v[c] if i + 1 < len(s) and v[c] < v[s[i + 1]] else v[c]
    return t
out = []
for line in open(os.path.join(here, "transcription.txt")):
    if line.startswith("#"): continue
    for tok in line.split():
        out.append(" " if tok == "/" else ALPH[rom(tok) - 1])
print("hashes OK"); print("".join(out).strip())
