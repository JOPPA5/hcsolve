import sys
from PIL import Image, ImageDraw
im=Image.open(sys.argv[1]).rotate(90,expand=True)
boxes=[tuple(map(int,b.split(','))) for b in sys.argv[3:]]
s=10;tiles=[im.crop(b).resize(((b[2]-b[0])*s,(b[3]-b[1])*s),Image.LANCZOS) for b in boxes]
W=sum(t.width for t in tiles)+10*len(tiles);H=max(t.height for t in tiles)
out=Image.new('RGB',(W,H),'white');x=0
for t in tiles: out.paste(t,(x,0));x+=t.width+10
out.save(sys.argv[2])
