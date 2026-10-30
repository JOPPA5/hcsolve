import sys
from PIL import Image
im=Image.open(sys.argv[1]).rotate(-90,expand=True)
out=sys.argv[2]
boxes={'c_r08':(40,276,240,312),'c_r03':(400,106,640,142),'c_r09tisic':(480,270,660,312),'c_r04vcera':(260,138,460,174)}
ims=[]
for n,b in boxes.items():
    c=im.crop(b); c=c.resize((c.width*4,c.height*4),Image.LANCZOS); ims.append(c)
W=max(i.width for i in ims); H=sum(i.height for i in ims)
s=Image.new('RGB',(W,H),'white'); y=0
for i in ims: s.paste(i,(0,y)); y+=i.height
s.save(out+'/c_controls.png')
