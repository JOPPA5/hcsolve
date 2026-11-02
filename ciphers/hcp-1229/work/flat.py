from PIL import Image,ImageOps,ImageFilter,ImageChops
import sys
src='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1229/work/hires/cpc_1914-01-07_HU__HU_Jasz-Arokszalas_jolanka-46_adr.jpg'
a=sys.argv
box=tuple(int(x) for x in a[2:6]); s=int(a[6])
im=Image.open(src).convert('RGB').crop((box[0]-60,box[1]-60,box[2]+60,box[3]+60))
g=im.split()[0]  # red channel suppresses brown stain
bg=g.filter(ImageFilter.GaussianBlur(22))
d=ImageChops.subtract(bg,g)  # ink darker than bg
d=ImageOps.invert(d)
d=ImageOps.autocontrast(d,cutoff=0.3)
d=d.crop((60,60,60+box[2]-box[0],60+box[3]-box[1]))
d=d.resize((d.width*s,d.height*s),Image.LANCZOS)
d.save('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1229/work/crops/'+a[1]+'.png')
