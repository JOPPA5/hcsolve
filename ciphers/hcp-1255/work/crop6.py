from PIL import Image
W='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1255/work/'
im=Image.open(W+'hires/cpc_1912-03-11_HU__HU_Jasz-Arokszalas_jolanka-08_adr.jpg').convert('RGB')
def c(n,x0,x1,y0,y1,z=3):
    p=im.crop((x0,y0,x1,y1)); p.resize((p.width*z,p.height*z),Image.LANCZOS).save(W+'rows/'+n+'.png')
c('r18e',960,1540,1590,1705); c('r16m',500,1040,1405,1525); c('r17e',760,1530,1500,1610,2); c('r15a',70,760,1310,1420,2)
