import sys
from PIL import Image
im=Image.open('hires/cpc_1916-02-15_HU_Mezokovesd_HU_Szomolya_szomolya-18_adr.jpg').convert('RGB')
crops={'top':(100,30,1700,330),'a':(30,130,1600,560),'b':(30,520,1600,1060),'c':(30,1040,1600,1530),'d':(30,1500,1600,2150),
'date':(1400,20,2700,170)}
for k,b in crops.items():
    c=im.crop(b); c=c.resize((c.width*1,c.height*1)); c.save('crops/%s.png'%k)
