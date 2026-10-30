import sys
from PIL import Image, ImageOps
src, out = sys.argv[1], sys.argv[2]
im = Image.open(src).rotate(90, expand=True).convert('L')
im = ImageOps.autocontrast(im, cutoff=1)
ys = {'h':590,'r1':622,'r2':665,'r3':706,'r4':748,'r5':790,'r6':832}
for k,y in ys.items():
    for j,(x0,x1) in enumerate([(165,410),(390,630)]):
        c = im.crop((x0,y-30,x1,y+30)); c=c.resize((c.width*4,c.height*4), Image.LANCZOS)
        c.save(f'{out}/v_{k}_{j}.png')
c = im.crop((360,850,600,950)); c=c.resize((c.width*4,c.height*4), Image.LANCZOS); c.save(f'{out}/v_oval.png')
