import os
D=os.path.dirname(os.path.abspath(__file__))
K=dict(LP='k',B2='a',B3='e',ST='d',CH='v',BW='s',IT='j',CL='o',CD='i',CS='i',WV='l',S2='n',S3='m',S4='[nm]',GM='t',CR='u',CZ='z',GY='gy',SX='b',FF='r',TS='[hp]',OV='[?]',CRD='ü')
mine=[];
for l in open(D+'/ledger_review.txt'):
    if l[0]=='#' or not l.strip(): continue
    r,*t=l.split(); mine.append((r,t))
sol={}
for l in open(D+'/../../work/ledger.txt'):
    if l[0]=='#' or not l.strip(): continue
    r,*t=l.split(); sol[r]=t
n=0
for r,t in mine:
    s=''.join(K[x] for x in t); n+=len(t)
    so=sol[r]; note=''
    if len(so)!=len(t): note=f' LEN solver {len(so)} mine {len(t)}'
    d=[]
    for a,b in zip(t,so):
        v=K[a]; b0=b.split(':')[0].rstrip('?').lower(); b0={'sd':'d'}.get(b0,b0)
        if ':' in b: b0='ü'
        if not(v==b0 or (a=='TS' and b0 in 'hpd') or a=='OV' or a=='S4'): d.append((a,b))
    print(r,s,note,d or '')
print(n,'signs; solver',sum(len(v) for v in sol.values()))
