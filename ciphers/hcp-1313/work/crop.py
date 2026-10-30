import sys
from PIL import Image, ImageOps, ImageFilter
import numpy as np
W='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1313/work/'
im=Image.open(W+'hires/cpc_1912-04-07_HU__HU_Jasz-Arokszalas_jolanka-15_adr.jpg').convert('RGB')
a=np.asarray(im).astype(float)
g=a[:,:,1]; b=a[:,:,2]
# local contrast of green channel
G=Image.fromarray(g.astype('uint8'))
bl=np.asarray(G.filter(ImageFilter.GaussianBlur(45))).astype(float)
d=np.clip((g-bl)*3.2+190,0,255).astype('uint8')
E=Image.fromarray(d)
def crop(name,box,s=2,mode='both'):
    c=E.crop(box); c=c.resize((c.width*s,c.height*s),Image.LANCZOS); c.save(W+'crops/'+name+'.png')
if __name__=='__main__':
    # overview by bands
    n=0
    for y in range(40,2100,340):
        crop(f'o{n:02d}',(60,y,1000,y+400),1); crop(f'p{n:02d}',(900,y,1840,y+400),1); n+=1
