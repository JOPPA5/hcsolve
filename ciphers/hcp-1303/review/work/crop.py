import sys
from PIL import Image, ImageOps
im=Image.open('../../work/hires/cpc_--13_HU__HU_Jasz-Arokszalas_jolanka-84_adr.jpg').convert('RGB')
s=1.72
def c(n,x0,y0,x1,y1,z=2):
    r=im.crop([int(v*s) for v in (x0,y0,x1,y1)])
    r=ImageOps.autocontrast(r.resize((r.width*z,r.height*z),Image.LANCZOS),cutoff=1); r.save('crops/%s.png'%n)
# strips
c('a1',50,40,480,330);c('a2',430,40,920,330)
c('b1',50,300,480,600);c('b2',430,300,920,600)
c('c1',50,580,480,880);c('c2',430,580,920,880)
c('d1',50,860,480,1215);c('d2',430,860,950,1215);c('d3',900,960,1900,1215,1)
c('s',1520,70,1830,380)
