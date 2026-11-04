import re,sys
# independent: key derived by me from Heute/sende/Ansichten/von/Brueckenau/linke/Mitte
K=dict(zip('1234567890','aeiouelmnrs'.replace('el','l',1)))
K=dict(zip('1234567890',['a','e','i','o','u','l','m','n','r','s']))
lines=[l.rstrip('\n') for l in open(sys.argv[1]) if l.strip() and not l.startswith('#')]
used=set()
for l in lines:
    if l.startswith('@'): print(l[1:]); continue
    l=re.sub(r'\[[^\]]*\]','',l); l=l.replace('5^','ü')
    out=re.sub(r'\{([^}]*)\}',lambda m:'<'+m.group(1)+'>',l)
    parts=re.split(r'(<[^>]*>)',out)
    s=''.join(p[1:-1] if p.startswith('<') else ''.join(K.get(c,c) for c in p) for p in parts)
    used|=set(c for p in parts if not p.startswith('<') for c in p if c.isdigit())
    print(s)
print('digits used:',sorted(used))
