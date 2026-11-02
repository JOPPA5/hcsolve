import sys,os; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from crops import *
from PIL import Image
import numpy as np
R={6:(557,557,561),7:(626,640,650),8:(711,711,720),9:(790,800,812),10:(847,860,870),11:(922,931,941),12:(988,997,1011),
13:(1071,1114,1118),14:(1147,1184,1200),15:(1227,1255,1285),16:(1316,1325,1344),17:(1391,1396,1405),18:(1462,1462,1467),
19:(1532,1527,1546),20:(1607,1612,1631),21:(1692,1692,1711),22:(1776,1771,1795),23:(1852,1852,1875),24:(1918,1927,1946),
25:(1992,1997,2016),26:(2049,2058,2072),27:(2110,2115,2118)}
for r,ys in R.items():
    xb=2060 if r<22 else 3420
    h=50; W=xb-150; o=Image.new('RGB',(W,2*h))
    for x in range(150,xb):
        y=int(np.interp(x,[300,1000,1700,3400],list(ys)+[ys[2]+(20 if r>=22 else 0)])); o.paste(im.crop((x,y-h,x+1,y+h)),(x-150,0))
    seg=480; step=450; xs=list(range(0,W-100,step)); sc=1420/seg; H=int(2*h*sc)
    out=Image.new('RGB',(1420,len(xs)*(H+6)),'white')
    for i,x0 in enumerate(xs):
        s=o.crop((x0,0,min(W,x0+seg),2*h)); s=s.resize((int(s.width*sc),H),Image.LANCZOS)
        out.paste(ImageEnhance.Contrast(s).enhance(1.6),(0,i*(H+6)))
    # split tall ones in two images
    n=len(xs)
    if n>5:
        out.crop((0,0,1420,5*(H+6))).save(D+f'/crops/N{r:02d}a.png'); out.crop((0,5*(H+6),1420,n*(H+6))).save(D+f'/crops/N{r:02d}b.png')
    else: out.save(D+f'/crops/N{r:02d}.png')
    print(r,n)
