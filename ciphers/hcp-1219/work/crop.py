import sys
from PIL import Image
im=Image.open('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1219/work/hires/cpc_--_HU__HU_Jasz-Arokszalas_jolanka-65_adr.jpg').convert('RGB')
S=1.7225
def c(n,x0,y0,x1,y1,z=2):
    b=[int(v*S) for v in (x0,y0,x1,y1)]
    r=im.crop(b); r=r.resize((r.width*z,r.height*z),Image.LANCZOS); r.save(f'crops/{n}.png')
bands=[(50,110),(105,165),(150,215),(205,265),(255,315),(295,360),(350,395+15),(395,450),(440,505),(500,565),(555,605),(600,650),(640,695),(690,730),(725,780),(770,820),(810,860),(850,905),(895,950),(945,995),(1000,1045)]
for i,(a,b) in enumerate(bands,1):
    c(f'r{i:02d}a',40,a,420,b); c(f'r{i:02d}b',400,a,800,b+ (10 if i in(7,8) else 0))
c('b1a',40,1040,700,1125);c('b1b',680,1040,1300,1125);c('b1c',1280,1040,1900,1125)
c('b2a',40,1100,700,1190);c('b2b',680,1100,1300,1190);c('b2c',1280,1100,1900,1190)
c('stamp',1530,110,1800,410,3)
cs=[85,130,190,240,283,325,382,428,490,540,593,650,700,750,805,850,885,925,972,1020]
for i,y in enumerate(cs,1):
    c(f'r{i:02d}a',40,y-38,430,y+38); c(f'r{i:02d}b',410,y-38,800,y+38)
for nm,y0,y1 in (('A',1048,1102),('C',1098,1148),('D',1132,1188)):
    for k in range(6):
        x=40+k*315
        c(f'{nm}{k}',x,y0,x+340,y1,3)
