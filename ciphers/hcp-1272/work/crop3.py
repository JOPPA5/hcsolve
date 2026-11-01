from PIL import Image, ImageOps
im=Image.open('hires/cpc_1912-04-30_HU__HU_Jasz-Arokszalas_jolanka-17_adr.jpg').convert('RGB')
S=1.7225
def c(n,x0,y0,x1,y1,z=4):
    b=[int(v*S) for v in (x0,y0,x1,y1)]
    r=im.crop(b); r=r.resize((r.width*z,r.height*z),Image.LANCZOS); r.save('crops/%s.png'%n)
c('q17',250,1135,480,1185,5)
c('q5',45,365,260,445,4)
c('qw',130,1035,260,1090,5)
# stamp, green channel autocontrast
b=[int(v*S) for v in (1520,270,1810,460)]
r=im.crop(b).split()[1]
r=ImageOps.autocontrast(r,cutoff=1).resize(((b[2]-b[0])*3,(b[3]-b[1])*3),Image.LANCZOS); r.save('crops/stampG.png')
r=im.crop(b).split()[2]
r=ImageOps.autocontrast(r,cutoff=1).resize(((b[2]-b[0])*3,(b[3]-b[1])*3),Image.LANCZOS); r.save('crops/stampB.png')
