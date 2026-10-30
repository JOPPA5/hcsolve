from PIL import Image
im=Image.open('hires/cpc_1912-05-15_HU__HU_Jasz-Arokszalas_jolanka-21_adr.jpg').convert('RGB')
B={'r10end':(760,540,960,610),'r18b':(40,1010,560,1080),'r13':(40,700,300,770)}
for n,b in B.items():
    b=[int(x*1.7225) for x in b]; c=im.crop(b); s=min(4,1800/c.width); c.resize((int(c.width*s),int(c.height*s)),Image.BICUBIC).save(f'crops/z_{n}.png')
