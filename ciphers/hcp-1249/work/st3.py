from PIL import Image, ImageOps
d='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1249/work/'
im=Image.open(d+'hires/cpc_1914-03-25_HU__HU_Jasz-Arokszalas_jolanka-51_adr.jpg').convert('RGB')
for n,b,z in (('s6',(2640,440,3080,530),4),('s7',(2640,520,3080,620),4),('s8',(2640,580,3080,700),4)):
    c=im.crop(b); bl=c.split()[2]
    ImageOps.autocontrast(bl,cutoff=1).resize((c.width*z,c.height*z),Image.BICUBIC).save(d+'crops/'+n+'.png')
c=im.crop(b:=(2640,190,3080,700)).resize((1320,1530),Image.LANCZOS); c.save(d+'crops/st_color.png')
