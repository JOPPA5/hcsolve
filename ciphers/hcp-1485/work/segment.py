# Segment the cipher lines of work/upright.jpg into glyph columns for inspection.
import sys
from PIL import Image, ImageOps, ImageDraw
src, out = sys.argv[1], sys.argv[2]
im = Image.open(src).convert('L')
px = im.load()
rows = [(88,128),(143,181),(188,226),(238,270),(283,320),(326,362),(360,400),(404,439),(490,526),(530,566),(568,602)]
TH = 95
for li,(y0,y1) in enumerate(rows):
    cols = []
    for x in range(568, 925):
        cols.append(sum(1 for y in range(y0,y1) if px[x,y] < TH))
    segs=[]; inside=False
    for i,c in enumerate(cols):
        x=568+i
        if c>0 and not inside: start=x; inside=True
        if c==0 and inside: segs.append((start,x)); inside=False
    if inside: segs.append((start,925))
    print(li+1, len(segs), segs)
    # draw line with segment markers
    crop = ImageOps.autocontrast(im.crop((565,y0-4,925,y1+4)),cutoff=1).convert('RGB')
    S=6
    crop = crop.resize((crop.width*S, crop.height*S), Image.BICUBIC)
    d=ImageDraw.Draw(crop)
    for k,(a,b) in enumerate(segs):
        d.line([((a-565)*S,0),((a-565)*S,12)],fill=(255,0,0),width=2)
        d.text(((a-565)*S+2,0),str(k),fill=(255,0,0))
    for half in range(2):
        w=crop.width//2
        crop.crop((half*w-(40 if half else 0),0,(half+1)*w,crop.height)).save('%s/seg%02d_%d.png'%(out,li+1,half))
