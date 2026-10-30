import sys
from PIL import Image, ImageOps
src,out=sys.argv[1],sys.argv[2]
im=Image.open(src)
msg=im.crop((150,140,380,610)).rotate(90,expand=True)
msg.save(out+'/msg.png')
w,h=msg.size
print(w,h)
g=ImageOps.autocontrast(msg.convert('L'),cutoff=1)
# three lines: split vertically into thirds roughly, each enlarged 4x in two halves
for i,(y0,y1) in enumerate([(0,90),(70,150),(130,230)]):
    for j,(x0,x1) in enumerate([(0,240),(220,470)]):
        c=g.crop((x0,y0,x1,y1)); c=c.resize((c.width*4,c.height*4),Image.LANCZOS); c.save(f'{out}/l{i+1}_{j+1}.png')
