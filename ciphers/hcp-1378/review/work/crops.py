import sys
from PIL import Image
r=Image.open('work/hires/pc_hcp_59_adr.JPG').rotate(90,expand=True)
C={'l1':(370,1010,1090,1090),'l2':(470,1085,1090,1170),'l3':(430,1170,1000,1260),'l4':(430,1255,900,1350),
'l5':(420,1340,1090,1430),'l6':(530,1420,950,1500),'l7':(100,1490,1090,1610),
'w_pxo':(590,1085,760,1165),'w_tfou':(740,1185,980,1260),'w_dbse':(430,1262,640,1345),'w_pg':(660,1262,860,1350),'w_cpz':(900,1090,1080,1170),'w_nz':(480,1090,600,1170),'w_ibwf':(430,1175,640,1270),'w_mart':(560,1345,830,1420),'w_gh':(380,1010,540,1090)}
for k,b in C.items():
    c=r.crop(b); s=4 if k[0]=='w' else 2.4
    c=c.resize((int(c.width*s),int(c.height*s)),Image.LANCZOS); c.save(f'review/work/{k}.png')
