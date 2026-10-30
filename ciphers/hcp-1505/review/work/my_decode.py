import sys,string
alpha=string.ascii_uppercase[::-1]  # 1->Z ... 26->A
txt=open(sys.argv[1]).read().split('\n')
out=[];cnt=0
for ln in txt:
    if not ln.strip(): continue
    ws=[]
    for w in ln.split('|'):
        ns=[int(x) for x in w.split()]; cnt+=len(ns)
        ws.append(''.join(alpha[n-1] for n in ns))
    out.append(' '.join(ws))
print('\n'.join(out)); print('numbers:',cnt)
