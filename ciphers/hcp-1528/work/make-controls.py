#!/usr/bin/env python3
from PIL import Image,ImageDraw
from pathlib import Path
import json
p=Path(__file__).resolve().parent;im=Image.open(p.parent/'source/picture.jpg')
boxes={'jo':(302,137,340,174),'jsem':(501,45,564,78),'jiz':(276,77,330,110),'ti':(139,536,181,568),'do-D':(171,138,201,173),'k-zarmoutis':(40,475,78,510),'k-dik':(155,42,182,78),'z-za':(187,42,220,78),'z-zadnou':(283,175,377,208),'signature':(222,537,338,570),'a-posila':(29,537,139,570),'r2word':(709,76,853,112),'R05 I-J':(641,175,666,212),'I-DIK':(148,43,161,77),'J-JSEM':(538,47,558,78),'R12 K-Z':(143,410,162,445),'K-VSAK':(123,410,143,445),'K-KDE':(334,441,357,478),'Z-ZA':(185,43,208,78),'Z-ZADNOU':(344,174,367,211)}
canvas=Image.new('RGB',(900,len(boxes)*120),'white');d=ImageDraw.Draw(canvas)
for i,(name,box) in enumerate(boxes.items()):
 crop=im.crop(box).resize(((box[2]-box[0])*3,(box[3]-box[1])*3),Image.Resampling.NEAREST)
 canvas.paste(crop,(200,i*120));d.text((5,i*120+20),name,fill='black')
canvas.save(p/'same-card-controls.png');(p/'control-boxes.json').write_text(json.dumps(boxes,indent=2)+'\n')
