from PIL import Image
im=Image.open('hires/cpc_1913-01-_HU__HU_Jasz-Arokszalas_jolanka-114_adr.jpg').convert('RGB')
def c(n,b,s=4):
    r=im.crop(b); r=r.resize((r.width*s,r.height*s),Image.BICUBIC); r.save('crops/'+n+'.png')
c('z1',(90,1960,560,2090))
c('z2',(90,1900,450,2040))
c('z3',(90,250,800,370),3)
c('z4',(800,250,1560,370),3)
c('z5',(2660,120,3020,300),5)
c('z6',(2300,60,2800,620),3)
