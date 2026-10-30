from PIL import Image, ImageDraw, ImageEnhance
import numpy as np
src='ciphers/hcp-1295/work/hires/cpc_1912-06-06_HU__HU_Jasz-Arokszalas_jolanka-24_adr.jpg'
im=Image.open(src).convert('RGB').crop((80,40,1680,2140))
def prof(a):
    r=im.rotate(a,resample=Image.BILINEAR,fillcolor=(230,200,160))
    x=np.asarray(r).astype(int); m=((x[...,0]-x[...,1])>70)
    return m.sum(1)
best=max([(np.var(prof(a)),a) for a in np.arange(-6,0.01,.25)])
print(best); a=best[1]
p=prof(a).astype(float); k=np.ones(9)/9; s=np.convolve(p,k,'same')
pk=[i for i in range(20,len(s)-20) if s[i]==s[i-20:i+21].max() and s[i]>0.3*s.max()]
print(pk,len(pk))
r=im.rotate(a,resample=Image.BICUBIC,fillcolor=(230,200,160))
r.save('ciphers/hcp-1295/work/crops/desk.png')
from PIL import ImageFont
d=r.copy()
def strip(name,y0,y1,x0,x1):
    c=d.crop((x0,y0,x1,y1)); c=c.resize((c.width*2,c.height*2),Image.LANCZOS)
    ImageEnhance.Contrast(c).enhance(1.3).save('ciphers/hcp-1295/work/crops/'+name+'.png')
ys=list(range(0,2100,250))
for i,y in enumerate(ys):
    strip(f'D{i}a',y,y+300,0,830); strip(f'D{i}b',y,y+300,760,1600)
