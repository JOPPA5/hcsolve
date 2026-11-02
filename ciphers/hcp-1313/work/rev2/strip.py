import sys
from PIL import Image, ImageOps, ImageFilter
import numpy as np
W='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1313/work/'
im=Image.open(W+'hires/cpc_1912-04-07_HU__HU_Jasz-Arokszalas_jolanka-15_adr.jpg').convert('RGB')
enh=Image.open(W+'crops/enh_full.png')
a=np.asarray(im).astype(float)
# wash-neutral: green minus part of blue? pink wash absorbs green; ink absorbs all. use R (wash nearly transparent in red)
r=Image.fromarray(a[...,0].astype('uint8'))
def crop(name,x0,y0,x1,y1,s=3):
    out=[]
    for src in (enh,r):
        c=src.crop((x0,y0,x1,y1))
        if src is r: c=ImageOps.autocontrast(c,cutoff=1)
        out.append(c.resize(((x1-x0)*s,(y1-y0)*s),Image.BICUBIC))
    h=out[0].height
    o=Image.new('L',(out[0].width,2*h+6),255)
    o.paste(out[0],(0,0));o.paste(out[1],(0,h+6))
    o.save(W+'rev2/'+name+'.png')
rows={6:790,7:895,8:1023,9:1143,10:1264,11:1393,12:1522}
for n,y in rows.items():
    crop(f'r{n}a',50,y-110,850,y+110,2)
    crop(f'r{n}b',800,y-110,1650,y+110,2)
