#!/usr/bin/env python3
from pathlib import Path
import json,hashlib,csv
from collections import Counter
from PIL import Image,ImageDraw
R=Path(__file__).resolve().parents[1];W=R/'work'
key={'1':'Y','2':'U','3':'O','4':'I','5':'E','6':'A','7':'J','8':'L','b':'P','c':'S','d':'T','f':'V','g':'K','h':'R','m':'N','n':'M','p':'B','q':'Z','r':'H','s':'C','t':'D','ř':'CH'}
raw=[
'fh581 t4g q6 th6r5 bc6mg3. 3pc6r5n 75r3 p18',
'7c5n s6cd5sm5 f58n4 bh5gf6b5m. s85sm6 c5t86s-',
'g3f6 c5 6c4 nm3r3 bh5c85ř86; m5n6n 3 d5d3 mn5',
'2hs3f6m5 m5f5cd5 6m4 d2c5m4. m5m685q4n d5q',
'g d5n, gt3q t674 c4 cm6t 2hs3f6d4 cf374 m5f5cd2',
'74m1n4.',
'bh6m4 cf5r3 cht5sg6 cb8m4n 6 3tb3f4n n2 bh5t',
'sdfhd h3g5n. 7c5n m1m4 s585 tm1 f 2h6t5 6 d6g5',
'c5 t385 cdh6f274; 75m m6r3t32 q6c58 7c5n tm5c',
'fb385tm5 t3n2. d4c4s fh581ř b2c 6 b3qth6f2 b3c486',
'd4 df27 b5b32c, gd5h1 cf5n2 sht5sg2 bh575, 6p1',
'cdh6f483 r3tm5 r5qg5 cf6dg1. p2t2 fqb3n4m6d4.'
]
ys=[(573,614),(607,645),(637,676),(669,709),(700,743),(735,765),(759,795),(789,832),(820,865),(855,896),(883,927),(918,959)]
record={'method':'Manual visual transcription from source/picture.jpg, upright lossless ROTATE_90. Known family key transfer. Cipher glyph labels are shape labels, not printed Latin plaintext. Row boxes enclose whole rows, overlapping where ascenders intersect; position indices are not individual glyph pixel boxes.','rows':[],'ordinary':['19.XII.1903 below cipher.','Postal address to Anna Ticha, teacher in Zirovnice near Pocatky, in ordinary script on address side.'],'marks':['R07 PRED underlined.','R10 VRELYCH has a separate caron above final Y-associated unit or adjoining CH glyph; base-letter transcription retains VRELYCH. The diacritic is not an additional base cipher unit.','No canceled cipher unit identified.']} 
positions=[];total=0
for i,(s,(y1,y2)) in enumerate(zip(raw,ys),1):
 text=''.join(key.get(c,c) for c in s);active=sum(c in key for c in s)
 row={'id':f'R{i:02}','box_upright_xyxy':[35,y1,640,y2],'cipher':s,'plaintext':text,'active_units':active};record['rows'].append(row)
 idx=0
 for c in s:
  if c in key:
   total+=1;idx+=1;positions.append([total,row['id'],idx,c,key[c]])
counts=Counter(c for row in record['rows'] for c in row['cipher'] if c in key)
record['counts']={'rows':len(record['rows']),'active_units':sum(counts.values()),'CH_units':counts['ř'],'base_letters':sum(counts[c]*len(key[c]) for c in counts),'observed_assigned_classes':len(counts),'unassigned_active_units':0,'class_counts':dict(sorted(counts.items()))}
record['writer_slips']=[{'row':'R02','literal':'CLECNA','editorial':'slecna','evidence':'Initial angular s/C matches the fourth sign; round c/S occurs in JSEM and CASTECNE.'},{'row':'R03','literal':'NME','editorial':'mne','evidence':'Final mn5 has m/N followed by n/M, opposite the nm/MN order in MNOHO in the same row.'},{'row':'R11','literal':'CRDECKU','editorial':'srdecku','evidence':'Initial angular s/C differs from round c/S beginning R07 SRDECKA.'}]
record['uncertain_positions']=[{'global_position':next(x[0] for x in positions if x[1]=='R06' and x[2]==4),'row':'R06','row_position':4,'preferred_shape':'1','preferred_plaintext':'Y','bounded_alternative_shape':'2','bounded_alternative_plaintext':'U','reason':'Retraced heavy ink creates a closed, 2-like upper loop. Height and foot favour 1/Y, retained as preferred reading; less certain than neighbouring signs.'}]
(W/'key.json').write_text(json.dumps(key,ensure_ascii=False,indent=2)+'\n')
(W/'transcription.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
(W/'transcription.txt').write_text(''.join(row['id']+' '+row['cipher']+'\n' for row in record['rows']))
(W/'literal.txt').write_text(''.join(row['plaintext']+'\n' for row in record['rows']))
with (W/'positions.csv').open('w') as f:
 w=csv.writer(f);w.writerow(['global_position','row','row_position','shape_label','base_plaintext']);w.writerows(positions)
source_hash={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted((R/'source').iterdir()) if p.is_file()}
(W/'source-sha256.json').write_text(json.dumps(source_hash,indent=2)+'\n')
im=Image.open(R/'source/picture.jpg').transpose(Image.Transpose.ROTATE_90)
im.save(W/'upright.png')
indexed=im.copy();d=ImageDraw.Draw(indexed)
for row in record['rows']:
 b=row['box_upright_xyxy'];d.rectangle(b,outline='red',width=1);d.text((4,b[1]),row['id'],fill='red')
indexed.save(W/'indexed.png')
for row in record['rows']:
 b=row['box_upright_xyxy'];im.crop(b).resize((1815,(b[3]-b[1])*3)).save(W/(row['id']+'.png'))
references=['ciphers/hcp-1520/work/key.json','batches/easy-2026-10-28/published-anna-ticha-key.txt']
(W/'reference-sha256.json').write_text(json.dumps({f:hashlib.sha256((R.parent.parent/f).read_bytes()).hexdigest() for f in references},indent=2)+'\n')
files=[W/name for name in ['key.json','transcription.json','positions.csv','transcription.txt','literal.txt','source-sha256.json','reference-sha256.json','build-record.py','make-controls.py','make-review1-controls.py','decode.py','upright.png','indexed.png','focused-controls.json','focused-controls.png','review1-controls.json','review1-controls.png']]+[W/(row['id']+'.png') for row in record['rows']]+sorted(W.glob('review1-R*.png'))
rec_hash={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest() for p in files}
(W/'record-sha256.json').write_text(json.dumps(rec_hash,indent=2)+'\n')
for row in record['rows']:print(row['id'],row['active_units'],row['plaintext'])
print('units',total,'CH',sum(s.count('ř') for s in raw),'letters',sum(len(key[c]) for s in raw for c in s if c in key))
