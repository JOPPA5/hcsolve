from PIL import Image
im=Image.open('../../work/hires/cpc_1913-01-_HU__HU_Jasz-Arokszalas_jolanka-114_adr.jpg').convert('RGB')
def c(n,b,s=2):
    r=im.crop(b); r=r.resize((r.width*s,r.height*s),Image.LANCZOS); r.save('crops/'+n+'.png')
c('row19',(80,1775,1100,1880),3 if False else 2)
c('row19b',(1000,1760,1560,1880),2)
c('z21d',(2700,1910,3050,2020),4)
c('z21d2',(2880,1900,3250,2020),4)
c('row22a',(780,2005,1560,2100),2)
