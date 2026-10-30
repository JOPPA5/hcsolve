from PIL import Image, ImageOps
im=Image.open('../../work/hires/cpc_--13_HU__HU_Jasz-Arokszalas_jolanka-84_adr.jpg').convert('RGB')
s=1.72
def c(n,x0,y0,x1,y1,z=3,rot=0):
    r=im.crop([int(v*s) for v in (x0,y0,x1,y1)])
    r=r.resize((r.width*z,r.height*z),Image.LANCZOS)
    if rot: r=r.rotate(rot,expand=True)
    ImageOps.autocontrast(r,cutoff=1).save('crops/%s.png'%n)
c('pm_c',830,170,1040,300,4,180)
c('pm_c2',830,120,1160,360,3,180)
c('pmE',1500,400,1660,470,4,0)
c('pmE180',1500,400,1660,470,4,180)
c('pmA',1420,130,1520,270,4,0)
