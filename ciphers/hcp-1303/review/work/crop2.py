from PIL import Image, ImageOps
im=Image.open('../../work/hires/cpc_--13_HU__HU_Jasz-Arokszalas_jolanka-84_adr.jpg').convert('RGB')
s=1.72
def c(n,x0,y0,x1,y1,z=3):
    r=im.crop([int(v*s) for v in (x0,y0,x1,y1)])
    r=ImageOps.autocontrast(r.resize((r.width*z,r.height*z),Image.LANCZOS),cutoff=1); r.save('crops/%s.png'%n)
c('r10er',530,690,720,770,6)
c('r12tail',640,830,880,890,5)
c('r14a',880,960,1250,1040,3)
c('r14b',1250,960,1660,1040,3)
c('r15a',860,1040,1250,1120,3)
c('r15b',1200,1040,1660,1120,3)
c('r16a',55,1110,260,1200,5)
c('r16b',640,1090,800,1160,6)
c('p1',1000,1110,1720,1180,2)
c('p2',60,1170,500,1220,3)
c('p3',1200,1150,1720,1215,2)
c('edge',1760,970,1900,1190,3)
c('r13blot',590,910,780,985,5)
