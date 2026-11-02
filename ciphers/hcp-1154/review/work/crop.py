from PIL import Image, ImageOps
import sys
im=Image.open('../../work/hires/cpc_1915-11-29_HU_Mezokovesd_HU_Szomolya_szomolya-07_adr.jpg').convert('RGB')
R={'h':(100,90,1600,240,2),
'r0':(760,1140,1560,1270,3),
'r1a':(50,1215,800,1345,3),'r1b':(780,1215,1560,1345,3),
'r2a':(50,1320,800,1450,3),'r2b':(780,1320,1560,1450,3),
'r3a':(50,1430,800,1560,3),'r3b':(780,1430,1560,1560,3),
'r4a':(50,1530,800,1660,3),'r4b':(780,1530,1570,1660,3),
'r5a':(50,1620,800,1740,3),'r5b':(780,1620,1570,1740,3),
'r6a':(50,1700,800,1830,3),'r6b':(780,1700,1570,1830,3),
'r7':(50,1750,900,1850,3),
}
for k,(a,b,c,d,s) in R.items():
    x=im.crop((a,b,c,d)); x=x.resize((x.width*s,x.height*s),Image.LANCZOS); ImageOps.autocontrast(x,cutoff=1).save(f'crops/{k}.png')
