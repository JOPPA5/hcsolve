from PIL import Image, ImageFilter, ImageOps, ImageChops
im=Image.open('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1282/work/hires/cpc_-04-11_HU__HU_Jasz-Arokszalas_jolanka-94_adr.jpg').convert('RGB')
box=(1440,1830,1590,1960)
c=im.crop(box)
out=Image.new('L',(150*6*3+20,130*6),255)
for i,ch in enumerate(c.split()):
    bl=ch.filter(ImageFilter.GaussianBlur(9))
    d=ImageChops.subtract(bl,ch,offset=128)
    d=ImageOps.autocontrast(d,cutoff=0.5).resize((900,780),Image.LANCZOS)
    out.paste(d,(i*910,0))
out.save('blot_hp.png')
