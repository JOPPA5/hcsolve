from PIL import Image
import sys
P='work/hires/cpc_1912-03-26_HU__HU_Jasz-Arokszalas_jolanka-12_adr.jpg'
im=Image.open(P).convert('RGB')
# (row, x0,x1 in row crop coords) gallery of loop signs
rows=[(60,190),(170,300),(285,410),(400,525),(520,690),(650,770),(760,900),(880,1020),(990,1125),(1100,1235),(1200,1330),(1310,1435),(1430,1555),(1540,1700),(1710,1850)]
items=[('i r2',2,1010,1130),('o r2',2,630,750),('o r2b',2,1340,1460),('o r6a',6,170,280),('o r6b',6,520,620),('o r6c',6,870,970),('i r6',6,1150,1260),
('i r7',7,150,270),('i r7b',7,1450,1560),('i r13',13,1060,1180),('o r11',11,690,790),('o r11b',11,1420,1500),
('A r8',8,510,650),('B r8',8,970,1080),('C r8',8,1380,1460)]
from PIL import ImageDraw
sc=4;cols=5
cw=140*sc;ch=150*sc
sheet=Image.new('RGB',(cols*cw,((len(items)+cols-1)//cols)*ch),'white')
d=ImageDraw.Draw(sheet)
for n,(lab,r,a,b) in enumerate(items):
    y0,y1=rows[r-1]
    y0-=5;y1=y0+150
    c=im.crop((60+a,y0,60+b,y1))
    c=c.resize((c.width*sc,c.height*sc),Image.LANCZOS)
    x,y=(n%cols)*cw,(n//cols)*ch
    sheet.paste(c,(x,y)); d.text((x+4,y+4),lab,fill='blue')
sheet=sheet.resize((sheet.width*2//3,sheet.height*2//3))
sheet.save('work/crops2/loops.png'); print(sheet.size)
