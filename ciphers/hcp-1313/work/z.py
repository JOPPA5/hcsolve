import sys
from PIL import Image
W='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1313/work/crops/'
# usage: name x0 y0 x1 y1 scale -> stacks enh (top) and enh2 (bottom)
n=sys.argv[1]; x0,y0,x1,y1=map(int,sys.argv[2:6]); s=float(sys.argv[6])
A=Image.open(W+'enh_full.png').crop((x0,y0,x1,y1)); B=Image.open(W+'enh2_full.png').crop((x0,y0,x1,y1))
w,h=int(A.width*s),int(A.height*s)
o=Image.new('L',(w,2*h+6),0); o.paste(A.resize((w,h),Image.LANCZOS),(0,0)); o.paste(B.resize((w,h),Image.LANCZOS),(0,h+6)); o.save(W+n+'.png')
