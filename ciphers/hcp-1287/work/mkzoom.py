from PIL import Image
im=Image.open('hires/cpc_1912-05-15_HU__HU_Jasz-Arokszalas_jolanka-21_adr.jpg').convert('RGB')
# name: display-coords box
B={'r3end':(780,150,1010,240),'r4dark':(380,205,620,285),'r5end':(780,245,1010,310),'r6':(40,300,300,380),
'r10':(450,540,760,610),'r11a':(50,590,420,670),'r11b':(600,590,960,670),'r12':(640,650,900,710),
'r15end':(600,820,900,890),'r18':(560,1010,950,1075),'r19':(50,1070,300,1130),'r20':(250,1100,520,1170),'r21a':(40,1160,330,1225),'r21b':(620,1110,980,1225)}
for n,b in B.items():
    b=[int(x*1.7225) for x in b]; c=im.crop(b); s=min(4,1800/c.width); c.resize((int(c.width*s),int(c.height*s)),Image.BICUBIC).save(f'crops/z_{n}.png')
