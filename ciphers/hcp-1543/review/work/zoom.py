import sys
from PIL import Image
im=Image.open(sys.argv[1]).rotate(-90,expand=True)
out=sys.argv[2]
for name,box in [('u1',(110,136,175,174)),('u2',(85,198,150,238)),('r01name',(180,40,265,78)),('zctrl',(330,40,420,78))]:
    c=im.crop(box); c=c.resize((c.width*8,c.height*8),Image.LANCZOS); c.save(f'{out}/{name}.png')
