import sys
from PIL import Image, ImageEnhance
im=Image.open('hires/cpc_1912-07-03_HU__HU_Jasz-Arokszalas_jolanka-28_adr.jpg').convert('RGB')
S=1.72
# bands in displayed y
ys=[(60,175),(165,285),(275,395),(385,505),(495,615),(605,725),(715,835),(825,945),(935,1055),(1045,1225)]
for i,(a,b) in enumerate(ys):
  for j,(l,r) in enumerate([(40,330),(300,600),(570,900)]):
    c=im.crop((int(l*S),int(a*S),int(r*S),int(b*S)))
    c=c.resize((c.width*3,c.height*3),Image.LANCZOS)
    c=ImageEnhance.Contrast(c).enhance(1.4)
    c.save(f'crops/b{i}_{j}.png')
c=im.crop((int(1520*S),int(100*S),int(1800*S),int(420*S))).rotate(180).resize((1440,1650),Image.LANCZOS); c=ImageEnhance.Contrast(c).enhance(1.4); c.save('crops/stamp.png')
c=im.crop((int(1500*S),int(780*S),int(1900*S),int(860*S)));c=c.resize((c.width*3,c.height*3));c.save('crops/addr.png')
c=im.crop((int(600*S),int(1110*S),int(1930*S),int(1230*S)));c=c.resize((c.width*2,c.height*2));c.save('crops/foot.png')
