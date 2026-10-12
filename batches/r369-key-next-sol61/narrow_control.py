from pathlib import Path
import importlib.util,json,random
B=Path(__file__).resolve().parent
# Concrete refinement: inventory proves that a one-substitution channel,
# under this exact prepared text, must be N in predicted cipher vs literal U.
source=Path('batches/r364-cpsat-main/solve.py').read_text()
needle='m.add(sum(mismatch)<=errors)'
source=source.replace(needle,needle+'\n  for v,c in zip(out,cipher):\n   if c=="u":m.add_allowed_assignments([v],[[20],[13]])\n   else:m.add(v==ord(c)-97)')
(B/'narrow_engine.py').write_text(source)
sp=importlib.util.spec_from_file_location('narrow',B/'narrow_engine.py');engine=importlib.util.module_from_spec(sp);sp.loader.exec_module(engine)
truth=json.loads((B/'control-truth.json').read_text());c=truth['ciphertext'];at=c.index('n');bad=c[:at]+'u'+c[at+1:]
truth.update(corrupted_ciphertext=bad,error_index0=at,error_channel='predicted N -> observed U')
(B/'narrow-control-truth.json').write_text(json.dumps(truth,indent=2)+'\n')
for name,keys,cap in [('known',truth['keys'],10),('blind',None,60)]:
 result=engine.solve(truth['plaintext'],bad,[21,19,20],seconds=cap,errors=1,known_keys=keys)
 (B/('narrow-control-'+name+'.json')).write_text(json.dumps(result,indent=2)+'\n');print(name,result['status'],flush=True)
