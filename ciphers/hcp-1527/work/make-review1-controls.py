"""Source-derived controls for the six Review 1 findings; not OCR or mutation of originals."""
from pathlib import Path
from PIL import Image,ImageDraw
import json,hashlib
R=Path(__file__).resolve().parents[1];W=R/'work'
im=Image.open(R/'source/picture.jpg').transpose(Image.Transpose.ROTATE_90)
controls=[
('R02-name','R02 SEDLAC-: extra angular s/C before hyphen',[544,603,642,650]),
('R02-CLECNA','R02 CLECNA: angular s/C at first and fourth positions',[459,603,560,650]),
('R03-MNOHO','R03 MNOHO: n/M then m/N control',[184,634,302,680]),
('R03-NME','R03 final mn5/NME: m/N then n/M',[556,634,640,680]),
('R10-POSILA','R10 POSILA: fourth sign underbarred 4/I',[541,852,643,901]),
('R01-BYL','R01 BYL: flagged/footed 1/Y control',[570,568,641,619]),
('R11-CRDECKU','R11 CRDECKU: initial angular s/C',[392,880,525,931]),
('R07-SRDECKA','R07 SRDECKA: initial round c/S control',[196,755,321,800]),
('R06-JINYMI','R06 JINYMI: retraced fourth sign, preferred 1/Y, possible 2/U',[35,733,156,769])]
out=Image.new('RGB',(1200,len(controls)*265),'white');d=ImageDraw.Draw(out)
for i,(name,label,b) in enumerate(controls):
 d.text((5,i*265+4),label,fill='black');z=im.crop(b).resize(((b[2]-b[0])*5,(b[3]-b[1])*5),Image.Resampling.NEAREST);z.save(W/f'review1-{name}.png');out.paste(z,(5,i*265+24))
out.save(W/'review1-controls.png')
(W/'review1-controls.json').write_text(json.dumps({'source':'source/picture.jpg','source_sha256':hashlib.sha256((R/'source/picture.jpg').read_bytes()).hexdigest(),'frame':'PIL ROTATE_90; native674x1024; lossless counterclockwise transpose','display':'5x uniform nearest neighbour; no enhancement','controls':[{'file':'review1-'+name+'.png','label':label,'box_upright_xyxy':box} for name,label,box in controls]},indent=2)+'\n')
