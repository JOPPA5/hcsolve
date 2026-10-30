import sys,json
K={'1':'y','2':'u','3':'o','4':'i','5':'e','6':'a','8':'l','b':'p','c':'s','d':'t','f':'v','g':'k','h':'r','m':'n','n':'m','p':'b','q':'z','r':'h','s':'c','t':'d','y':'j','H':'ch','F':'f'}
txt=open(sys.argv[1],encoding='utf-8').read()
out=[];unk=set()
i=0
while i<len(txt):
    if txt.startswith('⟦U1⟧',i): out.append('[U1]'); i+=4; continue
    ch=txt[i]
    if ch in K: out.append(K[ch])
    elif ch.isalnum(): unk.add(ch); out.append('?')
    else: out.append(ch)
    i+=1
print(''.join(out)); print('unmapped:',unk, file=sys.stderr)
