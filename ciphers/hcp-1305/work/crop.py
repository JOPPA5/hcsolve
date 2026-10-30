import sys
from PIL import Image
im=Image.open('hires/cpc_1912--_HU__HU_Jasz-Arokszalas_jolanka-98_adr.jpg')
f=1.72
# display coords: name,x0,y0,x1,y1,scale
C=[('r01-04',60,50,1000,300,1.15),('r05-08',50,290,920,510,1.25),('r09-12',50,510,920,770,1.25),('r13-16',50,760,920,1010,1.25),
('r17a',50,1010,520,1140,2.2),('r17b',480,1010,920,1140,2.2),('r18a',50,1090,640,1230,1.9),('r18b',620,1090,1250,1230,1.9),('r18c',1200,1060,1880,1230,1.7),
('stamp',1590,110,1880,420,3),('edge',1780,880,1890,1230,3),('addr',960,220,1520,320,2)]
for n,a,b,c,d,s in C:
    r=im.crop((int(a*f),int(b*f),int(c*f),int(d*f)))
    r=r.resize((int(r.width*s),int(r.height*s)),Image.LANCZOS); r.save(f'crops/{n}.png')
