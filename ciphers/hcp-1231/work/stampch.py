import glob
from PIL import Image,ImageOps,ImageChops
f=glob.glob('hires/*adr.jpg')[0]
im=Image.open(f).convert('RGB').crop((2720,200,3200,800))
r,g,b=im.split()
print(im.size)
for n,c in (('R',r),('G',g),('B',b)):
    c2=ImageOps.autocontrast(c,cutoff=1).resize((1200,1500),Image.LANCZOS); c2.save(f'crops/st{n}.png')
im.resize((1200,1500),Image.LANCZOS).save('crops/stRGB.png')
# green excess removed: pencil = min channel ratio
import numpy as np
a=np.asarray(im).astype(float)
# green ink has g>r; remove by taking max(r,g,b)
m=a.max(axis=2).astype('uint8')
c=ImageOps.autocontrast(Image.fromarray(m),cutoff=1).resize((1200,1500),Image.LANCZOS);c.save('crops/stMAX.png')
