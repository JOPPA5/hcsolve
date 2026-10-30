import sys
from PIL import Image
names=sys.argv[2:]
ims=[Image.open('work/bands/'+n+'.png') for n in names]
W=max(i.width for i in ims);H=sum(i.height+10 for i in ims)
o=Image.new('RGB',(W,H),'white');y=0
for i in ims: o.paste(i,(0,y)); y+=i.height+10
o.save('work/bands/'+sys.argv[1]+'.png')
