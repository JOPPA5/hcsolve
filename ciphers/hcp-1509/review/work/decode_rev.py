"""Reviewer's independent decoder for hcp-1509 (own key table, own parser).
Run from repo root: python3 -I ciphers/hcp-1509/review/work/decode_rev.py"""
import collections, sys
T = "ciphers/hcp-1509/work/transcription.txt"
# Reviewer's key, built from reading the scan (not loaded from work/key.json)
K = {"16/1":"A","6":"B","c":"C","h":"D","8":"E","S":"F","9":"G","=":"H","*":"I",
     "3":"K","T":"L","N":"M","11":"N","11_":"O","11_\"":"Ö","7":"R","4":"S","1":"T",
     ":":"U",":\"":"Ü","11=":"V","111":"W","hz":"Z"}
cnt = collections.Counter(); bad=[]; n=0; words=[]
for ln in open(T, encoding="utf-8"):
    ln = ln.strip()
    if not ln or ln.startswith("#"): continue
    w = ""
    for t in ln.split():
        if t == "x":
            if w: words.append(w); w=""
        elif t.startswith("#"):
            words.append(t[1:])
        else:
            n += 1; cnt[t]+=1
            w += K.get(t, "?")
            if t not in K: bad.append(t)
    if w: words.append(w)
print(" ".join(words))
print("signs", n, "unknown", bad)
print(sorted(((K[k],v) for k,v in cnt.items()), key=lambda x:-x[1]))
