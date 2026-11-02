import sys
from PIL import Image
out=sys.argv[1]; ims=[Image.open(n+'.png') for n in sys.argv[2:]]
W=max(i.width for i in ims);H=sum(i.height+12 for i in ims)
m=Image.new('L',(W,H),255);y=0
for i in ims: m.paste(i,(0,y));y+=i.height+12
m.save(out);print(m.size)
