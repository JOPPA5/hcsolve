"""Reviewer's independent decoder for hcp-1031 (own key table, typed from review crops)."""
import sys, collections
K = dict(zip("+cCQL7T8ijX6MN0935SZUJ", "abcdefghijklmnoprsztuw"))
LIT = set("VI4.,-")
lines = [l.rstrip("\n").split("\t") for l in open(sys.argv[1], encoding="utf-8") if l.strip() and not l.startswith("#")]
cnt = collections.Counter(); out = []
for tag, ct in lines:
    s = ""
    for ch in ct:
        if ch == '"': s = s[:-1] + {"a":"ä","o":"ö","u":"ü"}[s[-1]]
        elif ch in K: s += K[ch]; cnt[ch] += 1
        elif ch in LIT: s += ch; cnt["lit:"+ch] += 1 if ch in "VI4" else 0
        else: raise SystemExit("unknown "+ch)
    out.append(s); print(tag, s)
print("key signs", sum(v for k, v in cnt.items() if not k.startswith("lit")), "literal", {k: v for k, v in cnt.items() if k.startswith("lit") and v})
print("freq", cnt.most_common())
