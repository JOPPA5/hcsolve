"""Reviewer's independent decode: glyph-name transcription -> letters with key taken from HCP1216 sign table; diff vs solver ledger.
Run: python3 -I ciphers/hcp-1250/review/work/check.py (from repo root)"""
import re,collections
K=dict(bar2='a',bar3='e',six='b',d='d',plus='f',hook='g',ts='h',dot='i',invT='j',sec='k',wave='l',st3='m',st2='n',loop='o',fbar='r',rbowl='s',gamma='t',x='u',chev='v',y='y',tail='z',bow2='cs',OVER='?',BLOT='?',FAINT='?')
K['lo:']='ö'; K['x:']='ü'
mine={}
for l in open('ciphers/hcp-1250/review/work/my_transcription.txt',encoding='utf-8'):
    if l.startswith('#') or not l.strip(): continue
    p=l.split(); mine[p[0]]=[K[t] for t in p[1:]]
SK={'F':'r',')':'s','X':'u','6':'b','+':'f','CS':'cs','[L]':'?','[A]':'?','E/I':'?'}
tot=0;bad=0;c=collections.Counter()
for l in open('ciphers/hcp-1250/work/ledger.txt',encoding='utf-8'):
    if l.startswith('#') or not l.strip(): continue
    p=l.split(); s=[SK.get(t,t.lower()) for t in p[1:]]
    m=mine[p[0]]; tot+=len(s); c.update(s)
    if [x.replace('h','p') for x in s]!=[x.replace('h','p') for x in m]:
        bad+=1; print('DIFF',p[0],''.join(s),'|',''.join(m))
    print(p[0],''.join(m))
print('signs',tot,'rows differing',bad); print(c.most_common())
