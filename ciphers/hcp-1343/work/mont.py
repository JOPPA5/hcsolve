import sys
from PIL import Image
out=sys.argv[1]; fs=sys.argv[2:]
ims=[Image.open('crops/%s.png'%f) for f in fs]
W=max(i.width for i in ims);H=sum(i.height+8 for i in ims)
m=Image.new('L',(W,H),255);y=0
for i in ims: m.paste(i,(0,y));y+=i.height+8
m.save('crops/%s.png'%out);print(m.size)
