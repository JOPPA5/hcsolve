import itertools,sys
W=set(open('common.txt').read().split())
bylen={}
for w in W: bylen.setdefault(len(w),[]).append(w)
def segs(s,maxw=3):
    if not s: yield []; return
    if maxw==0: return
    for i in range(1,len(s)+1):
        for r in segs(s[i:],maxw-1): yield [s[:i]]+r
def search(words,m,inv,out,res):
    if not words: res.append(list(out)); return
    cw=words[0]
    for w in bylen.get(len(cw),[]):
        m2=dict(m);i2=dict(inv);ok=True
        for c,p in zip(cw,w):
            if c in m2:
                if m2[c]!=p: ok=False;break
            else:
                if p in i2: ok=False;break
                m2[c]=p;i2[p]=c
        if ok:
            out.append(w);search(words[1:],m2,i2,out,res);out.pop()
variants={}
for w5 in (['EP'],['XP'],['EZP']):
  for q in ('Q','A'):
    for pre in ('','U'):
      w6=pre+'GE'+q+'RDEKST'
      for seg in segs(w6):
        base=['ABC','DEFG','HIJKLM','NEO']+w5+seg
        for rev in (False,True):
          ws=[x[::-1] for x in base[::-1]] if rev else base
          ws=sorted(ws,key=lambda x:-len(x));res=[];search(ws,{}, {},[],res)
          for r in res: print(rev,w5,q,pre,' '.join(r),'|',ws)
