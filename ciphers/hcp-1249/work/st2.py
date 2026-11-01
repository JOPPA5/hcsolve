from PIL import Image, ImageOps
d='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1249/work/'
im=Image.open(d+'hires/cpc_1914-03-25_HU__HU_Jasz-Arokszalas_jolanka-51_adr.jpg').convert('RGB')
for n,b in (('s1',(2640,190,3060,300)),('s3',(2640,300,3060,400)),('s5',(2640,400,3060,560))):
    c=im.crop(b); bl=c.split()[2]; g=c.split()[1]
    o=Image.new('L',(c.width*4,c.height*8+10),255)
    o.paste(ImageOps.autocontrast(bl,cutoff=1).resize((c.width*4,c.height*4),Image.BICUBIC),(0,0))
    o.paste(ImageOps.autocontrast(g,cutoff=1).resize((c.width*4,c.height*4),Image.BICUBIC),(0,c.height*4+10))
    o.save(d+'crops/'+n+'.png')
