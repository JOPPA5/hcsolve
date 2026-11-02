import sys,os; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from crops import *
from PIL import Image
Y=[185,255,334,412,500,555,623,705,780,840,920,985,1075,1165,1230,1320,1388,1462,1530,1609,1692,1777,1846,1915,1982,2045,2105]
for r,y in enumerate(Y,1):
    segs=[(140,800),(760,1420),(1380,2040),(2000,2660),(2620,3440)]
    if y<1700: segs=segs[:4]
    o=Image.new('RGB',(1400,len(segs)*262),'white')
    for i,(a,b) in enumerate(segs):
        yy=y-int((a-150)*0.022)
        c=im.crop((a,yy-58,b,yy+58))
        c=c.resize((1400,int(1400*116/(b-a))),Image.LANCZOS)
        o.paste(ImageEnhance.Contrast(c).enhance(1.6),(0,i*262))
    o.save(D+f'/crops/row{r:02d}.png')
