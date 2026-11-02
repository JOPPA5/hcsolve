from PIL import Image, ImageEnhance
import glob,sys,os
b=os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
im=Image.open(glob.glob(b+'/work/hires/*_adr.jpg')[0]).convert('RGB')
s=3468/1024
def c(n,x0,y0,x1,y1,z=2.0):
    r=im.crop((int(x0*s),int(y0*s),int(x1*s),int(y1*s)))
    r=ImageEnhance.Contrast(r).enhance(1.5)
    r=r.resize((int(r.width*z),int(r.height*z)),Image.LANCZOS); r.save(b+'/review/work/%s.png'%n)
for n,y0,y1 in [('t',68,100),('a3',100,142),('a4',138,178),('a5',174,214),('a6',208,246),('a7',245,287),('a8',282,322),('a9',552,590)]:
    c(n+'L',15,y0,265,y1); c(n+'R',250,y0,505,y1)
c('op1',20,48,500,108,1.2); c('tail',20,570,500,640,1.3); c('v1',20,325,505,450,1.2); c('v2',20,445,505,585,1.2)
c('t0L',15,12,265,55); c('t0R',250,12,505,55)
c('end5',470,176,510,216,7); c('z7h',415,210,480,246,6); c('z7e',60,245,125,285,6); c('dot4',15,142,75,175,6); c('dot7',110,250,180,285,6); c('top3',120,15,200,55,5)
c('t1',20,565,270,640,1.8); c('t2',250,565,500,640,1.8); c('sig',380,500,500,575,3)
c('o1',20,48,260,105,2); c('o2',250,48,500,105,2)
c('over',200,14,262,58,6); c('udv',420,44,505,88,5); c('udv2',15,76,120,106,5); c('marad',20,600,190,640,3.5); c('pm',730,15,970,140,1.5); c('dalt',430,325,510,370,5)
c('over2',240,15,300,55,7)
