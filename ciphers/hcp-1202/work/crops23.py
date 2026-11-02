import sys,os; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from crops import *
from PIL import Image
ys=[1003,1082,1159,1233,1323,1391,1465,1530,1603,1690,1771,1845,1909,1985,2043,2108]
for r,y in enumerate(ys):
    strips=[]
    for x,dy in ((150,0),(760,-14),(1370,-28),(1980,-42)):
        strips.append(im.crop((x,y-62+dy,x+640,y+62+dy)).resize((1408,273),Image.LANCZOS))
    out=Image.new('RGB',(1408,4*280),'white')
    for i,s in enumerate(strips): out.paste(ImageEnhance.Contrast(s).enhance(1.5),(0,i*280))
    out.save(D+f'/crops/L{r:02d}.png')
