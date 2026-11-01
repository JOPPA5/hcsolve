import sys
from PIL import Image, ImageEnhance
im=Image.open('crops/sheared.png')
k=3445/1500
# n,x0,x1,yc,h
for spec in sys.argv[1:]:
    n,x0,x1,yc,h=spec.split(',');x0,x1,yc,h=map(float,(x0,x1,yc,h))
    r=im.crop((int(x0*k),int((yc-h)*k),int(x1*k),int((yc+h)*k)))
    z=1500/r.width
    r.resize((1500,int(r.height*z)),Image.LANCZOS).save('crops/%s.png'%n)
