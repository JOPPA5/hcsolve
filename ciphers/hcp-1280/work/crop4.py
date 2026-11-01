from PIL import Image, ImageOps, ImageFilter, ImageChops
im=Image.open('hires/cpc_1912-03-13_HU__HU_Jasz-Arokszalas_jolanka-09_adr.jpg').convert('RGB')
S=3445/1024
x=im.crop((int(838*S),int(85*S),int(965*S),int(165*S)));r,g,b=x.split()
blur=g.filter(ImageFilter.GaussianBlur(18))
hp=ImageChops.subtract(blur,g,scale=0.35,offset=0)
hp=ImageOps.invert(ImageOps.autocontrast(hp))
hp.resize((g.width*4,g.height*4),Image.BICUBIC).save('crops/z_box_hp.png')
