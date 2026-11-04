import sys
from PIL import Image
im=Image.open(sys.argv[1]); out=sys.argv[2]
s=3468/1024
rows=[(305,340),(340,375),(385,420),(422,457),(452,490),(500,535),(533,570),(580,620)]
for i,(a,b) in enumerate(rows):
    for j,(x0,x1) in enumerate([(100,400),(390,700),(690,980)]):
        c=im.crop((int(x0*s),int(a*s),int(x1*s),int(b*s)))
        c=c.resize((c.width//2*1,c.height//2*1))
        c.save(f"{out}/r{i+1}_{j}.png")
