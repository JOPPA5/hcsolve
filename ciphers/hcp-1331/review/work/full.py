from PIL import Image
import glob
d='ciphers/hcp-1331/'
for f in glob.glob(d+'work/hires/*'):
    im=Image.open(f); print(f,im.size)
a=Image.open(d+'work/hires/pc_hcp_12_adr.JPG').convert('RGB')
print(a.size)
for rot,n in ((90,'r90'),(270,'r270')):
    b=a.rotate(rot,expand=True); b.thumbnail((1600,1600)); b.save(d+'review/work/adr_%s.png'%n)
