#!/usr/bin/env python3
"""Reviewer's independent check for hcp-1504: join the reviewer's reading and re-segment it with a
dictionary DP (fewest words, /usr/share/dict/words + 'a','i'), without using the solver's words.txt."""
import sys
reading = open(sys.argv[1]).read()
s = "".join(l for l in reading.splitlines() if not l.startswith("#")).replace(" ", "")
words = {w.strip().lower() for w in open("/usr/share/dict/words")} | {"a", "i"}
words = {w for w in words if len(w) > 1 or w in "ai"}
INF = (10**9, "")
best = [INF] * (len(s) + 1); best[0] = (0, ""); back = [None] * (len(s) + 1)
for j in range(1, len(s) + 1):
    for i in range(max(0, j - 12), j):
        w = s[i:j]
        cost = 1 if w in words else (5 * len(w))   # unknown fragments heavily penalised
        if best[i][0] + cost < best[j][0]:
            best[j] = (best[i][0] + cost, ""); back[j] = i
out = []; j = len(s)
while j: i = back[j]; out.append(s[i:j]); j = i
out.reverse()
print("letters:", len(s)); print("joined :", s); print("DP seg :", " ".join(out))
print("not in dictionary:", [w for w in out if w not in words])
