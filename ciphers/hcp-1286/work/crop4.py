from PIL import Image, ImageEnhance, ImageFilter
im=Image.open('hires/cpc_1914-01-10_HU__HU_Jasz-Arokszalas_jolanka-47_adr.jpg').convert('RGB')
L=im.convert('L').point(lambda v: 205 if v<105 else min(255,max(0,int((v-110)*255/95))))
L=L.filter(ImageFilter.GaussianBlur(0.8))
def c(name,x0,y0,x1,y1,s=3.3):
    b=tuple(int(v*1.72) for v in (x0,y0,x1,y1))
    r=L.crop(b); r=r.resize((int(r.width*s),int(r.height*s)),Image.BICUBIC); r.save('crops/%s.png'%name)
c('w1',290,160,600,290); c('w2',580,160,890,290)
c('w3',290,280,600,410); c('w4',580,270,890,400)
c('w5',290,400,600,530); c('w6',580,390,890,520)
