from PIL import Image, ImageOps
r=Image.open('rot.png').convert('RGB')
C={'h':(330,890,1000,1010),'l1':(330,970,1100,1090),'l2':(330,1060,1100,1190),'l3':(330,1150,1120,1290),
'l4':(370,1250,1020,1360),'l5':(370,1320,1100,1450),'l6a':(180,1400,620,1570),'l6b':(560,1400,1000,1570),'l7a':(200,1500,700,1640),'l7b':(640,1500,1040,1660)}
for k,b in C.items():
    c=r.crop(b); c=ImageOps.autocontrast(c,cutoff=1); c=c.resize((c.width*3,c.height*3),Image.LANCZOS); c.save(f'c_{k}.png')
