import sys
from PIL import Image,ImageOps
im=Image.open('work/hires/cpc_1916-06-09_HU_Mezokovesd_HU_Szomolya_szomolya-38_adr.jpg').convert('L')
# darkness profile along candidate stroke, vertical band
for y in range(1320,1480,10):
    row=im.crop((560,y,900,y+10)).resize((68,1))
    print(y,''.join('#' if p<90 else '+' if p<130 else '.' for p in row.getdata()))
