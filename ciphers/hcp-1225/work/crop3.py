from PIL import Image, ImageOps
im=Image.open('hires/cpc_1912-02-29_HU__HU_Jasz-Arokszalas_jolanka-06_adr.jpg').convert('RGB')
def c(n,b,s=3):
    x=im.crop(b); x.resize((x.width*s,x.height*s),Image.LANCZOS).save('crops/'+n+'.png')
c('st1',(2830,110,3200,240),4)
c('st2',(2830,200,3200,320),4)
c('adc',(2660,1270,3400,1420),2)
c('addrend',(3000,1400,3440,1800),2)
c('sz',(1880,330,2120,520),4)
c('sigend',(2500,380,2800,560),4)
