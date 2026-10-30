import sys,itertools
S='/private/tmp/claude-501/-Users-tomaspavuk-Desktop-hcsolve/7cce98b2-6c30-466a-96a4-334b405baba7/scratchpad/corp.txt'
fr={}
for l in open(S):
    w,c=l.split(); fr[w]=int(c)
for w in 'A I'.split(): fr[w]=100
for w in "MEET MEETING STAND TAXI BAND BUS CAB TRAM TRAIN SEAT PIER GATE LANE ROAD STILE".split(): fr.setdefault(w,5)
def pat(s):
    m={};return tuple(m.setdefault(c,len(m)) for c in s)
bypat={}
for w in fr:
    bypat.setdefault(pat(w),[]).append(w)
def solve(C,top=40):
    by=[bypat.get(pat(c),[]) for c in C]
    order=sorted(range(len(C)),key=lambda k:len(by[k]))
    res=[]
    def rec(i,mp,inv,out,score):
        if i==len(C):
            res.append((score,' '.join(out[k] for k in range(len(C)))));return
        k=order[i];c=C[k]
        for w in by[k]:
            m2=dict(mp);i2=dict(inv);ok=True
            for x,y in zip(c,w):
                if x in m2:
                    if m2[x]!=y: ok=False;break
                elif y in i2: ok=False;break
                else: m2[x]=y;i2[y]=x
            if ok:
                out[k]=w;rec(i+1,m2,i2,out,score+__import__('math').log(fr[w]+1))
    rec(0,{}, {}, {},0)
    res.sort(reverse=True)
    print(C,[len(b) for b in by],len(res))
    for s,r in res[:top]: print(round(s,1),r)
# merges: d/q, e/l, g/i
for d2 in 'dq':
  for e2 in 'el':
    for g in 'ig':
      solve(['abc','d'+'e'+'f'+g,'hiif'+'k'+e2+'m','nhao','cfp'+d2+'o'],top=12)
