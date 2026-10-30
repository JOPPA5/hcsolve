import sys
from PIL import Image, ImageEnhance
im=Image.open('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1293/work/hires/cpc_--_HU__HU_Jasz-Arokszalas_jolanka-76_adr.jpg').convert('RGB')
O='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1293/review/work/crops/'
def c(n,box,s=2.3,rot=0,con=1.8):
    t=im.crop(box)
    if rot: t=t.rotate(rot,expand=True)
    t=t.resize((int(t.width*s),int(t.height*s)),Image.LANCZOS)
    ImageEnhance.Contrast(t).enhance(con).save(O+n+'.png')
c('all',(0,0,3445,2210),0.55)
# rows in strips
y=0
for i,a in enumerate(range(200,2000,300)):
    c('Ls%d'%i,(90,a,950,a+340),2.2); c('Rs%d'%i,(900,a,1760,a+340),2.2)
c('r19a',(90,1720,900,1960),2.3)
c('r19b',(800,1720,1500,1960),2.3)
c('r21a',(90,1900,800,2100),2.6)
c('r21b',(750,1900,1450,2100),2.6)
c('r21c',(1400,1900,2050,2100),2.6)
c('r23a',(90,2030,800,2180),2.6)
c('r23b',(750,2030,1450,2180),2.6)
c('r23c',(1400,2030,2100,2180),2.6)
c('r23d',(2050,2030,2750,2180),2.6)
c('r23e',(2700,2030,3400,2180),2.6)
c('blot',(380,990,1050,1120),2.8)
c('ba',(860,1180,1120,1300),4)
c('r4d',(620,330,960,440),4)
c('box',(1540,60,1900,600),2.4,rot=90)
c('box0',(1450,330,1880,600),4)
c('n23',(680,2040,1150,2180),4)
c('r21e',(1560,1930,2060,2070),3.6)
c('c1',(3120,1960,3400,2170),3)
c('Ea',(3190,1400,3400,2130),2.6,rot=90)
c('Eb',(3190,720,3400,1450),2.6,rot=90)
c('Ec',(3190,40,3400,770),2.6,rot=90)
c('Ta',(2780,50,3400,250),2.9,rot=180)
c('Tb',(2200,50,2840,250),2.9,rot=180)
c('Tc',(1560,50,2260,250),2.9,rot=180)
c('p14',(90,1370,1000,1480),2,con=2)
c('h3',(90,290,420,400),4)
c('d4',(620,330,900,450),4)
c('blob',(860,2060,1000,2170),8,con=2.2)
c('st1',(2780,290,3200,560),3.5,con=2.2)
c('st2',(2780,540,3200,790),3.5,con=2.2)
import numpy as np
a=np.asarray(im).astype(int); f=a[:,:,2]-a[:,:,1]
def cf(n,box,s=3.5):
    x0,y0,x1,y1=box; v=np.clip((f[y0:y1,x0:x1]+45)*255/85,0,255).astype('uint8')
    t=Image.fromarray(255-v); t.resize((int(t.width*s),int(t.height*s)),Image.LANCZOS).save(O+n+'.png')
cf('st3',(2780,430,3200,800))
c('p14',(270,1280,800,1375),3.4,con=2)
c('d10',(450,830,620,950),4,con=2)
