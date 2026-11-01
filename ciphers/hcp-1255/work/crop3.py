from PIL import Image
W='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1255/work/'
im=Image.open(W+'hires/cpc_1912-03-11_HU__HU_Jasz-Arokszalas_jolanka-08_adr.jpg').convert('RGB')
def c(n,x0,x1,y0,y1,z=3):
    p=im.crop((x0,y0,x1,y1)); p.resize((p.width*z,p.height*z),Image.LANCZOS).save(W+'rows/'+n+'.png')
c('r10b',1000,1530,900,1010)
c('r11a',70,600,985,1100); c('r11b',560,1100,985,1100)
c('r12a',70,600,1075,1200); c('r12b',560,1100,1075,1200); c('r12c',1000,1530,1075,1200)
c('r5a',70,600,440,560); c('r8b',960,1530,700,810); c('r9a',70,600,780,900)
