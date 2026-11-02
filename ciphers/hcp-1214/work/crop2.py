from PIL import Image, ImageOps
import glob
im=Image.open(glob.glob('hires/*adr.jpg')[0]).convert('L')
s=3445/1024
c=im.crop((int(15*s),int(15*s),int(520*s),int(610*s)))
c=c.rotate(-3.5,resample=Image.BICUBIC,fillcolor=200,expand=True)
c=ImageOps.autocontrast(c,cutoff=1); c.save('crops/deskew.png'); print(c.size)
W,H=c.size
y=0;i=0
while y<H-50:
    d=c.crop((0,y,W,y+420)); d.save(f'crops/d{i}.png'); i+=1; y+=360
print(i)
