"""hcp-1033 decoder: 5x5 number square (I=J omitted, no J on card), rows numbered in reverse.

Run from repo root:  python3 -I ciphers/hcp-1033/work/decode.py
"""
import hashlib, os, re, sys

D = os.path.dirname(os.path.abspath(__file__))
C = os.path.dirname(D)

HASHES = {
    "source/picture-large.jpg": "6bc393ce0239bbd5820f9594cdba595e90a9f39f5d897fcd6870f409e18c8bd3",
    "source/address-large.jpg": "93791c060d2743df546cc4aa354912a9961b6e3970cd0ece0febf6f48e64d695",
    "work/hires/cpc_1906-08-23_DE_Munsterlager_DE_Ahlden__pic.jpg": "cca3595e874650ad8806bb799dd5d757e9935237a75442ed7df940e684fb4fe5",
    "work/hires/cpc_1906-08-23_DE_Munsterlager_DE_Ahlden__adr.jpg": "989e57e5725f385b898d69b76b75ab1c3d9250ce37c5a0b4633c89e49971fa42",
}
ok = True
for p, h in HASHES.items():
    got = hashlib.sha256(open(os.path.join(C, p), "rb").read()).hexdigest()
    print(("OK   " if got == h else "FAIL ") + p)
    ok &= got == h
if not ok:
    sys.exit("source hash mismatch")

# Alphabet without J, in blocks of five; block k (A-E, F-K, L-P, Q-U, V-Z) gets numbers 21-25, 16-20, 11-15, 6-10, 1-5.
ALPHA = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
KEY = {}
for i, ch in enumerate(ALPHA):
    row, col = divmod(i, 5)
    KEY[(4 - row) * 5 + col + 1] = ch
UML = {"A": "Ä", "O": "Ö", "U": "Ü"}

print("\nKey:", " ".join(f"{n}={KEY[n]}" for n in sorted(KEY)))
print()
for line in open(os.path.join(D, "transcription.txt"), encoding="utf-8"):
    line = line.rstrip("\n")
    if not line.strip() or line.startswith("#"):
        if line.startswith("# postscript"):
            print("[postscript]")
        continue
    out = []
    for tok in re.findall(r'\{?\d+\}?"?|[-!,=:.]', line):
        m = re.fullmatch(r'\{?(\d+)\}?("?)', tok)
        if m:
            ch = KEY[int(m.group(1))]
            if m.group(2):
                ch = UML[ch]
            out.append(ch.lower())
        elif tok == "-":
            out.append(" ")
        elif tok == ".":
            continue
        elif tok in "=:":
            out.append("=")
        else:
            out.append(tok)
    print(re.sub(r" +", " ", "".join(out)).strip())
