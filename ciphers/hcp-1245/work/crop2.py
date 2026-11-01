import sys
from PIL import Image, ImageEnhance
im=Image.open('hires/cpc_1912-03-20_HU__HU_Jasz-Arokszalas_jolanka-11_adr.jpg')
f=1.72
for name,x0,y0,x1,y1,s in [('z1',75,1090,430,1200,4),('z2',400,1090,780,1200,4),('z3',530,1140,800,1205,5),('z4',90,1020,450,1110,4),('z5',60,490,330,570,5),('z6',550,425,930,500,4),('z7',500,490,920,560,4),('z8',640,560,930,650,4),('z9',110,770,500,840,4)]:
    c=im.crop((int(x0*f),int(y0*f),int(x1*f),int(y1*f)))
    c=c.resize((c.width*s//2,c.height*s//2),Image.LANCZOS)
    ImageEnhance.Contrast(c).enhance(1.4).save(f'crops/{name}.png')
