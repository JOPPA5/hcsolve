#!/usr/bin/env python3
from pathlib import Path
import json
from PIL import Image,ImageDraw
R=Path(__file__).resolve().parents[1];W=R/'work'
im=Image.open(R/'source/picture.jpg').transpose(Image.Transpose.ROTATE_270)
controls=[
('C01','A02 DUSICKO: D / I / C classes',[43,638,149,682]),
('C02','A06 SRDECKEM: E after K, not A',[70,747,195,792]),
('C03','A07 ANUNKO and BUD: 2=U control',[110,777,244,825]),
('C04','A08 VZDIT: 4=I; 1=Y in SVYM above',[125,748,238,854]),
('C05','A10 CHOROBU: neutral special CH shape',[117,862,231,906]),
('C06','A11 PREMUZE and continuation arrow',[137,891,263,931]),
('C07','B03 TISIC: source base letters',[549,684,636,736]),
('C08','B04 VRELYCH UPRIMNYCH: two CH units',[437,715,635,767]),
('C09','B06 MYSLEN: dark pen stroke in M label n',[528,774,636,825]),
('C10','B07 CH / DLI and B08 TEBE',[437,806,635,877])]
out=Image.new('RGB',(850, sum((b[3]-b[1])*4+48 for _,_,b in controls)+10),'white');d=ImageDraw.Draw(out);y=5
for cid,label,b in controls:
 d.text((8,y),f'{cid}: {label}; upright xyxy={b}',fill='black');y+=23
 crop=im.crop(b);crop.save(W/(cid+'-native.png'))
 enlarged=crop.resize((crop.width*4,crop.height*4),Image.Resampling.NEAREST)
 out.paste(enlarged,(8,y));enlarged.save(W/(cid+'.png'));y+=enlarged.height+25
out.save(W/'focused-controls.png')
(W/'focused-controls.json').write_text(json.dumps({'orientation':'source/picture.jpg lossless ROTATE_270','dimensions':[674,1024],'processing':'Original pixels cropped, nearest-neighbor enlarged 4x; no contrast, sharpening, interpolation, cleanup or synthesized strokes.','controls':[{'id':cid,'note':label,'box_upright_xyxy':b} for cid,label,b in controls]},indent=2)+'\n')
