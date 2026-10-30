from PIL import Image, ImageOps
r=Image.open('rot.png').convert('RGB')
C={'boy':(810,960,1030,1060,6),'opu':(830,1160,1110,1290,5),'many':(690,1260,980,1350,6),'thanks':(370,1360,620,1440,6),'card':(790,1370,1090,1450,5),
'fv':(440,1410,800,1590,6),'m1':(610,960,760,1060,6),'m2':(420,1560,680,1650,6),'girl':(680,1540,960,1640,5),'head':(340,895,960,990,3)}
for k,(a,b,c,d,s) in C.items():
    x=r.crop((a,b,c,d)); x=ImageOps.autocontrast(x,cutoff=1); x=x.resize((x.width*s,x.height*s),Image.BICUBIC); x.save(f'z_{k}.png')
