import sys,glob
from PIL import Image
im=Image.open(glob.glob('work/hires/*_adr.jpg')[0]).convert('L')
# dark-ink vertical profile for row 24 between the e and the o
y0,y1=1775,1845
for x in range(860,960,2):
    d=sum(im.getpixel((x,y))<110 for y in range(y0,y1))
    print(x,'#'*d)
