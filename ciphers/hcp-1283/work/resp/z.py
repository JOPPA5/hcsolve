import sys
from PIL import Image
sh=Image.open('review/work/sheared.png').convert('RGB')
a=sys.argv[1:]
for i in range(0,len(a),6):
    n,x0,y0,x1,y1,s=a[i],*map(int,a[i+1:i+6])
    c=sh.crop((x0,y0,x1,y1)); c.resize((c.width*s,c.height*s),Image.LANCZOS).save('work/resp/%s.png'%n)
