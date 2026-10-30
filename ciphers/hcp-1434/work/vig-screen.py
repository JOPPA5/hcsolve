# Vigenere/Beaufort dictionary-key screen for HCP 1434 (Claude Opus 5.5, 2026-10-30)
W=set(w.strip().upper() for w in open('/usr/share/dict/words') if w.strip().islower() and w.strip().isalpha())
W4={w for w in W if 4<=len(w)<=8}
keys=[w for w in W if 3<=len(w)<=8]+['DEANE','MISSDEANE','LOVE','KISS']
cts=['PHSTNAAHSEHHGGTOGAAAAFNYNJASFCEAN','PHSTNHSEHHGGTOGFNYNJSFCEN']
def cov(p):
    best=[0]*(len(p)+1)
    for i in range(len(p)):
        best[i+1]=max(best[i+1],best[i])
        for L in range(4,9):
            if i+L<=len(p) and p[i:i+L] in W4: best[i+L]=max(best[i+L],best[i]+L)
    return best[-1]
out=[]
for ct in cts:
    c=[ord(x)-65 for x in ct]
    for k in keys:
        kk=[ord(x)-65 for x in k]
        for mode in ('vig','beau','var'):
            if mode=='vig': p=[(x-kk[i%len(kk)])%26 for i,x in enumerate(c)]
            elif mode=='beau': p=[(kk[i%len(kk)]-x)%26 for i,x in enumerate(c)]
            else: p=[(x+kk[i%len(kk)])%26 for i,x in enumerate(c)]
            s=''.join(chr(x+65) for x in p)
            out.append((cov(s)/len(s),s,k,mode))
out.sort(reverse=True)
for o in out[:25]: print(o)
