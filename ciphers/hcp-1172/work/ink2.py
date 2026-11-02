import glob
from PIL import Image
im=Image.open(glob.glob('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1172/work/hires/*adr.jpg')[0]).convert('RGB')
r=im.split()[0].point(lambda v:0 if v<85 else (255 if v>135 else int((v-85)*5.1)))
for n,b in {'r3a':(60,430,950,570),'r3b':(880,430,1760,570),'r4':(60,540,950,690)}.items():
    c=r.crop(b); c.resize((c.width*2,c.height*2),Image.LANCZOS).save('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1172/work/crops/'+n+'.png')
