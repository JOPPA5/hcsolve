from PIL import Image, ImageOps
im=Image.open('hires/cpc_1912-04-30_HU__HU_Jasz-Arokszalas_jolanka-17_adr.jpg').convert('RGB')
S=1.7225
g=im.split()[1]
def c(n,x0,y0,x1,y1,z=5):
    b=[int(v*S) for v in (x0,y0,x1,y1)]
    r=g.crop(b); r=ImageOps.autocontrast(r,cutoff=2).resize(((b[2]-b[0])*z,(b[3]-b[1])*z),Image.BICUBIC); r.save('crops/%s.png'%n)
c('s6',1515,345,1800,395)
c('s7',1515,380,1800,425)
c('s8',1515,405,1800,450)
