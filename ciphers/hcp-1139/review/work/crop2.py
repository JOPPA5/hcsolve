from PIL import Image
import glob
im=Image.open(glob.glob('work/hires/*adr.jpg')[0]).convert('RGB')
S=3468/1024
def c(n,l,t,r,b,z=5,rot=0):
    x=im.crop((int(l*S),int(t*S),int(r*S),int(b*S)))
    x=x.resize((int(x.width*z),int(x.height*z)),Image.LANCZOS)
    if rot: x=x.rotate(rot,expand=True)
    x.save(f'review/work/crops/{n}.png')
c('l5end',420,125,515,165)
c('l3blot',330,70,420,115)
c('l2s',20,40,110,75)
c('l15t',255,425,360,470,4)
c('l18tub',255,530,370,572,4)
c('l20o',395,580,515,615,4)
c('l19hoz',100,555,280,590,3)
c('l5o',455,130,500,165,7)
c('box',455,465,492,590,4,rot=-90)
c('date',425,205,480,465,2,rot=-90)
c('l21ma',235,600,340,632,4)
