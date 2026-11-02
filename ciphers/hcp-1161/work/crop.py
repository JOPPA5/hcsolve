import sys
from PIL import Image
p='hires/cpc_1915-12-18_HU_Mezokovesd_HU_Szomolya_szomolya-12_adr.jpg'
im=Image.open(p); 
s=2.0
# rows in hires coords
for i,(y0,y1) in enumerate([(40,330),(300,590),(560,850),(820,1110),(1080,1370),(1340,1630),(1600,1890),(1860,2130)]):
    im.crop((30,y0,1400,y1)).resize((int(1370*s*.9),int((y1-y0)*s*.9)),Image.LANCZOS).save(f'crops/b{i}.png')
