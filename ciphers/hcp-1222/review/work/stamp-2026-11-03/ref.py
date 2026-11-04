import sys
from PIL import Image, ImageOps
im=Image.open(sys.argv[1]).convert('RGB')
for name,box in [('r1',(80,80,1500,250)),('r17',(80,1640,1500,1800)),('r7',(80,640,1500,800))]:
    c=ImageOps.autocontrast(im.crop(box).split()[2],cutoff=1)
    c.save(sys.argv[2]+f'/ref_{name}.png')
