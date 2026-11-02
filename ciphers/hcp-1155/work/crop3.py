import glob
from PIL import Image
im=Image.open(glob.glob('hires/*_adr.jpg')[0]).convert('RGB')
B={'e1':(1540,1975,2100,2095),'e2':(2060,1990,2620,2110),'e3':(2560,1990,3100,2110),'e4':(2900,1990,3440,2110),
'g1':(20,1125,560,1240),'g2':(1000,1120,1640,1240),'g3':(1000,1200,1640,1320),'g4':(20,1400,620,1520),'g5':(500,1400,1120,1520),'g6':(20,1490,560,1600),'g7':(520,1490,1100,1600)}
for k,b in B.items():
    r=im.crop(b); r.resize((r.width*3,r.height*3),Image.LANCZOS).save('crops/'+k+'.png')
