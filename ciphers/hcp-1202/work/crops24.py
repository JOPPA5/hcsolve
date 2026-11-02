import sys,os; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from crops import *
from PIL import Image
def strips(name,boxes,w=1400):
    ims=[]
    for b in boxes:
        s=w/(b[2]-b[0]); c=im.crop(b).resize((w,int((b[3]-b[1])*s)),Image.LANCZOS)
        ims.append(ImageEnhance.Contrast(c).enhance(1.6))
    H=sum(i.height+10 for i in ims); o=Image.new('RGB',(w,H),'white'); y=0
    for i in ims: o.paste(i,(0,y)); y+=i.height+10
    o.save(D+'/crops/'+name+'.png')
strips('Y1',[(1300,1990,1830,2100),(1800,1990,2330,2110),(2300,2010,2830,2120),(2800,2010,3400,2130)])
strips('Y2',[(1300,2070,1830,2180),(1800,2080,2330,2185),(2300,2080,2830,2185),(2800,2080,3400,2190)])
strips('Y3',[(1950,1800,2480,1910),(2450,1810,2980,1920),(2900,1820,3400,1930),(2250,1880,2800,2000)])
strips('Y4',[(2750,1880,3400,2000),(2000,1900,2500,2010),(2700,1970,3400,2070)])
