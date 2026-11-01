import numpy as np, sys
from PIL import Image
im=Image.open('crops/sheared.png')
k=3445/1500
a=np.asarray(im).astype(float)
R,G,B=a[...,0],a[...,1],a[...,2]
# inkness: how much greener/yellower-dark vs. paper, suppress grey stamp
sat=(a.max(2)-a.min(2))/(a.max(2)+1)
V=a.max(2)/255
gmr=G-R
v=np.clip((gmr+25)/45,0,1)*np.clip((sat-.25)/.3,0,1)
for spec in sys.argv[1:]:
    n,x0,x1,yc,h=spec.split(',');x0,x1,yc,h=map(float,(x0,x1,yc,h))
    s=(int((yc-h)*k),int((yc+h)*k),int(x0*k),int(x1*k))
    d=v[s[0]:s[1],s[2]:s[3]]
    o=Image.fromarray((255*(1-d)).astype('uint8')).convert('L')
    z=1500/o.width
    o.resize((1500,int(o.height*z)),Image.LANCZOS).save('crops/%s.png'%n)
