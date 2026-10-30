import re
W=sorted({w.strip().lower() for w in open('/usr/share/dict/words')})
for m in ['d..r','o.d','b.y','m.ss','y.u','l..t','n.g.t','n.c.t','n.r.t','de...e','da...e']:
    r=re.compile('^'+m+'$'); c=[w for w in W if r.match(w)]
    print(m,len(c),' '.join(c[:40]))
