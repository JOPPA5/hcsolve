from pathlib import Path
import importlib.util,json,random,os
B=Path(__file__).resolve().parent
(B/'owned-pid.txt').write_text(str(os.getpid())+'\n')
source=Path('batches/r369-key-next-sol61/narrow_engine.py').read_text()
source=source.replace('hint_keys=None):','hint_keys=None,blocked_keys=None):')
source=source.replace('validation=m.validate();', 'if blocked_keys:\n  differences=[]\n  for starts,key,w in zip(allstarts,blocked_keys,widths):\n   q,r=divmod(N,w);at=0\n   for col in key:\n    different=m.new_bool_var(f"block{w}_{col}");m.add(starts[col]!=at).only_enforce_if(different);m.add(starts[col]==at).only_enforce_if(different.Not());differences.append(different);at+=q+(col<r)\n  m.add_bool_or(differences)\n validation=m.validate();')
source=source.replace('allstarts=[]','allstarts=[]\n if isinstance(alignments,str):\n  progressive=alignments=="progressive_unknown"\n  shared=m.new_int_var(1,min(w-j if progressive else w for j,w in enumerate(widths)),"unknown_n")\n  alignments=[shared+j if progressive else shared for j in range(len(widths))]')
source=source.replace('m.add(sum(before)==alignments[j]-1)','m.add(sum(before)==alignments[j]-1)\n   # Exact packed boundary: q preceding chunks plus one per preceding long column.\n   m.add(starts[0]==q*(alignments[j]-1)+sum(before[:max(0,r-1)]))')
source=source.replace('alignments=alignments,ortools_version=', 'alignments="shared_or_progressive_unknown" if alignments and not isinstance(alignments[0],int) else alignments,ortools_version=')
source=source.replace('if alignments:assert all(k.index(0)+1==n for k,n in zip(keys,alignments))','if alignments:\n   resolved=[n if isinstance(n,int) else solver.value(n) for n in alignments]\n   assert all(k.index(0)+1==n for k,n in zip(keys,resolved))\n   result["resolved_alignments"]=resolved')
(B/'engine.py').write_text(source)
sp=importlib.util.spec_from_file_location('aligned',B/'engine.py');engine=importlib.util.module_from_spec(sp);sp.loader.exec_module(engine)
def save(name,obj):(B/(name+'.json')).write_text(json.dumps(obj,indent=2)+'\n')
widths=[21,19,20];p=('overtezajtradopoludniaspolahlivostnovehospojeniaaposlitepresnupisomnuzpravuostavedokladovpredodchodom').ljust(110,'x');assert len(p)==110
for mode,seed in [('common_unknown',36961201),('progressive_unknown',36961202)]:
 rng=random.Random(seed);n=rng.randrange(1,18);keys=[]
 for j,w in enumerate(widths):
  key=list(range(1,w));rng.shuffle(key);key.insert(n-1+(j if mode=='progressive_unknown' else 0),0);keys.append(key)
 c=p
 for key in keys:c=engine.enc(c,key)
 at=c.index('n');bad=c[:at]+'u'+c[at+1:]
 save(mode+'-truth',dict(plaintext=p,ciphertext=c,observed_ciphertext=bad,keys=keys,n=n,error_position1=at+1,seed=seed,mode=mode))
 known=engine.solve(p,bad,widths,seconds=15,errors=1,alignments=mode,known_keys=keys);save(mode+'-known',known);print(mode,'known',known['status'],flush=True)
 blind=engine.solve(p,bad,widths,seconds=120,errors=1,alignments=mode);save(mode+'-blind',blind);print(mode,'blind',blind['status'],flush=True)
 if blind['status'] in ['OPTIMAL','FEASIBLE']:
  blind['all_planted_keys_recovered']=blind['keys']==keys;save(mode+'-blind',blind)
  second=engine.solve(p,bad,widths,seconds=60,errors=1,alignments=mode,blocked_keys=blind['keys']);save(mode+'-second-witness',second)
  rows=json.loads(Path('batches/repeat369-365-sol61/closest-inventory.json').read_text());row=next(x for x in rows if x['first_sentence_X']==1 and x['second_sentence_X']==1)
  result=engine.solve(row['plaintext'],row['ciphertext'],widths,seconds=120,errors=1,alignments=mode);result.update(preparation=row,source_error_conditional=True);save(mode+'-target',result);print(mode,'target',result['status'],flush=True)
