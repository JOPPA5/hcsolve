from PIL import Image
W='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1255/work/'
im=Image.open(W+'hires/cpc_1912-03-11_HU__HU_Jasz-Arokszalas_jolanka-08_adr.jpg').convert('RGB')
def c(n,x0,x1,y0,y1,z=3):
    p=im.crop((x0,y0,x1,y1)); p.resize((p.width*z,p.height*z),Image.LANCZOS).save(W+'rows/'+n+'.png')
c('r16a',560,1090,1450,1570); c('r18b',960,1530,1630,1750); c('r19b',960,1530,1720,1830)
c('r20',70,1100,1820,1920,2)
c('r2b',640,1200,160,270); c('r7a',70,620,590,700); c('r7b',860,1530,590,700)
c('stamp',2750,3280,160,720,2); c('top',1550,2800,380,620,1)
