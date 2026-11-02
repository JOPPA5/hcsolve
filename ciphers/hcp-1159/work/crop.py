from PIL import Image
import glob,sys
im=Image.open(glob.glob('hires/*adr.jpg')[0]).convert('RGB')
def c(n,x0,y0,x1,y1,s=2):
    r=im.crop((x0,y0,x1,y1)); r=r.resize((r.width*s,r.height*s),Image.LANCZOS); r.save('crops/%s.png'%n)
a=sys.argv
if len(a)>1:
    c(a[1],*map(int,a[2:6]),int(a[6]) if len(a)>6 else 3)
else:
    c('head',40,50,1000,640,2)
    c('l1',40,620,800,800,2)
    c('l1b',760,620,1540,800,2)
    c('l2',40,780,800,1010,2)
    c('l2b',760,780,1560,1010,2)
    c('l3',40,1000,800,1170,2)
    c('l3b',760,1000,1600,1170,2)
    c('l4',40,1150,800,1320,2)
    c('l4b',760,1150,1600,1320,2)
    c('l5',40,1290,800,1480,2)
    c('l5b',760,1290,1620,1480,2)
    c('l6',40,1450,800,1700,2)
    c('l6b',760,1450,1620,1700,2)
    c('foot',40,1660,1540,2120,1)
