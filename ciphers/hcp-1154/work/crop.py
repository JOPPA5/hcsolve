import sys
from PIL import Image, ImageOps
Image.MAX_IMAGE_PIXELS=None
im=Image.open('hires/cpc_1915-11-29_HU_Mezokovesd_HU_Szomolya_szomolya-07_adr.jpg').convert('RGB')
cr={'h':(90,70,1640,240,2),
'a1':(60,1140,860,1290,3),'a2':(760,1140,1600,1290,3),
'b1':(40,1250,820,1400,3),'b2':(780,1250,1600,1400,3),
'c1':(40,1370,820,1520,3),'c2':(780,1370,1600,1520,3),
'd1':(40,1470,820,1620,3),'d2':(780,1470,1600,1620,3),
'e1':(40,1570,820,1720,3),'e2':(780,1570,1600,1720,3),
'f1':(40,1660,820,1810,3),'f2':(780,1660,1600,1810,3),
'g1':(40,1740,820,1880,3),
'n1':(60,1800,860,2000,2),'n2':(800,1800,1760,2000,2),'n3':(40,1960,860,2190,2),'n4':(800,1960,1760,2190,2),
}
for k,(x0,y0,x1,y1,s) in cr.items():
    c=im.crop((x0,y0,x1,y1)); c=c.resize((c.width*s,c.height*s),Image.LANCZOS); c=ImageOps.autocontrast(c,cutoff=1); c.save(f'crops/{k}.png')
