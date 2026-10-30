"""Authoring helper only; manual readings, never OCR."""
from pathlib import Path
import json, hashlib, re
from PIL import Image
W=Path(__file__).resolve().parent; C=W.parent; R=C.parent.parent
key=json.loads((R/'ciphers/hcp-1520/work/key.json').read_text());key.update({'7':'j','ř':'ch','v':'f'})
(W/'key.json').write_text(json.dumps(key,ensure_ascii=False,indent=2)+'\n')
raw=[
('M01','d4c4s5h1 t4g q6 th6r1 {G01} 84cd5g tm5cm4! d6g5'),
('M02','nm5 c5 6m4sg3 n6 {G02} 75t4m6, f584s5 cd1cg6'),
('M03','b3 d3p5. t3f385m5 m5 {G03} c5, th6r32cg2, p6d4 m5n2-'),
('M04','c4, fqt4d f4c, q5 y5m {G04} d5p5 6 bh3 fqt1 n6n h6t.'),
('M05','q627686 yc4 n3y4 t2c4 {G05} s5832 6 m5m4 d6n y4q'),
('M06','n4cd6 bh3 m4g3r3 y4m5r {G06} t3f385m32 cf3y4 cdh6f4n'),
('M07','6c4 s5832 f5cb385s m{G07}4 b6m6 t5g6m6, c gd5-'),
('M08','h1n p2t5n5 bh3{C01}q5d4{G08} b6n5dm4 gm4r2 t5g6m-'),
('M09','cg32, y6g yc5n c4 {G09}d3 y4q q6n832f68 bh4'),
('M10','s5s48cg5n g3ms5hd5. t5m, gt1 3ty5t2 t3c2t'),
('M11','m5f4n, n1c84n fc6g, q5 p2t f5 sdfhd5g f5s5h m5p'),
('S01','f b6d5g h6m3. q685q4 {U01}{G10}d3n, gt1 p2t2 c 2sd5n'),
('S02','gf6hd68m4n r3d3f. d4c4s 2bh4nm1ř b2c d4 b3c486'),
('S03','f5sm5 df27 b5b32c, gd5h1 c5 m6 c84p5m5 bc6mg3'),
('S04','m5cn4hm5 d5c4.')]
spans={f'G{i:02}':{'type':'unknown_span','cause':'Printed bouquet/stem or flower obscures handwriting','cipher_unit_count':None} for i in range(1,11)}
spans['C01']={'type':'overwritten_span','cause':'Dense horizontal/overwritten ink between readable bh3 and q5d4; authorial cancellation intention not established','cipher_unit_count':None,'possible_underlying_cipher':'r84','possible_underlying_plain':'hli','excluded_uncertain_span_from_active_unit_count':True,'count_convention':'Readable surrounding bh3 and q5d4 included provisionally as active; uncertain middle ink excluded; no definite cancellation claim'}
spans['U01']={'type':'unknown_unit','cause':'Visible pre-flower glyph m/n uncertain','cipher_unit_count':1,'glyph_candidates':['m','n'],'plain_candidates':['n','m']}
records=[];gi=0
for name,text in raw:
 units=[];pos=0
 for s in re.findall(r'\{[^}]+\}|.',text):
  if s.startswith('{'):
   sid=s[1:-1];u={'kind':spans[sid]['type'],'id':sid}
   if spans[sid]['type']=='unknown_unit':
    gi+=1;pos+=1;u.update({'line_index':pos,'global_index':gi})
   units.append(u);continue
  if s in key:
   gi+=1;pos+=1;units.append({'kind':'cipher','line_index':pos,'global_index':gi,'glyph':s,'plain':key[s]})
  else:
   assert not s.isalnum(),(name,s)
   units.append({'kind':'separator','value':s})
 records.append({'id':name,'manual_cipher':text,'units':units})
rec={'status':'PARTIAL_MANUAL_TRANSCRIPTION','method':'Manual visual inspection, transferred published family key; no OCR, no independent key discovery','physical_order':'Main M01–M11 then upper inverted margin S01–S04','lines':records,'spans':spans,'noncipher':{'picture_date':'22./IX.1903','address':['Velectěná Slečna','slečna Anna Tichá','učitelka v','Žirovnici','u Počátek.'],'address_encrypted_text':False,'all_sides_and_margins_inspected':True},'active_visible_cipher_units':gi}
(W/'transcript.json').write_text(json.dumps(rec,ensure_ascii=False,indent=2)+'\n')
im=Image.open(C/'source/picture.jpg').rotate(-90,expand=True)
yboxes=[(625,668),(663,698),(696,730),(725,759),(755,792),(789,825),(818,854),(847,884),(878,919),(914,947),(942,978)]
rows=[]
for j,(a,b) in enumerate(yboxes,1):
 name=f'M{j:02}';box=[28,a,656,b];out=W/'rows'/f'{name}.png';im.crop(box).resize((1884,(b-a)*3)).save(out)
 rows.append({'id':name,'view':'picture rotated 90 degrees clockwise','box':box,'crop':str(out.relative_to(C))})
# Original upper band upside down; rotate 180 to read the second block.
side=Image.open(C/'source/picture.jpg').crop((20,24,640,145)).rotate(180,expand=True)
for j,(a,b) in enumerate([(0,43),(31,73),(62,100),(90,121)],1):
 name=f'S{j:02}';out=W/'rows'/f'{name}.png';side.crop((0,a,620,b)).resize((1860,(b-a)*3)).save(out)
 rows.append({'id':name,'view':'original upper band [20,24,640,145] rotated 180','box_in_band':[0,a,620,b],'crop':str(out.relative_to(C))})
(W/'row-index.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
controls=[
 {'file':'patek-native.png','view':'original upper band [20,24,640,145] rotated 180','box_in_band':[0,0,195,45],'decision':'f b6d5g, one b/P then one 6/A; former duplicated b rejected'},
 {'file':'patek-nearest.png','view':'same native patek crop, nearest-neighbour 8x','box_in_band':[0,0,195,45]},
 {'file':'controls-po-tobe.png','view':'picture rotated 90 clockwise; nearest-neighbour 8x','box':[36,693,175,728],'read':'b3 d3p5'},
 {'file':'controls-anicko.png','view':'picture rotated 90 clockwise; nearest-neighbour 8x','box':[160,663,295,699],'read':'6m4sg3 n6'}]
(W/'control-index.json').write_text(json.dumps(controls,ensure_ascii=False,indent=2)+'\n')
files=[C/'source/picture.jpg',C/'source/address.jpg',C/'source/metadata.md',C/'SOURCES.md',W/'transcript.json',W/'key.json',W/'row-index.json',R/'batches/easy-2026-10-28/public-reference-199/picture.jpg',R/'batches/easy-2026-10-28/public-reference-199/provenance.json',R/'batches/easy-2026-10-28/published-anna-ticha-key.txt']
files += [C/x['crop'] for x in rows]
files += [W/'control-index.json']+[W/x['file'] for x in controls]
manifest={'sha256':{str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest() for p in files},'note':'Verifies evidence and manual record bytes only, not reading correctness.'}
(W/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
