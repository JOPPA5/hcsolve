import sys,glob
from PIL import Image, ImageOps
im=Image.open(glob.glob('hires/*_adr.jpg')[0]).convert('RGB')
r=im.split()[0]
Z={'c1a':(60,30,720,130),'c1b':(600,30,1400,130),
'c2a':(40,2090,800,2210),'c2b':(600,2070,1250,2200),'c2c':(1200,2030,1830,2200),
'l3':(40,250,900,340),'l3b':(800,250,1650,340),'l4':(40,350,900,440),'l4b':(850,350,1650,440),
'l5':(40,440,900,540),'l5b':(850,440,1650,540),'l6':(40,530,900,610),
'd':(480,1440,1800,1560),
'x1':(60,1900,900,2020),'x1b':(850,1880,1750,2010),'x2':(60,1990,900,2090),'x2b':(850,1950,1800,2090),
'adr':(1750,400,3200,950),'adr2':(1750,1000,3300,2150)}
for k,b in Z.items():
    s=3 if k[:3]!='adr' else 1
    c=r.crop(b); c=ImageOps.autocontrast(c,cutoff=0.5).resize((c.width*s,c.height*s),Image.LANCZOS)
    if c.width>2000: c=c.resize((2000,int(c.height*2000/c.width)))
    c.save(f'crops/z_{k}.png')
