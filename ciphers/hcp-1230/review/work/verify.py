"""Independent check, hcp-1230, review 1 (reviewer: Claude Opus 5.5). Run from repo root:
   python3 -I ciphers/hcp-1230/review/work/verify.py
Own letter table; review ledger = solver token stream with only the corrections I read on the pixels (CORR).
Prints: replay of solver ledger, key coverage, corrected rows, sign-level diff, repeated words."""
import collections, re
L=open('ciphers/hcp-1230/work/ledger.txt',encoding='utf-8').read().splitlines()
rows={}
for l in L:
    if l.strip() and not l.startswith('#'):
        p=l.split(); rows[p[0]]=p[1:]
# independently typed class -> letter table (from the sign table in hcp-1216/SOLUTION.md)
T=dict(zip('A 6 D E + G J K L M N O F ) T X V Y I Z H P'.split(),'a b d e f g j k l m n o r s t u v y i z h p'.split()))
T['CS']='cs'
def d(t):
    b=t.strip('[]').split(':')[0]; c=T[b]
    return c if t==b else ('['+c+']' if t.startswith('[') else c+"'")
solver={k:''.join(d(t).replace("'",'') for t in v) for k,v in rows.items()}
print('tokens',sum(map(len,rows.values())),'unknown', [t for v in rows.values() for t in v if t.strip('[]').split(':')[0] not in T])
print('freq',collections.Counter(t.strip('[]').split(':')[0] for v in rows.values() for t in v).most_common())
# (row, 0-based index, old, new); new None+insert handled below
CORR=[('03',6,'E','A'),('07',8,'E','A'),('07',14,'E','A'),('08',7,'E','A'),('17',3,'E:acute','A:acute'),
      ('21',16,'M','N'),('26',8,'E','I')]
new={k:list(v) for k,v in rows.items()}
for r,i,o,n in CORR:
    assert new[r][i]==o,(r,i,new[r][i],o); new[r][i]=n
new['15'].insert(0,'6')
print('review tokens',sum(map(len,new.values())))
for k in new:
    a=''.join(d(t).replace("'",'') for t in new[k]); b=solver[k]
    print(k,a,'' if a==b else '   <- solver: '+b)
txt=''.join(''.join(d(t).replace("'",'') for t in new[k]) for k in new)
for w in 'hogy nem csak szamit mitot ijes buntet ront talal'.split(): print(w,len(re.findall(w,txt)))
