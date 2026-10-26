#!/usr/bin/env python3
"""Reviewer's independent A1Z26 decoder for hcp-1492 (does not import solver code)."""
import re, sys
from collections import defaultdict
path = sys.argv[1]
seen = defaultdict(set); total = 0
for line in open(path, encoding="utf-8"):
    if line.startswith("#") or not line.strip():
        continue
    out = []
    for tok in re.findall(r"\d+|[?\-]|\s{1,}", line.rstrip("\n")):
        if tok.isdigit():
            n = int(tok); total += 1
            assert 1 <= n <= 26, n
            ch = chr(ord("A") + n - 1); seen[n].add(ch); out.append(ch)
        elif tok.isspace():
            out.append(" ")
        elif tok == "?":
            out.append("?")
    print(re.sub(r" +", " ", "".join(out)).strip())
print("numbers:", total, "distinct:", len(seen), "conflicts:", [k for k, v in seen.items() if len(v) > 1])
