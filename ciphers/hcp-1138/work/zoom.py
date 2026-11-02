from PIL import Image, ImageEnhance
import sys,os
d=os.path.dirname(os.path.abspath(__file__))
r=Image.open(d+'/crops/rot48.png')
S=1.361
for name,x0,y0,x1,y1 in [('a',1150,960,1560,1080),('b',1500,930,1800,1060),('c',130,950,560,1060),('d',880,590,1230,680),('e',1700,890,1900,980),('f',800,840,1100,920),('g',1040,1000,1200,1070)]:
    c=r.crop((int(x0*S),int(y0*S),int(x1*S),int(y1*S)))
    c=c.resize((c.width*4,c.height*4),Image.LANCZOS)
    ImageEnhance.Contrast(c).enhance(1.4).save(d+'/crops/z_%s.png'%name)
