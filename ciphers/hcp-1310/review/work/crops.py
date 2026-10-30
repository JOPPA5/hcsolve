import sys
from PIL import Image, ImageEnhance
im=Image.open(sys.argv[1]).convert('RGB')
S=3445/1024
# block crops, display coordinates
def c(n,l,t,r,b,z=2.2):
    x=im.crop((int(l*S),int(t*S),int(r*S),int(b*S)));x=x.resize((int(x.width*z),int(x.height*z)),Image.LANCZOS)
    ImageEnhance.Contrast(x).enhance(1.3).save(sys.argv[2]+'/'+n+'.png')
ys=[(20,120),(110,210),(200,300),(290,390),(380,480),(470,560),(550,630)]
for i,(a,b) in enumerate(ys):
    c(f'L{i}',20,a,240,b); c(f'R{i}',225,a,480,b)
c('stamp',780,50,925,215,3)
c('addr',720,395,970,440,2.5)
c('foot',440,585,1000,630,1.6)
