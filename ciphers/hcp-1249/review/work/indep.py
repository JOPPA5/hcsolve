# Independent decoder for HCP1249 (reviewer). Key typed from the HCP1216 SOLUTION.md table, not imported from work/decode.py.
import re,sys,collections
L='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1249/work/ledger.txt'
K=dict(A='a',B='b',D='d',E='e',G='g',H='h',I='i',J='j',K='k',L='l',M='m',N='n',O='o',T='t',V='v',Y='y',C='c',CS='cs',F='r',X='u',Z='z')
K[')']='s';K['6']='b';K['+']='f'
A={'acute':'́','diaeresis':'̈','double-acute':'̋','dot':''}
import unicodedata as U
rows={};cnt=collections.Counter()
for ln in open(L,encoding='utf-8'):
    if ln.startswith('#') or not ln.strip(): continue
    lab,*t=ln.split();o=''
    for x in t:
        b,_,a=x.partition(':');b=b.rstrip('#')
        cnt[b]+=1
        if b.startswith('{'): o+=b.strip('{}').split('|')[0];continue
        o+=U.normalize('NFC',(K[b] if b in K else b)+A.get(a,''))
    rows[lab]=o
for k,v in rows.items(): print(k,v)
s=''.join(rows.values())
print(sum(cnt.values()),'signs',len(cnt),'classes');print(sorted(cnt.items(),key=lambda x:-x[1]))
for w in ('hogy','nem','kedvesem','alig','arokszalas','mert','meg'):print(w,len(re.findall(w,s)))
print('p/h ledger tokens H:',cnt['H'])
