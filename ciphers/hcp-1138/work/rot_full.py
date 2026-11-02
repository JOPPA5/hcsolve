#!/usr/bin/env python3
"""Upright full-card view of the address side (left 2300 px, full card height and the whole cipher block), plus row-end and row-13 enlargements.
Replaces rot48.png, whose crop box cut off the right ends of rows 9-11."""
import sys
from PIL import Image
import os
D=os.path.dirname(os.path.abspath(__file__))
im=Image.open(D+'/hires/cpc_1916-03-17_HU_Mezokovesd_HU_Szomolya_szomolya-23_adr.jpg').convert('RGB').crop((0,0,2300,2298))
print(im.size)
r=im.rotate(-51,expand=True,fillcolor=(255,255,255),resample=Image.BICUBIC)
print(r.size)
r.save(D+'/crops/full51.png')
s=r.width/1500
def crop(n,box,z):
    c=r.crop(tuple(int(v*s) for v in box)); c=c.resize((int(c.width*z),int(c.height*z)),Image.LANCZOS); c.save(D+'/crops/%s.png'%n); print(n,c.size)
crop('rowends',(1040,580,1400,730),2)
crop('row13',(250,690,560,780),2.5)
crop('row14',(190,730,560,810),2.5)
