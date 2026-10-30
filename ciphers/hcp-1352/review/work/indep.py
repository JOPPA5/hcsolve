# independent Caesar -1 decoder, own transcription typed from the reviewer's reading
rows=["Ublf dbsf J Ibwf nbef","op njtublft J bn wfsz","nvdi bnvtfe xjui pvs","ofx qmbo Nz mpwf","po b Qptu dbse Ipx","ojdf uijt jt Tfdsfu Mpp"]
d=lambda s:''.join(chr((ord(c.upper())-65-1)%26+65) if c.isalpha() else c for c in s)
n=0
for r in rows:
    print(r,'=>',d(r)); n+=sum(c.isalpha() for c in r)
print(n)
