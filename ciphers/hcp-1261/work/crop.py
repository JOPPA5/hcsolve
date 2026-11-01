import sys
from PIL import Image
im=Image.open('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1261/work/hires/cpc_1912-03-07_HU__HU_Jasz-Arokszalas_jolanka-07_adr.jpg').convert('RGB')
print(im.size)
# bands in hires px
S=3445/1024
bands=[(15,130),(120,230),(220,350)]
y=20
n=0
for y0 in range(10,640,105):
    for x0,x1 in ((10,260),(240,510)):
        c=im.crop((int(x0*S),int(y0*S),int(x1*S),int((y0+125)*S)))
        c=c.resize((c.width*2//1,c.height*2//1),Image.LANCZOS) if False else c
        c.save(f'crops/b{y0:03d}_{x0:03d}.png')
c=im.crop((int(815*S),int(25*S),int(950*S),int(190*S))); c=c.resize((c.width*2,c.height*2),Image.LANCZOS); c.save('crops/stamp.png')
c=im.crop((int(10*S),int(490*S),int(60*S),int(625*S))).rotate(-90,expand=True); c=c.resize((c.width*2,c.height*2),Image.LANCZOS); c.save('crops/leftedge.png')
c=im.crop((int(10*S),int(590*S),int(860*S),int(630*S)));c.save('crops/bottom.png')
