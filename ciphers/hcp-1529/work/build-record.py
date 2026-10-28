"""Explicit work-only generation from manual record. Inspect before running.
Preserves original digest manifest and fixed key; decode.py never writes.
"""
from pathlib import Path
import collections,csv,hashlib,json
from PIL import Image,ImageDraw
R=Path(__file__).resolve().parents[1];W=R/'work'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
originals=json.loads((W/'source-sha256.json').read_text());old=json.loads((W/'record-sha256.json').read_text())
for p,digest in originals.items():assert sha(R/p)==digest,'Original changed: '+p
assert sha(W/'key.json')==old['work/key.json'],'Fixed key changed'
key=json.loads((W/'key.json').read_text());record=json.loads((W/'transcription.json').read_text());positions=[];counts=collections.Counter();n=0
im=Image.open(R/'source/picture.jpg');indexed=im.copy();draw=ImageDraw.Draw(indexed)
for row in record['rows']:
 c=row['cipher'];box=row['box_original_xyxy'];assert row['plaintext']==''.join(key.get(v,v) for v in c);j=0
 for word,token in enumerate(c.split(),1):
  for v in token:
   if v in key:j+=1;n+=1;counts[v]+=1;positions.append([n,row['id'],j,word,v,key[v]])
   else:assert v in ',.'
 assert j==row['active_units'];im.crop(box).save(W/(row['id']+'-native.png'));draw.rectangle(box,outline='red',width=1);draw.text((box[0],box[1]),row['id'],fill='red')
indexed.save(W/'indexed.png');(W/'transcription.txt').write_text('\n'.join(r['cipher'] for r in record['rows'])+'\n');(W/'plaintext.txt').write_text('\n'.join(r['plaintext'] for r in record['rows'])+'\n')
with (W/'positions.csv').open('w',newline='') as f:
 out=csv.writer(f);out.writerow(['global_ordinal','row','row_ordinal','word_ordinal','shape_label','base_plain']);out.writerows(positions)
limits=[{'row':r['id'],**v} for r in record['rows'] for v in r.get('source_reading_limits',[])]
(W/'inventory.json').write_text(json.dumps({'label_counts':dict(sorted(counts.items())),'active_units':n,'CH_units':sum(counts[c] for c in key if key[c]=='CH'),'base_letters':sum(counts[c]*len(key[c]) for c in key),'source_reading_limits':limits},indent=2)+'\n')
files=['key.json','transcription.json','positions.csv','transcription.txt','plaintext.txt','inventory.json','decode.py','build-record.py','make-controls.py','review1-z-usti-controls.json','review1-z-usti-controls.png','review1-context-check.json']
(W/'record-sha256.json').write_text(json.dumps({'work/'+p:sha(W/p) for p in files},indent=2)+'\n');print('Generated',n,'positions; counts',dict(sorted(counts.items())))
