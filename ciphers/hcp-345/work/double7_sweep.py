from pathlib import Path
import subprocess,json,random
p=Path(__file__).parent;d=json.loads((p/'double-controls.json').read_text());controls={};rng=random.Random(3456107)
for n in [60,65]:
 plain=d[str(n)]['plaintext'];ks=[rng.sample(range(w),w) for w in [7,6]];ct=plain
 for k in ks:ct=''.join(ct[j::len(k)] for j in k)
 path=p/f'double7-control-{n}.txt';path.write_text(ct+'\n');d[f'{n}-7-6']={'plaintext':plain,'keys':ks,'ciphertext':ct}
 out=subprocess.check_output([str(p/'double_exact'),str(p/'quadgrams.tsv'),str(path),'7'],text=True);(p/f'double7-control-{n}-new-result.txt').write_text(out)
(p/'double7-controls.json').write_text(json.dumps(d,indent=2)+'\n')
for n in [60,65]:
 z=dict(l.split(' ',1) for l in (p/f'double7-control-{n}-new-result.txt').read_text().splitlines());controls[str(n)]={'exact':z['plaintext']==d[f'{n}-7-6']['plaintext'],'evaluations':int(z['evaluations']),'score':float(z['score'])}
(p/'double7-control-report.json').write_text(json.dumps(controls,indent=2)+'\n');assert all(z['exact'] for z in controls.values())
results={}
for i in range(14):
 dest=p/f'double7-target-omit-{i}.txt'
 out=subprocess.check_output([str(p/'double_exact'),str(p/'quadgrams.tsv'),str(p/f'omit-{i}.txt'),'7'],text=True);dest.write_text(out)
 z=dict(l.split(' ',1) for l in dest.read_text().splitlines());results[str(i)]=z;print(i,z['score'],flush=True)
(p/'double7-target-report.json').write_text(json.dumps(results,indent=2)+'\n')
