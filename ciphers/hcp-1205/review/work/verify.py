"""Reviewer check: (1) rerun solver command, compare with the literal block in SOLUTION.md;
(2) independent decode of the ledger with a key table typed from HCP1267/1216, not imported from decode.py;
(3) sign statistics; (4) decode of reviewer's own sign-class transcription of the contested rows.
Run: python3 -I ciphers/hcp-1205/review/work/verify.py"""
import re,subprocess,collections,os,math
R='/Users/tomaspavuk/Desktop/hcsolve/'; D=R+'ciphers/hcp-1205/'
out=subprocess.run(['python3','-I',D+'work/decode.py'],capture_output=True,text=True).stdout
sol=open(D+'SOLUTION.md',encoding='utf-8').read()
blk=re.search(r'## Literal decipherment.*?```\n(.*?)```',sol,re.S).group(1)
want=[l for l in blk.splitlines() if l.strip()]
got=[re.sub(r'^\s*','',l) for l in out.splitlines() if re.match(r'\s*(\d\d|U\d|S\d) ',l)]
print('rows',len(got),'identical to claimed block:',got==want)
# independent ledger decode
K={'a':'a','b':'b','d':'d','e':'e','f':'f','g':'g','i':'i','j':'j','k':'k','l':'l','m':'m','n':'n','o':'o','ö':'ö','p':'p','r':'r','s':'s','t':'t','u':'u','ü':'ü','v':'v','y':'y','z':'z',
   'C':'cs','G':'gy','Y':'y','H':'h','P':'p','N':'n','D':'h','M':'m','#':'{struck}','?':'?'}
c=collections.Counter(); mine=[]
for l in open(D+'work/ledger.txt',encoding='utf-8'):
    if l.startswith('#') or not l.strip(): continue
    lab,t=l.split(); mine.append(lab+' '+''.join(K[x] for x in t)); c.update(x for x in t if x!='?')
print('independent decode equals command output:',mine==got)
print('signs',sum(c.values()),'; uncovered tokens: 0 (KeyError otherwise)')
n=sum(c.values()); print('IC of ledger tokens %.4f'%(sum(v*(v-1) for v in c.values())/(n*(n-1))))
print(sorted(c.items(),key=lambda kv:-kv[1]))
print('homograph-class tokens H,P,N,D,M,Y:',{k:c[k] for k in 'HPNDMY'})
# reviewer's own sign-class transcription, read from review/work/crops, contested rows only
S={'a2':'a','e3':'e','m3':'m','n2':'n','hp':'{h/p/n}','dd':'d/h','X':'u','Ẍ':'ü','loop':'g','gy':'gy','oh':'o','öh':'ö','ic':'i','T':'t','F':'r','Fb':'r','S':'k','wv':'l','Vv':'v','J':'j','sb':'s','sz':'sz','b6':'b','5':'5','+':'f','ux':'u+'}
rows={'05*':'hp ic sz e3 m3 hp a2 F m3 e3 dd',
'08*':'hp e3 sb T F e3 m3 e3 gy e3 S 5 ic S e3 n2',
'13e':'hp a2',
'21*':'hp e3 F sz e3 a2',
'24e':'wv e3 T e3 dd oh gy',
'25e':'a2 F oh S oh',
'U6e+U7':'S e3 wv m3 e3 b6 öh wv n2 e3'}
for k,v in rows.items(): print(k,''.join(S[t] for t in v.split()))
