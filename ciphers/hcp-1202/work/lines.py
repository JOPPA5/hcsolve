import sys,os; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from crops import *
from PIL import Image
def line(name,x0,y0,x1,y1,xa,xb,h=62):
    # straighten by column shifts, output in 3 stacked parts
    W=xb-xa; out=Image.new('RGB',(W,2*h))
    for x in range(xa,xb):
        y=int(y0+(y1-y0)*(x-x0)/(x1-x0))
        out.paste(im.crop((x,y-h,x+1,y+h)),(x-xa,0))
    n=3; seg=W//n+30; r=Image.new('RGB',(1420,n*(int(2*h*1420/seg)+6)),'white')
    for i in range(n):
        s=out.crop((i*(W//n),0,min(W,i*(W//n)+seg),2*h)).resize((1420,int(2*h*1420/seg)),Image.LANCZOS)
        r.paste(ImageEnhance.Contrast(s).enhance(1.6),(0,i*(int(2*h*1420/seg)+6)))
    r.save(D+'/crops/'+name+'.png')
line('R15',300,1225,1900,1290,150,2040)
line('R16',300,1320,1900,1335,150,2040)
line('R17',300,1391,1800,1400,150,2040)
line('R18',300,1462,1800,1470,150,2040)
line('LA',300,1985,1900,1985,150,2060)
line('L4a',300,2040,2200,2042,150,1500)
line('L4b',1400,2045,3300,2054,1400,3420)
line('L5',300,2110,3000,2130,150,3420,55)
