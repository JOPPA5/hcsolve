# Independent Caesar -1 decoder for the reviewer's own reading of hcp-1403.
import sys
def dec(s):
    out=[]
    for ch in s:
        if ch.isalpha():
            b=ord('A') if ch.isupper() else ord('a')
            out.append(chr((ord(ch)-b-1)%26+b).upper())
        else: out.append(ch)
    return ''.join(out)
solver = ["Nz. Pxo. Efbs.","J. bn. tp. Tpssz.","J. dbo'u. xsjuf.","npsf.","\"up-ojhiu.\"","Zpvs","Hjsm"]
reviewer = ["Nz. Pxo. El. Cpz.","J. bn. tp. Tpssz.","J. dbo'u. xsjuf.","n?[tall]?[minims]?f s. (>=6 signs; npsf not supported)","\"up-ojhiu.\"","Zpvs. Px[o]?","El. Hjsm"]
for name,lines in (("solver",solver),("reviewer",reviewer)):
    print("==",name)
    for l in lines: print(f"{l:40s} -> {dec(l)}")
for cand in ["npsf","npuifs","mfuufs","nbuufs"]:
    print(cand,"->",dec(cand))
import datetime; print("1908-02-07 weekday:", datetime.date(1908,2,7).strftime('%A'))
