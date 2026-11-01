# Independent decoder: own table (from HCP1216 key table), own loop; prints as-ledger and reviewer-corrected text.
import re,sys
L='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1279/work/ledger.txt'
T={'F':'r',')':'s','X':'u','6':'b','+':'f','H':'H','CS':'C','*':'?','AE':'#','OI':'@'}
for c in 'ACDEGIJKLMNOTVYZ':T[c]=c.lower()
FIX={('01',9):'A',('09',17):'D',('14',7):'O',('19',8):'E',('S3',6):')'}
rows={}
for l in open(L,encoding='utf-8'):
    if l.startswith('#') or not l.strip():continue
    a=l.split();rows[a[0]]=a[1:]
def d(t):
    t=t.strip('[]').split(':')[0];return T[t]
n=0
for k,v in rows.items():
    n+=len(v)
    a=''.join(d(t) for t in v)
    w=list(v)
    for (r,i),s in FIX.items():
        if r==k: print('  fix',k,i,w[i],'->',s); w[i]=s
    print(k,a,'' if w==v else '=> '+''.join(d(t) for t in w))
print('signs',n)
s=''.join(''.join(d(t) for t in v) for v in rows.values())
import collections
print(sorted(collections.Counter(rows[k][i].split(':')[0] for k in rows for i in range(len(rows[k]))).items()))
for w in ['Hogy','mert','Henz','csak'.replace('cs','C'),'maga','kivanja']:print(w,s.count(w))
