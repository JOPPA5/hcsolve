#!/usr/bin/env python3
"""Read-only validation/decryption of a manual source-wide transcription candidate."""
from pathlib import Path
from collections import Counter
from PIL import Image
import json,hashlib,csv,io,re
R=Path(__file__).resolve().parents[1];W=R/'work';REPO=R.parents[1]
def check(name,base):
 d=json.loads((W/name).read_text())
 for p,h in d.items(): assert hashlib.sha256((base/p).read_bytes()).hexdigest()==h,p
 return len(d)
sources=check('source-sha256.json',R);references=check('reference-sha256.json',REPO);records=check('record-sha256.json',R);canonical=check('canonical-sha256.json',R)
guard=json.loads((REPO/'batches/easy-2026-10-28/cz246-251-252-source-sha256.json').read_text())
assert len(guard)==9
for p,h in json.loads((W/'source-sha256.json').read_text()).items(): assert guard['ciphers/hcp-1571/'+p]==h
key=json.loads((W/'key.json').read_text());family=json.loads((REPO/'ciphers/hcp-1520/work/key.json').read_text())
assert key=={k:v.upper() for k,v in family.items()} and len(key)==len(set(key.values()))==22
record=json.loads((W/'transcription.json').read_text());positions=[];texts=[];counts=Counter();rowcounts=[]
for row in record['rows']:
 text=''.join(key.get(c,c) for c in row['cipher']);assert text==row['plaintext'];texts.append(text)
 units=[c for c in row['cipher'] if c in key];assert len(units)==row['active_units'];rowcounts.append(len(units));counts.update(units)
 for c in row['cipher']: assert c in key or c in ' .,?!-'
 for j,c in enumerate(units,1): positions.append([str(len(positions)+1),row['id'],str(j),c,key[c]])
assert [r['id'] for r in record['rows']]==[f'R{i:02}' for i in range(1,14)]
assert rowcounts==[41,37,36,38,26,40,42,38,41,36,38,36,26]
assert len(positions)==475 and counts['H']==7 and sum(len(key[c])*n for c,n in counts.items())==482 and len(counts)==22
expected=list(csv.reader(io.StringIO((W/'positions.csv').read_text())))
assert expected[0]==['global_id','row','row_unit_index','cipher_label','plaintext'] and expected[1:]==positions
literal='\n'.join(texts)+'\n';cipher='\n'.join(r['cipher'] for r in record['rows'])+'\n'
assert literal==(W/'literal.txt').read_text() and cipher==(W/'transcription.txt').read_text()
assert re.search(r'```text\n(.*?)```',(R/'SOLUTION.md').read_text(),re.S).group(1)==literal
# Whole-plaintext inverse, independently scanning every character; CH is the longest unit.
inv={v:k for k,v in key.items()};encoded=[];i=0
while i<len(literal):
 if literal.startswith('CH',i): encoded.append(inv['CH']);i+=2
 elif literal[i] in inv: encoded.append(inv[literal[i]]);i+=1
 else:
  assert literal[i] in ' .,?!-\n';encoded.append(literal[i]);i+=1
assert ''.join(encoded)==cipher,'Full inverse differs; no per-token forward lookup used'
original=Image.open(R/'source/picture.jpg').transpose(Image.Transpose.ROTATE_270);up=Image.open(W/'upright.png')
assert original.size==up.size==(674,1024) and original.tobytes()==up.tobytes()
for row in record['rows']:
 crop=original.crop(row['bbox']);zoom=crop.resize((crop.width*3,crop.height*3),Image.Resampling.NEAREST);saved=Image.open(W/(row['id']+'-rawNN.png'))
 assert saved.size==zoom.size and saved.tobytes()==zoom.tobytes(),row['id']
controls=json.loads((W/'source-controls.json').read_text())
for box in controls['boxes']:
 crop=original.crop(box['bbox']);native=Image.open(W/box['native']);assert native.size==crop.size and native.tobytes()==crop.tobytes(),box['id']
 zoom=crop.resize((crop.width*box['scale'],crop.height*box['scale']),Image.Resampling.NEAREST);saved=Image.open(W/box['crop']);assert saved.size==zoom.size and saved.tobytes()==zoom.tobytes(),box['id']
uncertainties=json.loads((W/'uncertainties.json').read_text())
for item in uncertainties['items']:
 row=next(r for r in record['rows'] if r['id']==item['row']);units=[c for c in row['cipher'] if c in key];a,b=item['row_units'];assert ''.join(units[a-1:b])==''.join(c for c in item['cipher'] if c in key)
 a,b=item['global_units'];assert ''.join(p[3] for p in positions[a-1:b])==''.join(c for c in item['cipher'] if c in key)
 assert ''.join(key.get(c,c) for c in item['cipher'])==item['literal']
qa=json.loads((W/'qa-followup.json').read_text())
assert qa['changes']==[{'global':396,'before':'g','after':'q'},{'global':399,'before':'d','after':'s'}]
for change in qa['changes']: assert positions[change['global']-1][3]==change['after']
assert qa['new_selected_word']=='h3q5qf2s586' and qa['new_literal']=='ROZEZVUCELA'
assert 'ROZEKVUTELA' not in literal and 'ROZEZVUCELA' in literal
# Review 1 corrections: R02 unmarked r (BYH, editorial bych), R08 d5p5 TEBE, R09 gt1 KDY.
assert ' p1r ' in record['rows'][1]['cipher'] and ' d5p5,' in record['rows'][7]['cipher'] and ' gt1 ' in record['rows'][8]['cipher']
assert 'BYH VSAK' in literal and 'NA TEBE,' in literal and 'KDY MI POSLES' in literal and 'ZDA' not in literal and 'TOBE' not in literal
print(literal,end='')
print(f'\nPASS: {sources} original pins + own3 of immutable9-entry batch; {references} reference hashes; {records} record hashes; {canonical} canonical artifact hashes.')
print('13 rows (upper9/lower4),475 active units,7 marked CH,482 base letters,22 labels; positions/literals/SOLUTION equality and actual whole-fixed-key inverse pass.')
print(f'Original rotation,13 row crops and{len(controls["boxes"])} native/NN controls match pixels;5 indexed shape/editorial checks retained.')
print('Candidate readings/alternatives remain disclosed. Hash/inverse/crop agreement does not prove manual glyph truth. Ordinary print/date/address excluded.')
print('Key inventory:',' '.join(f'{c}:{counts[c]}' for c in key))
