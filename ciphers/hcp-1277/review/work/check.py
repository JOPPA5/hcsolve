"""Independent decode of the ledger with the reviewer's own table + reviewer corrections; word-count checks."""
import re,sys
T=dict(zip('A B C D E G I J K L M N O R S T U V Y Z'.split(),'a b c d e g i j k l m n o r s t u v y z'.split()))
T.update({'F':'r',')':'s','X':'u','6':'b','+':'f','H':'h','GY':'gy','CS':'cs','#':'?','[':'…'})
rows={}
for l in open('work/ledger-opus.txt',encoding='utf-8'):
    if l.startswith('#') or not l.strip(): continue
    p=l.split(); rows[p[0]]=p[1:]
def dec(ts):
    o=''
    for t in ts:
        b,_,a=t.partition(':'); s=T[b]
        o+={'o':'ö','u':'ü'}[s] if a else s
    return o
lit={k:dec(v) for k,v in rows.items()}
fix=dict(lit)
assert lit['10'].startswith('zenmegymostmerv'); fix['10']=lit['10'].replace('mostmer','mostmar')
assert lit['25'].startswith('kuldtek'); fix['25']=lit['25'].replace('kuldtek','küldtek',1)
fix['24']=lit['24'].replace('t?t','tut',1)
for k in fix: print(k,fix[k], '' if fix[k]==lit[k] else '   <- reviewer change')
all_=''.join(lit[k] for k in lit if not k.startswith('S'))
from collections import Counter
print(len(sum((v for k,v in rows.items() if not k.startswith('S')),[])),'tokens main;',Counter(t.split(':')[0] for k,v in rows.items() for t in v).most_common())
for w in ['hogy','edesem','viszontlat','visza','szeret','ede']:
    print(w,len(re.findall(w,all_)))
print('GY tokens',sum(t=='GY' for v in rows.values() for t in v))
print('Y tokens',sum(t=='Y' for v in rows.values() for t in v))
