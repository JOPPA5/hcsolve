import sys,glob
from PIL import Image
for f in glob.glob('hires/*.jpg'):
    im=Image.open(f); print(f,im.size)
    t='adr' if f.endswith('adr.jpg') else 'pic'
    im.thumbnail((1800,1800)); im.save(f'crops/{t}_full.png')
