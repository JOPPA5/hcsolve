#!/usr/bin/env python3
"""Reviewer's independent decode of hcp-1034 (own sign names, own reading from review/work crops).
Run: python3 -I ciphers/hcp-1034/review/work/verify.py"""
# reviewer's own glyph names
K = {"tri":"I","tri.":"i","vtri.":"i","#2":"n","#3":"m","box":"d","Dh":"e","Df":"e","oval":"c",
     "Lhook":"h","Xloop":"f","u":"u","r":"r","P":"l","Nz":"b","Vh":"b","x":"a","Xtall":"G",
     "Klong":"s","8":"z","ck":"k","oK":"k","o/":"t","dag":"v"}
ROWS = [
 "tri #2 box Dh #3 | tri. oval Lhook | #3 tri. oval Lhook | Xloop u r | box Df tri. #2 Dh P tri. Dh Nz Dh",
 "x oval? Xloop | #3 Dh r ck | Klong x #3 | oK Dh tri. o/ | Lhook Dh r 8 P tri. oval Lhook - Vh Dh box x #2 .",
 "oK Dh , | dag Dh r | Nz P Dh tri. Nz Dh | vtri. oval Lhook | #3 tri. o/ | Xtall r u Klong 8 | u #2 box",
 "oK u Klong 8",
 "box Dh tri. #2 | o/ r . | Xloop r tri. o/ 8 .",
]
out=[]; n=0
for r in ROWS:
    s=""
    for t in r.split():
        if t=="|": s+=" "
        elif t in ".,-": s+=t
        elif t=="oval?": s+="[c->u]"; n+=1
        else: s+=K[t]; n+=1
    out.append(s); print(s)
print("signs:",n)
inv={}
for k,v in K.items(): inv.setdefault(v,[]).append(k)
print("letters with >1 glyph:",{k:v for k,v in inv.items() if len(v)>1})
