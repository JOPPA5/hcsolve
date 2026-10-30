import sys
from PIL import Image
src,out=sys.argv[1],sys.argv[2]
im=Image.open(src).rotate(-90,expand=True)
im.save(out+'/upright.png')
for name,box,s in [('top',(0,0,674,520),2),('r04',(20,130,660,180),4),('r06',(20,195,660,245),4),('r01',(20,35,660,85),4),('lower',(0,340,674,500),3)]:
    c=im.crop(box); c=c.resize((c.width*s,c.height*s),Image.LANCZOS); c.save(f'{out}/{name}.png')
