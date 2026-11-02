from PIL import Image
im=Image.open('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1223/work/hires/cpc_1913-01-_HU__HU_Jasz-Arokszalas_jolanka-114_adr.jpg').convert('RGB')
def c(n,b,s=3):
    r=im.crop(b); r=r.resize((r.width*s,r.height*s),Image.BICUBIC); r.save('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1223/work/crops/'+n+'.png')
c('z21word',(2500,1900,3250,2030),2)
c('zr14',(780,1320,1560,1500),2)
c('zr01',(60,50,1000,190),2)
