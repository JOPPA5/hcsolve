import sys
from PIL import Image
W='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1313/work/crops/'
n=sys.argv[1]; x0,y0,x1,y1=map(int,sys.argv[2:6]); s=float(sys.argv[6])
B=Image.open(W+'enh2_full.png').crop((x0,y0,x1,y1)); B.resize((int(B.width*s),int(B.height*s)),Image.LANCZOS).save(W+n+'.png')
