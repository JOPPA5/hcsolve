from PIL import Image, ImageOps
import numpy as np
o=Image.open('crops/sheared.png').convert('L')
a=np.asarray(o.crop((80,0,1500,2100))).astype(float)
ink=(a<np.median(a)-45).sum(1).astype(float)
p=np.convolve(ink,np.ones(11)/11,'same')
pk=[i for i in range(30,2070) if p[i]==p[i-28:i+29].max() and p[i]>25]
print(pk,len(pk))
for j,y in enumerate(pk):
    for k,(x0,x1) in enumerate(((60,830),(800,1570))):
        r=o.crop((x0,y-55,x1,y+55)); r=r.resize((int(r.width*2.5),int(r.height*2.5)),Image.LANCZOS)
        ImageOps.autocontrast(r,cutoff=1).save(f'crops/row{j:02d}{"LR"[k]}.png')
