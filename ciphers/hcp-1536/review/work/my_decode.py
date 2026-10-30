import json,sys
base='/Users/tomaspavuk/Desktop/hcsolve/ciphers/'
# independent key from sister card hcp-1545 (family key), with y=J label and H=CH label
k=json.load(open(base+'hcp-1545/work/key.json'))
key={kk.lower() if kk.isalpha() and kk!='ř' else kk:v for kk,v in k.items()}
key['y']='J'; key['H']='CH'; key.pop('7',None); key.pop('ř',None)
d=json.load(open(base+'hcp-1536/work/transcription.json'))
from collections import Counter
c=Counter()
for r in d['rows']:
    out=''
    for ch in r['transcription']:
        if ch in key: out+=key[ch]; c[ch]+=1
        elif ch.isalnum(): out+='?'+ch+'?'
        else: out+=ch
    print(r['id'],out.replace('[U01]','[U01]'))
print(sorted(c.items()), sum(c.values()))
