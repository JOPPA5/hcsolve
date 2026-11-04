import sys,re
alpha="ABCDEFGHIKLMNOPQRSTUVWXYZ"
key={i+2:c for i,c in enumerate(alpha)}
src=open(sys.argv[1]).read().splitlines()
for line in src:
    if line.startswith('#') or not line.strip(): continue
    out=[]
    for tok in re.split(r'(\s+-\s+|\s+\+|\s+)',line):
        if tok is None: continue
        if re.fullmatch(r'\s+-\s+',tok): out.append(' '); continue
        if re.fullmatch(r'\s+\+',tok): out.append(' !'); continue
        if tok.strip()=='' : out.append(' '); continue
        t=re.sub(r'\[.*?\]','',tok)
        w=''
        for n in t.split('.'):
            if not n or n in "-+": continue
            m=re.fullmatch(r'(\d+)(")?',n)
            w+=key[int(m.group(1))]+('"' if m.group(2) else '')
        out.append(w)
    print(re.sub(' +',' ',''.join(out)).strip())
