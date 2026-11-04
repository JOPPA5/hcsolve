import sys
W={}
for l in open('/Users/tomaspavuk/Desktop/hcsolve/batches/scoring-sol61/german/words.tsv'):
    w,f=l.rstrip('\n').split('\t'); W[w]=int(f)
def pat(s):
    m={};return tuple(m.setdefault(c,len(m)) for c in s)
def q(cw,fixed={},n=25,minf=0):
    p=pat(cw); out=[]
    for w,f in W.items():
        if len(w)!=len(cw) or f<minf: continue
        if pat(w)!=p: continue
        ok=True
        for c,x in zip(cw,w):
            if c in fixed and fixed[c]!=x: ok=False;break
            if c not in fixed and x in fixed.values(): ok=False;break
        if ok: out.append((f,w))
    out.sort(reverse=True); return out[:n]
if __name__=='__main__':
    cw=sys.argv[1].split(',') if ',' in sys.argv[1] else list(sys.argv[1])
    fx=dict(kv.split('=') for kv in sys.argv[2:])
    for f,w in q(cw,fx): print(f,w)
