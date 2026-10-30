#!/usr/bin/env python3
"""Explicit manual record/crop generator; never invoked by the default decoder."""
from pathlib import Path
import hashlib,json,csv
from PIL import Image,ImageDraw
R=Path(__file__).resolve().parents[1];W=R/'work'
key={'1':'Y','2':'U','3':'O','4':'I','5':'E','6':'A','8':'L','q':'Z','g':'K','f':'V','h':'R','t':'D','r':'H','c':'S','s':'C','n':'M','m':'N','p':'B','b':'P','d':'T','y':'J','ř':'CH','v':'F'}
raw=[
('T01','fh581 t4g cht5sg3 n3y5 q86d5, q6 th6r5 [U1]',[0,0,614,37]),
('T02','y6g t6h4 c5 m1m4 c r86f4sg32? y6 yc5n, p3r2t4g,',[0,31,614,66]),
('T03','p385cd cf5 r86f1 y4q bh5n3r8, gd5h5 nm5 m1m4',[0,59,614,95]),
('T04','bh4c83 f584s5 m5fr3t. 2 m6c y4q p84q4 c5 t3p6',[0,88,614,125]),
('T05','f6m3sm4 6 c m4 h3qnm3q5m4 bh6s5. d6g5 y6',[0,119,614,160]),
('B01','fqb3n4m6n m6 83mcg1 h3g fd5d3 t3p5,',[28,675,642,716]),
('B02','gt1 n3y5 cht5sg3 qt5 t8583 m6 qg32cg6ř.',[28,712,642,750]),
('B03','cg3t6. 6 d1 r5q32mg5 řf48g1 fqt1 d6g',[28,748,642,783]),
('B04','h1ř85 bhř6y4. y6g dh6f4 6m2cg6 [U2]',[28,780,642,818]),
('B05','t832r5 f5s5h1? n2y q4f3d y5 m6h6nm5 y5tm3-',[28,814,642,852]),
('B06','df6hm1. fs5h6 řd58 yc5n m6fcd4f4d4 f5s5h',[28,850,642,887]),
('B07','g3ms5hd «Issajův» f h2t38v4m5, qthq58 yc5n',[28,885,642,924]),
('B08','c5 fc6g bh484c t832r3 f 2h6[U4]. d4c4s fh581ř',[28,920,642,956]),
('B09','b2c b3c486 b5b32c cf5n2 y5[U3]n2 cht5sg2.',[28,952,642,991])]
unknowns={'U1':{'kind':'span','reading':'Unknown dark word after DRAHE; PSANKO is contextual/visual candidate only.','box_top_xyxy':[460,0,614,38],'unit_count':None},'U2':{'kind':'span','reading':'Dark word following ANUSKA; NYNEJSI is candidate only.','box_upright_xyxy':[465,778,642,819],'unit_count':None},'U4':{'kind':'span','reading':'Final dark portion after URA; DE is contextual candidate only.','box_upright_xyxy':[393,922,435,955],'unit_count':None},'U3':{'kind':'span','reading':'Dark middle of JE...MU; DINE (JEDINEMU as whole word) is contextual candidate only.','box_upright_xyxy':[361,954,452,989],'unit_count':None}}
import re
pat=re.compile(r'\[U(?:1|2|3|4)\]|«[^»]*»|.')
record={'method':'Manual visual transcription from immutable picture.jpg. Base image ROTATE_90, top margin further ROTATE_180. No OCR. Known family key transfer. Conservative unresolved spans have unknown unit count. Shallow v/F transferred after targeted comparison with published card199 original photo; initially held unknown. No language-based completion inserted.','coordinate_systems':{'top':'top-upright.png, crop [28,35,642,195] of upright.png, then ROTATE_180; size 614x160','bottom':'upright.png is ROTATE_90 of original; size 674x1024'},'unknowns':unknowns,'rows':[],'ordinary':['Handwritten date 14.XI.1903 on picture.','Address in ordinary script: Anna Ticha, teacher, Zirovnice near Pocatky.','B07 quoted ordinary title transcribed Issajův; reading uncertain; not encrypted and not expanded to a historical identity.'],'marks':['T04 has an upward continuation arrow at right.','T05 starts with a retraced/overwritten VANOCNI. No distinct canceled cipher unit can be separated reliably.','Small caron-like marks above special CH glyphs are represented by ř; other accents are editorial.']}
positions=[];ord=0;unknown=0
for ident,s,box in raw:
 out=[];rowidx=0;parts=[]
 for token in pat.findall(s):
  if token in key:
   ord+=1;rowidx+=1;parts.append({'cipher':token,'plain':key[token]});out.append(key[token]);positions.append([ord,ident,rowidx,'known',token,key[token]])
  elif token.startswith('[U'):
   unknown+=1;parts.append({'unknown':token[1:-1]});out.append(token);positions.append(['',ident,'','unresolved',token,''])
  elif token.startswith('«'):
   parts.append({'ordinary':token});out.append(token)
  else:
   assert token in ' .,?;-';parts.append({'literal':token});out.append(token)
 record['rows'].append({'id':ident,'coordinate_system':'top' if ident.startswith('T') else 'bottom','row_box_xyxy':box,'cipher':s,'parts':parts,'plaintext':''.join(out),'known_units':rowidx})
(W/'key.json').write_text(json.dumps(key,ensure_ascii=False,indent=2)+'\n')
(W/'transcription.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
with (W/'positions.csv').open('w') as f:
 w=csv.writer(f);w.writerow(['known_global_ordinal','row','known_row_ordinal','status','shape_label','base_plaintext']);w.writerows(positions)
source_hash={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted((R/'source').iterdir()) if p.is_file()}
(W/'source-sha256.json').write_text(json.dumps(source_hash,indent=2)+'\n')
rec_hash={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest() for p in [W/'key.json',W/'transcription.json',W/'positions.csv']}
refpaths=['batches/easy-2026-10-28/public-reference-199/picture.jpg','batches/easy-2026-10-28/published-anna-ticha-key.txt']
reference_hash={p:hashlib.sha256((R.parents[1]/p).read_bytes()).hexdigest() for p in refpaths}
(W/'reference-sha256.json').write_text(json.dumps(reference_hash,indent=2)+'\n')
(W/'record-sha256.json').write_text(json.dumps(rec_hash,indent=2)+'\n')
im=Image.open(R/'source/picture.jpg').transpose(Image.Transpose.ROTATE_90);im.save(W/'upright.png');top=im.crop((28,35,642,195)).transpose(Image.Transpose.ROTATE_180);top.save(W/'top-upright.png')
for name,base,sy in [('indexed-bottom.png',im,'bottom'),('indexed-top.png',top,'top')]:
 marked=base.copy();d=ImageDraw.Draw(marked)
 for row in record['rows']:
  if row['coordinate_system']!=sy:continue
  b=row['row_box_xyxy'];d.rectangle(b,outline='red',width=1);d.text((max(0,b[0]-25),b[1]),row['id'],fill='red');base.crop(b).resize(((b[2]-b[0])*3,(b[3]-b[1])*3)).save(W/(row['id']+'.png'))
 marked.save(W/name)
for row in record['rows']:print(row['id'],row['known_units'],row['plaintext'])
print('known_units',ord,'unresolved records',unknown,'CH',sum(s.count('ř') for _,s,_ in raw))
