from pathlib import Path
import importlib.util,json,hashlib,os
B=Path(__file__).resolve().parent;(B/'owned-pid.txt').write_text(str(os.getpid())+'\n')
rows=json.loads(Path('batches/repeat369-365-sol61/closest-inventory.json').read_text())
dedup={}
for row in rows:dedup.setdefault(row['plaintext'],[]).append(row)
assert len(dedup)==2
preferred=next(row for row in rows if row['first_sentence_X']==1 and row['second_sentence_X']==1)
alternative=next(group[0]for p,group in dedup.items()if p!=preferred['plaintext'])
assert alternative['first_sentence_X']==0 and alternative['plaintext'].endswith('xxxxx')
assert len(alternative['plaintext'])==110 and alternative['ciphertext']==preferred['ciphertext']
(B/'preparation-dedup.json').write_text(json.dumps([dict(plaintext=p,source_rows=group,preferred_already_tested=p==preferred['plaintext'])for p,group in dedup.items()],indent=2)+'\n')
(B/'alternative-preparation.json').write_text(json.dumps(alternative,indent=2)+'\n')
def save(name,obj):(B/(name+'.json')).write_text(json.dumps(obj,indent=2)+'\n')
# Clone only the already calibrated native definitions; do not run its control/old target.
native=Path('batches/r369-native-main/run.py').read_text().split('rows=json.loads((root/')[0]
native=native.replace('def run_case(name,p,c,cap=10):','def run_case(name,p,c,cap=10,blocked_keys=None):')
native=native.replace('build_seconds=time.monotonic()-at;rows=[]','build_seconds=time.monotonic()-at;rows=[]\n    if blocked_keys:solver.add(z3.Or(*[z3.Not(rank[j][col][r])for j,key in enumerate(blocked_keys)for r,col in enumerate(key)]))')
(B/'native.py').write_text(native)
sp=importlib.util.spec_from_file_location('native',B/'native.py');n=importlib.util.module_from_spec(sp);sp.loader.exec_module(n)
common=n.run_case('common-target',alternative['plaintext'],alternative['ciphertext'],cap=15)
if any(r['status']=='sat'for r in common):
 hit=next(r for r in common if r['status']=='sat');n.run_case('common-second-witness',alternative['plaintext'],alternative['ciphertext'],cap=10,blocked_keys=hit['keys'])
progressive=Path('batches/r369-regular22-next-sol61/progressive/engine.py').read_text();(B/'progressive.py').write_text(progressive)
sp=importlib.util.spec_from_file_location('progressive',B/'progressive.py');e=importlib.util.module_from_spec(sp);sp.loader.exec_module(e)
result=e.solve(alternative['plaintext'],alternative['ciphertext'],seconds=120);result['conditional_preparation']=alternative;save('progressive-target',result);print('progressive target',result['status'],flush=True)
if result['status']=='sat':save('progressive-second-witness',e.solve(alternative['plaintext'],alternative['ciphertext'],seconds=60,blocked_keys=result['keys']))
sources=[Path('ciphers/hcp-369/source/cryptogram.jpg'),Path('batches/solved-context-main/365/plaintext.jpg'),Path('batches/r369-native-main/run.py'),Path('batches/r369-regular22-next-sol61/progressive/engine.py')]
save('hashes',{str(p):hashlib.sha256(p.read_bytes()).hexdigest()for p in sources})
