from PIL import Image, ImageOps
import numpy as np
im=Image.open('hires/cpc_1912-02-29_HU__HU_Jasz-Arokszalas_jolanka-06_adr.jpg').convert('RGB')
b=(2840,120,3210,340)
x=np.asarray(im.crop(b)).astype(float)
g=x[...,1]; r=x[...,0]; bl=x[...,2]
rows=[]
for lo,hi in [(40,200),(60,120),(50,100)]:
    a=np.clip((g-lo)/(hi-lo),0,1)*255
    rows.append(Image.fromarray(a.astype('uint8')).resize(((b[2]-b[0])*3,(b[3]-b[1])*3),Image.LANCZOS))
W=rows[0].width;H=rows[0].height
o=Image.new('L',(W,H*2+10),255)
o.paste(rows[0],(0,0));o.paste(rows[1],(0,H+10));o.save('crops/st_enh.png')
print(np.percentile(g,[1,5,25,50]))
