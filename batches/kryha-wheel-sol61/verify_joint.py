from pathlib import Path
import json
p=Path(__file__).resolve().parent;f=p/'control-m26';ls=(f/'joint-result.txt').read_text().splitlines();text=ls[0].split()[1];plain=(f/'plaintext.txt').read_text().strip();P=[int(x) for x in ls[1].split(',') if x];O=[int(x) for x in ls[2].split(',') if x];tail=ls[3].split();stops=[int(x) for x in tail[0].split(',') if x];phase=int(tail[1]);coords=json.loads((p/'wheel52.json').read_text())['unwrapped_effective_coordinates'];I={c:i for i,c in enumerate(P)};inv={x:i for i,x in enumerate(O)};enc=[];origin=coords[stops[phase]-1]
for i,c in enumerate(text):
 D=coords[stops[(phase+i)%26]-1]+179*((phase+i)//26)-origin;enc.append(chr(97+inv[(I[ord(c)-97]+D)%26]))
assert ''.join(enc)==(f/'ciphertext.txt').read_text().strip()
r=dict(language_score=float(ls[0].split()[0]),control_matches=sum(a==b for a,b in zip(text,plain)),exact_control=text==plain,reencryption_exact=True,seed_selection='highest language score only',input_slots=P,output_positions=O,active_holes=stops,phase=phase,scope='stop count 26 given; mask, phase and rings unknown',budget='8x100000 joint proposals')
(f/'joint-verification.json').write_text(json.dumps(r,indent=2));print(r['exact_control'],r['control_matches'],r['language_score'])
