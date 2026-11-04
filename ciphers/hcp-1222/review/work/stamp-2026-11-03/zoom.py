import sys
from PIL import Image, ImageOps
im=Image.open(sys.argv[1]).convert('RGB')
for name,box in [('row4start',(2770,320,2900,420)),('row1end',(2940,140,3080,260)),('row5end',(2840,420,3020,520)),('row6',(2720,450,2980,580))]:
    c=ImageOps.autocontrast(im.crop(box).split()[2],cutoff=1)
    c.resize((c.width*6,c.height*6),Image.LANCZOS).save(sys.argv[2]+f'/z6_{name}.png')
