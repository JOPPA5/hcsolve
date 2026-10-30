#!/usr/bin/env python3
"""Regenerate manual transcription artifacts; never edits the immutable sources."""
from pathlib import Path
from PIL import Image,ImageDraw
import json,csv,hashlib,re
R=Path(__file__).resolve().parents[1];W=R/'work';REPO=R.parents[1]
key={'1':'Y','2':'U','3':'O','4':'I','5':'E','6':'A','7':'J','8':'L','b':'P','c':'S','d':'T','f':'V','g':'K','h':'R','m':'N','n':'M','p':'B','q':'Z','r':'H','s':'C','t':'D','ř':'CH'}
rows=[
'd4c4s5h1 t4g q6 3p6 th6r5 84cdg1 6 q6 fqb3-',
'n4mg2. 76 fqb3n4m68 m52cd685. 74q c5 n5',
'cht5sg3 m5rm5f6? - 3 c86fm3cd4 7c5n d5md3-',
'gh6d5 m5n58 qt5 q6tm5 m6fcd5f1. p18 7c5n',
'c5 t4f6d m6 bh2f3t 4 m6 f86cdm4 c86fm3cd',
'm6 cd6h3n5cdcg5n m6n5cd4. fc3p3d2 p18 7c5n',
'm6 bh3n3s4 ph6dh6 3m3r3 qm6n5r3 n5r3 g3n4c6h5',
'q 74r86f1. d4c4s fh581r b3qth6f2 6 t832r1r f6cm4-',
'f1ř b2c b3c486 df27 b.']
ys=[(687,734),(720,768),(750,802),(783,834),(814,863),(844,898),(875,927),(905,951),(930,976)]
record={'method':'Manual image reading; source/picture.jpg losslessly rotated 270 degrees counterclockwise. Known family key transfer. Shape labels approximate handwriting, not plaintext letters. Positions enumerate all base cipher units. R02 positions 18-19 (5 2 -> EU in NEUSTALE) are a restoration of the stem-covered span formerly recorded as U1 (Claude Opus 5.5, 2026-10-29; accepted in review 1).','rows':[],'restorations':{'U1':{'row':'R02','positions':[18,19],'box_upright_xyxy':[342,728,391,762],'reading':'Stem-covered span after initial N and before STALE. Room for exactly two signs: a small dark sign with a hooked top, consistent with a small 5 (E), only partly visible; then a clearly visible 2 (U). Read 5 2 -> NEUSTALE (neustale). The 2 is read from the pixels; the 5 is partly visible and also required by Czech. See work/claude/neustale.png and review/work/r02_stem_red.png.'}},'marks':['R08 final r after VRELY and DLOUHY has no unambiguously visible CH caron in the current reading; retain H literally. R09 ř is manually read with a separate caron, hence CH; these H/CH readings are not independently confirmed.','R01 DRAHE, R03 SLAVNOSTI and R04 NAVSTEVY partly cross the printed stem; all selected base shapes are still read as visible ink.','No cancellation intention identified.','Underlined final glyph after TVUJ is tentatively transcribed b -> P, followed by an ordinary dot and date 6.VII.1903; this shape assignment is not independently confirmed; it may be an initial, but the sender is not identified.'],'ordinary':['Address side: Velectěná Slečna / slečna Anna Tichá / učitelka v / Žirovnici / u Počátek. Printed Postkarte; publisher C.H. Odemar, Magdeburg 1215; 5 Heller stamp; Prague and Žirovnice postal cancellations. No ciphertext on address side or picture margins beyond the nine rows recorded.']}
RESTORED={('R02',18),('R02',19)}
positions=[];allout=[];total=0
for i,(s,(y1,y2)) in enumerate(zip(rows,ys),1):
 out=[];tokens=[];idx=0
 for token in re.findall(r'\{U1\}|.',s):
  if token=='{U1}': tokens.append({'kind':'unknown','id':'U1','length':None});out.append('⟦U1⟧');positions.append(['',f'R{i:02}','U1','UNKNOWN_LENGTH','⟦U1⟧']);continue
  if token in key:
   idx+=1;total+=1;tokens.append({'kind':'glyph','shape':token,'restored':True} if (f'R{i:02}',idx) in RESTORED else {'kind':'glyph','shape':token});out.append(key[token]);positions.append([total,f'R{i:02}',idx,token,key[token]])
  else: tokens.append({'kind':'punctuation','text':token});out.append(token)
 plain=''.join(out);allout.append(plain)
 record['rows'].append({'id':f'R{i:02}','box_upright_xyxy':[54,y1,646,y2],'cipher':s,'tokens':tokens,'plaintext':plain,'readable_units':idx})
(W/'key.json').write_text(json.dumps(key,ensure_ascii=False,indent=2)+'\n')
(W/'transcription.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
(W/'ciphertext.txt').write_text('\n'.join(rows)+'\n')
(W/'literal.txt').write_text('\n'.join(allout)+'\n')
with (W/'positions.csv').open('w') as f:
 w=csv.writer(f);w.writerow(['known_global_position','row','known_row_position_or_span','shape_label','base_plaintext']);w.writerows(positions)
im=Image.open(R/'source/picture.jpg').transpose(Image.Transpose.ROTATE_270);im.save(W/'upright.png');indexed=im.copy();d=ImageDraw.Draw(indexed)
for row in record['rows']:
 box=row['box_upright_xyxy'];d.rectangle(box,outline='red',width=1);d.text((5,box[1]+12),row['id'],fill='red');im.crop(box).resize((1776,(box[3]-box[1])*3)).save(W/(row['id']+'.png'))
d.rectangle(record['restorations']['U1']['box_upright_xyxy'],outline='yellow',width=2)
indexed.save(W/'indexed.png')
for name in ('picture.jpg','address.jpg','metadata.md'):
 guard=json.loads((REPO/'batches/easy-2026-10-28/cz226-228-229-source-sha256.json').read_text());rel=str((R/'source'/name).relative_to(REPO));assert hashlib.sha256((R/'source'/name).read_bytes()).hexdigest()==guard[rel]
files=[W/'key.json',W/'transcription.json',W/'positions.csv',W/'ciphertext.txt',W/'literal.txt']
(W/'record-sha256.json').write_text(json.dumps({str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest() for p in files},indent=2)+'\n')
for line in allout:print(line)
print(total,'mapped units; CH',sum(s.count('ř') for s in rows),'; restored R02 positions 18-19 (5 2)')
