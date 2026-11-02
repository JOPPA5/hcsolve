import sys,os; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from crops import *
from PIL import Image
def strips(name,boxes,w=1420):
    ims=[]
    for b in boxes:
        s=w/(b[2]-b[0]); c=im.crop(b).resize((w,int((b[3]-b[1])*s)),Image.LANCZOS)
        ims.append(ImageEnhance.Contrast(c).enhance(1.6))
    H=sum(i.height+8 for i in ims); o=Image.new('RGB',(w,H),'white'); y=0
    for i in ims: o.paste(i,(0,y)); y+=i.height+8
    o.save(D+'/crops/'+name+'.png')
# r25 tail, y approx 1960->2030
strips('P1',[(1320,1960,1860,2080),(1800,1985,2340,2095),(2280,2000,2820,2100),(2760,2000,3400,2110)])
# r26 
strips('P2',[(150,2010,690,2130),(650,2030,1190,2130),(1150,2030,1690,2140),(1650,2040,2190,2140)])
strips('P3',[(2150,2050,2690,2150),(2650,2050,3190,2160),(2900,2040,3420,2160)])
# r27
strips('P4',[(150,2090,690,2190),(650,2090,1190,2190),(1150,2090,1690,2190),(1650,2090,2190,2190)])
strips('P5',[(2150,2090,2690,2190),(2650,2090,3190,2190),(2900,2090,3420,2190)])
strips('P6',[(1400,1300,1950,1400),(1850,1320,2300,1420),(1320,1250,1850,1350),(150,1350,700,1450)])
