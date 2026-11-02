import sys
from PIL import Image, ImageEnhance
ink=Image.open('crops/ink.png')
im=Image.open('hires/cpc_1914-10-15_HU__HU_Budapest_jolanka-55_adr.jpg').convert('RGB')
name,x0,y0,x1,y1=sys.argv[1],*map(int,sys.argv[2:6])
s=2000/(x1-x0)
a=ink.crop((x0,y0,x1,y1)).resize((2000,int((y1-y0)*s)),Image.BICUBIC).convert('RGB')
b=ImageEnhance.Contrast(ImageEnhance.Color(im.crop((x0,y0,x1,y1))).enhance(2.5)).enhance(1.4).resize(a.size,Image.BICUBIC)
o=Image.new('RGB',(2000,a.height*2+6),'red'); o.paste(a,(0,0)); o.paste(b,(0,a.height+6)); o.save('crops/%s.png'%name)
