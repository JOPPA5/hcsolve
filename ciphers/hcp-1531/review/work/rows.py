import sys,json
from PIL import Image
im=Image.open(sys.argv[1]); t=json.load(open(sys.argv[2])); out=sys.argv[3]
for r in t['rows']:
    x0,y0,x1,y1=r['box_source_xyxy']
    c=im.crop((x0-8,y0-4,x1+8,y1+4)); c=c.resize((c.width*3,c.height*3),Image.LANCZOS); c.save(f"{out}/{r['id']}.png")
