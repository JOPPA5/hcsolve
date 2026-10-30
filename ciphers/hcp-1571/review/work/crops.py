import sys
from PIL import Image
src,out=sys.argv[1],sys.argv[2]
im=Image.open(src).transpose(Image.ROTATE_270)
print(im.size)
im.save(out+'/rot.png')
rows={'R01':(40,78),'R02':(66,105),'R03':(90,129),'R04':(113,151),'R05':(139,176),'R06':(163,200),'R07':(188,226),'R08':(211,250),'R09':(236,273),'R10':(848,888),'R11':(875,918),'R12':(900,944),'R13':(929,970)}
for k,(a,b) in rows.items():
    for h,(x0,x1) in enumerate([(50,350),(330,645)]):
        c=im.crop((x0,a,x1,b)); c=c.resize((c.width*4,c.height*4),Image.LANCZOS); c.save(f'{out}/{k}_{h}.png')
