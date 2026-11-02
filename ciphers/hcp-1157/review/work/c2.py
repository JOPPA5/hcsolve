from PIL import Image
import numpy as np
im=Image.open('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1157/work/hires/cpc_1915-12-03_HU_Mezokovesd_HU_Szomolya_szomolya-08_adr.jpg').convert('RGB')
out='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1157/review/work/'
S=[('z_end1',1380,60,1560,170,5),('z_end2',920,170,1000,270,6),('z_ang',60,160,640,270,3),
('z_hany',300,1860,1000,2000,3),('z_mar',1100,1890,1700,2010,3),('z_ki',880,2020,1560,2130,3),('z_oln',2380,1980,3300,2140,3)]
for n,a,b,c,d,z in S:
    t=im.crop((a,b,c,d)); t.resize((t.width*z,t.height*z),Image.LANCZOS).save(out+n+'.png')
