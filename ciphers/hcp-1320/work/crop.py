import sys
from PIL import Image, ImageOps, ImageEnhance
im=Image.open('hires/pc_hcp_1_adr.JPG').convert('RGB')
# left panel, rotated so text is upright candidates
l=im.crop((60,50,800,1120))
for name,rot in (('L_rot90',90),('L_rot270',270)):
    r=l.rotate(rot,expand=True)
    r=r.resize((r.width*2,r.height*2),Image.LANCZOS)
    r.save(f'crops/{name}.jpg',quality=92)
