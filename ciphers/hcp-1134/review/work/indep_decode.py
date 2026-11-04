# Independent decoder (reviewer). J-less alphabet numbered from 2; '"' = umlaut; SZ kept literal.
import sys
alpha="ABCDEFGHIKLMNOPQRSTUVWXYZ"
key={i+2:c for i,c in enumerate(alpha)}
uml={'A':'Ä','O':'Ö','U':'Ü'}
rows=["12.10.6.3.6.19-19.4.9.2\".20.26.4.9.6.14","19.6.14.5.6-5.10.6.18-5.10.6",
"3.6.19.20.6.14-8.18.21\".19.26.6","5.6.10.14.6.14-23.21.14.19.4.9","7.21\".18-19.15.14.14.20.2.8",
"11.2.14.14-10.4.9-14.10.4.9.20","6.18.7.21\".12.12.6.14","19.21.19.10"]
n=0;used=set()
for r in rows:
    ws=[]
    for w in r.split('-'):
        s=''
        for t in w.split('.'):
            u=t.endswith('"'); v=int(t.rstrip('"')); n+=1; used.add(v)
            c=key[v]; s+=uml[c] if u else c
        ws.append(s)
    print(' '.join(ws))
print(n,'numbers; used',sorted(used))
