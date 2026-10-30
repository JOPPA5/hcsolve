"""Reviewer's independent decoder: own key table, solver ledger as input, then reviewer's corrections
(pixel-checked, crops in review/work/c/). Run from the cipher directory: python3 -I review/work/indep.py"""
import re,collections
K=dict(A='a',B='b',D='d',E='e',G='g',H='h',I='i',J='j',K='k',L='l',M='m',N='n',O='o',T='t',V='v',Y='y',Z='z')
K.update({'F':'r',')':'s','X':'u','6':'b','+':'f','CS':'cs'})
rows={}
for l in open('work/ledger-opus.txt',encoding='utf-8'):
    if l.startswith('#') or not l.strip(): continue
    p=l.split(); rows[p[0]]=p[1:]
def dec(toks):
    out=[]
    for t in toks:
        b=re.sub(r'[\^#?]','',t.split(':')[0]); s=K[b]
        if ':' in t: s={'o':'ö','u':'ü'}[s]
        out.append(s)
    return ''.join(out)
base={k:dec(v) for k,v in rows.items()}
import copy
fix=copy.deepcopy(rows)
def sub(r,i,old,new):
    assert fix[r][i]==old,(r,i,fix[r][i]); fix[r][i]=new
# index positions located by searching
def find(r,seq,start=0):
    s=fix[r]
    for i in range(start,len(s)):
        if s[i:i+len(seq)]==seq: return i
    raise SystemExit((r,seq))
sub('02',find('02',['Z','I']) +1,'I','O:diaeresis')
sub('10',find('10',['T','A','D','E',')'])+1,'A','E')
sub('18',find('18',['K','O','Z','T'])+1,'O','O:diaeresis')
i=find('28',['F','A','E','F','E',')']); sub('28',i+5,')','K')
i=find('28',['L','A','K','O','Z','N','I']); fix['28'].insert(i+2,'L')
i=find('29',['V','A','L','E']); sub('29',i+1,'A','E')
new={k:dec(v) for k,v in fix.items()}
for k in rows:
    if base[k]!=new[k]: print(k,'\n  solver  ',base[k],'\n  reviewer',new[k])
txt=''.join(new[k] for k in new)
print('signs solver',sum(map(len,rows.values())),'reviewer',sum(map(len,fix.values())))
all_=''.join(base[k] for k in base if not k.startswith('S'))
for w in ['hogy','megkaptam','sora','boldog','szeret','hen','minel','elobb','megsz']:
    print(w,all_.count(w))
c=collections.Counter(re.sub(r'[\^#?]','',t.split(':')[0]) for v in rows.values() for t in v)
print(sorted(c.items(),key=lambda x:-x[1]))
