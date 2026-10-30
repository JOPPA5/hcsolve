import re,sys,collections
K=dict(bar2='a',bar3='e',six='b',dT='d',hP='h',xc='z',ux='u',uxd='ü',fp='f',bowlR='s',bowlLR='cs',sect='k',ging='g',yloop='y',oloop='o',oloopdd='ő',iloop='i',gam='t',gamgam='tt',wave='l',chev='v',eff='r',stroke2='n',stroke3='m',invT='j',half='½',nine='9',barQ='{a|e}',HID='[s]')
led={}
for l in open('work/ledger-opus.txt',encoding='utf-8'):
    if l[0]=='#' or not l.strip(): continue
    t=l.split(); led[t[0]]=t[1:]
def tok(x):
    b,_,a=x.partition(':'); b=b.rstrip('?') if len(b)>1 else b
    s={'1/2':'½','TT':'tt','CS':'cs'}.get(b,b.lower())
    return {'u:d':'ü','o:dd':'ő'}.get(s+(':'+a if a else ''),s)
n=0;mine={}
for l in open('review/work/my_signs.txt',encoding='utf-8'):
    if l[0]=='#' or not l.strip(): continue
    t=l.split(); mine[t[0]]=[K[x] for x in t[1:]]; n+=len(t)-1
print('my signs',n,'ledger',sum(map(len,led.values())))
for r in led:
    a=[tok(x) for x in led[r]]; b=[x.replace('h','h') for x in mine[r]]
    a2=[{'p':'h'}.get(x,x) for x in a]
    if a2!=b: print('DIFF',r,''.join(a),''.join(b))
txt=''.join(''.join(tok(x) for x in led[r]) for r in led)
for w in ['hogy','nem','vasar','legjob','soraim','edes','feri']: print(w,txt.count(w))
print(collections.Counter(x for r in led for x in led[r]).most_common(40))
