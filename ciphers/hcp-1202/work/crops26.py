import sys,os; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from crops import *
from PIL import Image
def seg(y0,y1):
    c=im.crop((135,y0,262,y1)).rotate(-90,expand=True)
    return ImageEnhance.Contrast(c.resize((int(c.width*2.4),int(c.height*2.4)),Image.LANCZOS)).enhance(1.6)
segs=[seg(1560,2130),seg(1000,1600),seg(450,1040)]
o=Image.new('RGB',(1450,3*320),'white')
for i,s in enumerate(segs): o.paste(s,(0,i*320))
o.save(D+'/crops/M_cw.png')
segs=[s.rotate(180) for s in segs]
o=Image.new('RGB',(1450,3*320),'white')
for i,s in enumerate(segs): o.paste(s,(0,i*320))
o.save(D+'/crops/M_ccw.png')
crop('T1',(1450,100,2900,300),1.0)
crop('T1r',(1450,100,2900,300),1.0,rot=180)
crop('Q2',(2720,2030,3080,2100),3.9)
crop('S2',(1720,2045,2300,2125),2.5)
crop('S3',(1250,2045,1760,2120),2.8)
