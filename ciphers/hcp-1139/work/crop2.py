from PIL import Image
import glob
im=Image.open(glob.glob('hires/*adr.jpg')[0]).convert('RGB')
S=1.927
def c(n,l,t,r,b,z=4,rot=0):
    x=im.crop((int(l*S),int(t*S),int(r*S),int(b*S)))
    if rot: x=x.rotate(rot,expand=True)
    x.resize((int(x.width*z),int(x.height*z)),Image.LANCZOS).save(f'crops/{n}.png')
c('z_l3',  20,125,300,185,3)   # kedjól e?v
c('z_l5end',600,215,910,290,3)
c('z_l5a', 30,205,300,270,3)
c('z_tub', 420,930,740,1000,3)
c('z_meged',560,740,740,800,4)
c('z_udv', 540,1030,890,1085,3)
c('z_box', 790,800,860,1040,3,-90)
c('z_date', 730,380,860,800,2,-90)
c('z_top', 800,350,860,800,2,-90)
c('z_bl', 30,1020,330,1110,3)
