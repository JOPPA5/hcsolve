"""Round-2 recheck: zoomed crops of single words (upright frame); args: name x0 y0 x1 y1 scale."""
import sys
from pathlib import Path
from PIL import Image
p=Path(__file__).resolve().parent; root=p.parent.parent
im=Image.open(root/'source/picture.jpg').transpose(Image.Transpose.ROTATE_90)
a=sys.argv[1:]
while a:
    n,x0,y0,x1,y1,s=a[:6];a=a[6:]
    c=im.crop(tuple(map(int,(x0,y0,x1,y1)))); s=int(s)
    c.resize((c.width*s,c.height*s),Image.LANCZOS).save(p/f'z_{n}.png')
