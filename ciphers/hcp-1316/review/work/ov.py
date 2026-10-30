from PIL import Image
import sys
im=Image.open(sys.argv[1]); print(im.size)
im.thumbnail((1500,1000)); im.save(sys.argv[2])
