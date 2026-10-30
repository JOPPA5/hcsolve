# independent run-length measurement of marks along one line (R channel threshold)
import sys
from PIL import Image
im=Image.open('source/address-large.jpg').convert('RGB')
y=int(sys.argv[1]); x0=int(sys.argv[2]); x1=int(sys.argv[3]); th=int(sys.argv[4]) if len(sys.argv)>4 else 140
W=im.width
cols=[]
for x in range(x0,x1):
    dark=[yy for yy in range(y-5,y+6) if im.getpixel((x,yy))[0]<th]
    cols.append(len(dark))
runs=[];i=0
while i<len(cols):
    if cols[i]>0:
        j=i
        while j<len(cols) and cols[j]>0: j+=1
        h=max(cols[i:j]); runs.append((x0+i,j-i,h)); i=j
    else: i+=1
print(' '.join(f'{x}:{w}x{h}' for x,w,h in runs))
