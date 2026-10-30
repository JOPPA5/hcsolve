from PIL import Image, ImageEnhance
r=Image.open('work/hires/pc_hcp_48_adr.JPG').convert('RGB').rotate(90,expand=True)
boxes={'r0':(440,950,1090,1040),'r1a':(440,1020,760,1130),'r1b':(740,1040,1060,1190),'r2':(420,1130,960,1230),
'r3a':(400,1220,740,1320),'r3b':(720,1220,1090,1320),'r4':(410,1300,1050,1430),'r5':(430,1420,1080,1510),'r6':(60,1500,1000,1640),
'ibooz':(410,1225,640,1320),'sfu':(640,1220,860,1320),'sfu2':(840,1220,1080,1320),'mp':(620,1030,860,1140),'wjoh':(830,1040,1050,1140),'cpz':(880,1110,1060,1190)}
for k,b in boxes.items():
    c=r.crop(b); s=4 if (b[2]-b[0])<400 else 3
    c=c.resize((c.width*s,c.height*s),Image.LANCZOS)
    c=ImageEnhance.Contrast(c).enhance(1.5); c.save(f'review/work/{k}.png')
