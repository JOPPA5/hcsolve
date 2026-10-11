from pathlib import Path
import subprocess,json
root=Path(__file__).resolve().parents[3]
g=root/'batches/scoring-sol61/german'
w=root/'ciphers/hcp-332/work'
results={}
for inp in sorted(w.glob('german-*-input.txt')):
 name=inp.stem.replace('-input','-pair')
 prefix=w/name
 subprocess.run(['python3',str(g/'anchors.py'),str(inp),str(prefix)],check=True)
 with prefix.with_suffix('.generation.txt').open('w') as f:
  subprocess.run([str(g/'pairs'),str(prefix.with_suffix('.anchors.tsv')),str(prefix.with_suffix('.seeds.txt')),'20000'],stderr=f,check=True)
 with prefix.with_suffix('.result.txt').open('w') as out,prefix.with_suffix('.progress.txt').open('w') as err:
  subprocess.run([str(g.parent/'mono-frequency-seeded-strict'),str(g),str(inp),str(prefix.with_suffix('.seeds.txt'))],stdout=out,stderr=err,check=True)
 results[name]=prefix.with_suffix('.result.txt').read_text().strip()
 print(name,results[name],flush=True)
(w/'german-pair-summary.json').write_text(json.dumps(results,indent=2)+'\n')
