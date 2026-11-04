"""Independent reviewer check for hcp-993: own key, own parser, coverage counts."""
import re, sys, collections
from pathlib import Path
T = Path(sys.argv[1]).read_text(encoding="utf-8")
K = dict(zip("0 1 2 3 4 5 6 7 8 9 arc hook revc Ibar U V phi plus neq w2o vbar Uuml ouml".split(),
             "o l n m e s b t h g i r c z u d a f k w v ü ö".split()))
cnt = collections.Counter(); restored = []; out = []
for line in T.splitlines():
    if line.startswith("#") or not line.strip(): continue
    lab, body = line.split(":", 1)
    body = re.sub(r"\[plain Kurrent German: ([^\]]*)\]", lambda m: "«" + m.group(1) + "»", body)
    body = re.sub(r"\[two rows of dots[^\]]*\]", "«dots»", body)
    res = []
    for seg in re.split(r"(«[^»]*»)", body):
        if seg.startswith("«"): res.append(seg.upper()); continue
        for w in seg.split("/"):
            s = ""
            for t in w.split():
                core = t.strip(".,!=-")
                if not core: s += t; continue
                kind = "card"
                if core[0] == "(": kind = "restored"; core = core[1:-1]
                elif core[0] == "<": kind = "supplied"; core = core[1:-1]
                elif core[0] == "{": kind = "emended"; core = core[1:-1].split("=")[1]
                elif core[0] == "[": s += core[1:-1]; continue
                if core not in K: sys.exit("UNKNOWN " + t)
                cnt[kind] += 1
                if kind != "card": restored.append((lab.strip(), kind, K[core]))
                s += K[core]
            res.append(s)
    out.append(f"{lab.strip():5s} " + " ".join(x for x in res if x))
print("\n".join(out)); print(dict(cnt)); print(restored)
