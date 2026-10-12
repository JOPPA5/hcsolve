from pathlib import Path
import importlib.util,json,random,time
B=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('engine','batches/r364-cpsat-main/solve.py');engine=importlib.util.module_from_spec(spec);spec.loader.exec_module(engine)
def save(name,obj): (B/(name+'.json')).write_text(json.dumps(obj,indent=2)+'\n')
widths=[21,19,20]
# Fresh independently authored control. Known-key consistency is separate from blind recovery.
p=('podajihnedpresnuzpravuostavespojeniaapripravcestovnedokladypreodchodnasledujucirannouvlakovoulinkou').ljust(110,'x')
assert len(p)==110
r=random.Random(36961121);keys=[]
for w in widths:
 k=list(range(w));r.shuffle(k);keys.append(k)
c=p
for k in keys:c=engine.enc(c,k)
# Deliberate one-symbol channel error, selected independently of search.
bad=list(c);bad[37]='z' if c[37]!='z' else 'q';bad=''.join(bad)
save('control-truth',dict(plaintext=p,keys=keys,ciphertext=c,corrupted_ciphertext=bad,error_index0=37,seed=36961121))
known=engine.solve(p,bad,widths,seconds=10,errors=1,known_keys=keys);save('control-known-key',known);print('known',known['status'],flush=True)
blind=engine.solve(p,bad,widths,seconds=60,errors=1);save('control-blind',blind);print('blind',blind['status'],flush=True)
if blind['status'] not in ['OPTIMAL','FEASIBLE']:
 print('No target launched: blind calibration gate failed.',flush=True)
 raise SystemExit(0)
# Encoding already independently exhaustively audited; exploratory actual branches despite possible blind timeout.
rows=json.loads(Path('batches/repeat369-365-sol61/closest-inventory.json').read_text())
for i,row in enumerate(rows):
 if row['source']!='369':continue
 result=engine.solve(row['plaintext'],row['ciphertext'],widths,seconds=60,errors=1)
 result.update(preparation=row,exploratory=True,blind_control_status=blind['status'],source_symbol_error_hypothesis=True)
 save('target-'+str(i),result);print('target',i,result['status'],flush=True)
