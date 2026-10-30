#!/usr/bin/env python3
"""Reviewer's independent decode: own table, own re-typed tokens from reading the crops. Run with python3 -I."""
import string,datetime
U=string.ascii_lowercase
T={U[(i+1)%26]:U[i] for i in range(26)}
d=lambda w:''.join(T.get(c,c) for c in w.lower()).upper()
solver=[("Nz","Pxo","Cpz"),("Kvtu","ibe","b"),("gjof","xbml"),("mpwfmz","xfbuifs"),("J","ipqf","zpv","bsf"),("xfmm","Nz","gspn"),("zpvs","Pxo","Hjsm")]
reviewer=[("Nz","Pxo","[E.L.]","Cpz"),("Kvtu","Ibe","b"),("gjof","xbml"),("mpwfmz","xfbuifs"),("J","ipqf","zpv","bsf"),("xfmm","[M-L]","Gspn"),("zpvs","Pxo","[E.L.]","Hjsm")]
for name,t in(("solver tokens",solver),("reviewer tokens",reviewer)):
    print(name)
    n=0
    for l in t:
        print("  "," ".join(w if w[0]=='[' else d(w) for w in l)); n+=sum(len(w) for w in l if w[0]!='[')
    print("  enciphered letters:",n)
print(datetime.date(1907,9,26).strftime("%A"))
