from PIL import Image, ImageEnhance
import sys
im=Image.open('../../work/hires/cpc_1913-12-16_HU__HU_Jasz-Arokszalas_jolanka-45_adr.jpg').convert('RGB')
# rows blocks: each crop holds 3-4 rows, left and right half
ys=[80,420,750,1060,1370,1650,1860,2110]
for i in range(7):
    for j,(l,r) in enumerate([(50,620),(560,1130),(1070,1680)]):
        c=im.crop((l,ys[i],r,ys[i+1]+30))
        c=ImageEnhance.Contrast(c).enhance(1.6)
        c=c.resize((c.width*3,c.height*3),Image.LANCZOS)
        c.save(f'crops/r{i}{"ABC"[j]}.png')
c=im.crop((2640,240,3200,720)); c=ImageEnhance.Contrast(c).enhance(1.6); c.resize((c.width*3,c.height*3),Image.LANCZOS).save('crops/stamp.png')
