import sys
from PIL import Image, ImageEnhance
im=Image.open('hires/cpc_1914-06-10_HU__HU_Jasz-Arokszalas_jolanka-54_adr.jpg').convert('RGB')
k=3445/1500
W,H=im.size
sl=float(sys.argv[1])
sh=im.transform((W,H),Image.AFFINE,(1,0,0, sl,1,0),Image.BICUBIC)  # src y = dst y + sl*x
sh=ImageEnhance.Contrast(ImageEnhance.Color(sh).enhance(1.8)).enhance(1.25)
sh.save('crops/sheared.png')
sh.crop((int(30*k),int(100*k),int(760*k),int(470*k))).resize((1500,760)).save('crops/sh_top.png')
sh.crop((int(30*k),int(460*k),int(760*k),int(930*k))).resize((1500,966)).save('crops/sh_bot.png')
