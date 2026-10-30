# independent decoder: reviewer's own transcription, typed from enlarged crops, no import from work/
words="Nz Pxo Mpwjoh Cpz Dsjdlfu Nbudi up Ebz Hbvou xpo Zpvs Pxo Hjsm".split()
a="abcdefghijklmnopqrstuvwxyz"
tot=0
for k in range(26):
    tr=str.maketrans(a,a[-k:]+a[:-k] if k else a)
    out=[w.lower().translate(tr) for w in words]
    if k in(0,1,25): print(k,' '.join(out))
print('letters',sum(map(len,words)))
import os
wl=[l.strip().lower() for l in open('/usr/share/dict/words')] if os.path.exists('/usr/share/dict/words') else []
import re
for pat in ['^ga.n.$','^ga.nt$','^ga..t$','^gau..$','^g.unt$']:
    print(pat,sorted({w for w in wl if re.match(pat,w)}))
