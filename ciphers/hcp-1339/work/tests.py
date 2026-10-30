#!/usr/bin/env python3
"""hcp-1339: tests of the initial-letter hypothesis. No key exists; this checks the transcription,
letter statistics against English word-initial frequencies and letter frequencies, and the card-to-card overlaps."""
import collections,math,hashlib,json,random,sys
ROOT='ciphers/hcp-1339/'
H={'source/address-large.jpg':'d964372c86e956ffc7ca392ad520fbc5548c5dfec6c1f994675fe11950082e70',
   'source/picture-large.jpg':'5cb7557979fe67f1b66dee00b0f20acc405b40173350f6175bf8c954533f2a21',
   'work/hires/pc_hcp_20_adr.JPG':'6ba1f53dee32b6882a45d1f58d26dfcdb1468499e7d986f811707d950bff90e4'}
for f,h in H.items():
    assert hashlib.sha256(open(ROOT+f,'rb').read()).hexdigest()==h,f
print('hashes OK')
T=[l.split() for l in open(ROOT+'work/transcription.txt') if l.strip() and not l.startswith('#')]
print('lines',len(T),'signs',sum(map(len,T)))
txt=[c for l in T for c in l if c.isalpha()]
# working readings of the six sister cards (quick, low-confidence, NOT edited in their directories)
sis={'1322':'MODAAHQSD AOHTTDMLA AHA SIWNM LDAWYMMHBOTD FYEDAACEMC',
'1338':'MODAAHQSD HAMRD HYAGOAD WELTAFKFYEAADC',
'1335':'MODAAHQSD DNFNTW FMDADHYA FMBO WFLAK FYDC',
'1336':'MODAAHQSD HIGBAD HYAFBDWF LTAFKFYE AADC',
'1334':'MODAAHQSD ADLWTDD DEMNYDHYW GOAD WELTA FKFYEDC',
'1337':'MODAAHQSD IWSPTSYDHYAGO ADWFLAKF YDC'}
EN='etaoinshrdlcumwfgypbvkjxqz'
ef=dict(zip('abcdefghijklmnopqrstuvwxyz',[8.2,1.5,2.8,4.3,12.7,2.2,2.0,6.1,7.0,.15,.77,4.0,2.4,6.7,7.5,1.9,.1,6.0,6.3,9.1,2.8,1.0,2.4,.15,2.0,.07]))
# word-initial frequencies (common printed-English table)
wf=dict(zip('abcdefghijklmnopqrstuvwxyz',[11.7,4.4,5.2,3.2,2.8,4.0,1.6,4.2,7.3,.5,.6,2.4,3.8,2.3,7.6,4.3,.2,2.8,6.7,16.0,1.2,.8,5.5,.04,.8,.04]))
def ll(s,m):
    t=sum(m.values());return sum(math.log(m[c.lower()]/t) for c in s)/len(s)
allc=txt+[c for v in sis.values() for c in v if c.isalpha()]
c=collections.Counter(allc);print('freq (card plus sisters):',c.most_common())
print('per-letter log-lik, letter-frequency model   %.3f'%ll(allc,ef))
print('per-letter log-lik, word-initial model       %.3f'%ll(allc,wf))
print('E share %.1f%% (running English 12.7%%); A+D+H+F+W share %.1f%%'%(100*c['E']/len(allc),100*sum(c[x] for x in 'ADHFW')/len(allc)))
s=''.join(txt);print('this card:',s,len(s))
for n,v in sis.items():
    v=v.replace(' ','')
    best=max(((i,j,k) for i in range(len(s)) for j in range(len(v)) for k in [next((k for k in range(0,99) if i+k>=len(s) or j+k>=len(v) or s[i+k]!=v[j+k]),0)]),key=lambda t:t[2])
    print(n,'longest common run',best[2],s[best[0]:best[0]+best[2]])
