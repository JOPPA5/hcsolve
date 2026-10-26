#!/usr/bin/env python3
"""Convert the solver's token names to the reviewer's cell notation (by stroke geometry) and
print in the reviewer's input format, so decode_review.py can decode the solver's transcription."""
import sys
geom = {"BR":"1","B":"2","BL":"3","R":"4","C":"5","L":"6","TR":"7","T":"8","TL":"9",
        "V":"v",">":">","<":"<","^":"^"}
for line in open(sys.argv[1], encoding="utf-8"):
    line=line.strip()
    if not line or line.startswith("#"): print(line); continue
    out=[]
    for t in line.split():
        base, dot = t[:-1], t[-1]
        out.append(geom[base] + ("." if dot=="1" else ""))
    print(" ".join(out))
