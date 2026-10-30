from PIL import Image
import os
d=os.path.dirname(os.path.abspath(__file__))
im=Image.open(d+'/hires/cpc_--_HU__HU_Jasz-Arokszalas_jolanka-78_adr.jpg').convert('RGB')
# left half / right half per band
bands=[(60,215),(190,345),(300,455),(410,570),(520,680),(620,780),(720,890),(830,1000),(950,1100),(1050,1200),(1160,1310),(1270,1420),(1370,1530),(1480,1640),(1590,1740),(1660,1800),(1780,1920),(1860,2010),(1920,2100)]
for i,(a,b) in enumerate(bands):
    for j,(x0,x1) in enumerate([(70,620),(560,1100),(1050,1650)]):
        c=im.crop((x0,a,x1,b)); c=c.resize((c.width*3,c.height*3),Image.LANCZOS)
        c.save(f'{d}/crops/b{i:02d}_{j}.png')
c=im.crop((2640,190,3130,770)).rotate(0)
c=c.resize((c.width*3,c.height*3),Image.LANCZOS); c.save(d+'/crops/stamp.png')
c.rotate(-90,expand=True).save(d+'/crops/stamp_r.png'); c.rotate(90,expand=True).save(d+'/crops/stamp_l.png')
c=im.crop((1000,1880,3300,2120)); c.resize((c.width*2,c.height*2)).save(d+'/crops/bottom_right.png')
