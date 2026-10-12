"""Exact two regular stages and one irregular stage. No planted search hints."""
import sys,time
from collections import Counter
sys.path.insert(0,'/private/tmp/hcsolve-z3')
import z3

def enc(p,k):
    return ''.join(p[i::len(k)] for i in k)

def inv(c,k):
    p=['']*len(c);at=0
    for col in k:
        for pos in range(col,len(c),len(k)):
            p[pos]=c[at];at+=1
    assert at==len(c)
    return ''.join(p)

def build(p,c,w=22,v=21,bidirectional=False):
    N=len(p);h,rem=divmod(N,w);q,r=divmod(N,v)
    assert rem==0 and Counter(p)-Counter(c)==Counter(n=1) and Counter(c)-Counter(p)==Counter(u=1)
    s=z3.SolverFor('QF_FD');s.set(random_seed=3691221221)
    ranks=[[[z3.Bool(f'r{j}_{col}_{k}') for k in range(w)] for col in range(w)] for j in range(2)]
    for rank in ranks:
        for row in rank:s.add(z3.PbEq([(b,1) for b in row],1))
        for k in range(w):s.add(z3.PbEq([(rank[col][k],1) for col in range(w)],1))
    for k in range(w):s.add(ranks[0][0][k]==ranks[1][0][k])
    states={}
    for k in range(v+1):
        for l in range(max(0,k-(v-r)),min(k,r)+1):states[k,l]=z3.Bool(f's{k}_{l}')
        s.add(z3.PbEq([(b,1) for (kk,l),b in states.items() if kk==k],1))
    edges=[[] for _ in range(v)];byrank=[[] for _ in range(v)]
    for col in range(v):
        long=int(col<r);L=q+long
        for (k,l),state in states.items():
            if k==v or (k+1,l+long) not in states:continue
            # The chosen column cannot occur among the already selected columns.
            if long and l==r:continue
            if not long and k-l==v-r:continue
            at=q*k+l;b=z3.Bool(f'e{col}_{k}_{l}')
            edges[col].append((k,l,at,b));byrank[k].append(b)
            s.add(z3.Implies(b,z3.And(state,states[k+1,l+long])))
            if col==0:
                s.add(z3.Implies(b,ranks[0][0][k]) if k<w else z3.Not(b))
        s.add(z3.PbEq([(b,1) for k,l,at,b in edges[col]],1))
    for bits in byrank:s.add(z3.PbEq([(b,1) for b in bits],1))
    for k in range(v,w):s.add(z3.Not(ranks[0][0][k]))
    errors={i:z3.Bool(f'err{i}') for i,x in enumerate(c) if x=='u'}
    s.add(z3.PbEq([(b,1) for b in errors.values()],1))
    supports={}
    for col in range(v):
        for row in range(q+int(col<r)):
            for x in set(p):
                sup=[]
                for k,l,at,b in edges[col]:
                    dst=at+row
                    if c[dst]==x:sup.append(z3.And(b,z3.Not(errors[dst])) if dst in errors else b)
                    elif x=='n' and c[dst]=='u':sup.append(z3.And(b,errors[dst]))
                supports[col,row,x]=sup
    clauses=0
    for i,x in enumerate(p):
        col0,row0=i%w,i//w
        for r0 in range(w):
            pos1=h*r0+row0;col1,row1=pos1%w,pos1//w
            for r1 in range(w):
                pos2=h*r1+row1;col2,row2=pos2%v,pos2//v
                s.add(z3.Or(z3.Not(ranks[0][col0][r0]),z3.Not(ranks[1][col1][r1]),*supports[col2,row2,x]));clauses+=1
    if bidirectional:
        for col2,opts in enumerate(edges):
            for k,l,at,b in opts:
                for row2 in range(q+int(col2<r)):
                    pos2=col2+row2*v;r1,row1=divmod(pos2,h);dst=at+row2
                    for col1 in range(w):
                        pos1=col1+row1*w;r0,row0=divmod(pos1,h);support=[]
                        for col0 in range(w):
                            src=col0+row0*w;bit=ranks[0][col0][r0]
                            if p[src]==c[dst]:support.append(z3.And(bit,z3.Not(errors[dst])) if dst in errors else bit)
                            elif p[src]=='n' and c[dst]=='u':support.append(z3.And(bit,errors[dst]))
                        s.add(z3.Or(z3.Not(b),z3.Not(ranks[1][col1][r1]),*support));clauses+=1
    return s,ranks,edges,clauses

def run(p,c,cap=8,w=22,v=21,on_row=None,bidirectional=False):
    start=time.monotonic();s,ranks,edges,clauses=build(p,c,w,v,bidirectional);construction=time.monotonic()-start;rows=[]
    for n in range(1,min(w,v)+1):
        s.set(timeout=int(cap*1000));start=time.monotonic();result=s.check(ranks[0][0][n-1]);row={'n':n,'status':str(result),'seconds':time.monotonic()-start}
        if result==z3.sat:
            m=s.model();keys=[]
            for rank in ranks:
                keys.append(sorted(range(w),key=lambda col:next(k for k,b in enumerate(rank[col]) if z3.is_true(m.eval(b)))))
            keys.append([col for k,col in sorted((k,col) for col,opts in enumerate(edges) for k,l,at,b in opts if z3.is_true(m.eval(b)))])
            assert all(key.index(0)==n-1 for key in keys)
            predicted=p
            for key in keys:predicted=enc(predicted,key)
            mismatch=[i for i,(a,b) in enumerate(zip(predicted,c)) if a!=b]
            assert len(mismatch)==1 and predicted[mismatch[0]]=='n' and c[mismatch[0]]=='u'
            decoded=predicted;literal=c
            for key in keys[::-1]:decoded=inv(decoded,key);literal=inv(literal,key)
            assert decoded==p
            check=literal
            for key in keys:check=enc(check,key)
            assert check==c
            row.update(keys=keys,predicted_ciphertext=predicted,literal_plaintext=literal,mismatch_position1=mismatch[0]+1,full_encoder_inverse_exact=True)
        elif result==z3.unknown:row['reason']=s.reason_unknown()
        rows.append(row)
        if on_row:on_row(dict(plaintext=p,ciphertext=c,widths=[w,w,v],construction_seconds=construction,clauses=clauses,rows=rows))
        if result==z3.sat:break
    return dict(plaintext=p,ciphertext=c,widths=[w,w,v],construction_seconds=construction,clauses=clauses,rows=rows)
