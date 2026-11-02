import sys
from PIL import Image
fs=sys.argv[2:]; ims=[Image.open(f'review/work/crops/{f}.png') for f in fs]
w=max(i.width for i in ims);h=sum(i.height+10 for i in ims)
o=Image.new('RGB',(w,h),'white');y=0
for i in ims:o.paste(i,(0,y));y+=i.height+10
o.save(f'review/work/crops/{sys.argv[1]}.png');print(o.size)
