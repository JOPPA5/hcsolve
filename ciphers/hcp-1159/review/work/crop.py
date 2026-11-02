import sys,glob
from PIL import Image, ImageEnhance
H='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1159/work/hires/'
im=Image.open(glob.glob(H+'*adr.jpg')[0]).convert('RGB')
n=sys.argv[1]; x0,y0,x1,y1=map(int,sys.argv[2:6]); s=int(sys.argv[6]) if len(sys.argv)>6 else 3
r=im.crop((x0,y0,x1,y1)); r=r.resize((r.width*s,r.height*s),Image.LANCZOS)
r=ImageEnhance.Contrast(r).enhance(1.6); r.save('crops/%s.png'%n)
