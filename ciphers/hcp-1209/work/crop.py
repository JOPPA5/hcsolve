import sys
from PIL import Image,ImageOps
im=Image.open('hires/cpc_1914-11-23_HU__HU_Budapest_jolanka-56_adr.jpg').convert('RGB')
print(im.size)
# text column rows y 40..2110 x 60..1650
n=0
for y in range(40,2100,400):
    c=im.crop((60,y,1680,y+460)); c=ImageOps.autocontrast(c.convert('L'),cutoff=1)
    c=c.resize((c.width*5//4,c.height*5//4)); c.save(f'crops/t{n}.png'); n+=1
c=im.crop((2650,120,3300,760)).resize((1300,1280));c.save('crops/stamp.png')
c=im.crop((1650,150,2350,320)).resize((1400,340));c.save('crops/top.png')
c=im.crop((1700,800,3400,2100));c.save('crops/addr.png')
