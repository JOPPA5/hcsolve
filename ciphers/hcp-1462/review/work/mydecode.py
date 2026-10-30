import sys
lines=[l.strip() for l in open(sys.argv[1]) if l.strip() and not l.startswith('#')]
n=0
for c in lines:
    c=''.join(ch for ch in c if ch.isalpha())
    if c.startswith('PS'): c=c[2:]
    out=[];i,j=0,len(c)-1;f=True
    while i<=j:
        if f: out.append(c[i]);i+=1
        else: out.append(c[j]);j-=1
        f=not f
    n+=len(c);print(c,''.join(out))
print(n)
