from pathlib import Path
import json,subprocess
p=Path(__file__).resolve().parent;key=json.loads((p/'ring-control-key.json').read_text());plain=(p/'ring-control-plain.txt').read_text().strip();ct=(p/'ring-control-cipher.txt').read_text().strip();az=''.join(chr(97+key['output_positions'][ord(c)-97])for c in ct);(p/'ring-az-output.txt').write_text(' '.join(map(str,range(26)))+'\n');exe=p/'ring_attack_known_output';controls=[]
def run(name,s,phase,sign):
 f=p/(name+'.txt');f.write_text(s+'\n');out=subprocess.check_output([str(exe),str(p),str(f),str(phase),str(sign),str(p/'ring-az-output.txt')],text=True);(p/(name+'-result.txt')).write_text(out);x=out.splitlines();return dict(score=float(x[0].split()[0]),plaintext=x[0].split()[1],input_slots=[int(v)for v in x[1].split(',')if v],output_positions=[int(v)for v in x[2].split(',')if v])
for drop in (0,5,20):
 r=run(f'ring-az-control-drop{drop}',az[drop:],(6+drop)%17,-1);r.update(drop=drop,exact=r['plaintext']==plain[drop:]);controls.append(r);print('AZCONTROL',drop,r['exact'],flush=True);assert r['exact']
(p/'ring-az-controls.json').write_text(json.dumps(controls,indent=2));body=''.join((p/'transcription.txt').read_text().split()).lower();rows=[]
for drop in (0,5,20):
 for phase in range(17):
  for sign in (-1,1):
   r=run(f'ring-az-target-drop{drop}-phase{phase}-sign{sign}',body[drop:],phase,sign);r.update(drop=drop,phase=phase,sign=sign);rows.append(r);print('AZTARGET',drop,phase,sign,r['score'],flush=True);(p/'ring-az-target-results.json').write_text(json.dumps(rows,indent=2))
