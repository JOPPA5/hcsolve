"""hcp-951: decode the A=1..Z=26 number substitution. Run from repo root:
   python3 -I ciphers/hcp-951/work/decode.py
"""
import hashlib, os, sys
D = os.path.dirname(os.path.abspath(__file__))
C = os.path.dirname(D)
HASHES = {
 "source/picture-large.jpg": "be0a4669784605923e74cdc9d080b216b5d66531a18f269423b0796b31ddd3cc",
 "source/address-large.jpg": "7e8ef07c905b57260e696026c4ab59646046caa2ff1c2b36f8aebafa3cd0298f",
 "work/hires/cpc_1940-01-05_DE__DE_Sturzbach__pic.jpg": "c565fcd1da98c1d8a2dd4f36600a97d7a549d1315bec6c0bda252865684a5241",
 "work/hires/cpc_1940-01-05_DE__DE_Sturzbach__adr.jpg": "a11e44fce99855b490e9ef1d3130c31741f00e47a57d4ebfc0e045f7fdffb918",
}
ok = True
for p, h in HASHES.items():
    got = hashlib.sha256(open(os.path.join(C, p), "rb").read()).hexdigest()
    print(("OK  " if got == h else "BAD ") + p)
    ok &= got == h
if not ok:
    sys.exit("hash mismatch")
KEY = {i: chr(64 + i) for i in range(1, 27)}  # 1=A ... 26=Z
out = []
for line in open(os.path.join(D, "transcription.txt"), encoding="utf-8"):
    line = line.strip()
    if not line or line.startswith("#"):
        continue
    words = []
    for grp in line.split(";"):
        if grp.strip().startswith("="):
            words.append(grp.strip()[1:]); continue
        nums = [int(x) for x in grp.replace(" ", "").split(",") if x]
        w = "".join(KEY[n] for n in nums)
        words.append(w)
    out.append(" ".join(words))
print("\n".join(out))
