from PIL import Image
import sys
im=Image.open('work/hires/cpc_1915-12-28_HU_Mezokovesd_HU_Szomolya_szomolya-13_adr.jpg').convert('RGB')
strips=[('t0',40,50,1700,180),('p1',40,140,1700,460),('p2',40,440,1700,760),('p3',40,740,1700,1060),('p4',40,1040,1700,1360),
('c1',40,1440,900,1700),('c2',860,1440,1720,1700),('c3',40,1660,900,1920),('c4',860,1660,1720,1920),('c5',40,1880,900,2170),('c6',860,1880,1760,2170)]
for n,a,b,c,d in strips:
    r=im.crop((a,b,c,d)); s=2 if n[0]=='c' else 1
    r=r.resize((r.width*s,r.height*s),Image.LANCZOS); r.save(f'work/crops/{n}.png')
