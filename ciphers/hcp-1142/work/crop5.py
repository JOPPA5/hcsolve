# enhanced 4x crop of the middle of the foot word: crop5.py <adr scan> <out.png>
from PIL import Image,ImageOps
import sys
im=Image.open(sys.argv[1]).convert('RGB');S=3468/1024
r=im.crop((int(250*S),int(576*S),int(385*S),int(612*S)));r=ImageOps.autocontrast(r.convert('L'),cutoff=1)
r.resize((r.width*4,r.height*4),Image.LANCZOS).save(sys.argv[2])
