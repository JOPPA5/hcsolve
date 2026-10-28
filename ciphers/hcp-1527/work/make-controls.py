from pathlib import Path
from PIL import Image,ImageDraw
import json
R=Path(__file__).resolve().parents[1];W=R/'work'
im=Image.open(R/'source/picture.jpg').transpose(Image.Transpose.ROTATE_90)
boxes=[('R08 CTVRT',[47,787,178,830]),('R07 PRED',[554,756,637,798]),('R01 DIK + ZA',[161,571,285,618]),('R01 PSANKO',[308,571,444,618]),('R04 NENALEZIM TEZ',[424,669,637,716]),('R12 STRAVILO',[44,917,181,961])]
out=Image.new('RGB',(1020,len(boxes)*190),'white');d=ImageDraw.Draw(out)
for i,(label,box) in enumerate(boxes):
 d.text((5,i*190+8),label,fill='black');z=im.crop(box);z=z.resize((z.width*4,z.height*3),Image.Resampling.NEAREST);out.paste(z,(160,i*190))
out.save(W/'focused-controls.png')
(W/'focused-controls.json').write_text(json.dumps({'source':'source/picture.jpg','working_transform':'PIL ROTATE_90, no resampling','boxes_upright_xyxy':dict(boxes),'display_scale':'4x horizontal, 3x vertical nearest neighbour; no sharpening/denoising'},indent=2)+'\n')
