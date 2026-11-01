import sys
from PIL import Image
im=Image.open('work/hires/cpc_1916-04-22_HU_Mezokovesd_HU_Szomolya_szomolya-31_adr.jpg').convert('RGB')
W,H=im.size
S=W/1024
boxes={'l1':(20,70,460,150),'l2':(20,150,500,215),'l3':(20,195,500,260),'l4':(20,235,500,300),'l5':(20,270,500,335),'l6':(20,310,500,375),'l7':(20,350,500,410),'l8':(20,385,500,440),'l9':(20,420,500,480),'l10':(20,450,500,505),'l11':(200,465,440,540),'l12':(60,525,580,625),'a1':(470,150,940,240),'a2':(470,240,940,340),'a3':(470,330,940,405),'a4':(500,450,920,545),'a5':(500,520,860,605),'st':(630,30,950,260)}
for k,b in boxes.items():
    c=im.crop(tuple(int(x*S) for x in b))
    c=c.resize((c.width*3//2,c.height*3//2),Image.LANCZOS)
    c.save(f'work/crops/{k}.png')
