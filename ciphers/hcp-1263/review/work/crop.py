from PIL import Image
import sys
im=Image.open('../../work/hires/cpc_1913--_HU__HU_Jasz-Arokszalas_jolanka-109_adr.jpg').convert('RGB')
# bands of rows in hires px
bands=[(100,430),(400,680),(650,920),(890,1150),(1130,1400),(1380,1640),(1620,1880),(1860,2110)]
for i,(a,b) in enumerate(bands):
    for j,(l,r) in enumerate([(80,900),(820,1680)]):
        c=im.crop((l,a,r,b)); c=c.resize((c.width*2,c.height*2),Image.LANCZOS); c.save(f'crops/b{i}{"LR"[j]}.png')
c=im.crop((2580,240,3080,780)); c.resize((1500,1620),Image.LANCZOS).save('crops/stamp.png')
