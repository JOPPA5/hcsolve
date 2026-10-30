from PIL import Image, ImageOps
im=Image.open('rot.png').convert('RGB')
B={'l1a':(330,1015,700,1125),'l1b':(640,1030,960,1160),
'l2a':(330,1110,620,1250),'l2b':(560,1110,860,1250),
'l3a':(340,1215,640,1310),'l3b':(610,1200,950,1320),
'l4a':(330,1290,640,1420),'l4b':(620,1300,950,1400),
'l5a':(340,1400,700,1490),'l5b':(680,1390,1000,1500),
'l6a':(350,1470,660,1570),'l6b':(640,1460,1070,1580),
'l7':(520,1540,1060,1650)}
for k,b in B.items():
    c=im.crop(b); c=ImageOps.autocontrast(c,cutoff=1)
    c=c.resize((c.width*4,c.height*4),Image.LANCZOS); c.save(f'r_{k}.png')
