import sys
from PIL import Image
im=Image.open('hires/cpc_1912-05-15_HU__HU_Jasz-Arokszalas_jolanka-21_adr.jpg').convert('RGB')
bands=[(40,270),(230,450),(410,640),(600,830),(790,1010),(970,1200),(1160,1380),(1340,1560),(1520,1740),(1700,1920),(1860,2110)]
for i,(a,b) in enumerate(bands):
    for j,(l,r) in enumerate([(60,960),(860,1760)]):
        c=im.crop((l,a,r,b)); c=c.resize((c.width*2,c.height*2),Image.LANCZOS); c.save(f'crops/b{i:02d}{"LR"[j]}.png')
c=im.crop((2650,270,3180,720));c.resize((c.width*3,c.height*3),Image.LANCZOS).save('crops/stamp.png')
c=im.crop((1680,480,2750,720));c.resize((c.width*2,c.height*2),Image.LANCZOS).save('crops/szep.png')
c=im.crop((1650,820,3250,1800));c.save('crops/addr.png')
