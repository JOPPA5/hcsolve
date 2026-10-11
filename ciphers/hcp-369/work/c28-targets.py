import json,subprocess
from pathlib import Path
p=Path(__file__).parent;out=Path('batches/c28-solvers');out.mkdir(exist_ok=True)
controls=json.loads((p/'c28-controls.json').read_text())
assert len(controls)==2 and all(x['exact_folded'] for x in controls)
rows=[]
for n in [369,367,334,332]:
 raw=Path(f'ciphers/hcp-{n}/work/transcription.txt').read_text().lower()
 c=''.join(x if x.isalpha() else '.' for x in raw if x.isalpha() or x=='?')
 for order in ['forward','reverse']:
  s=c if order=='forward' else c[::-1];f=out/f'{n}-{order}-input.txt';f.write_text(s+'\n')
  r=subprocess.run([str(p/'mono-c28'),'batches/scoring-sol61/frequency',str(f),'40'],capture_output=True,text=True)
  (out/f'{n}-{order}-result.txt').write_text(r.stdout+'\n'+r.stderr)
  fields=r.stdout.strip().split();key=fields[1];plain=fields[2];rawpt=fields[3][4:]
  row=dict(cipher=n,order=order,input=s,score=float(fields[0]),key_encoded=key,folded_plaintext=plain,plaintext=rawpt.replace('{','č').replace('|','š'),symbols=len(s),erasure_positions=[i for i,x in enumerate(s) if x=='.'])
  rows.append(row);(out/'summary.json').write_text(json.dumps(rows,indent=2,ensure_ascii=False))
  print(n,order,row['score'],row['plaintext'],flush=True)
