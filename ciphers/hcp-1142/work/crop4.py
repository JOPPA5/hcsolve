from PIL import Image
im=Image.open('hires/cpc_1906--_HU_Mezokovesd_HU_Szomolya_szomolya-41_adr.jpg').convert('RGB')
f=1.73
c=im.crop(tuple(int(v*f) for v in (400,695,590,770))); c=c.resize((c.width*4,c.height*4),Image.LANCZOS); c.save('crops/picin.png')
