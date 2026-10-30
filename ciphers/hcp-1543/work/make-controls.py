#!/usr/bin/env python3
from pathlib import Path
import json
from PIL import Image,ImageDraw
R=Path(__file__).resolve().parents[1];W=R/'work'
im=Image.open(R/'source/picture.jpg').transpose(Image.Transpose.ROTATE_270)
items=[
('R01 name: 6m4g3, ANIKO; less-secure g/K over discarded q/Z',(180,40,285,89)),
('R01 definite DIK ZA comparison (g/K then q/Z)',(345,42,445,86)),
('R11 JANKOVE: contains g/K',(145,382,280,423)),
('R05 comma ZE MOJE: q/Z comparison',(525,166,649,210)),
('R04 Z HRA[opaque]E: first word r/H, compare loop P below',(29,130,215,177)),
('R06 SRDE[opaque]KO OPET; no cancellation intent assumed',(29,198,335,243)),
('R09 VRELYCH,VASNI VYCH PUS: CH and PUS marks',(29,308,355,354)),
('R09 POSILA TI STALE: compare b/P shape',(350,310,649,355)),
('R01 DRAHY: r/H shape control',(428,42,520,84)),
('R06 PRI VODILA: b/P shape control',(330,198,490,243)),
('R14 RUCENI: verifies closing PORUCENI, not POZDRAVY',(29,470,200,499))
]
canvas=Image.new('RGB',(1400,len(items)*210),'white');d=ImageDraw.Draw(canvas)
record=[]
for i,(label,box) in enumerate(items):
    d.text((8,i*210+3),label,fill='black');crop=im.crop(box);factor=min(4,1380/crop.width,175/crop.height);crop=crop.resize((int(crop.width*factor),int(crop.height*factor)));canvas.paste(crop,(8,i*210+25));record.append({'label':label,'source':'source/picture.jpg','transform':'clockwise90','box_upright_xyxy':box})
canvas.save(W/'controls.png');(W/'controls.json').write_text(json.dumps(record,indent=2)+'\n')
