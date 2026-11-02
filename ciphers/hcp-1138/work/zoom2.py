from PIL import Image, ImageEnhance
import os
d=os.path.dirname(os.path.abspath(__file__))
r=Image.open(d+'/crops/rot48.png')
S=1.361
for name,x0,y0,x1,y1 in [('h',680,430,1000,530),('i',540,1050,820,1130),('j',800,1070,1100,1160),('k',780,370,1250,460),('l',430,1020,620,1110)]:
    c=r.crop((int(x0*S),int(y0*S),int(x1*S),int(y1*S)))
    c=c.resize((c.width*4,c.height*4),Image.LANCZOS)
    ImageEnhance.Contrast(c).enhance(1.4).save(d+'/crops/z_%s.png'%name)
