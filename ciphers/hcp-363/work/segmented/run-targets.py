from pathlib import Path
import subprocess,json,time
p=Path(__file__).resolve().parent;root=p.parents[3]
# The only v4 change avoids copying immutable chunk strings during proposals.
control=p/'control19-v4-results.txt'
with control.open('w') as out,(p/'control19-v4-progress.txt').open('w') as err:
 subprocess.run([str(p/'search-v4'),str(root/'batches/scoring-sol61'),str(p/'bigrams.tsv'),str(p.parent/'control-19.txt'),'19'],stdout=out,stderr=err,check=True)
expected=json.loads((p.parent/'controls.json').read_text())['control-19']['plaintext']
assert control.read_text().splitlines()[0].split()[-1]==expected
assert control.read_text()==(p/'control19-v3-results.txt').read_text()
assert (p/'control22-v4-results.txt').read_text()==(p/'control22-v3-results.txt').read_text()
inputs=[('omit3x',p/'omit-3-x.txt'),('omit25x',p/'omit-25-x.txt'),('400x',p.parent/'cipher-x.txt'),('omit3a',p/'omit-3-a.txt'),('omit25a',p/'omit-25-a.txt'),('400a',p.parent/'cipher-a.txt')]
summary={}
for width in [19,22,16,17,18,20,21]:
 for name,inp in inputs:
  dest=p/f'target-{name}-w{width}-results.txt';progress=p/f'target-{name}-w{width}-progress.txt'
  if not dest.exists() or not dest.read_text().strip():
   with dest.open('w') as out,progress.open('w') as err:
    subprocess.run([str(p/'search-v4'),str(root/'batches/scoring-sol61'),str(p/'bigrams.tsv'),str(inp),str(width)],stdout=out,stderr=err,check=True)
  summary[f'{name}-w{width}']=dest.read_text().splitlines()[0]
  (p/'target-summary.json').write_text(json.dumps(summary,indent=2)+'\n')
  print(name,width,summary[f'{name}-w{width}'],flush=True)
