from PIL import Image, ImageEnhance
im=Image.open('hires/cpc_1914-01-10_HU__HU_Jasz-Arokszalas_jolanka-47_adr.jpg').convert('RGB')
def c(name,x0,y0,x1,y1,s=3.3):
    b=tuple(int(v*1.72) for v in (x0,y0,x1,y1))
    r=im.crop(b); r=r.resize((int(r.width*s),int(r.height*s)),Image.BICUBIC)
    ImageEnhance.Contrast(r).enhance(1.7).save('crops/%s.png'%name)
c('b1',440,1105,800,1205); c('b2',780,1090,1140,1195)
c('b3',1120,1080,1480,1190); c('b4',1460,1060,1720,1190)
c('t1',1620,120,1830,290,3.4); c('t2',1600,280,1830,450,3.4)
c('k1',620,650,830,720,4.5)  # kulvesben end
c('k2',380,670,640,720,4.5)
c('j1',640,920,960,1050,3.3)
c('j2',640,1040,960,1090,3.3)
