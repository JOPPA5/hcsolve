import sys
from PIL import Image, ImageOps
im=Image.open('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1279/work/hires/cpc_1914-04-12_HU__HU_Jasz-Arokszalas_jolanka-53_adr.jpg').convert('RGB')
out='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1279/work/crops/'
def c(n,x0,y0,x1,y1,s=3):
    r=im.crop((x0,y0,x1,y1)); r=r.resize((r.width*s,r.height*s),Image.LANCZOS); r=ImageOps.autocontrast(r,cutoff=1); r.save(out+n+'.png')
if len(sys.argv)>1:
    a=sys.argv; c(a[1],*map(int,a[2:7]))
else:
    y=50;i=0
    while y<1830:
        c(f'L{i:02d}',60,y,800,y+300); c(f'R{i:02d}',760,y,1500,y+300); y+=270;i+=1
    c('B0',60,1880,1100,2120,2);c('B1',1050,1880,2200,2120,2);c('B2',2150,1880,3300,2120,2);c('S',2650,130,3200,480,3)
