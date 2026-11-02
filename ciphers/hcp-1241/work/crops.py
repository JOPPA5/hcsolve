import sys
from PIL import Image
im=Image.open('hires/cpc_1912-05-12_HU__HU_Jasz-Arokszalas_jolanka-20_adr.jpg')
# rows y in display coords
n=0
for i,(y0,y1) in enumerate([(45,175),(155,285),(265,395),(375,505),(485,615),(595,725),(705,835),(815,945),(925,1055),(1035,1170)]):
  for j,(x0,x1) in enumerate([(50,530),(480,1010)]):
    b=[int(v*1.72) for v in (x0,y0,x1,y1)]
    c=im.crop(b); c=c.resize((c.width*2,c.height*2),Image.LANCZOS); c.save(f'crops/r{i}{"ab"[j]}.png')
b=[int(v*1.72) for v in (1500,110,1800,450)]
c=im.crop(b);c.resize((c.width*2,c.height*2),Image.LANCZOS).save('crops/stamp.png')
b=[int(v*1.72) for v in (840,900,1900,1240)]
c=im.crop(b);c.save('crops/foot.png')
b=[int(v*1.72) for v in (40,1120,560,1250)]
c=im.crop(b);c.resize((c.width*2,c.height*2),Image.LANCZOS).save('crops/bot.png')
