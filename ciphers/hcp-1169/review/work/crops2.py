from PIL import Image
import glob
im=Image.open(glob.glob('../../work/hires/*adr.jpg')[0]).convert('RGB')
S=3468/1024
def c(n,x0,y0,x1,y1,z=4):
    k=im.crop((int(x0*S),int(y0*S),int(x1*S),int(y1*S)))
    k.resize((k.width*z,k.height*z),Image.LANCZOS).save('crops/'+n+'.jpg',quality=92)
c('closing',30,345,500,415,1 if 0 else 2)
c('sziv7',415,295,500,335,4)
c('note1',30,385,500,520,2)
c('note2',30,510,290,625,3)
c('note3',270,540,560,630,3)
c('addr',500,250,980,625,2)
c('stamp',710,5,980,250,2)
