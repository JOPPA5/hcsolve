# independent decoder: own key table typed from the reviewer's reading of the sister key, not imported from the solver
import re,sys
K=dict(zip("0 0, 1 1. 1: 1' .1 :1 1, 2 2, 2. 3 3, 3. 4 4, 4. 5 5, 5. 6 6, 6. 7 7, 7. 8 8, 9 9,".split(),
 "o ö i a e á u ü b c cs é d r v f g gy h l ly j n ny k s sz m t p z".split()))
out=[];c={}
for l in open(sys.argv[1],encoding='utf8'):
    if l.startswith('#') or not l.strip(): continue
    line=[]
    for t in l.split():
        if t=='/': line.append(' ');continue
        if t in '!()-': line.append(t if t=='-' else '');continue
        t=re.sub(r'\{.*\}','',t)
        c[t]=c.get(t,0)+1; line.append(K[t])
    out.append(''.join(line))
print('\n'.join(out)); print(sum(c.values()),len(c)); print(sorted(c.items(),key=lambda x:-x[1]))
print('unused key signs',set(K)-set(c))
