import sys
from PIL import Image, ImageOps
im=Image.open('hires/cpc_--_HU__HU_Jasz-Arokszalas_jolanka-68_adr.jpg').convert('RGB')
# tiles: rows bands
H=[(50,330),(290,570),(530,810),(770,1050),(1010,1290),(1250,1530),(1490,1770),(1730,2090)]
for i,(a,b) in enumerate(H):
    for j,(l,r) in enumerate([(50,900),(800,1650)]):
        c=im.crop((l,a,r,b)); c=c.resize((c.width*2,c.height*2),Image.LANCZOS); c=ImageOps.autocontrast(c,cutoff=1)
        c.save(f'crops/t{i}{"LR"[j]}.png')
# bottom right
for j,(l,r) in enumerate([(1600,2450),(2350,3250)]):
    c=im.crop((l,1650,r,2090)); c=c.resize((c.width*2,c.height*2),Image.LANCZOS); c.save(f'crops/b{j}.png')
c=im.crop((2500,120,3100,720)); c=c.resize((1800,1800),Image.LANCZOS); c.save('crops/stamp.png')
