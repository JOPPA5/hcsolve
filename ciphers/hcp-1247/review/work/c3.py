from PIL import Image, ImageOps
im=Image.open('../../work/hires/cpc_1913-09-19_HU__HU_Jasz-Arokszalas_jolanka-44_adr.jpg').convert('RGB')
def c(n,box,sc):
    x=im.crop(box); x=ImageOps.autocontrast(x,cutoff=1).resize((int(x.width*sc),int(x.height*sc)),Image.LANCZOS); x.save('c/'+n,quality=92)
c('bb3.jpg',(2840,370,3160,470),5)
c('bb4.jpg',(2840,450,3160,560),5)
c('bb0.jpg',(2800,170,3200,340),4)
c('bb5.jpg',(2840,540,3180,690),4.5)
