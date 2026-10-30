# Run from repo root: python3 -I ciphers/hcp-1335/work/analyse.py
import collections, hashlib, math, os, re
B='ciphers/hcp-1335/'
for f,h in [('source/address-large.jpg','af1d48b78a59842b5637cfa56a991660e618eb5a5b071f73f8ff4c93962cc008'),
            ('source/picture-large.jpg','3c4f760408f65a0fb03162552ba34151a987c4ade8dd9ff49b7ae669051a866e')]:
    assert hashlib.sha256(open(B+f,'rb').read()).hexdigest()==h,f
this=''.join(re.sub(r'[^A-Z]','',l) for l in open(B+'work/transcription.txt') if not l.startswith('#'))
pool=[''.join(l.split()[1:]) for l in open(B+'work/sisters_rough.txt') if not l.startswith('#')]
print('this card',len(this),this)
allt=this+''.join(pool)
c=collections.Counter(allt); n=len(allt)
print('pooled',n,c.most_common())
print('IC this %.3f pooled %.3f'%tuple(sum(v*(v-1) for v in collections.Counter(s).values())/(len(s)*(len(s)-1)) for s in (this,allt)))
# English letter frequency vs word-initial frequency (standard published approximations, per cent)
L=dict(zip('ABCDEFGHIJKLMNOPQRSTUVWXYZ',[8.2,1.5,2.8,4.3,12.7,2.2,2.0,6.1,7.0,.15,.77,4.0,2.4,6.7,7.5,1.9,.1,6.0,6.3,9.1,2.8,1.0,2.4,.15,2.0,.07]))
I=dict(zip('ABCDEFGHIJKLMNOPQRSTUVWXYZ',[11.6,4.7,3.5,2.7,2.0,3.8,2.0,7.2,6.3,.6,.7,2.7,4.4,2.4,6.3,2.6,.2,1.7,7.8,16.7,1.2,.6,6.7,.05,1.6,.03]))
def ll(s,d):
    t=sum(d.values()); return sum(math.log(d[ch]/t) for ch in s)
A='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for k in range(26):
    s=''.join(A[(A.index(ch)+k)%26] for ch in allt)
    print('shift %2d  ll(text-letters) %8.1f  ll(word-initials) %8.1f  %s'%(k,ll(s,L),ll(s,I),''.join(A[(A.index(ch)+k)%26] for ch in this)))
print('E share pooled %.1f%% (ordinary English ~12.7%%, word-initial ~2%%)'%(100*c['E']/n))
