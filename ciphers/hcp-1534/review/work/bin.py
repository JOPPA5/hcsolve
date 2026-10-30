import sys
from PIL import Image
up=Image.open('upright.png').convert('L')
x0,y0,x1,y1,t=map(int,sys.argv[1:6])
for y in range(y0,y1):
    print(''.join('#' if up.getpixel((x,y))<t else ('+' if up.getpixel((x,y))<t+40 else '.') for x in range(x0,x1)))
