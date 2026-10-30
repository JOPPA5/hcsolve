#!/usr/bin/env python3
"""Mutating, lossless/NN-only source crop and index authoring."""
from pathlib import Path
from PIL import Image,ImageDraw
import json,hashlib
R=Path(__file__).resolve().parents[1];W=R/'work';im=Image.open(R/'source/picture.jpg').transpose(Image.Transpose.ROTATE_270)
record=json.loads((W/'transcription.json').read_text());key=json.loads((W/'key.json').read_text())
regions=[
('C01','g/K versus q/Z: JAK, OBYCEJNE, PRAZE','R06',[380,162,637,207]),
('C02','d/T and t/D: TAKOVYMTO, ANTILKEM candidate','R10',[58,846,371,894]),
('C03','t/D in ANDELKU versus d/T in KTERA','R03',[58,87,260,133]),
('C04','p/B in BYCH versus b/P in PILNE (C05)','R02',[147,64,280,109]),
('C05','b/P in PILNE; compare p/B (C04)','R03',[352,87,455,134]),
('C06','m/N versus n/M: MNE and PILNE','R03',[290,87,447,134]),
('C07','m/N versus n/M: MAME, OPET; tall h/R in URADE','R07',[58,185,301,233]),
('C08','angular s/C in TESIC versus round c/S in SE','R05',[447,137,576,183]),
('C09','c/S versus s/C; m/N and n/M in VZPOMINAM DENNE','R08',[58,210,637,255]),
('C10','4/I versus1/Y: TISICKRAT and ROZTOMILY','R01',[58,39,637,83]),
('C11','marked H/CH in VLASTNICH and SVYCH','R04',[330,110,485,156]),
('C12','marked H/CH in MYCH','R05',[290,137,370,183]),
('C13','R11 selected ROZEZVUCELA; unit5q/Z,7 2/5,8s/C; previousg,d rejected','R11',[265,873,463,923]),
('C14','TI (underlined);4/I retained, underline not cancellation','R11',[95,873,180,922]),
('C15','TVUJ and VECNE closing; df2y, f5sm5','R13',[210,925,414,975]),
('C16','both OPET words; same b/P','R07',[58,185,637,233]),
('C17','all three marked CH signs in DLOUHYCH,VRELYCH,VASNIVYCH','R12',[58,898,637,946]),
('C18','R11 corrected word: unit3q reference; unit5q/Z (global396),unit7 2/5 (398),unit8s/C (399)','R11',[310,875,440,925]),
('C19','R11 odd word unit8 s/C versus d/T; global399; narrow source context','R11',[390,882,409,916]),
('C20','same-row g/K reference in SKVOSTNOU; compare targetword unit5 with C18 internalq','R11',[473,874,561,924]),
('C21','R05 TESIC final s/C reference versus target R11word unit8','R05',[464,139,529,182]),
('C22','R10 word2 unit3 d/T candidate (global351) versus t/D; narrow context','R10',[256,846,294,898]),
('C23','R03 ANDELKU third t/D reference; compare C22 d/T','R03',[90,88,123,137]),
('C24','R10 TAKOVYMTO unit8 d/T reference (global347); compare C22','R10',[177,846,212,898])]
manifest=[]
for cid,label,rid,box in regions:
 c=im.crop(box);native=cid+'-native.png';zoom=cid+'-rawNN.png';c.save(W/native)
 c.resize((c.width*3,c.height*3),Image.Resampling.NEAREST).save(W/zoom)
 row=next(r for r in record['rows'] if r['id']==rid)
 manifest.append({'id':cid,'label':label,'row':rid,'row_active_units':row['active_units'],'bbox':box,'native':native,'crop':zoom,'scale':3})
# Indexed panels contain raw crops with labels outside the source pixels.
for name,selected in [('rows-A',record['rows'][:4]),('rows-B',record['rows'][4:9]),('rows-C',record['rows'][9:])]:
 panel=Image.new('RGB',(1900,200*len(selected)),'white');d=ImageDraw.Draw(panel)
 for j,row in enumerate(selected):
  box=row['bbox'];c=im.crop(box);c=c.resize((c.width*3,c.height*3),Image.Resampling.NEAREST)
  d.text((5,j*200+3),f"{row['id']} bbox {box}; active1-{row['active_units']}; {row['cipher']}",fill='black')
  panel.paste(c,(5,j*200+30))
 panel.save(W/(name+'-indexed.png'))
for start in range(0,len(manifest),5):
 subset=manifest[start:start+5];panel=Image.new('RGB',(1900,210*len(subset)),'white');d=ImageDraw.Draw(panel)
 for j,b in enumerate(subset):
  d.text((5,j*210+3),b['id']+' '+b['row']+' '+b['label']+'; '+str(b['bbox']),fill='black');panel.paste(Image.open(W/b['crop']),(5,j*210+30))
 panel.save(W/f'controls-{start//5+1}-indexed.png')
(W/'source-controls.json').write_text(json.dumps({'source':'source/picture.jpg','rotation':'ROTATE_270 clockwise90','source_sha256':hashlib.sha256((R/'source/picture.jpg').read_bytes()).hexdigest(),'coordinate_system':'674x1024 working rotation; context boxes may include adjacent slanted lines; no invented glyph pixel boxes','boxes':manifest},indent=2)+'\n')
for name,ids in [('qa-gq',['C18','C20','C01']),('qa-sd',['C18','C19','C21','C24']),('qa-td',['C02','C22','C23','C24'])]:
 panel=Image.new('RGB',(1900,245*len(ids)),'white');d=ImageDraw.Draw(panel)
 for j,cid in enumerate(ids):
  b=next(b for b in manifest if b['id']==cid);c=Image.open(W/b['native']);scale=4
  d.text((5,j*245+3),cid+' '+b['label']+'; '+str(b['bbox']),fill='black')
  panel.paste(c.resize((c.width*scale,c.height*scale),Image.Resampling.NEAREST),(5,j*245+30))
 panel.save(W/(name+'-indexed.png'))
# Word indices are obtained from the manual labels, never OCR or grammar.
items=[]
for rid,word,alternatives in [('R03','nm5',['MNE (selected; n then m)','MME (second label hump segmentation remains a QA control)']),('R05','d5c4s',['TESIC (selected angular s/C)','TESIS is editorial correction, not silent key change']),('R10','6md48g5n',['ANTILKEM (selected d/T)','ANDILKEM (t/D alternative)']),('R11','d4',['TI (selected4/I)','TY intended editorial reading']),('R11','h3q5qf2s586',['ROZEZVUCELA selected from q at5,2 at7,s at8','wordunit5 q/Z supported by internalq reference; priorg/K rejected; global396','wordunit7 2/U selected;5/E alternative gives ROZEZVECELA; global398','wordunit8 s/C supported by angulars references; priord/T rejected; global399','Previous ROZEKVUTELA and its rozekvetela editorial interpretation rejected after source comparison'])]:
 row=next(r for r in record['rows'] if r['id']==rid);off=row['cipher'].index(word)
 start=1+sum(c in key for c in row['cipher'][:off]);n=sum(c in key for c in word)
 before=sum(r['active_units'] for r in record['rows'] if int(r['id'][1:])<int(rid[1:]))
 items.append({'row':rid,'cipher':word,'literal':''.join(key.get(c,c) for c in word),'row_units':[start,start+n-1],'global_units':[before+start,before+start+n-1],'alternatives_or_editorial':alternatives})
(W/'uncertainties.json').write_text(json.dumps({'opaque_spans':[],'note':'No unreadable span assigned a guessed length. Selected shape readings remain candidates; bounded alternatives are not extra cipher units.','items':items},indent=2)+'\n')
