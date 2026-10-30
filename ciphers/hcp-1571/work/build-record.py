#!/usr/bin/env python3
"""Mutating authoring helper for manual source reading; never OCR."""
from pathlib import Path
from PIL import Image,ImageDraw
import json,hashlib,csv
R=Path(__file__).resolve().parents[1];W=R/'work';REPO=R.parents[1]
guard=json.loads((REPO/'batches/easy-2026-10-28/cz246-251-252-source-sha256.json').read_text())
for p,h in json.loads((W/'source-sha256.json').read_text()).items():
 assert hashlib.sha256((R/p).read_bytes()).hexdigest()==h and guard['ciphers/hcp-1571/'+p]==h
key=json.loads((REPO/'ciphers/hcp-1520/work/key.json').read_text());key={k:v.upper() for k,v in key.items()}
rows=[
('R01','d4c4sgh6d t4g. 6m4sg3 n3y5 bh5th6r6, q6 h3qd3n481'),
('R02','84cd5g. n58 p1r fc6g y6 c6n bh4y5d4 c n5d832 m6'),
('R03','6mt58g2, gd5h6 c4s5 nm5 b48m5 m6b3n4m6, 6p1H'),
('R04','c5 c5dh48. 6fc6g c6n6 f86cdm4H cf1H h6t m5tp6 6'),
('R05','t85 n1H c5 m5h4t4. d5c4s c5 nm3r3'),
('R06','m6 cf6dg1? y6 dh6f4d4 y5 p2t2 y6g 3p1s5ym5 f bh6q5.'),
('R07','n6n5 3b5d f 2h6t5 r3tm1 cr3m 6 p2t2 h6t, 6q c5 fc5 3b5d'),
('R08','2g84tm4. m6 d5p5, t2c4sg3 n3y5 fqb3n4m6n t5mm5'),
('R09','h6m3, f5s5h 4 s581 t5m. gt1 n4 b3c85c c84p5m5 bc6mg3?'),
('R10','d6g3f1nd3 6md48g5n, t5f5mg3 n3y5 bh5th6r6,'),
('R11','yc4 d4 6 86cg6 df3y5 h3q5qf2s586 n4 cgf3cdm32'),
('R12','r2tp2 f t2c4!! - d4c4s t832r1H, fh581H, f6cm4f1H'),
('R13','b2c b3c486 d4 f5sm5 df2y b5b32c.')]
boxes=json.loads((W/'row-boxes-draft.json').read_text());record={'coordinate_system':'source/picture.jpg ROTATE_270 (clockwise90),674x1024; boxes left,top,right,bottom; slanted context may include adjacent rows. No individual glyph segmentation claimed.','rows':[],'ordinary':[{'type':'printed greeting','text':'Vesele vanoce! (printed accents visible)','bbox':[72,137,258,161]},{'type':'date','text':'20/XII.1902','bbox':[475,704,622,756]},{'type':'address-side','text':'Velectena Slecna / slecna Anna Ticha / ucitelka v Zirovnici / u Pocatek; postal marks, printed multilingual headings and watermark; no observed ciphertext continuation.'}],'unknown_spans':[],'provisional_shape_readings':[{'row':'R03','cipher':'nm5','literal':'MNE','note':'One-hump n/M then wider two-hump m/N before5/E; root QA requested.'},{'row':'R10','cipher':'6md48g5n','literal':'ANTILKEM','note':'Third d/T retained against intended ANDILKEM; compare same-row final d in d6g3f1nd3.'},{'row':'R11','cipher':'h3q5qf2s586','literal':'ROZEZVUCELA','note':'Source comparisons support q/Z at wordunit5 and s/C at wordunit8; previous g/K,d/T readings rejected. Existing2/U selected at7,5/E alternative retained. Root inspected focused comparisons; no key change.'}]}
positions=[];allunits=[]
for rid,cipher in rows:
 units=[c for c in cipher if c in key]; plain=''.join(key.get(c,c) for c in cipher)
 record['rows'].append({'id':rid,'block':'upper' if int(rid[1:])<=9 else 'lower','bbox':boxes[rid],'cipher':cipher,'plaintext':plain,'active_units':len(units)})
 for i,c in enumerate(units,1): positions.append([len(positions)+1,rid,i,c,key[c]])
 allunits+=units
(W/'key.json').write_text(json.dumps(key,ensure_ascii=False,indent=2)+'\n')
(W/'transcription.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
(W/'transcription.txt').write_text('\n'.join(r['cipher'] for r in record['rows'])+'\n')
(W/'literal.txt').write_text('\n'.join(r['plaintext'] for r in record['rows'])+'\n')
with (W/'positions.csv').open('w') as f:
 writer=csv.writer(f);writer.writerow(['global_id','row','row_unit_index','cipher_label','plaintext']);writer.writerows(positions)
im=Image.open(R/'source/picture.jpg').transpose(Image.Transpose.ROTATE_270);im.save(W/'upright.png');ann=im.copy();d=ImageDraw.Draw(ann)
for r in record['rows']:
 d.rectangle(r['bbox'],outline='red');d.text((r['bbox'][0],r['bbox'][1]),r['id'],fill='blue')
 c=im.crop(r['bbox']);c.resize((c.width*3,c.height*3),Image.Resampling.NEAREST).save(W/(r['id']+'-rawNN.png'))
ann.save(W/'indexed-rows.png')
print((W/'literal.txt').read_text());print('rows/counts',[(r['id'],r['active_units']) for r in record['rows']]);print('active',len(allunits),'CH',allunits.count('H'),'letters',sum(len(key[c]) for c in allunits),'labels',len(set(allunits)))
