# Round-2 independent decoder: own table and loop over the ledger; applies reviewer's row 20 correction; checks ledger counts and repeated words.
import re,collections
T=dict(zip('ACDEGIJKLMNOTVYZ','acdegijklmnotvyz'));T.update({'F':'r',')':'s','X':'u','6':'b','+':'f','H':'h','CS':'cs','*':'?','AE':'#','OI':'@','NH':'%'})
R={}
for l in open('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1279/work/ledger.txt',encoding='utf-8'):
    if l.strip() and l[0]!='#':
        a=l.split();R[a[0]]=a[1:]
def d(t):return T[re.sub(r'[\[\]]','',t).split(':')[0]]
for k,v in R.items():print(k,''.join(map(d,v)))
print('signs',sum(map(len,R.values())))
print('row20 sign 7:',R['20'][6],'-> A (review 2):',''.join(d('A' if i==6 else t) for i,t in enumerate(R['20'])))
s=''.join(''.join(map(d,v)) for k,v in R.items())
for w in 'hogy mert henz csak maga kivanja'.split():print(w,s.count(w))
