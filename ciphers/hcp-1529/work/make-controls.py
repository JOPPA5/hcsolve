"""Explicit source-pixel control generator; no denoising, sharpening, or OCR."""
from pathlib import Path
import json
from PIL import Image,ImageDraw
R=Path(__file__).resolve().parents[1];W=R/'work';im=Image.open(R/'source/picture.jpg')
boxes={
 'R01 ANICKO':(111,27,242,65),
 'R02 USTI':(908,57,978,96),
 'R03 PRI LICENI':(252,85,411,126),
 'R05 MISLENI SCHOPEN':(712,146,978,191),
 'R06 PROTOZE VSAK':(233,174,475,216),
 'R06 VZKAZAL':(633,175,791,217),
 'R07 V PATEK':(864,206,978,250),
 'R08 SRDECKO + ending':(549,590,978,639),
}
out=Image.new('RGB',(1940,len(boxes)*218),'white');d=ImageDraw.Draw(out)
for i,(label,box) in enumerate(boxes.items()):
 d.text((5,i*218+4),label,fill='black');c=im.crop(box);out.paste(c.resize((c.width*4,c.height*4),Image.Resampling.NEAREST),(205,i*218+15))
out.save(W/'focused-controls.png')
(W/'focused-controls.json').write_text(json.dumps({'source':'source/picture.jpg','transform':'none; original 1024x674 source coordinates','boxes_original_xyxy':boxes,'display':'4x nearest neighbour, no filtering'},indent=2)+'\n')
boxes_iy={
 'R05 MISLENI n4c85m4: second and final 4=I':(733,145,861,190),
 'R03 LICENI 84s5m4: two 4=I':(319,85,416,126),
 'R02 NEBYL m5p18: 1=Y before final8':(48,56,119,96),
 'R03 ZALOZNY q683qm1: final1=Y':(846,85,978,126),
}
out=Image.new('RGB',(1100,4*215),'white');d=ImageDraw.Draw(out)
for i,(label,box) in enumerate(boxes_iy.items()):
 d.text((5,i*215+4),label,fill='black');c=im.crop(box);out.paste(c.resize((c.width*6,c.height*4),Image.Resampling.NEAREST),(5,i*215+28))
out.save(W/'I-Y-control.png')
(W/'I-Y-control.json').write_text(json.dumps({'source':'source/picture.jpg','boxes_original_xyxy':boxes_iy,'display':'6x horizontal,4x vertical nearest neighbour; no source filtering'},indent=2)+'\n')
