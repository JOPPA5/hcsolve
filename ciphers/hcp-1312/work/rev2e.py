from PIL import Image,ImageOps
im=Image.open('hires/cpc_1912-04-_HU__HU_Jasz-Arokszalas_jolanka-104_adr.jpg').convert('RGB')
def c(n,b,s):
    i=im.crop(b); i=i.resize((int(i.width*s),int(i.height*s)),Image.LANCZOS); i.save('rev2/%s.png'%n)
c('stamp',(2640,220,3250,860),2.2)
c('addr1',(1650,380,2500,720),1.7)
c('addr2',(1750,1180,3200,1420),1)
c('addr3',(1850,1520,3200,1860),1.05)
