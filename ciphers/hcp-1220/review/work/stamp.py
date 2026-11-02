from PIL import Image, ImageOps
import glob
import numpy as np
im=Image.open(glob.glob('work/hires/*adr.jpg')[0]).convert('RGB')
# whole box at 3x
c=im.crop((2640,180,3160,790)); c.resize((c.width*2,c.height*2),Image.LANCZOS).save('review/work/box.png')
# independent ink map: purple ink absorbs green strongly relative to red/blue; blue imprint absorbs red
a=np.asarray(c).astype(float)+1
od=-np.log(a/255)
ink=od[...,1]-0.55*od[...,0]    # green absorption minus part of red absorption
g=np.clip((ink-np.percentile(ink,5))/(np.percentile(ink,99.7)-np.percentile(ink,5)),0,1)
o=Image.fromarray((255*(1-g)).astype('uint8'))
o.resize((o.width*2,o.height*2),Image.LANCZOS).save('review/work/box_ink.png')
for i,(y0,y1) in enumerate([(180,330),(300,420),(390,510),(470,600),(560,690),(640,790)]):
    c=im.crop((2640,y0,3160,y1)); c=ImageOps.autocontrast(c,cutoff=.5); c.resize((c.width*3,c.height*3),Image.LANCZOS).save(f'review/work/s{i}.png')
# row 7 blot and row 5 blot
for n,b in [('blot7',(800,800,1010,920)),('blot5',(640,540,860,700)),('blot11',(960,1250,1160,1390))]:
    c=im.crop(b); c.resize((c.width*5,c.height*5),Image.LANCZOS).save(f'review/work/{n}.png')
c=im.crop((1700,110,2600,800));c=ImageOps.autocontrast(c,cutoff=.5);c.save('review/work/pm.png')
