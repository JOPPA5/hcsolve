import sys
from PIL import Image, ImageOps
src=sys.argv[1]; out=sys.argv[2]; box=tuple(int(x) for x in sys.argv[3:7]); s=float(sys.argv[7]) if len(sys.argv)>7 else 2
im=Image.open(src).convert('RGB').crop(box)
im=im.resize((int(im.width*s),int(im.height*s)),Image.LANCZOS)
im.save(out)
