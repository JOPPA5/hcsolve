from PIL import Image
im=Image.open('../../work/hires/cpc_1913-01-_HU__HU_Jasz-Arokszalas_jolanka-114_adr.jpg').convert('RGB')
def c(n,b,s=4):
    r=im.crop(b); r=r.resize((r.width*s,r.height*s),Image.LANCZOS); r.save('crops/'+n+'.png')
c('z21L',(70,1955,420,2110))
c('z19',(600,1760,1000,1880))
c('z20',(620,1830,1120,1960))
c('z22b',(1150,2010,1560,2100))
c('z22a',(420,2010,800,2110))
c('z21g',(2340,1900,2750,2030),3)
c('zsig',(2740,380,3150,520))
