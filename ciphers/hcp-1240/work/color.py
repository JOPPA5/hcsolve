from PIL import Image, ImageOps
import numpy as np
im=Image.open('hires/cpc_1913-12-_HU__HU_Jasz-Arokszalas_jolanka-117_adr.jpg').convert('RGB')
A=np.asarray(im).astype(float)
print(A[1900:1905,2300:2303], A[120,300:303])
R,G,B=A[...,0],A[...,1],A[...,2]
# pencil index: blue relative to red
P=(B-R)
P=P-np.median(P)
P=np.clip(P,-5,70)
out=255-(P+5)/75*255
Image.fromarray(out.astype('uint8')).save('crops/pencil.png')
o=Image.open('crops/pencil.png')
def t(n,b,s=2.5):
    r=o.crop(b); r.resize((int(r.width*s),int(r.height*s)),Image.LANCZOS).save('crops/'+n+'.png')
    g=im.crop(b).convert('L'); ImageOps.autocontrast(g.resize((int(g.width*s),int(g.height*s)),Image.LANCZOS),cutoff=1).save('crops/g'+n+'.png')
t('b1',(1500,1820,2280,2075));t('b2',(2240,1820,3020,2075));t('b3',(2800,1800,3340,2075),3)
t('st',(2640,220,3170,780),3.4)
