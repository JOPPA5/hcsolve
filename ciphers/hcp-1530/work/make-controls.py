#!/usr/bin/env python3
"""Explicit focused controls, unfiltered original pixels and enlarged contact sheet."""
from pathlib import Path
import json
from PIL import Image,ImageDraw
R=Path(__file__).resolve().parents[1];W=R/'work'
upright=Image.open(R/'source/picture.jpg').transpose(Image.Transpose.ROTATE_90);top=upright.crop((28,35,642,195)).transpose(Image.Transpose.ROTATE_180)
controls=[('U1','top',[300,0,614,38],'Unresolved word after DRAHE; nearby DRAHE retained.'),('U2','bottom',[437,778,642,819],'Unresolved dark word after ANUSKA.'),('UF','bottom',[325,884,464,921],'RUDOLFINE shallow-v F; later published card199 photo transfer.'),('U3','bottom',[315,952,489,991],'JE...MU unresolved middle.'),('U4','bottom',[331,917,452,956],'URA... retained initial three shapes; final dark span unresolved.'),('T03-KTERE','top',[350,59,501,95],'Literal KTERE, not grammatical repair to KTERA.'),('T04-NEVHOD','top',[185,88,318,125],'Literal NEVHOD, not repaired to NEVHODNE.'),('B07-title','bottom',[165,882,306,925],'Ordinary-script Issajův, uncertain paleography.'),('B03-CH','bottom',[315,748,425,786],'CH comparator in CHVILKY.'),('B04-CH','bottom',[60,780,203,819],'CH comparator in RYCHLE and PRCHAJI.'),('B06-CH','bottom',[190,850,330,887],'CH comparator in CHTEL.'),('B05-f','bottom',[135,814,325,852],'Known tall f=V in VECERY for comparison with shallow UF.')]
manifest=[];tiles=[]
for ident,system,box,desc in controls:
 base=top if system=='top' else upright;x=base.crop(box);x.save(W/(ident+'-original.png'))
 if system=='top':original=[829+box[1],642-box[2],829+box[3],642-box[0]]
 else:original=[1024-box[3],box[0],1024-box[1],box[2]]
 manifest.append({'id':ident,'coordinate_system':system,'box_xyxy':box,'original_picture_xyxy':original,'file':ident+'-original.png','description':desc,'filter':'none; crop and lossless transpose only'})
 tile=Image.new('RGB',(1256,160),'white');d=ImageDraw.Draw(tile);d.text((8,4),ident+' : '+desc,fill='black');xx=x.resize((x.width*3,x.height*3));tile.paste(xx,(8,23));tiles.append(tile)
sheet=Image.new('RGB',(1256,160*len(tiles)),'white')
for i,tile in enumerate(tiles):sheet.paste(tile,(0,i*160))
sheet.save(W/'focused-controls.png');(W/'focused-controls.json').write_text(json.dumps(manifest,indent=2)+'\n')
