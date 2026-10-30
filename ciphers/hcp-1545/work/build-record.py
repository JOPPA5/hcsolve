#!/usr/bin/env python3
from pathlib import Path
from PIL import Image,ImageDraw,ImageFont
import json,csv,hashlib,re
R=Path(__file__).resolve().parents[1];W=R/'work';BASE=R.parents[1]
key=json.loads((BASE/'ciphers/hcp-1527/work/key.json').read_text())
rows=[
('R01',(405,612,635,650),'d4c4s5h1 t4g, q86d3','TISICERY DIK, ZLATO'),
('R02',(405,641,635,679),'n375, q6 th6r1 84cd5g.','MOJE, ZA DRAHY LISTEK.'),
('R03',(309,668,635,703),'q674cd5 t3cd686 74q f b6d5g','ZAJISTE DOSTALA JIZ V PATEK'),
('R04',(270,696,635,734),'n27 84cd5g, 75mq c5 gh4q3f68','MUJ LISTEK, JENZ SE KRIZOVAL'),
('R05',(270,721,635,759),'c df1n "m5q6b3n4m6n, th6r32cg2,','S TVYM "NEZAPOMINAM, DRAHOUSKU,'),
('R06',(270,746,635,785),'6m4 řf48g2, m1phq cd685 m6 cf374','ANI CHVILKU, NYBRZ STALE NA SVOJI'),
('R07',(270,775,635,816),'g382p5mg2 fh585 fqb3n4m6n. 76g','KOLUBENKU VRELE VZPOMINAM. JAK'),
('R08',(270,801,635,847),'cd374 f6c5 q685q4d3cd? bh475t5{U01}','STOJI VASE ZALEZITOST? PRIJEDE[U01]'),
('R09',(270,829,635,876),'t3 bh6r1? nm5 d6g5, 6m2mg3, s6c','DO PRAHY? MNE TAKE, ANUNKO, CAS'),
('R10',(310,857,635,902),'85d5n 2p4r6. bh6s274 f5','LETEM UBIHA. PRACUJI VE'),
('R11',(270,884,635,929),'f38m1ř řf484ř b48m5 m6 t574m6ř','VOLNYCH CHVILICH PILNE NA DEJINACH'),
('R12',(270,910,635,955),'s5s4845, 6p1ř 75 n3r8 75cd5 t3','CECILIE, ABYCH JE MOHL JESTE DO'),
('M01',(420,533,1000,580),'g3ms5 bh6qtm4m g d4cg2 bh4bh6f4d4. d4c4s 2bh4n-','KONCE PRAZDNIN K TISKU PRIPRAVITI. TISIC UPRIM-'),
('M02',(430,566,980,611),'m1ř b2c b3c486 df27 b5b32c, d5c4s4 c5 m6 3b5dm1','NYCH PUS POSILA TVUJ PEPOUS, TESICI SE NA OPETNY'),
('M03',(430,599,600,638),'th6r1 84cd5g.','DRAHY LISTEK.')]
rec={'method':'Manual transcription of immutable source/picture.jpg; all rows. R rows use ROTATE_270 coordinates (674x1024), M rows ROTATE_180 (1024x674). Base glyph labels transferred from prior published partial Anna Ticha key and hcp-1527. Diacritic strokes are present but not automatically interpreted; output is literal base-letter text. No cancellation presumed.', 'unknown_regions':{'U01':{'row':'R08','box_upright_xyxy':[602,811,623,835],'extent':'one or two cipher units; final rounded group after bh475t5','candidates':'d5 would give TE and PRIJEDETE; not yet visually established; no singleton length asserted'}},'rows':[]}
positions=[];globalidx=0
for rid,box,cipher,plain in rows:
 units=re.findall(r'\{U\d+\}|.',cipher);idx=0
 for token in units:
  if token in key or token.startswith('{U'):
   idx+=1;globalidx+=1
   positions.append([globalidx,rid,idx,token,key.get(token,'[U01]'),'mapped' if token in key else 'unknown_region_1-2_units'])
 rec['rows'].append({'id':rid,'orientation':'ROTATE_270' if rid[0]=='R' else 'ROTATE_180','box':box,'cipher':cipher,'plaintext':plain,'indexed_items':idx})
(W/'key.json').write_text(json.dumps(key,ensure_ascii=False,indent=2)+'\n')
(W/'transcription.json').write_text(json.dumps(rec,ensure_ascii=False,indent=2)+'\n')
with (W/'positions.csv').open('w') as f:
 writer=csv.writer(f);writer.writerow(['item','row','row_item','glyph_or_region','base_plaintext','status']);writer.writerows(positions)
(W/'plaintext.txt').write_text('\n'.join(r['plaintext'] for r in rec['rows'])+'\n')
orig=Image.open(R/'source/picture.jpg');up=orig.transpose(Image.Transpose.ROTATE_270);margin=orig.transpose(Image.Transpose.ROTATE_180)
for orientation,im in [('ROTATE_270',up),('ROTATE_180',margin)]:
 indexed=im.copy();d=ImageDraw.Draw(indexed)
 for row in rec['rows']:
  if row['orientation']!=orientation:continue
  d.rectangle(row['box'],outline='red',width=1);d.text((row['box'][0]-25,row['box'][1]),row['id'],fill='red')
  im.crop(row['box']).resize(((row['box'][2]-row['box'][0])*4,(row['box'][3]-row['box'][1])*4)).save(W/(row['id']+'.png'))
 indexed.save(W/('indexed-main.png' if orientation=='ROTATE_270' else 'indexed-margin.png'))
# Controls on same card: shape discrimination precedes nickname decision.
controls=[('5/E, LISTEK R02',(582,651,594,674),'ROTATE_270'),('6/A, DRAHY R02',(513,646,526,671),'ROTATE_270'),('c/S, LISTEK R02',(560,651,572,674),'ROTATE_270'),('signature PEPOUS M02',(675,570,755,604),'ROTATE_180'),('ANUNKO R09',(475,836,568,867),'ROTATE_270'),('DIK final g/K R01',(536,625,556,660),'ROTATE_270'),('R07 initial g/K',(275,781,293,804),'ROTATE_270'),('KRIZOVAL R04',(501,703,607,726),'ROTATE_270'),('R08 final region',(605,824,623,843),'ROTATE_270')]
canvas=Image.new('RGB',(1000,125*len(controls)),'white');d=ImageDraw.Draw(canvas)
for i,(label,box,orientation) in enumerate(controls):
 im=up if orientation=='ROTATE_270' else margin;crop=im.crop(box);crop.thumbnail((700,95));crop=crop.resize((crop.width*3,crop.height*3));crop.thumbnail((700,95));canvas.paste(crop,(300,i*125+15));d.text((5,i*125+20),label,fill='black')
canvas.save(W/'focused-controls.png');(W/'focused-controls.json').write_text(json.dumps(controls,indent=2)+'\n')
h=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
(W/'source-sha256.json').write_text(json.dumps({str(p.relative_to(R)):h(p) for p in (R/'source').iterdir() if p.is_file()},indent=2)+'\n')
refs=[BASE/'ciphers/hcp-1527/work/key.json',BASE/'batches/easy-2026-10-28/published-anna-ticha-key.txt',BASE/'batches/easy-2026-10-28/public-reference-199/picture.jpg',BASE/'batches/easy-2026-10-28/public-reference-199/provenance.json']
(W/'reference-sha256.json').write_text(json.dumps({str(p.relative_to(BASE)):h(p) for p in refs},indent=2)+'\n')
(W/'record-sha256.json').write_text(json.dumps({str(p.relative_to(R)):h(p) for p in [W/'key.json',W/'transcription.json',W/'positions.csv',W/'plaintext.txt',W/'focused-controls.json']},indent=2)+'\n')
