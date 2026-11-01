from PIL import Image, ImageOps
im=Image.open('hires/cpc_1912-03-13_HU__HU_Jasz-Arokszalas_jolanka-09_adr.jpg').convert('RGB')
S=3445/1024
box=(int(835*S),int(55*S),int(965*S),int(150*S))
x=im.crop(box);r,g,b=x.split()
g2=g.point(lambda v:0 if v<120 else min(255,int((v-120)*3)))
g2.resize((g.width*4,g.height*4),Image.BICUBIC).save('crops/z_box_hi.png')
ImageOps.autocontrast(b).resize((g.width*4,g.height*4),Image.BICUBIC).save('crops/z_box_b.png')
