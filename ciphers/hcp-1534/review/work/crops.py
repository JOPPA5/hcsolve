import sys, json
from PIL import Image
src, outdir = sys.argv[1], sys.argv[2]
im = Image.open(src)
print(im.size)
up = im.transpose(Image.ROTATE_90)
print(up.size)
up.save(outdir+'/upright.png')
rows = json.load(open(sys.argv[3]))['rows']
for r in rows:
    x0,y0,x1,y1 = r['box']
    c = up.crop((x0-4,y0-4,x1+4,y1+4))
    s = 4 if r['id'][0]!='S' else 5
    c = c.resize((c.width*s, c.height*s), Image.LANCZOS)
    c.save(f"{outdir}/R_{r['id']}.png")
