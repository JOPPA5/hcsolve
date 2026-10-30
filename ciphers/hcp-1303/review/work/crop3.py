from PIL import Image, ImageOps
im=Image.open('../../work/hires/cpc_--13_HU__HU_Jasz-Arokszalas_jolanka-84_adr.jpg').convert('RGB')
s=1.72
def c(n,x0,y0,x1,y1,z=3,rot=0):
    r=im.crop([int(v*s) for v in (x0,y0,x1,y1)])
    r=r.resize((r.width*z,r.height*z),Image.LANCZOS)
    if rot: r=r.rotate(rot,expand=True)
    ImageOps.autocontrast(r,cutoff=1).save('crops/%s.png'%n)
c('r15end',1600,1035,1860,1115,4)
c('r16mid',230,1110,430,1170,4)
c('j',760,1100,860,1170,6)
c('addrJ',960,480,1340,620,2)
c('addrJasz',1040,800,1460,930,2)
c('pm1',800,110,1200,440,2)
c('pm1rot',800,110,1200,440,2,180)
c('pm2',1460,330,1760,480,3)
