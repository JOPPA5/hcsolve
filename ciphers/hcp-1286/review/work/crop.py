import sys,glob
from PIL import Image,ImageEnhance
im=Image.open(glob.glob('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1286/work/hires/*adr*')[0]).convert('RGB')
a=sys.argv[1:]
for i in range(0,len(a),6):
    n=a[i];x0,y0,x1,y1,s=map(int,a[i+1:i+6])
    r=im.crop((x0,y0,x1,y1));r=r.resize((r.width*s,r.height*s),Image.LANCZOS)
    r=ImageEnhance.Color(r).enhance(2.0);r=ImageEnhance.Contrast(r).enhance(1.7)
    r.save('c/%s.png'%n)
