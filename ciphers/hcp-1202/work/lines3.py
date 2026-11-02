import sys,os; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from crops import *
from PIL import Image
import numpy as np
R={1:(192,178,170),2:(255,250,245),3:(330,325,318),4:(405,405,400),5:(490,490,485)}
for r,ys in R.items():
    h=58;xb=2060;W=xb-150;o=Image.new('RGB',(W,2*h))
    for x in range(150,xb):
        y=int(np.interp(x,[300,1000,1700],ys)); o.paste(im.crop((x,y-h,x+1,y+h)),(x-150,0))
    n=3; seg=W//n+40; H=int(2*h*1420/seg)
    out=Image.new('RGB',(1420,n*(H+6)),'white')
    for i in range(n):
        s=o.crop((i*(W//n),0,min(W,i*(W//n)+seg),2*h)).resize((1420,H),Image.LANCZOS)
        out.paste(ImageEnhance.Contrast(s).enhance(1.6),(0,i*(H+6)))
    out.save(D+f'/crops/K{r:02d}.png')
