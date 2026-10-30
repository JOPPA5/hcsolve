from PIL import Image, ImageOps, ImageEnhance
im=Image.open('rot.png').convert('RGB')
boxes={'h':(340,970,1100,1070),'l1':(340,1060,1060,1160),'l2a':(340,1140,760,1270),'l2b':(720,1140,1110,1290),
'l3':(340,1250,1020,1400),'l4a':(340,1370,720,1480),'l4b':(680,1370,1040,1520),'l5a':(340,1450,720,1590),'l5b':(680,1460,1040,1590),
'l6a':(90,1520,560,1660),'l6b':(520,1540,1000,1690),'l7':(780,1600,1110,1710)}
for k,b in boxes.items():
    c=im.crop(b); c=c.resize((c.width*4,c.height*4),Image.LANCZOS)
    c=ImageOps.autocontrast(c,cutoff=0.5); c.save(f'c_{k}.png')
