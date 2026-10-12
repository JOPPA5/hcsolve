from pathlib import Path
import importlib.util,json,os
B=Path(__file__).resolve().parent
(B/'direct-owned-pid.txt').write_text(str(os.getpid())+'\n')
source=Path('batches/r364-triple-next-sol61/direct.py').read_text()
source=source.replace('assert len(p)==len(c) and Counter(p)==Counter(c);','assert len(p)==len(c) and Counter(p)-Counter(c)==Counter(n=1) and Counter(c)-Counter(p)==Counter(u=1);')
source=source.replace("s=z3.SolverFor('QF_FD') if rank_partition else z3.Then('simplify','card2bv','bit-blast','sat').solver();","s=z3.SolverFor('QF_FD');")
source=source.replace('opts=[];literals=0','errors={i:z3.Bool(f"error{i}") for i,ch in enumerate(c) if ch=="u"};s.add(z3.PbEq([(v,1) for v in errors.values()],1))\n opts=[];literals=0')
source=source.replace('allowed=[V for at,V in opts[2][col2].items()if c[at+row2]==ch]','allowed=[]\n    for at,V in opts[2][col2].items():\n     pos=at+row2\n     if c[pos]==ch:allowed.append(z3.And(V,z3.Not(errors[pos])) if pos in errors else V)\n     elif ch=="n" and c[pos]=="u":allowed.append(z3.And(V,errors[pos]))')
source=source.replace('assert v==c;out.update(keys=keys,full_reencryption=True)','mis=[i for i,(a,b) in enumerate(zip(v,c)) if a!=b];assert len(mis)==1 and v[mis[0]]=="n" and c[mis[0]]=="u";out.update(keys=keys,full_reencryption=True,predicted_ciphertext=v,mismatches_index0=mis)')
source=source.replace('if reverse_support:\n','if reverse_support:raise ValueError("reverse support not implemented for one-error channel")\n if False:\n')
(B/'direct_engine.py').write_text(source)
sp=importlib.util.spec_from_file_location('direct',B/'direct_engine.py');e=importlib.util.module_from_spec(sp);sp.loader.exec_module(e)
t=json.loads((B/'common_unknown-truth.json').read_text());result=e.solve(t['plaintext'],t['observed_ciphertext'],seconds=120,common_rank=True)
if result['status']=='sat':result['all_planted_keys_recovered']=result['keys']==t['keys']
(B/'direct-common-control.json').write_text(json.dumps(result,indent=2)+'\n');print(result,flush=True)
