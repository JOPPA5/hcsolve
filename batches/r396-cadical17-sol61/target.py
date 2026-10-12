from run import *
from concurrent.futures import ThreadPoolExecutor,as_completed
from pysat.formula import CNF
from collections import Counter

def error_witness(model,names,p,raw,w):
 yes=set(x for x in model if x>0);changed=[int(name[7:])for name,v in names.items()if name.startswith('errorPF')and v in yes];assert len(changed)==1;at=changed[0];assert raw[at]=='p';selected=raw[:at]+'f'+raw[at+1:];r=witness(model,names,p,selected,w);literal=inverse(raw,r['keys']);assert encode(literal,r['keys'])==raw;diff=[i for i,(a,c)in enumerate(zip(literal,p))if a!=c];assert len(diff)==1 and literal[diff[0]]=='p'and p[diff[0]]=='f';r.update(raw_literal_plaintext=literal,raw_literal_reencode_exact=True,selected_ciphertext=selected,ciphertext_P_to_F_position1=at+1,plaintext_literal_P_instead_of_F_position1=diff[0]+1);return r

def audit_errors():
 p='fppaaaaa';w=3;outputs={False:{},True:{}}
 for prog in [False,True]:
  for n in range(1,2 if prog else 4):
   orders=[[k for k in permutations(range(w))if k.index(0)==n-1+(st if prog else 0)]for st in range(3)]
   for ks in product(*orders):
    ct=encode(p,ks);raw=ct.replace('f','p');outputs[prog].setdefault(raw,set()).add(n)
 cs=sorted(set(''.join(x)for x in permutations('pppaaaaa')));rows=[]
 for prog in [False,True]:
  for c in cs:
   _,names,clauses,_=cnf(p,c,w,progressive=prog,errorPF=True)
   for backend in ['cadical195','cadical300']:
    with Solver(name=backend,bootstrap_with=clauses)as s:
     for n in range(1,2 if prog else 4):
      r=s.solve(assumptions=[names[f'r0_0_{n-1}']]);assert r==(n in outputs[prog].get(c,set()))
      if r:error_witness(s.get_model(),names,p,c,w)
      rows.append(dict(progressive=prog,c=c,n=n,backend=backend,sat=r))
 (b/'error-progressive-audit.json').write_text(json.dumps(dict(cases=len(rows),cipher_inventory_permutations=len(cs),all_agree_exhaustive_key_reference=True,all_SAT_literal_error_witnesses_exact=True,rows=rows),indent=2)+'\n');print('error/progressive audit PASS',len(rows),flush=True)
def target_worker(mode,n):
 inp=json.loads((b/'actual-input.json').read_text());p,raw=inp['p'],inp['raw387_omit8'];names=json.loads((b/f'actual-{mode}-names.json').read_text());formula=CNF(from_file=str(b/f'actual-{mode}.cnf'))
 with Solver(name='cadical195',bootstrap_with=formula.clauses,use_timer=True)as s:
  s.conf_budget(500000);t=time.monotonic();status=s.solve_limited(assumptions=[names[f'r0_0_{n-1}']]);r=dict(mode=mode,n=n,status='sat'if status is True else'unsat'if status is False else'unknown',seconds=time.monotonic()-t,conflict_budget=500000,backend='cadical195',stats=s.accum_stats(),source_original387=True,omitted_group1=8,omitted_group='DWJPM',oneP_F_hypothesis=True)
  if status:r.update(error_witness(s.get_model(),names,p,raw,17))
  (b/f'actual-{mode}-{n}.json').write_text(json.dumps(r,indent=2)+'\n');print('actual',mode,n,r['status'],flush=True)
def bounded(case):
 mode,n=case;f=b/f'actual-{mode}-{n}.json'
 if f.exists():return json.loads(f.read_text())
 proc=mp.Process(target=target_worker,args=(mode,n));proc.start();proc.join(45)
 if proc.is_alive():proc.terminate();proc.join();f.write_text(json.dumps(dict(mode=mode,n=n,status='unknown',worker_wall_cap_seconds=45,process_terminated=True,conflict_budget=500000,backend='cadical195'))+'\n');print('actual wallcap',mode,n,flush=True)
 if not f.exists():raise RuntimeError(f'worker failed:{mode} {n},exit{proc.exitcode}')
 return json.loads(f.read_text())
if __name__=='__main__':
 if not(b/'error-progressive-audit.json').exists():audit_errors()
 assert json.loads((b/'cadical195-deep-conditioned.json').read_text())['status']=='sat';src=Path('batches/repeat396-387-sol61');p=(src/'preferred-prepared-plaintext50.txt').read_text().strip();case=json.loads((src/'closest-inventory.json').read_text())[0];raw=case['ciphertext'];positions=[i for i,ch in enumerate(raw)if ch=='p'];variants=[raw[:i]+'f'+raw[i+1:]for i in positions];assert positions==[2,19,22]and all(Counter(v)==Counter(p)for v in variants)
 full387=''.join(ch for ch in (src/'ciphertext387.txt').read_text().lower()if'a'<=ch<='z');full396=''.join(ch for ch in (src/'ciphertext396.txt').read_text().lower()if'a'<=ch<='z');assert len(full387)==len(full396)==55;assert full387[:35]+full387[40:]==raw;raw396=full396[:35]+full396[40:];assert Counter(p)-Counter(raw396)!=Counter(f=1)
 (b/'actual-input.json').write_text(json.dumps(dict(p=p,raw387_omit8=raw,raw396_omit8=raw396,omitted_group1=8,oneP_F_variants=variants,variant_positions1=[i+1 for i in positions],source396_preferred_incompatible_with_oneP_F_inventory=True,source_hashes={str(src/n):hashlib.sha256((src/n).read_bytes()).hexdigest()for n in ['ciphertext387.txt','ciphertext396.txt','preferred-prepared-plaintext50.txt','closest-inventory.json']},sentenceX_inventory_incompatible=True),indent=2)+'\n')
 for mode,prog in [('common',False),('progressive',True)]:
  d,names,clauses,bt=cnf(p,raw,progressive=prog,errorPF=True);(b/f'actual-{mode}.cnf').write_text(d);(b/f'actual-{mode}-names.json').write_text(json.dumps(names));print('actual CNF',mode,len(clauses),round(bt,2),flush=True)
 cases=[(m,n)for m,stop in [('common',18),('progressive',16)]for n in range(1,stop)];results=[]
 with ThreadPoolExecutor(max_workers=2)as pool:
  for future in as_completed([pool.submit(bounded,case)for case in cases]):
   r=future.result();results.append(r);(b/'actual-results.json').write_text(json.dumps(results,indent=2)+'\n')
 (b/'actual-summary.json').write_text(json.dumps(dict(cases=len(results),statuses=dict(Counter(r['status']for r in results)),expected=32),indent=2)+'\n')
