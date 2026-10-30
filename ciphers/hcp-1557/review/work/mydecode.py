import sys,re
K={'1':'y','2':'u','3':'o','4':'i','5':'e','6':'a','8':'l','q':'z','g':'k','f':'v','h':'r','t':'d','r':'h','c':'s','s':'c','n':'m','m':'n','p':'b','b':'p','d':'t','y':'j','H':'ch'}
t=open(sys.argv[1]).read()
out=[];unk=set();n=0
i=0
while i<len(t):
    if t.startswith('{U1}',i): out.append('{U1}');i+=4;continue
    c=t[i]
    if c in K: out.append(K[c]);n+=1
    elif c.isalnum(): unk.add(c);out.append('?')
    else: out.append(c)
    i+=1
print(''.join(out));print('units',n,'unmapped',unk)
