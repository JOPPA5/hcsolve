import sys
from PIL import Image
im=Image.open('../../work/hires/cpc_1913-06-13_HU__HU_Jasz-Arokszalas_jolanka-37_adr.jpg')
S=3445/1024
ys=[38,62,86,105,126,148,170,190]
for i,y in enumerate(ys,1):
    Y=int(y*S)
    for j,(a,b) in enumerate([(80,860),(800,1620)]):
        c=im.crop((a,Y-55,b,Y+55)); c=c.resize((c.width*5//2,c.height*5//2),Image.LANCZOS)
        c.save(f'row{i}{"ab"[j]}.png')
# plain
pl=[(200,232,'p1'),(232,266,'p2'),(266,300,'p3'),(300,335,'p4'),(335,370,'p5'),(370,405,'p6'),(405,440,'p7'),(440,475,'p8'),(475,505,'p9'),(505,535,'p10'),(530,575,'p11'),(565,605,'p12')]
for y0,y1,n in pl:
    c=im.crop((60,int(y0*S)-10,1700,int(y1*S)+10)); c=c.resize((c.width*3//2,c.height*3//2),Image.LANCZOS); c.save(n+'.png')
c=im.crop((1500,1680,3300,2060)); c.save('p_right.png')
c=im.crop((2400,200,3050,700)); c=c.resize((c.width*2,c.height*2)); c.save('stamp.png')
