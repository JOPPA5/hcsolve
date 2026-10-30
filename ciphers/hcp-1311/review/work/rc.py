from PIL import Image, ImageEnhance
import sys
im=Image.open('work/hires/cpc_--_HU__HU_Jasz-Arokszalas_jolanka-81_adr.jpg').convert('RGB')
# strips of ~3.5 rows; L, M, R thirds
n=0
y=50
while y<2180:
    for s,(a,b) in zip('LMR',[(70,620),(560,1110),(1050,1600)]):
        c=im.crop((a,y,b,y+290)).resize((1650,870),Image.LANCZOS)
        ImageEnhance.Contrast(c).enhance(1.7).save(f'review/work/crops/r{n:02d}{s}.png')
    y+=250;n+=1
print(n)
