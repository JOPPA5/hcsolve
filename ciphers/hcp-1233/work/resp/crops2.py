from PIL import Image, ImageFilter
import numpy as np
im=Image.open('ciphers/hcp-1233/work/hires/cpc_--_HU__HU_Jasz-Arokszalas_jolanka-67_adr.jpg').convert('RGB')
O='ciphers/hcp-1233/work/resp/'
def mask(c):
    a=np.asarray(c.filter(ImageFilter.GaussianBlur(1))).astype(float)
    m=(a[...,0]+a[...,2])/2-a[...,1]
    m=np.clip((m-m.min())/(np.percentile(m,99.8)-m.min()),0,1)
    return Image.fromarray((255*(1-m)).astype('uint8'))
def crop(n,b,s=3,m=False):
    c=im.crop(b)
    if m:c=mask(c)
    c.resize((c.width*s,c.height*s),Image.LANCZOS).save(O+n)
crop('r13.png',(70,1340,1000,1500),2)
crop('r18t.png',(2300,1850,3100,2000),3)
crop('r18tm.png',(2300,1850,3100,2000),3,True)
crop('z_a.png',(2640,1860,2920,2010),7)
crop('z_am.png',(2640,1860,2920,2010),7,True)
crop('z_b.png',(2860,1850,3130,2000),7)
crop('z_bm.png',(2860,1850,3130,2000),7,True)
crop('z_c.png',(2340,1860,2660,2010),6)
crop('z_cm.png',(2340,1860,2660,2010),6,True)
crop('z_r13.png',(60,1340,500,1480),5)
crop('z_r16.png',(60,1590,500,1730),5)
crop('z_r14.png',(1000,1400,1420,1540),5)
crop('z_d.png',(3050,1850,3300,2000),7)
crop('z_dm.png',(3050,1850,3300,2000),7,True)
