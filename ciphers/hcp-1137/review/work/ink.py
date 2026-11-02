from PIL import Image
import numpy as np
im=np.array(Image.open('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1137/work/hires/cpc_1916-06-10_HU_Mezokovesd_HU_Szomolya_szomolya-39_adr.jpg').convert('RGB')).astype(int)
x0,y0,x1,y1=2350,1860,3300,2130
c=im[y0:y1,x0:x1]
r,g,b=c[...,0],c[...,1],c[...,2]
# pencil is violet: blue >= green; stamp is brown: blue < green
v=(b-g)
o=np.clip(255-(v+10)*6,0,255).astype('uint8')
I=Image.fromarray(o).resize(((x1-x0)*2,(y1-y0)*2));I.save('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1137/review/work/crops/ink.png')
