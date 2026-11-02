import sys,glob
from PIL import Image
im=Image.open(glob.glob('hires/*_adr.jpg')[0]).convert('RGB')
# strips: rows of 4 lines approx, split left/right
def c(n,box,s=2):
    r=im.crop(box); r=r.resize((r.width*s,r.height*s),Image.LANCZOS); r.save('crops/'+n+'.png')
ys=[(30,420),(380,770),(730,1120),(1080,1470),(1430,1820),(1780,2170)]
for i,(a,b) in enumerate(ys):
    c(f's{i}L',(20,a,820,b)); c(f's{i}R',(780,a,1660,b))
c('lr1',(1480,1830,2500,2180)); c('lr2',(2400,1830,3420,2180))
