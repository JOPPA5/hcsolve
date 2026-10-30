#!/usr/bin/env python3
"""Reviewer's independent check for hcp-1460: own transcription (read from
review/work crops), own route implementation via index permutation."""
import sys
mine = ["DaSdeiare","Ftewseihtgldarha","ewtteocrtenChhid","lsngtnhsadahita",
        "akdegveouyitmes","hsogauainsotltrnci"]
def order(n):  # 0, n-1, 1, n-2, ...
    idx=[]; i,j=0,n-1
    while i<=j:
        idx.append(i); i+=1
        if i<=j: idx.append(j); j-=1
    return idx
pt=[''.join(l[k] for k in order(len(l))) for l in mine]
for c,p in zip(mine,pt): print(f"{c:20s} {p}")
# inverse: encrypt intended phrase and compare with card
def enc(p):
    out=['']*len(p)
    for pos,k in enumerate(order(len(p))): out[k]=p[pos]
    return ''.join(out)
print("enc(askedmetgiveyou) =", enc("askedmetgiveyou"), "card:", mine[4])
print("enc(hiscongratulations) =", enc("hiscongratulations"))
print("line6 without inserted s:", ''.join("hsogauainotltrnci"[k] for k in order(17)))
print("total letters", sum(map(len,mine)))
solver=open(sys.argv[1]).read().split()
print("transcription identical to solver's:", solver==mine)
