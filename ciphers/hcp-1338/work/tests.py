# Run from repo root: python3 -I ciphers/hcp-1338/work/tests.py
import hashlib,collections,os
b='ciphers/hcp-1338/'
for f,h in [('source/picture-large.jpg','57db55f8993ee6c1e9d0a5a2b06991ab41b86c5012d2ef7c305c48e4016d6bd1'),('source/address-large.jpg','c81987dd2d16f97c8f76aa72a8b7eae65afb29e97f4228c640bc2d420c8b5e26')]:
    assert hashlib.sha256(open(b+f,'rb').read()).hexdigest()==h,f
t=open(b+'work/transcription.txt').read().split(); s=''.join(t); n=len(s)
c=collections.Counter(s); print(n,c.most_common())
print('IC %.4f'%(sum(v*(v-1) for v in c.values())/(n*(n-1))))
# percent frequencies: all letters vs word-initial letters of English
allf=dict(zip('ETAOINSHRDLCUMWFGYPBVKJXQZ',[12.7,9.1,8.2,7.5,7.0,6.7,6.3,6.1,6.0,4.3,4.0,2.8,2.8,2.4,2.4,2.2,2.0,2.0,1.9,1.5,1.0,.8,.15,.15,.1,.07]))
ini=dict(zip('TAOSWHIBCMFPDGLNRYEUVJKQXZ',[16,11.7,7.6,6.7,5.5,7.2,7.3,4.4,5.2,3.8,4,4.3,3.2,2,2.4,2.3,2.8,.8,2.8,1.2,.8,.5,.6,.2,.05,.05]))
for name,f in (('all-letter',allf),('word-initial',ini)):
    print(name,'chi2 %.1f'%sum((c[l]-n*p/100)**2/(n*p/100) for l,p in f.items()))
W='THE AND YOU THAT WITH LOVE DEAR HAVE WILL FOR ARE'.split()
A='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for k in range(26):
    p=''.join(A[(A.index(x)+k)%26] for x in s)
    for lab,q in ((f'caesar+{k}',p),(f'rev+{k}',p[::-1])):
        print(lab,q,[w for w in W if w in q])
a=''.join(A[25-A.index(x)] for x in s); print('atbash',a,[w for w in W if w in a])
