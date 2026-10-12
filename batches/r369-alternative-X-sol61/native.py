"""Independent native finite-domain regular22 rank-partition experiment.

Only the disclosed preferred published crib is supplied. No planted key hints.
Original scans and cipher dirs are read-only. Constant alignment family only.
"""
from pathlib import Path
from collections import Counter
import sys,json,time,random,os
sys.path.insert(0,'/private/tmp/hcsolve-z3')
import z3
root=Path(__file__).resolve().parents[2];out=Path(__file__).resolve().parent
(out/'owned-pid.txt').write_text(str(os.getpid())+'\n')
def encode(p,key):return ''.join(p[i]for col in key for i in range(col,len(p),len(key)))
def inverse(c,key):
    result=['']*len(c);at=0
    for col in key:
        for i in range(col,len(c),len(key)):result[i]=c[at];at+=1
    assert at==len(c)
    return ''.join(result)
def build(p,c):
    w=22;h=5;assert len(p)==len(c)==w*h
    assert Counter(p)-Counter(c)==Counter(n=1)and Counter(c)-Counter(p)==Counter(u=1)
    solver=z3.SolverFor('QF_FD');solver.set(random_seed=3696242205)
    rank=[[[z3.Bool(f'key{j}col{k}rank{r}')for r in range(w)]for k in range(w)]for j in range(3)]
    for key in rank:
        for col in key:solver.add(z3.PbEq([(x,1)for x in col],1))
        for r in range(w):solver.add(z3.PbEq([(key[k][r],1)for k in range(w)],1))
    for r in range(w):solver.add(rank[0][0][r]==rank[1][0][r],rank[0][0][r]==rank[2][0][r])
    errors={i:z3.Bool(f'error{i}')for i,x in enumerate(c)if x=='u'}
    solver.add(z3.PbEq([(x,1)for x in errors.values()],1))
    clauses=0
    for i,x in enumerate(p):
        col0,row0=i%w,i//w
        for r0 in range(w):
            pos1=h*r0+row0;col1,row1=pos1%w,pos1//w
            for r1 in range(w):
                pos2=h*r1+row1;col2,row2=pos2%w,pos2//w;support=[]
                for r2 in range(w):
                    dst=h*r2+row2;bit=rank[2][col2][r2]
                    if c[dst]==x:support.append(z3.And(bit,z3.Not(errors[dst]))if dst in errors else bit)
                    elif x=='n'and c[dst]=='u':support.append(z3.And(bit,errors[dst]))
                solver.add(z3.Or(z3.Not(rank[0][col0][r0]),z3.Not(rank[1][col1][r1]),*support));clauses+=1
    return solver,rank,clauses
def save(name,data):(out/(name+'.json')).write_text(json.dumps(data,indent=2)+'\n')
def run_case(name,p,c,cap=10,blocked_keys=None):
    at=time.monotonic();solver,rank,clauses=build(p,c);build_seconds=time.monotonic()-at;rows=[]
    if blocked_keys:solver.add(z3.Or(*[z3.Not(rank[j][col][r])for j,key in enumerate(blocked_keys)for r,col in enumerate(key)]))
    # All legal ranks in fixed source-order, not the planted unknown rank.
    for r in range(22):
        solver.set(timeout=1000*cap);at=time.monotonic();status=solver.check(rank[0][0][r]);row=dict(n=r+1,status=str(status),seconds=time.monotonic()-at)
        if status==z3.sat:
            model=solver.model();keys=[]
            for layer in rank:keys.append(sorted(range(22),key=lambda col:next(k for k,b in enumerate(layer[col])if z3.is_true(model.eval(b)))))
            encoded=p
            for key in keys:encoded=encode(encoded,key)
            mismatch=[i for i,(a,b)in enumerate(zip(encoded,c))if a!=b]
            assert len(mismatch)==1 and encoded[mismatch[0]]=='n'and c[mismatch[0]]=='u'
            decoded=encoded;literal=c
            for key in keys[::-1]:decoded=inverse(decoded,key);literal=inverse(literal,key)
            assert decoded==p and all(k.index(0)==r for k in keys)
            row.update(keys=keys,predicted_ciphertext=encoded,raw_literal_plaintext=literal,mismatch_position1=mismatch[0]+1,full110_derived_error=True,independent_inverse_exact=True)
        elif status==z3.unknown:row['reason']=solver.reason_unknown()
        rows.append(row);save(name,dict(plaintext=p,ciphertext=c,build_seconds=build_seconds,clauses=clauses,rank_assumptions_reuse_one_solver=True,ranks=rows))
        print(name,r+1,row['status'],round(row['seconds'],2),flush=True)
        if status==z3.sat:return rows
    return rows
