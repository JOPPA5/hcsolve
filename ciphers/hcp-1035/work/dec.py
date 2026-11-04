import sys
A="ABCDEFGHIKLMNOPQRSTUVWXYZ"  # J omitted: 1..25
def d(tok):
    out=[]
    for w in tok.split('-'):
        s=''
        for n in w.split('.'):
            n=n.strip()
            if not n: continue
            s+= A[int(n)-1] if n.isdigit() and 1<=int(n)<=25 else '['+n+']'
        out.append(s)
    return ' '.join(out)
for a in sys.argv[1:]: print(a,'=>',d(a))
