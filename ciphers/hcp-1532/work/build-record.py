"""Explicit work-only generator; inspect before use. decode.py never writes.
The original source hashes must first pass the existing read-only audit.
"""
import collections,csv,hashlib,json
from pathlib import Path
from PIL import Image,ImageDraw
BASE=Path(__file__).resolve().parents[1];W=BASE/'work'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
old=json.loads((W/'manifest.json').read_text())
for path,digest in old['source_files'].items():assert sha(BASE/path)==digest,'Original changed: '+path
k=json.loads((W/'key.json').read_text());data=json.loads((W/'transcription.json').read_text())
assert sha(W/'key.json')==old['record_files']['work/key.json'],'Fixed key changed'
im=Image.open(BASE/'source/picture.jpg').convert('RGB');indexed=im.copy();pen=ImageDraw.Draw(indexed)
counts=collections.Counter();ambiguities=[];n=0
with (W/'index.csv').open('w',newline='') as f:
 out=csv.writer(f);out.writerow(['row','row_ordinal','global_ordinal','cipher_label','plaintext_unit','row_source_xyxy','status','candidate_cipher_labels','candidate_plaintext_units','observation','selected_reading_basis'])
 for row in data['rows']:
  box=row['box_source_xyxy'];pen.rectangle(box,outline='red');pen.text((box[0],box[1]-9),row['id'],fill='red')
  crop=im.crop(box)
  if row['id']=='M01':crop=crop.rotate(-90,expand=True)
  crop.resize((crop.width*3,crop.height*3)).save(W/(row['id']+'.png'))
  j=0;uncertainties={u['row_ordinal']:u for u in row.get('uncertainties',[])}
  for c in row['cipher']:
   if c not in k:continue
   j+=1;n+=1;counts[c]+=1;u=uncertainties.get(j)
   out.writerow([row['id'],j,n,c,k[c],','.join(map(str,box)),'ambiguous' if u else 'read','|'.join(u['candidate_labels']) if u else c,'|'.join(k[v] for v in u['candidate_labels']) if u else k[c],u['observation'] if u else '',u['selected_reading_basis'] if u else ''])
   if u:ambiguities.append({'row':row['id'],'row_ordinal':j,'global_ordinal':n,**u})
indexed.save(W/'indexed.png')
(W/'literal-cz.txt').write_text('\n'.join(r['plaintext'] for r in data['rows'])+'\n')
(W/'inventory.json').write_text(json.dumps({'selected_label_counts':dict(sorted(counts.items())),'active_units':n,'unambiguous_units':n-len(ambiguities),'ambiguous_units':len(ambiguities),'ambiguities':ambiguities},ensure_ascii=False,indent=2)+'\n')
files=['key.json','transcription.json','index.csv','literal-cz.txt','inventory.json','decode.py','build-record.py','review1-original-controls.json','review1-original-controls.png']
manifest={'source_files':old['source_files'],'record_files':{'work/'+p:sha(W/p) for p in files},'active_units':n,'base_letters':sum(len(k[c]) for r in data['rows'] for c in r['cipher'] if c in k),'CH_units':sum(r['cipher'].count('ř') for r in data['rows']),'ambiguous_units':len(ambiguities)}
(W/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n');print(json.dumps(manifest,indent=2))
