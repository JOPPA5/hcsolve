from pathlib import Path
import json,subprocess
b=Path(__file__).resolve().parent;r=b.parents[1];rows=json.load(open(r/'batches/kryha-two-mask-main/dp-targets.json'))
for variant in ('pixel-strong','pixel-strong-plus-moderate'):
 cts=[''.join(c.lower() for c in (r/f'batches/kryha-shift23-sol61/{n}-{variant}.txt').read_text() if c.isalpha())[20:375] for n in (350,351)]
 assert list(map(len,cts))==[355,355]
 for ix in (5,6):
  row=rows[ix];K=row['k'][20:]+row['k'][:20];inp=dict(ciphertexts=cts,O=row['output_positions'],K=K,delta=[(K[(j+1)%23]-K[j])%26 for j in range(23)],variant=variant,cycle_row=ix,absolute_crop_start=20,omitted_prefix=20,omitted_suffix=10,partial_body_hypothesis=True,source_errors_preserved=True)
  name=f'{variant}-row{ix}';(b/f'{name}-input.json').write_text(json.dumps(inp,indent=2)+'\n');subprocess.run(['python3',str(b/'run-profile.py'),str(b/f'{name}-input.json'),f'{name}-profile.txt'],check=True)
