"""Reviewer's independent decoder for hcp-1195 (no word-level fix tables).
Reads the solver's transcription, applies my own sign table, and prints every
homograph as a set so that every context call is visible."""
import sys
T = sys.argv[1]
KEY = {"H":"H","E":"E","Ey":"E","Ed":"E","Es":"E","I":"I","R":"R","Z":"Z","L":"L",
       "S":"S","T":"T","Td":"T","F":"(FV)","Fd":"W","K":"K","Kd":"G","U":"U","Ud":"Ü",
       "B":"B","Bd":"P","N":"N","Nd":"N","Nl":"N","D":"D","C":"C","A":"(AO)","M":"M",
       "GD":"[GD]","X":"[X]"}
counts = {}
for ln in open(T, encoding="utf-8"):
    if ln.startswith("#") or not ln.strip(): continue
    out = []
    for w in ln.split("/"):
        toks = [t for t in w.split() if t not in (".","-","--")]
        # reorder marks
        i, seq = 0, []
        while i < len(toks):
            if toks[i].endswith("@2") and i+1 < len(toks) and toks[i+1].endswith("@1"):
                seq += [toks[i+1][:-2], toks[i][:-2]]; i += 2
            else:
                seq.append(toks[i]); i += 1
        for t in seq: counts[t] = counts.get(t,0)+1
        out.append("".join(KEY[t] for t in seq))
    print(" ".join(out))
print("signs:", len(counts), "tokens:", sum(counts.values()))
print(sorted(counts.items(), key=lambda x:-x[1]))
