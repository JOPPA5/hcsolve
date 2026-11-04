import sys,re
al="ABCDEFGHIKLMNOPQRSTUVWXYZ"
k={str(i+2):c for i,c in enumerate(al)}
for line in open(sys.argv[1]):
    out=[]
    for w in line.strip().split('-'):
        w=w.strip()
        if not w: continue
        s=''
        for n in w.split('.'):
            um='"' in n; n=n.replace('"','')
            s+=k[n]+('"' if um else '')
        out.append(s)
    print(' '.join(out))
