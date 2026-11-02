import glob,numpy as np
from PIL import Image
im=np.asarray(Image.open(glob.glob('hires/*_adr.jpg')[0]).convert('RGB')).astype(float)
R,G,B=im[...,0],im[...,1],im[...,2]
# blue ink: B relatively high vs R; brown: R>B strongly
s=(B-R)  # blue positive, brown strongly negative, paper about -70
out=np.clip((s+75)/(70)*255,0,255)  # white for blue
m=np.clip(255-out,0,255)
Z={'i_k':(860,350,1540,440),'i_u':(60,1965,640,2075)}
for k,(x0,y0,x1,y1) in Z.items():
    c=Image.fromarray(m[y0:y1,x0:x1].astype('uint8')).resize(((x1-x0)*3,(y1-y0)*3),Image.LANCZOS); c.save(f'crops/{k}.png')
