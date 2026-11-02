from PIL import Image, ImageOps, ImageEnhance
import sys
im=Image.open('hires/cpc_1913-12-_HU__HU_Jasz-Arokszalas_jolanka-116_adr.jpg').convert('RGB')
import os; os.makedirs('crops',exist_ok=True)
W=[(50,850),(780,1600)]
y=40;i=0
while y<2150:
    for j,(a,b) in enumerate(W):
        c=im.crop((a,y,b,y+290))
        c=ImageOps.autocontrast(c.convert('L'),cutoff=1)
        c=c.resize((c.width*2,c.height*2),Image.LANCZOS)
        c.save(f'crops/b{i:02d}{"LR"[j]}.png')
    y+=250;i+=1
print(i)
