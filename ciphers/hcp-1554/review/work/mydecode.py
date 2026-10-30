import sys,re
K={'1':'y','2':'u','3':'o','4':'i','5':'e','6':'a','8':'l','q':'z','g':'k','f':'v','h':'r','t':'d','r':'h','c':'s','s':'c','n':'m','m':'n','p':'b','b':'p','d':'t','y':'j','H':'ch','v':'f'}
src=open(sys.argv[1],encoding='utf-8').read().splitlines()
lit=open(sys.argv[2],encoding='utf-8').read().splitlines()
from collections import Counter
cnt=Counter(); n=0
for i,l in enumerate(src):
    out=[];j=0
    while j<len(l):
        if l[j]=='⟦':
            k=l.index('⟧',j);out.append(l[j:k+1]);j=k+1;continue
        if l[j]=='[':
            k=l.index(']',j);out.append(l[j:k+1]);j=k+1;continue
        ch=l[j]
        if ch in K: out.append(K[ch]);cnt[ch]+=1;n+=1
        else: out.append(ch)
        j+=1
    s=''.join(out)
    L=lit[i].split(': ',1)[1] if ': ' in lit[i] else lit[i]
    print('OK ' if s==L else 'DIFF', s)
print('units',n,'classes',len(cnt),sorted(set(K)-set(cnt)))
print(sorted(cnt.items(),key=lambda x:-x[1]))
