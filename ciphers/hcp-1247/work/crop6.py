from PIL import Image, ImageOps
im=Image.open('hires/cpc_1913-09-19_HU__HU_Jasz-Arokszalas_jolanka-44_adr.jpg').convert('RGB')
def c(n,box,sc=5,rot=0):
    x=im.crop(box)
    if rot: x=x.rotate(rot,expand=False,resample=Image.BICUBIC)
    x=x.resize((int(x.width*sc),int(x.height*sc)),Image.LANCZOS); ImageOps.autocontrast(x,cutoff=0.5).save('crops/'+n)
c('b4.png',(2800,450,3200,620),4.5,10)
c('b5.png',(2780,540,3220,720),4.5,10)
c('r19s.png',(90,1500,560,1640),4)
c('r2z.png',(480,130,760,240),5)
c('sttop.png',(2650,180,3000,520),3)
