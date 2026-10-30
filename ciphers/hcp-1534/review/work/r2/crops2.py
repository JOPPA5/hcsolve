import sys, json
from PIL import Image
src, rec, outdir = sys.argv[1:4]
up = Image.open(src).transpose(Image.ROTATE_90)
rows = {r['id']: r for r in json.load(open(rec))['rows']}
for rid in sys.argv[4:]:
    x0,y0,x1,y1 = rows[rid]['box']
    w = x1-x0
    parts = 1 if w < 260 else 2
    for i in range(parts):
        a = x0 + i*w//parts - 6; b = x0 + (i+1)*w//parts + 6
        c = up.crop((max(a,0), y0-5, b, y1+5))
        c = c.resize((c.width*5, c.height*5), Image.LANCZOS)
        c.save(f"{outdir}/R2_{rid}_{i}.png")
