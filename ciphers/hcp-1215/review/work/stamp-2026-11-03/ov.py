import sys
from PIL import Image
im=Image.open(sys.argv[1]); w,h=im.size
im.resize((w//4,h//4)).save(sys.argv[2])
