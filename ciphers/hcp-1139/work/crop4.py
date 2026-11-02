from PIL import Image
import glob
im=Image.open(glob.glob('hires/*adr.jpg')[0]).convert('RGB')
S=1.927
def c(n,l,t,r,b,z=4):
    x=im.crop((int(l*S),int(t*S),int(r*S),int(b*S)))
    x.resize((int(x.width*z),int(x.height*z)),Image.LANCZOS).save(f'crops/{n}.png')
c('x_hozzad',150,985,380,1040,4)
c('x_hu',540,1060,740,1112,4)
