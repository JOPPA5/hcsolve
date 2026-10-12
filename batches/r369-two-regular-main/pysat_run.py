"""Exact same Boolean family, different CDCL engine. Budgets keep UNKNOWN."""
from pathlib import Path
import sys,time,json,argparse,threading,hashlib
sys.path.insert(0,'/private/tmp/hcsolve-pysat')
from pysat.solvers import Solver
from pysat.formula import CNF
from engine import build,enc,inv,z3
b=Path(__file__).resolve().parent

def run(p,c,name='cadical300',budget=20000,w=22,v=21,reverse=False,save=None):
    at=time.monotonic();native,ranks,edges,clauses=build(p,c,w,v,reverse)
    goal=z3.Goal();goal.add(*native.assertions())
    cnfgoal=z3.Then('simplify','card2bv','bit-blast','tseitin-cnf')(goal)[0]
    text=cnfgoal.dimacs(include_names=True);cnf=CNF(from_string=text)
    ids={line.split(maxsplit=2)[2]:int(line.split()[1]) for line in text.splitlines() if line.startswith('c ')}
    build_seconds=time.monotonic()-at;rows=[]
    data=dict(plaintext=p,ciphertext=c,widths=[w,w,v],bidirectional=reverse,solver=name,budget=budget,build_seconds=build_seconds,cnf_variables=cnf.nv,cnf_clauses=len(cnf.clauses),dimacs_sha256=hashlib.sha256(text.encode()).hexdigest(),rows=rows)
    def vid(bit):return ids[str(bit)]
    with Solver(name=name,bootstrap_with=cnf.clauses,use_timer=True) as s:
        for n in range(1,min(w,v)+1):
            at=time.monotonic();timer=None
            if name.startswith('glucose'):
                timer=threading.Timer(budget,s.interrupt);timer.start()
                status=s.solve_limited(assumptions=[vid(ranks[0][0][n-1])],expect_interrupt=True)
                timer.cancel();s.clear_interrupt()
            else:
                s.conf_budget(budget);status=s.solve_limited(assumptions=[vid(ranks[0][0][n-1])])
            row=dict(n=n,status={True:'sat',False:'unsat',None:'unknown'}[status],seconds=time.monotonic()-at,stats=s.accum_stats())
            if status:
                selected=set(x for x in s.get_model() if x>0)
                keys=[]
                for rank in ranks:
                    keys.append(sorted(range(w),key=lambda col:next(k for k,bit in enumerate(rank[col]) if vid(bit) in selected)))
                keys.append([col for k,col in sorted((k,col) for col,opts in enumerate(edges) for k,l,at,bit in opts if vid(bit) in selected)])
                assert all(k.index(0)==n-1 for k in keys)
                predicted=p
                for key in keys:predicted=enc(predicted,key)
                mismatch=[i for i,(x,y) in enumerate(zip(predicted,c)) if x!=y]
                assert len(mismatch)==1 and predicted[mismatch[0]]=='n' and c[mismatch[0]]=='u'
                decoded=predicted;literal=c
                for key in keys[::-1]:decoded=inv(decoded,key);literal=inv(literal,key)
                assert decoded==p
                back=literal
                for key in keys:back=enc(back,key)
                assert back==c
                row.update(keys=keys,predicted_ciphertext=predicted,literal_plaintext=literal,mismatch_position1=mismatch[0]+1,independent_complete_encoder_inverse=True)
            rows.append(row)
            if save:
                save(data);print(name,n,row['status'],round(row['seconds'],2),flush=True)
            if status:break
    return data

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--solver',default='cadical300');ap.add_argument('--budget',type=float,default=20000);ap.add_argument('--reverse',action='store_true');args=ap.parse_args()
    truth=json.loads((b/'control-truth.json').read_text());prefix=args.solver+('-reverse' if args.reverse else '')
    def saver(name):
        return lambda data:(b/(name+'.json')).write_text(json.dumps(data,indent=2)+'\n')
    result=run(truth['plaintext'],truth['observed_ciphertext'],name=args.solver,budget=int(args.budget) if not args.solver.startswith('glucose') else args.budget,reverse=args.reverse,save=saver(prefix+'-control'))
    if not any(row['status']=='sat' for row in result['rows']):
        print('No full blind-control witness; actual target gated off',flush=True);sys.exit(0)
    rows=json.loads(Path('batches/repeat369-365-sol61/closest-inventory.json').read_text());cases={r['plaintext']:r for r in rows}
    for j,case in enumerate(cases.values()):
        run(case['plaintext'],case['ciphertext'],name=args.solver,budget=int(args.budget) if not args.solver.startswith('glucose') else args.budget,reverse=args.reverse,save=saver(prefix+'-target'+str(j)))
