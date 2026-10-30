import json
from PIL import Image
up=Image.open('upright.png')
for r in json.load(open('../../work/transcription.json'))['rows']:
    x0,y0,x1,y1=r['box']
    n = 1 if x1-x0<250 else 3
    w=(x1-x0)/n
    for i in range(n):
        a=int(x0+i*w)-6; b=int(x0+(i+1)*w)+6
        c=up.crop((a,y0-2,b,y1+2)); s=6
        c.resize((c.width*s,c.height*s),Image.LANCZOS).save(f"H_{r['id']}_{i}.png")
