# side-by-side top/bottom halves of a vertical region. usage: pair.py x0a x1a x0b x1b scale out
import sys,subprocess
from PIL import Image
x0a,x1a,x0b,x1b=map(int,sys.argv[1:5]); sc=sys.argv[5]; out=sys.argv[6]
py=sys.executable
subprocess.run([py,'-I','work/zoom2.py',str(x0a),'40',str(x1a),'1100',sc,'/tmp/_a.png'] if False else [py,'-I','work/zoom2.py',str(x0a),'40',str(x1a),'1100',sc,out+'.a.png'],check=True)
subprocess.run([py,'-I','work/zoom2.py',str(x0b),'1080',str(x1b),'2140',sc,out+'.b.png'],check=True)
a=Image.open(out+'.a.png');b=Image.open(out+'.b.png')
c=Image.new('RGB',(a.width+b.width+10,max(a.height,b.height)),'white');c.paste(a,(0,0));c.paste(b,(a.width+10,0));c.save(out)
import os; os.remove(out+'.a.png'); os.remove(out+'.b.png')
