from pathlib import Path
import json
b=Path(__file__).resolve().parent
source=(b/'run-counts.py').read_text();ns={'__file__':str(b/'run-counts.py')};exec(source[:source.index('controls=json.load')],ns)
records=[]
for name in ['controls.json','count-controls.json','controls-j.json']:
 for c in json.load(open(b/name)):
  m=c.get('m',23);hs=','.join(map(str,c['holes']))+',';row=['0',str(c['holes'][0]),str(c['initial_displacement']),hs,c['plaintext']];v=ns['verify'](c['ciphertext'],row,m);records.append(dict(file=name,label=c.get('label',f'm{m}'),length=len(c['plaintext']),independent_absolute_inverse_and_adjacent_reencryption=True))
(b/'planted-control-verification.json').write_text(json.dumps(records,indent=2)+'\n');print('independently verified',len(records),'controls')
