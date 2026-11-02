from PIL import Image
import glob
im=Image.open(glob.glob('hires/*adr.jpg')[0]).convert('RGB')
S=1.927
def c(n,l,t,r,b,z=4,rot=0):
    x=im.crop((int(l*S),int(t*S),int(r*S),int(b*S)))
    if rot: x=x.rotate(rot,expand=True)
    x.resize((int(x.width*z),int(x.height*z)),Image.LANCZOS).save(f'crops/{n}.png')
c('y_ev',320,125,470,190,5)
c('y_tub',520,935,640,1000,6)
c('y_meged',500,745,680,805,4)
c('y_box',795,810,860,1035,4,90)
c('y_pm',930,20,1720,470,1)
