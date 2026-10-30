from PIL import Image, ImageOps
import sys
i=Image.open('work/hires/pc_hcp_42_adr.JPG').rotate(90,expand=True).convert('L')
rows={'r1':(410,960,1060,1080),'r2a':(420,1020,760,1130),'r2b':(740,1010,1080,1130),'r3':(420,1090,1080,1210),'r4':(420,1160,1080,1260),'r5':(420,1210,780,1320),'r5b':(740,1210,1080,1330),'r6':(420,1270,1060,1390),'r7':(640,1350,1000,1440)}
for k,b in rows.items():
    c=ImageOps.autocontrast(i.crop(b),cutoff=1)
    c.resize((c.width*3,c.height*3),Image.LANCZOS).save(f'review/work/{k}.png')
