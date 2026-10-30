#!/usr/bin/env python3
"""hcp-1337: is the letter string ordinary (enciphered) text or word initials? Run from repo root."""
import hashlib, math, string, sys
from collections import Counter
D='ciphers/hcp-1337/'
H={'source/picture-large.jpg':'934d15f3e58e828101da0290d2acc7913f5009522e2e3e81c2f3b90511c4b620',
   'source/address-large.jpg':'65a1aab364dca57f475e8c0cfdb5fa0da1713568432f087b2e570fd1e0a0df64',
   'work/hires/pc_hcp_18_pic.JPG':'d516d16688cfd3f5d602700b6f153f69530acea25fd0392fddfa082e39bab541',
   'work/hires/pc_hcp_18_adr.JPG':'48df4ebc6e0dc2726b479d4c1ed3e0e2adafd52b7af61ec887f37895a828ebfa'}
for f,h in H.items():
    assert hashlib.sha256(open(D+f,'rb').read()).hexdigest()==h,f
print('source hashes OK')
c=''.join(l.split() and ''.join(l.split()) or '' for l in open(D+'work/transcription.txt') if not l.startswith('#'))
print('1337 string:',c,len(c),'signs')
fam=''.join(''.join(l.split()[1:]) for l in open(D+'work/family.txt') if not l.startswith('#'))
print('family signs:',len(fam),Counter(fam).most_common())
# English letter frequency and word-initial frequency, % (standard approximate tables)
L=dict(zip(string.ascii_uppercase,[8.2,1.5,2.8,4.3,12.7,2.2,2.0,6.1,7.0,.15,.77,4.0,2.4,6.7,7.5,1.9,.1,6.0,6.3,9.1,2.8,1.0,2.4,.15,2.0,.07]))
I=dict(zip(string.ascii_uppercase,[11.7,4.4,5.2,3.2,2.8,4.0,1.6,4.2,7.3,.5,.6,2.4,3.8,2.3,7.6,4.3,.2,2.8,6.7,16.,1.2,.6,5.5,.01,.8,.01]))
for name,s in (('1337',c),('family',fam)):
    C=Counter(s);n=len(s)
    ll=lambda T:sum(C[k]*math.log(T[k]/sum(T.values())) for k in C)
    print(name,'log-lik text %.1f  initials %.1f; share of ETAOIN (text ~.56 / initials ~.46): %.2f; E+T+N+R: %.2f'%(ll(L),ll(I),sum(C[k] for k in 'ETAOIN')/n,sum(C[k] for k in 'ETNR')/n))
print('Caesar shifts of the stock opening MODAAHQSD and 1337 line 2:')
sh=lambda s,k:''.join(chr((ord(x)-65+k)%26+65) for x in s)
for k in range(26): print(k,sh('MODAAHQSD',k),sh('QSDIWSPT',k))
