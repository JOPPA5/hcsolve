import sys
from PIL import Image
im=Image.open('../../work/hires/cpc_--09_HU__HU_Jasz-Arokszalas_jolanka-83_adr.jpg').convert('RGB')
# overlapping strips of left block, left half/right half
H=[(i,90+i*190) for i in range(11)]
for i,y in H:
    for j,(a,b) in enumerate([(90,830),(760,1500)]):
        im.crop((a,y,b,y+250)).resize((1480,500),Image.LANCZOS).save(f'crops/s{i:02d}{"LR"[j]}.png')
im.crop((1640,2180-2180+1900,2900,2110)).resize((1890,315*1),Image.LANCZOS).save('crops/foot.png')
im.crop((2640,220,3120,780)).resize((1440,1680),Image.LANCZOS).save('crops/stamp.png')
