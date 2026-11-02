# violet-ink separation: B-G highlights the copying pencil, suppresses black postmarks and paper
import sys
from PIL import Image, ImageChops, ImageOps
src='work/hires/cpc_1916-06-12_HU_Mezokovesd_HU_Szomolya_szomolya-40_adr.jpg'
im=Image.open(src).convert('RGB')
r,g,b=im.split()
d=ImageChops.subtract(b,g,1,10)   # B-G
d=ImageOps.autocontrast(d,cutoff=(0,0.3))
d=ImageOps.invert(d)
d.save('work/crops/violet_full.png')
y=30;i=0
def crop(n,box,s=2):
    c=d.crop(box);c=c.resize((c.width*s,c.height*s),Image.LANCZOS);c.save('work/crops/%s.png'%n)
for a,b_,n in [(30,640,'a'),(580,1190,'b'),(1130,1720,'c')]:
    y=30;i=0
    while y<2150:
        crop('V%02d%s'%(i,n),(a,y,b_,y+270)); y+=220;i+=1
