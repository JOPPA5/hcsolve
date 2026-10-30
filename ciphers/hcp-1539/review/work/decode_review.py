import sys
key={'1':'y','2':'u','3':'o','4':'i','5':'e','6':'a','8':'l','q':'z','g':'k','f':'v','h':'r','t':'d','r':'h','c':'s','s':'c','n':'m','m':'n','p':'b','b':'p','d':'t','y':'j','H':'ch'}
import re
t=open(sys.argv[1],encoding='utf-8').read()
unk=set()
def dec(s):
    out=[];i=0
    while i<len(s):
        ch=s[i]
        if ch=='{':
            j=s.index('}',i); alts=s[i+1:j].split('|'); out.append('{'+'|'.join(key[a] for a in alts)+'}'); i=j+1; continue
        if ch in key: out.append(key[ch])
        elif ch.isalnum(): unk.add(ch); out.append('?')
        else: out.append(ch)
        i+=1
    return ''.join(out)
for line in t.splitlines(): print(dec(line))
print('unknown symbols:',unk)
