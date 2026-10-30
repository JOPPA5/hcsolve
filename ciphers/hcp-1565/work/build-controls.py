"""Authoring only: source crops and nearest-neighbour controls; never OCR."""
from pathlib import Path
from PIL import Image, ImageDraw
import json
W=Path(__file__).resolve().parent
p=Image.open(W.parent/'source/picture.jpg')
frames={'original':p,'ccw90':p.transpose(Image.Transpose.ROTATE_90)}
spec=[
 ('C01','original',[393,534,515,575],'H02 q82c3f6d4 / zlusovati; c/S, f/V'),
 ('C02','original',[595,586,730,628],'H04 t32f6n / douvam; tall f/V'),
 ('C03','original',[857,537,974,582],'H02 s3 m5y / co nej; s/C versus c/S'),
 ('C04','original',[443,588,568,628],'H04 t2dg84f5 / dutklive; t/D versus d/T'),
 ('C05','original',[854,507,970,548],'H01 3p86q48 / oblazil; p/B'),
 ('C06','original',[705,563,972,609],'H03 monopolu / obedvam; m/N,n/M,p/B,b/P'),
 ('C07','ccw90',[306,862,410,904],'M03 p86q4c4 / blazisi; c/S preferred, s/C alternative'),
 ('C08','ccw90',[123,809,255,849],'M01 6n3hg6 / amorka'),
 ('C09','ccw90',[250,811,372,850],'M01 ct5848 / sdelil; c/S, d/T,4/I'),
 ('C10','ccw90',[167,889,493,937],'M04 dravu a dlouhych pus posila; H/CH'),
 ('C11','ccw90',[197,921,315,966],'M05 b5b32 plus unresolved heart U06'),
 ('C12','ccw90',[25,810,170,970],'Postmark crossings U01-U05; no cancellation'),
 ('C13','ccw90',[290,920,458,994],'Ordinary handwritten date; month remains QA point'),
]
items=[];panels=[]
for cid,frame,box,label in spec:
 im=frames[frame].crop(box)
 native=cid+'-native.png'; nn=cid+'-nn.png'
 im.save(W/native);big=im.resize((im.width*3,im.height*3),Image.Resampling.NEAREST);big.save(W/nn)
 sheet=Image.new('RGB',(1050,im.height+big.height+44),'white');d=ImageDraw.Draw(sheet)
 d.text((5,3),cid+' '+label,fill='black');sheet.paste(im,(5,22));sheet.paste(big,(5,im.height+32));panels.append(sheet)
 items.append({'id':cid,'frame':frame,'box':box,'label':label,'native':native,'nearest_neighbour':nn})
contact=Image.new('RGB',(1050,sum(im.height for im in panels)),'white');y=0
for im in panels:contact.paste(im,(0,y));y+=im.height
contact.save(W/'controls.png')
(W/'controls.json').write_text(json.dumps({'source':'source/picture.jpg','coordinate_frames':{'original':[1024,674],'ccw90':[674,1024]},'method':'Native source crops plus 3x nearest-neighbour copies, no filtering or OCR. Labels report manual readings, not automatic proof.','controls':items},indent=2)+'\n')
