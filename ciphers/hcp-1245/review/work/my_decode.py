K=dict(zip("3b 2b six ds sect wave 3s 2t loop fbar bowl gam cross zc chev hook invT dcurve lowy gysign opp".split(),
 "e a b d k l m n o r s t u z v g j i y gy cs".split()))
K.update({'2s':'d','2s?':'?','BLOT':'?','BLOTy':'?y'})
o=[]
for l in open('my_ledger.txt'):
    s=''
    for t in l.split():
        if t=='|':continue
        s+= t[1].lower() if t[0]=='L' else K[t]
    o.append(s); print(s)
