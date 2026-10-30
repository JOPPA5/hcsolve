import sys
from PIL import Image, ImageOps, ImageEnhance
im=Image.open('hires/cpc_--_HU__HU_Jasz-Arokszalas_jolanka-76_adr.jpg').convert('RGB')
def c(n,box,s=2.3,rot=0):
    t=im.crop(box)
    if rot: t=t.rotate(rot,expand=True)
    t=t.resize((int(t.width*s),int(t.height*s)),Image.LANCZOS)
    t=ImageEnhance.Contrast(t).enhance(1.6)
    t.save('tiles/%s.png'%n)

for i,a in enumerate(range(240,2000,270)):
    c('L%d'%i,(100,a,920,a+350)); c('R%d'%i,(860,a,1680,a+350))
for i,x in enumerate(range(100,3400,560)):
    c('B%d'%i,(x,1900,x+640,2160),3)
c('T0',(1590,60,2300,240),2.6)
c('T1',(2200,60,2900,240),2.6)
c('T2',(2800,60,3400,240),2.6)
c('V',(1560,180,1820,560),3)
c('stamp',(2750,280,3300,780),2.2)
for i,y in enumerate(range(60,2150,520)):
    c('E%d'%i,(3180,y,3400,y+560),2.2,rot=90)
# right edge, letters upright (card turned clockwise), bottom part first
c('Ea',(3180,1500,3400,2160),2.6,rot=-90)
c('Eb',(3180,900,3400,1560),2.6,rot=-90)
c('Ec',(3180,300,3400,960),2.6,rot=-90)
c('Ed',(3130,40,3400,520),2.6,rot=-90)
c('Ta',(2800,50,3400,250),2.8,rot=180)
c('Tb',(2200,50,2860,250),2.8,rot=180)
c('Tc',(1590,50,2260,250),2.8,rot=180)
c('Sa',(2750,290,3200,800),2.8,rot=180)
c('Sb',(2750,290,3200,800),2.8,rot=90)
c('Sc',(2750,290,3200,800),2.8,rot=-90)
c('Vb',(1570,170,1830,560),3,rot=180)
c('Vc',(1570,170,1830,560),3,rot=90)
c('Vd',(1570,170,1830,560),3,rot=-90)
c('Wc',(1570,60,1900,620),2.9,rot=90)
c('Wn',(1500,380,1880,640),4)
c('z11a',(420,1000,1000,1130),3.2)
c('z11b',(900,1000,1500,1130),3.2)
c('z8',(100,670,700,800),3.2)
c('z8b',(600,690,1250,800),3)
c('z7',(1000,540,1720,690),2.7)
c('z6',(900,500,1720,600),2.3)
c('z18',(100,1590,820,1720),2.7)
c('z23',(860,2000,1500,2160),3)
c('z21',(1300,1920,2000,2070),2.7)
c('corner',(1590,60,1800,260),4,rot=180)
from PIL import ImageOps
g=im.split()[1]
def cg(n,box,s=4,rot=0):
    t=g.crop(box); t=ImageOps.autocontrast(t,cutoff=1)
    t=t.point(lambda v:min(255,max(0,(v-90)*2.2)))
    if rot: t=t.rotate(rot,expand=True)
    t.resize((int(t.width*s),int(t.height*s)),Image.LANCZOS).save('tiles/%s.png'%n)
cg('s1',(2780,290,3200,540),4)
cg('s2',(2780,500,3200,780),4)
c('z23b',(1300,2020,1800,2160),3.6)
c('z23c',(100,2020,800,2160),2.7)
c('z22',(700,1960,1300,2100),3)
import numpy as np
a=np.asarray(im).astype(int)
f=a[:,:,2]-a[:,:,1]
def cf(n,box,s=4):
    x0,y0,x1,y1=box
    v=f[y0:y1,x0:x1]
    v=np.clip((v+45)*255/85,0,255).astype('uint8')
    t=Image.fromarray(255-v).filter(__import__('PIL.ImageFilter',fromlist=['x']).GaussianBlur(1))
    t.resize((int(t.width*s),int(t.height*s)),Image.LANCZOS).save('tiles/%s.png'%n)
cf('p1',(2800,440,3180,640),4.6)
cf('p2',(2800,600,3180,800),4.6)
c('addr',(1750,420,3150,2010),1.3)
