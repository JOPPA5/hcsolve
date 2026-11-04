import sys
from PIL import Image, ImageOps
im=Image.open(sys.argv[1]).convert('RGB')
for name,box in [('r17vig',(80,1700,800,1800)),('r1jolan',(950,100,1500,220))]:
    c=ImageOps.autocontrast(im.crop(box).split()[2],cutoff=1)
    c.resize((c.width*2,c.height*2),Image.LANCZOS).save(sys.argv[2]+f'/ref_{name}.png')
