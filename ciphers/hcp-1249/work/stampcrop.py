from PIL import Image, ImageOps
d='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1249/work/'
im=Image.open(d+'hires/cpc_1914-03-25_HU__HU_Jasz-Arokszalas_jolanka-51_adr.jpg').convert('RGB')
b=(2620,190,3080,720)
c=im.crop(b)
r,g,bl=c.split()
for n,ch in (('r',r),('b',bl)):
    o=ImageOps.autocontrast(ch,cutoff=1).resize((c.width*3,c.height*3),Image.LANCZOS)
    o.crop((0,0,c.width*3,c.height*3//2)).save(d+f'crops/st_{n}_top.png')
    o.crop((0,c.height*3//2,c.width*3,c.height*3)).save(d+f'crops/st_{n}_bot.png')
