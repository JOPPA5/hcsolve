# reviewer's sign comparison panel: candidate signs at the same scale
from PIL import Image, ImageDraw
im=Image.open('../../work/hires/cpc_1914-10-15_HU__HU_Budapest_jolanka-55_adr.jpg').convert('RGB')
P=[('r21 sign9',890,1850,985,1945),('r21 blob',1060,1845,1225,1965),('r17 i',935,1455,1020,1550),('r2 i',135,160,205,245),('stamp i',3020,685,3085,760),
   ('r18 i',560,1560,650,1640),('r19 z',1115,1665,1215,1745),('r20 s3',298,1755,420,1850),('r12 z',675,990,775,1075),('r7 ?d',540,560,640,640),('r1 d',770,70,850,150),('r9 ?',0,0,1,1)]
P=P[:-1]
S=4; W=1760; x=y=0; h=0
o=Image.new('RGB',(W,1000),'white'); d=ImageDraw.Draw(o)
for n,a,b,c,e in P:
    t=im.crop((a,b,c,e)); t=t.resize((t.width*S,t.height*S),Image.LANCZOS)
    if x+t.width>W: x=0;y+=h+30;h=0
    o.paste(t,(x,y+20)); d.text((x+4,y+2),n,fill='black'); x+=t.width+12; h=max(h,t.height+20)
o.crop((0,0,W,y+h+10)).save('crops/panel.jpg',quality=90)
