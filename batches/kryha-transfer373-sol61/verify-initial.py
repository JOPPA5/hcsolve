from pathlib import Path
import json
b=Path(__file__).resolve().parent;s=(b/'experiments.py').read_text();ns={'__file__':str(b/'experiments.py')};exec(s[:s.index('records=[]')],ns);P=ns['baseP'];O=ns['baseO'];out=[]
for c in json.load(open(b/'controls.json')):
 a=sorted((x.split()for x in (b/(c['label']+'-beam128.txt')).read_text().splitlines()),key=lambda q:float(q[0]),reverse=True);v=ns['verify'](c['ciphertext'],a[0],P,O,1,23);assert v['plaintext']==c['plaintext'];v.update(label=c['label'],whole_exact=650,mask_exact=v['holes']==c['holes'],offset_exact=v['initial_displacement']==c['initial_displacement']);out.append(v)
(b/'control-verification.json').write_text(json.dumps(out,indent=2)+'\n');print('Two full650 controls inverse/re-encryption pass')
