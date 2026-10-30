#!/usr/bin/env python3
"""Independent check of HCP1287. Own sign codes, own key, physical rows as seen on my 3x-5x crops.
Run from ciphers/hcp-1287 with python3 -I review/work/my_decode.py"""
import re,collections
# sign classes as drawn (one code per sign, space separated)
KEY={'2b':'a','6':'b','€':'c','bb':'cs','sl':'d','3b':'e','+':'f','lp':'g','ts':'H','crv':'i','T':'j','S':'k','wv':'l',
'3s':'m','2s':'n','o':'o','F':'r','rb':'s','G':'t','x':'u','ch':'v','y':'y','xt':'z','o..':'ö','o"':'ő','x..':'ü','Q':'?'}
R="""S 3b sl ch 3b rb T o wv 2b 2s S 2b 3s G x sl 2b G o 3s
ts o lp y rb xt 3b F 3b 2s € rb 3b rb 3b 2s 3s 3b lp 3b F S 3b xt
G x.. 2s S 3b ts ts 3b 2s 2b S o F G 3b 3s 3b G 3b S 3b xt G
wv 2b 2s y G crv T 3b 2s rb xt 3b ts G 3b 3s 3b G 3b rb 3s 3b lp
2s 3b 3s wv 2b G 2b 3s sl 3b 3s 3b lp T o wv 2b 2s S 2b 3s
rb 3b 2b xt x sl ch 2b F wv o T 2b o.. G rb xt o.. F
2b T x wv G 3b wv x G o wv T 2b F 2b crv rb
6 3b ch crv G 3b S 2b G 3b 3s G o" S 2b ts o wv
2s 2b T 2b 6 2b 2b G 3b 3s 3b G 3b rb x G 2b 2s
3b wv 3s 3b 2s G 3b 3s 2b rb F F 2b T S G 2b 2s y 2b
F 2b 2b ts o wv 2s 2b lp y 6 2b G 2b 2s rb xt o wv
G 2b S 3b 2s crv rb o G 3s 2b F 2b sl G 2b 3s Q o
F 2b crv 2b rb 3b lp 3b sl 3b S wv 2b 2s y 2b crv
3b rb + 3b wv 3b rb 3b lp 3b crv S 3b wv 3s x wv 2b G
G x 2s S 3b sl 3b rb T o wv 2b 2s S 2b 3s 3s 3b rb
x T rb 2b lp o G 2s 3b 3s crv F ts 2b G o S
3s crv 2s G ts o lp y 2s 3b 3s G x sl o 3s
3s 3b sl crv lp G 2b F 2b rb G F 2b T S sl 3b 2b 3s crv
3b xt G crv wv 3b G crv 2s 3b 3s 6 2b T 2b S 2b F 3s 3b sl crv lp
G 2b F G 6 3b bb 3b rb rb o F 2b crv G ch 2b F ch 2b
crv rb G 3b 2s ch 3b wv 3b 2b ch crv rb xt o 2s G wv 2b G 2b rb crv lp
3b sl 3b rb 3b 3s""".split('\n')
mine=[[KEY[t] for t in r.split()] for r in R]
for i,r in enumerate(mine,1): print(f'{i:02d}',''.join(r))
c=collections.Counter(t for r in R for t in r.split()); print(sum(c.values()),'signs',sorted(c.items(),key=lambda a:-a[1]))
# compare with solver ledger, flattened
L=[]
for l in open('work/ledger-opus.txt',encoding='utf-8'):
    if l.startswith('#') or not l.strip(): continue
    L.append(l.split()[1:])
m={'F':'r',')':'s','X':'u','Z':'z','6':'b','+':'f','HH':'H','PP':'H','DD':'d','CS':'cs','NINE':'?'}
def d(t):
    b,_,a=t.partition(':'); b=b.strip('[]'); s=m.get(b,b.lower())
    return {'':s,'U':{'o':'ö','u':'ü'}.get(s,s),'DA':'ő'}[a]
sol=[d(t) for r in L for t in r]; me=[t for r in mine for t in r]
print('flat equal:',sol==me,len(sol),len(me))
for i,(a,b) in enumerate(zip(sol,me)):
    if a!=b: print(i,a,b);break
print('row lengths solver',[len(r) for r in L]); print('row lengths mine  ',[len(r) for r in mine])
t=''.join(me)
for w in ['jolankam','temet','strajk','rrajk','nem','medig','hogy']: print(w,len(re.findall(w,t)))
