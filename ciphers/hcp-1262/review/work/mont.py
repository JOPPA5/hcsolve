import sys
from PIL import Image
d='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1262/review/work/crops/'
out=sys.argv[1]; ims=[Image.open(d+n+'.png') for n in sys.argv[2:]]
W=max(i.width for i in ims);H=sum(i.height+6 for i in ims)
m=Image.new('RGB',(W,H),'white');y=0
for i in ims: m.paste(i,(0,y)); y+=i.height+6
m.save(d+out+'.png')
