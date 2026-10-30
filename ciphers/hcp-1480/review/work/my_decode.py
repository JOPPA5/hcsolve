import sys, collections
k=dict(tri='D',sq='E',circ='A',div='R',vdown='S',rect='T',x='I',xcirc='J',cup='U',lowc='C',
wave='W',rtri='H',bar='L',lt='O',dotlt='O',caret='V',two='N',sqx='K',arch='Y',tee='M')
inv=collections.defaultdict(set)
n=0
for line in open(sys.argv[1]):
    out=[]
    for w in line.split('|'):
        t=w.split(); n+=len(t); out.append(''.join(k[s] for s in t))
        for s in t: inv[s].add(k[s])
    print(' '.join(out))
print(n,'signs; letters',len(set(k.values())),'; shape classes',len(k))
