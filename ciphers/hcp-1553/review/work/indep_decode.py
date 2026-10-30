import sys
# independent key, written from hcp-1545 family key (7/y both J here; H = CH; K = G proposed)
K={'1':'y','2':'u','3':'o','4':'i','5':'e','6':'a','7':'j','y':'j','8':'l','b':'p','c':'s','d':'t',
   'f':'v','g':'k','h':'r','m':'n','n':'m','p':'b','q':'z','r':'h','s':'c','t':'d','H':'ch','K':'g'}
txt=open(sys.argv[1]).read()
import re
out=[]
i=0
while i<len(txt):
    if txt[i]=='<':
        j=txt.index('>',i); tok=txt[i+1:j]
        out.append(K.get(tok,'['+tok+']')); i=j+1; continue
    ch=txt[i]
    out.append(K.get(ch,ch) if ch.isalnum() else ch); i+=1
print(''.join(out))
