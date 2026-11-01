from PIL import Image
im=Image.open('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1263/work/hires/cpc_1913--_HU__HU_Jasz-Arokszalas_jolanka-109_adr.jpg')
c=im.crop((480,1540,1320,1660)); c=c.resize((c.width*5//2*1,c.height*5//2),Image.LANCZOS); c.save('crops/r17.png')
c=im.crop((780,1540,1120,1660)); c.resize((c.width*5,c.height*5),Image.LANCZOS).save('crops/r17z.png')
