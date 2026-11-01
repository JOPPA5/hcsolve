from PIL import Image
import sys
# stack rows in one image per half for fewer reads
for grp in [(3,4),(5,6),(7,8),(9,10),(11,12),(13,14),(15,)]:
    for h in 'ab':
        ims=[Image.open(f'r{i:02d}{h}.png') for i in grp]
        W=ims[0].width;H=sum(i.height for i in ims)
        o=Image.new('RGB',(W,H),'white');y=0
        for i in ims:o.paste(i,(0,y));y+=i.height
        o.save(f's{grp[0]:02d}{h}.png')
