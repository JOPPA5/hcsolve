from pathlib import Path
from PIL import Image,ImageDraw,ImageFont
import json
W=Path(__file__).resolve().parent
im=Image.open(W.parent/'source/picture.jpg')
font=ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc',16)
items=[('M01', [380,109,944,149]),('M02',[382,137,945,172]),('M03',[383,160,937,197]),('M04',[382,186,951,224]),('I04',[645,181,702,209]),('M07',[381,270,951,306]),('M08',[380,299,944,344]),('M11',[430,387,961,444]),('M14',[380,481,941,534])]
out=Image.new('RGB',(1772,len(items)*202),'white');d=ImageDraw.Draw(out)
for i,(name,b) in enumerate(items):
 y=i*202;d.text((12,y+5),f'{name}: source box {b}; raw nearest-neighbor 3x',font=font,fill='black')
 crop=im.crop(b).resize(((b[2]-b[0])*3,(b[3]-b[1])*3),Image.Resampling.NEAREST)
 out.paste(crop,(12,y+30));d.rectangle((11,y+29,12+crop.width,y+30+crop.height),outline='black')
 for x in range(((b[0]+9)//10)*10,b[2],10):
  xx=12+(x-b[0])*3;yy=y+35+crop.height;d.line((xx,yy-5,xx,yy),fill='black');d.text((xx-10,yy),str(x),font=font,fill='black')
out.save(W/'control-row-boxes-rawNN.png')
(W/'control-row-boxes.json').write_text(json.dumps({'source':'picture.jpg','scale':3,'resampling':'nearest neighbor','boxes':dict(items)},indent=2)+'\n')
# Isolated raw-nearest-neighbor crops with their full source-row context.
groups={
 'gq':[
  ('U2 M08 standalone', [550,311,575,342], 'M08',[380,299,944,344]),
  ('U3 M11 standalone', [587,405,609,435], 'M11',[430,387,961,444]),
  ('U5 M14 initial', [412,492,438,526], 'M14',[380,481,941,534]),
  ('g/K M11 KDO initial',[435,398,462,433],'M11',[430,387,961,444]),
  ('g/K M08 KAZDY initial',[479,309,503,341],'M08',[380,299,944,344]),
  ('q/Z M07 ZA initial',[380,277,403,310],'M07',[381,270,951,306]),
  ('q/Z M01 ZA initial',[735,123,760,155],'M01',[380,109,944,149]),
  ('q/Z M05 JEZ last',[657,222,678,250],'M05',[380,214,956,251]),
 ],
 's4':[
  ('U1 M02 angular glyph',[543,144,556,161],'M02',[382,137,945,172]),
  ('s/C M04 CASE initial',[628,197,644,217],'M04',[382,186,951,224]),
  ('s/C I04 MOCI third',[677,188,689,201],'I04',[640,182,700,208]),
  ('4/I M02 MINKU second',[400,139,418,164],'M02',[382,137,945,172]),
  ('4/I M07 LISTKY second',[709,278,723,298],'M07',[381,270,951,306]),
 ]}
allrecords={}
for group,parts in groups.items():
 out=Image.new('RGB',(1800,len(parts)*210),'white');d=ImageDraw.Draw(out)
 for i,(label,b,rid,rowbox) in enumerate(parts):
  y=i*210;d.text((10,y+3),f'{label} | glyph source box {b} | glyph raw NN 5x',font=font,fill='black')
  glyph=im.crop(b).resize(((b[2]-b[0])*5,(b[3]-b[1])*5),Image.Resampling.NEAREST)
  out.paste(glyph,(10,y+28));d.rectangle((9,y+27,10+glyph.width,y+28+glyph.height),outline='black')
  d.text((180,y+23),f'{rid} source row box {rowbox}; row raw NN 2x',font=font,fill='black')
  crop=im.crop(rowbox).resize(((rowbox[2]-rowbox[0])*2,(rowbox[3]-rowbox[1])*2),Image.Resampling.NEAREST)
  out.paste(crop,(180,y+48));d.rectangle((179,y+47,180+crop.width,y+48+crop.height),outline='black')
  for x in range(((rowbox[0]+19)//20)*20,rowbox[2],20):
   xx=180+(x-rowbox[0])*2;yy=y+54+crop.height;d.line((xx,yy-5,xx,yy),fill='black');d.text((xx-10,yy),str(x),font=font,fill='black')
 out.save(W/f'control-{group}-rawNN.png')
 allrecords[group]=[{'label':label,'glyph_box':b,'row':rid,'row_box':rb} for label,b,rid,rb in parts]
(W/'control-panels.json').write_text(json.dumps({'source':'picture.jpg','glyph_scale':5,'row_scale':2,'resampling':'nearest neighbor','groups':allrecords},indent=2)+'\n')
