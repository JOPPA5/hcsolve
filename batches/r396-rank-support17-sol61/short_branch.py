from run import *
tr=json.loads((b/'control-input.json').read_text());p,c=tr['p'],tr['c'];t=time.monotonic();s,ranks,clauses=build(p,c);bt=time.monotonic()-t;rows=[]
# Fixed source-order enumeration of final-stage short-column ranks; daily n stays unknown.
for sh in range(17):
 s.set(timeout=3000);t=time.monotonic();status=s.check(ranks[2][16][sh]);row=dict(last_short_rank=sh,status=str(status),seconds=time.monotonic()-t,common_n_unknown=True,timeout_ms=3000)
 if status==z3.sat:
  md=s.model();ks=[sorted(range(17),key=lambda col:next(rr for rr,bit in enumerate(layer[col])if z3.is_true(md.eval(bit))))for layer in ranks];pred=p;dec=c
  for k in ks:pred=enc(pred,k)
  for k in ks[::-1]:dec=inv(dec,k)
  assert pred==c and dec==p;row.update(keys=ks,p=p,c=c,n=ks[0].index(0)+1,full50_encoder_inverse_exact=True)
 elif status==z3.unknown:row['reason']=s.reason_unknown()
 rows.append(row);(b/'short-branch-results.json').write_text(json.dumps(dict(clauses=clauses,build_seconds=bt,results=rows),indent=2)+'\n');print('short',sh,status,flush=True)
 if status==z3.sat:break
