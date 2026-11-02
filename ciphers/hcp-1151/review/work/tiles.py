import glob
from PIL import Image, ImageOps
base='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1151/'
im=Image.open(glob.glob(base+'work/hires/*_adr.jpg')[0]).convert('RGB')
g=im.split()[1]
def t(n,box,s=2.2):
    r=g.crop(box); r=ImageOps.autocontrast(r,cutoff=0.5); r=r.resize((int(r.width*s),int(r.height*s)),Image.LANCZOS); r.save(base+'review/work/crops/%s.png'%n)
ys=[(80,410),(390,720),(700,1030),(1010,1340),(1320,1740),(1720,2040)]
for i,(a,b) in enumerate(ys):
    t('t%dL'%i,(30,a,860,b)); t('t%dR'%i,(830,a,1660,b))
    if i<2: t('t%dX'%i,(1640,a,2740,b),1.8)
t('t5X',(1340,1720,2520,2060),1.7)
