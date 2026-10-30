import sys
from PIL import Image
im=Image.open(sys.argv[1]).transpose(Image.Transpose.ROTATE_270)
im.save('upright.png')
def c(name,box,s):
    t=im.crop(box); t.resize((t.width*s,t.height*s),Image.Resampling.LANCZOS).save(name)
c('U1.png',(470,70,640,120),5)
c('U2.png',(460,150,600,200),5)
c('U3.png',(60,250,260,300),5)
for i,(y0,y1) in enumerate([(20,110),(100,190),(180,270),(260,350),(340,430),(420,520)]):
    c(f'band{i}.png',(0,y0,674,y1),2)
