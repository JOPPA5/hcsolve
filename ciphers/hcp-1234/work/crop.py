import sys
from PIL import Image
im=Image.open('hires/cpc_1913-12-16_HU__HU_Jasz-Arokszalas_jolanka-45_adr.jpg').convert('RGB')
bands=[(100,430),(420,750),(740,1070),(1060,1390),(1380,1710),(1660,2120)]
for i,(a,b) in enumerate(bands):
    for j,(l,r) in enumerate([(60,900),(860,1740)]):
        c=im.crop((l,a,r,b)); c=c.resize((c.width*2,c.height*2),Image.LANCZOS); c.save(f'crops/b{i}{"LR"[j]}.png')
c=im.crop((2650,250,3200,720)); c.resize((c.width*3,c.height*3),Image.LANCZOS).save('crops/stamp.png')
c=im.crop((1700,1880,3100,2120)); c.resize((c.width*2-400,(c.height*2-400*c.height//c.width)),Image.LANCZOS).save('crops/bottomR.png')
