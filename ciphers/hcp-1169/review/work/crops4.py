from PIL import Image
import glob
im=Image.open(glob.glob('../../work/hires/*adr.jpg')[0]).convert('RGB')
S=3468/1024
def c(n,x0,y0,x1,y1,z=4,src=im):
    k=src.crop((int(x0*S),int(y0*S),int(x1*S),int(y1*S)))
    k.resize((k.width*z,k.height*z),Image.LANCZOS).save('crops/'+n+'.jpg',quality=92)
c('sz7',395,268,500,312,4)
c('esik',255,190,420,225,3)
c('kona',390,545,510,600,4)
c('fin3',440,455,510,500,5)
c('tt',30,470,300,530,3)
p=Image.open(glob.glob('../../work/hires/*pic.jpg')[0]).convert('RGB')
c('printed',170,510,460,575,3,p)
