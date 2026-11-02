from PIL import Image
import sys
im=Image.open('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1157/work/hires/cpc_1915-12-03_HU_Mezokovesd_HU_Szomolya_szomolya-08_adr.jpg').convert('RGB')
out='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1157/review/work/'
S=[('l1a',60,60,800,170,3),('l1b',760,60,1500,170,3),('l2a',60,160,560,270,3),('l2b',500,160,1000,270,3),('l2c',950,170,1600,300,3),
('r1',40,250,1600,500,2),('r2',40,480,1600,760,2),('r3',40,740,1600,1020,2),('r4',40,1000,1600,1250,2),('r5',40,1230,1600,1500,2),('r6',40,1480,1600,1760,2),('r7',40,1740,1600,1960,2),('r8',40,1880,1700,2160,2),
('r9',1500,1800,3350,2160,2),('pm',2400,560,3200,1020,2)]
for n,a,b,c,d,z in S:
    t=im.crop((a,b,c,d)); t.resize((t.width*z,t.height*z),Image.LANCZOS).save(out+n+'.png')
