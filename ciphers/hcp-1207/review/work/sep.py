from PIL import Image, ImageOps
im=Image.open('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1207/work/hires/cpc_--_HU__HU_Budapest_jolanka-62_adr.jpg').convert('RGB')
O='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1207/review/work/crops/'
r,g,b=im.split()
# pencil is violet: high B-relative; seal is grey/black. use R channel lifted (violet is dark in G, seal dark in all)
from PIL import ImageChops
diff=ImageChops.subtract(b,g,scale=0.5)  # violet pencil > card? 
box=(1800,1560,3340,2070)
for n,ch in (('sepRG',ImageChops.subtract(r,g,scale=0.3,offset=0)),('sepG',g),('sepBG',diff)):
    i=ImageOps.autocontrast(ch.crop(box),cutoff=1); i.resize((i.width*13//10,i.height*13//10)).save(O+n+'.png')
