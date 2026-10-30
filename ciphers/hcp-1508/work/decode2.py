#!/usr/bin/env python3
"""hcp-1508: verify source hashes, decode work/transcription-v2.txt.

Key = Leah Doane family key (hcp-1506/1507). Every value in KEY is attested
on this card (14=K twice: LOOK, AWAKEN). 5=V is not in KEY because V is
written here only as a letter-shaped sign. Unattested numbers stay in
brackets, e.g. [2].
"""
from pathlib import Path
import hashlib, json
base = Path(__file__).resolve().parents[1]
KEY = {1:"M",3:"E",4:"R",6:"L",7:"O",8:"T",9:"P",10:"S",11:"F",12:"A",
       13:"G",14:"K",15:"B",16:"U",17:"I",18:"D",20:"C",21:"W",22:"H",
       24:"X",25:"N",26:"Y"}
assert len(set(KEY.values())) == len(KEY)
exp = json.loads((base/"work/source-sha256.json").read_text())
for name, digest in exp.items():
    got = hashlib.sha256((base/"source"/name).read_bytes()).hexdigest()
    assert got == digest, f"hash mismatch: {name}"
print("source hashes OK:", ", ".join(sorted(exp)))
nums = mapped = signs = 0
out = []
for line in (base/"work/transcription-v2.txt").read_text().splitlines():
    if not line.strip() or line.startswith("#"):
        continue
    words = []
    for w in line.split(" / "):
        w = w.strip()
        if w.startswith("{"):
            words.append(w[1:-1]); continue
        s = ""
        for t in w.split("."):
            if t.startswith("["):
                signs += 1; s += t[1:-1]
            else:
                nums += 1
                if int(t) in KEY:
                    mapped += 1; s += KEY[int(t)]
                else:
                    s += f"[{t}]"
        words.append(s)
    out.append(" ".join(words))
print("\n".join(out))
print(f"numeral signs: {nums}, mapped: {mapped}, unmapped: {nums-mapped}; "
      f"non-numeral letter signs: {signs}")
