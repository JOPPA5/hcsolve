import sys
from PIL import Image, ImageEnhance
im=Image.open('hires/cpc_1912--20_HU__HU_Jasz-Arokszalas_jolanka-101_adr.jpg').convert('RGB')
# rows in display coordinates (top,bottom)
n=0
for i,(t,b) in enumerate([(60,240),(230,420),(410,600),(590,780),(770,950),(940,1110),(1090,1190)]):
    c=im.crop((50,int(t*1.72),1700,int(b*1.72)))
    c=ImageEnhance.Contrast(c).enhance(1.5)
    c=c.resize((c.width*11//10*1,c.height*11//10),Image.LANCZOS) if 0 else c.resize((int(c.width*1.2),int(c.height*1.2)),Image.LANCZOS)
    c.save(f'crops/band{i}.png')
c=im.crop((2500,300,3100,850)).resize((1500,1375),Image.LANCZOS); c.save('crops/stamp.png')
