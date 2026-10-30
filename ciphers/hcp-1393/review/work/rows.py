import sys
from PIL import Image, ImageOps, ImageEnhance
src, out = sys.argv[1], sys.argv[2]
im = Image.open(src).rotate(90, expand=True).convert('L')
im = ImageOps.autocontrast(im, cutoff=1)
boxes = {
 'h':(170,575,500,610),
 'r1a':(170,600,400,645),'r1b':(380,600,620,645),
 'r2a':(170,640,400,685),'r2b':(380,640,620,685),
 'r3a':(170,680,400,725),'r3b':(380,680,620,725),
 'r4a':(170,720,400,770),'r4b':(380,720,630,770),
 'r5a':(170,770,400,815),'r5b':(380,770,620,815),
 'r6':(170,815,450,860),
 'oval':(360,850,600,950),
}
for k,b in boxes.items():
    c = im.crop(b); c = c.resize((c.width*4,c.height*4), Image.LANCZOS)
    c.save(f'{out}/{k}.png')
