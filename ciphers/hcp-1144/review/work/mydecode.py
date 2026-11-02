# Reviewer's independent decoder. Key typed from the hcp-1174/1178/1179 tables plus the extra signs on this card,
# read as raw tokens; ~x overrides ignored so the literal drawn sign shows. Optional corrections shown separately.
import re,collections,sys
K=dict(zip("0 0, 1 1. 1: 1' 1, :1 .1 2 2, 2. 3 3, 3. 4 4, 4. 5 5, 5. 6 6, 6. 7 7, 7. 8 8, 9 9,".split(),
 "o ö i a e á b ü u c cs é d r v f g gy h l ly j n ny k s sz m t p z".split()))
rows=[l.rstrip('\n') for l in open(sys.argv[1],encoding='utf-8') if l.strip() and not l.startswith('#')]
c=collections.Counter(); tot=0
for r in rows:
    o=[]
    for t in r.replace(')',' | ').split():
        if t=='|': o.append(' ');continue
        tot+=1; c[t.split('~')[0]]+=1
        o.append(K.get(t.split('~')[0].lstrip('?'),'<%s>'%t))
    print(''.join(o))
print(tot,'signs');print(sorted(c.items(),key=lambda x:-x[1]))
print('unkeyed:',[t for t in c if t.lstrip('?') not in K])
