from pathlib import Path
import json,hashlib
b=Path(__file__).resolve().parent;s=(b/'experiments.py').read_text();ns={'__file__':str(b/'experiments.py')};exec(s[:s.index('records=[]')],ns);r=b.parents[1];source=r/'batches/kryha373-collation-sol61/ciphertext650.txt';inp=b/'target650-latest.txt';
if not inp.exists():inp.write_bytes(source.read_bytes())
ct=inp.read_text().strip();assert len(ct)==650
cfg=b/'m23-original-cfg.txt';cfg.write_text((b/'known-rings-coordinates.txt').read_text().strip()+' 1\n');cases=[dict(label='m23-swap0-sign1',m=23,P=ns['baseP'],O=ns['baseO'],S=1,cfg=cfg)]
for row in json.load(open(b/'experiments-results.json')):
 z=row['blind_best'];cases.append(dict(label=row['label'],m=z['m'],P=z['P'],O=z['O'],S=z['displacement_sign'],cfg=b/(row['label']+'-cfg.txt')))
records=[]
for c in cases:
 qs=ns['run'](c['cfg'],inp,b/(c['label']+'-target-latest-beam.txt'),c['m']);vs=[ns['verify'](ct,q,c['P'],c['O'],c['S'],c['m'])for q in qs[:20]];records.append(dict(label=c['label'],candidates=vs));print(c['label'],vs[0]['score'],vs[0]['plaintext'][:80],flush=True);(b/'latest-variant-results.json').write_text(json.dumps(dict(source_snapshot_sha256=hashlib.sha256(inp.read_bytes()).hexdigest(),source='batches/kryha373-collation-sol61/ciphertext650.txt',configurations=records),indent=2)+'\n')
