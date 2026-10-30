# Reviewer round-2 independent Caesar -1 decoder of the reviewer's own reading
lines=["Nz. Pxo. Cpz.","J. bn. tp. Tpssz.","J. dbo'u. xsjuf.","mfuufs.","\"up-ojhiu.\"","Nz. Zpvs.","Hjsm"]
d=lambda s:''.join(chr((ord(c.upper())-66)%26+65) if c.isalpha() else c for c in s)
n=0
for l in lines: print(l.ljust(22),'->',d(l)); n+=sum(c.isalpha() for c in l)
print('shifted letters:',n)
import datetime;print(datetime.date(1908,2,7).strftime('%A'))
