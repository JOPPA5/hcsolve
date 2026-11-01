from PIL import Image,ImageOps
im=Image.open('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1253/work/hires/cpc_1913-02-22_HU__HU_Jasz-Arokszalas_jolanka-33_adr.jpg').convert('L')
print(im.size)
f=im.width/1024
c=ImageOps.autocontrast(im.crop((int(130*f),int(322*f),int(290*f),int(378*f))),cutoff=1)
c=c.resize((c.width*4,c.height*4),Image.LANCZOS); c.save('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1253/work/crops/r11tick.png')
