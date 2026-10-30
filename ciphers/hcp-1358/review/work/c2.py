from PIL import Image, ImageOps
r=Image.open('rot.png').convert('L')
b={'r1a':(250,890,700,1040),'r1b':(650,890,1120,1040),'r2a':(250,990,700,1130),'r2b':(650,990,1120,1130),
'r3a':(250,1080,700,1220),'r3b':(650,1080,1120,1220),'r4a':(250,1170,700,1320),'r4b':(650,1170,1120,1320),
'r5a':(250,1270,700,1420),'r5b':(650,1270,1120,1420),'r6a':(80,1430,620,1600),'r6b':(500,1400,1120,1600)}
for k,v in b.items():
    c=ImageOps.autocontrast(r.crop(v),cutoff=1); c.resize((c.width*3,c.height*3),Image.LANCZOS).save(k+'.png')
