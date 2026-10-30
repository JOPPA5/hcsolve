#!/usr/bin/env python3
"""Explicit mutator of work/ only. Manual shape labels, not OCR.
Native row boxes and ambiguity/control boxes were visually placed.
"""
from pathlib import Path
from PIL import Image,ImageDraw,ImageFont
import re,json,hashlib
W=Path(__file__).resolve().parent;C=W.parent;R=C.parents[1]
def write_json(name,obj): (W/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()
frozen=json.loads((R/'batches/easy-2026-10-28/cz239-241-source-sha256.json').read_text())
source={name:frozen[f'ciphers/hcp-1560/source/{name}'] for name in ['picture.jpg','address.jpg','metadata.md']}
for name,h in source.items():assert sha(C/'source'/name)==h,(name,'original changed')
write_json('source-sha256.json',source)
family=json.loads((R/'ciphers/hcp-1520/work/key.json').read_text())
key={label:plain.upper() for label,plain in dict(family,v='f').items()};write_json('key.json',key)
refs=['ciphers/hcp-1520/work/key.json','batches/easy-2026-10-28/published-anna-ticha-key.txt','batches/easy-2026-10-28/published-anna-ticha-key-provenance.json','batches/easy-2026-10-28/public-reference-199/picture.jpg','batches/easy-2026-10-28/public-reference-199/provenance.json']
write_json('reference-sha256.json',{name:sha(R/name) for name in refs})
write_json('input-sha256.json',{f'ciphers/hcp-1560/{name}':sha(C/name) for name in ['source/picture.jpg','source/address.jpg','source/metadata.md','SOURCES.md']})
im=Image.open(C/'source/picture.jpg').transpose(Image.Transpose.ROTATE_270);assert im.size==(674,1024);im.save(W/'upright.png')
boxes=[[52,25,638,67],[49,50,638,93],[49,77,638,120],[49,103,638,146],[45,129,638,173],[42,155,638,198],[44,181,638,225],[42,207,638,250],[244,232,638,276],[47,258,638,302],[43,284,638,328],[43,310,638,354],[415,334,638,376],[463,359,638,400],[503,384,626,423]]
texts=(W/'transcription.txt').read_text().splitlines();assert len(texts)==15
unknowns={
'U1':dict(row='R03',native_box=[532,80,568,113],unit_count=None,kind='blotted cipher span',description='Unasserted prefix after clear q5 and before clear suffix586; source retracing/overlap prevents a fixed glyph sequence or count. Musela is only a contextual completion.'),
'U2':dict(row='R06',native_box=[514,160,536,193],unit_count=None,kind='blotted cipher span',description='Unasserted ink after clear y and before next q6g5hm6; no fixed number of concealed signs. E/je is only a contextual completion.'),
'U3':dict(row='R10',native_box=[137,262,163,293],unit_count=None,kind='unclassified ink span',description='Heavy ink between c3p5 and d6g on printed halftone. Whether active cipher signs, punctuation, correction or no additional active unit is hidden is unresolved. No cancellation or fixed unit count asserted.')}
write_json('uncertainties.json',unknowns)
rows=[];positions=[];literal=[];known=0
for n,(text,box) in enumerate(zip(texts,boxes),1):
 rid=f'R{n:02}';tokens=[];out=[];ordinal=0
 for match in re.finditer(r'⟦U\d+⟧|.',text):
  token=match.group();item=dict(column=match.start()+1)
  if token in key:
   known+=1;ordinal+=1;item.update(type='glyph',cipher=token,base=key[token],known_index=known,row_known_ordinal=ordinal)
   positions.append(dict(known_index=known,row=rid,row_known_ordinal=ordinal,column=match.start()+1,label=token,base=key[token]));out.append(key[token])
  elif token.startswith('⟦'):
   ident=token[1:-1];assert ident in unknowns;item.update(type='unknown',id=ident);out.append(token)
  else:
   assert token in ' .,!?-';item.update(type='separator',text=token);out.append(token)
  tokens.append(item)
 crop=im.crop(box);crop.resize((crop.width*3,crop.height*3),Image.Resampling.NEAREST).save(W/(rid+'-rawNN.png'))
 plain=''.join(out);literal.append(plain);rows.append(dict(id=rid,orientation='native upright: picture.jpg lossless90degrees clockwise / ROTATE_270',native_box=box,crop=rid+'-rawNN.png',crop_scale=3,cipher=text,plaintext=plain,known_units=ordinal,tokens=tokens))
write_json('rows.json',dict(method='Manual shape transcription; native boxes locate physical row context and may include neighboring ascenders/descenders. Global known_index is an index of known glyphs, NOT original absolute cipher positions after uncounted spans. Columns are text offsets, not glyph coordinates.',rows=rows));write_json('positions.json',positions)
(W/'literal.txt').write_text('\n'.join(literal)+'\n')
fields=[
 dict(face='picture',orientation='90degrees clockwise native674x1024',kind='cipher',area=[42,25,638,423],description='15 physical rows; R01-R12 main text, R09 starts to right of printed FORTE; R13-R15 shorter descending right-hand ending/signature. No detached marginal cipher found.'),
 dict(face='picture',orientation='same',kind='ordinary handwritten date',area=[527,409,642,450],description='17.III.1903; ordinary numerals/date, not cipher.'),
 dict(face='picture',orientation='same',kind='printed',area=[119,231,249,268],description='FORTE, printed piano/dynamic text, not encrypted letters. Image depicts a couple beside piano; no cipher elsewhere in art, border or lower field.'),
 dict(face='picture',orientation='same',kind='overprint',area=[28,29,640,975],description='Grey HCPortal watermark and printed halftone may cross handwriting; not extra cipher symbols.'),
 dict(face='address',orientation='original upright1024x674',kind='ordinary handwritten address',area=[211,294,803,569],description='Velectěná Slečna / slečna Anna Tichá / učitelka v / Žirovnici / u Počátek. Diagonal strokes cross the destination area; no historical reason inferred.'),
 dict(face='address',orientation='original',kind='ordinary handwritten addition',area=[91,440,397,618],description='v Kamenici nad Lipou, lower left. Not cipher.'),
 dict(face='address',orientation='original',kind='printed',area=[65,61,543,265],description='Postkarte–Carte postale and multilingual postal headings; not cipher.'),
 dict(face='address',orientation='original',kind='printed/postal',area=[470,35,961,284],description='5-heller stamp and overlapping postmarks incl. PRAHA and destination-area lettering; exact postal dates not claimed or required for cipher reading.'),
 dict(face='address',orientation='rotated printing at left edge',kind='printed credit',area=[44,331,79,469],description='B.K.W.I.6575-style printer code; ordinary print, no cipher assignment.'),
 dict(face='address',orientation='original',kind='watermark/border',area=[22,24,981,650],description='Grey HCPortal collection watermark, rules and border; entire remaining face inspected, no extra encrypted region identified.'),
]
write_json('field-inventory.json',fields)
display=lambda value:value.replace('⟦','[').replace('⟧',']')
font=ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc',17);small=ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc',15)
for k in range(0,15,5):
 part=rows[k:k+5];height=sum(62+(r['native_box'][3]-r['native_box'][1])*3 for r in part);panel=Image.new('RGB',(1900,height),'white');draw=ImageDraw.Draw(panel);y=0
 for row in part:
  draw.text((8,y),row['id']+' '+display(row['plaintext']),font=font,fill='black');draw.text((8,y+22),'Native box '+str(row['native_box'])+'; source NN3x; cipher '+display(row['cipher']),font=small,fill='black')
  tile=Image.open(W/row['crop']);panel.paste(tile,(8,y+54));y+=tile.height+62
 panel.save(W/f'indexed-rows-{k+1:02}-{k+len(part):02}.png')
controls=[
 ('R03 blotted prefix U1, q5 / suffix586 / 2- retained',[496,75,638,120],5),
 ('R06 U2 after y, clear following q6g5hm6 retained',[489,154,637,198],5),
 ('R10 U3 ink before d6g; no cancellation/count asserted',[98,253,212,302],5),
 ('R05 ZANETU initial q: open terminal hook',[385,132,416,179],5),
 ('R01 ZA q/Z comparison: same open terminal hook',[432,27,454,70],5),
 ('R02 ZPRAVOU q/Z comparison',[411,51,438,95],5),
 ('R01 LISTEK g/K comparison: long returning loop',[573,29,597,74],5),
 ('R06 CHRIPKA g/K comparison: long returning loop',[468,157,489,198],5),
 ('R08 BICH BIL: source4/I, H/CH and8/L remain literal',[346,208,515,254],5),
 ('R09 BICH TE: same I/CH usage',[357,232,639,278],3),
 ('R10 BICH TE / LISOVAL: source I retained',[268,257,638,303],3),
 ('R02 VSAK: round c/S, not angular s/C',[283,51,343,95],5),
 ('R12 BRZKOU ZPRAVU over halftone: visible stems/loops',[42,306,280,354],5),
 ('R01 DIK: known underbarred4/I reference',[386,25,436,69],5),
 ('R08 VYHOVETI: known footed1/Y reference',[245,205,349,251],5),
 ('R13 DLOUHYCH: known1/Y before cappedCH',[486,334,574,377],5),
]
recs=[]
for n,(label,b,scale) in enumerate(controls,1):
 tile=im.crop(b);name=f'control-{n:02}-rawNN.png';tile.resize((tile.width*scale,tile.height*scale),Image.Resampling.NEAREST).save(W/name);recs.append(dict(id=n,description=label,native_box=b,scale=scale,file=name))
write_json('source-controls.json',dict(source_sha256=source['picture.jpg'],orientation='picture.jpg losslessROTATE_270 /90degrees clockwise; native674x1024',resampling='nearest',controls=recs))
for k in range(0,len(recs),5):
 part=recs[k:k+5];height=sum(51+(r['native_box'][3]-r['native_box'][1])*r['scale'] for r in part);panel=Image.new('RGB',(1900,height),'white');draw=ImageDraw.Draw(panel);y=0
 for rec in part:
  draw.text((8,y),rec['description'],font=font,fill='black');draw.text((8,y+22),'Native box '+str(rec['native_box'])+'; nearest-neighbor '+str(rec['scale'])+'x',font=small,fill='black');tile=Image.open(W/rec['file']);panel.paste(tile,(8,y+46));y+=tile.height+51
 panel.save(W/f'control-panel-{k//5+1}.png')
print(f'{len(rows)}rows; {known}known units; {sum(len(p["base"]) for p in positions)}known base letters; CH={sum(p["label"]=="H" for p in positions)}; observed classes={len(set(p["label"] for p in positions))}/23; unknown spans=3')
print('\n'.join(row['id']+' '+display(row['plaintext']) for row in rows))
