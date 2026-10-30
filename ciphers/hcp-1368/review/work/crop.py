from PIL import Image
im=Image.open('../../work/hires/pc_hcp_49_adr.JPG').rotate(90,expand=True).convert('RGB')
s=1/0.896
B={'L1':(430,930,1075,1040),'L2a':(430,1020,760,1130),'L2b':(740,1020,1090,1130),'L3a':(430,1100,760,1230),'L3b':(740,1100,1090,1230),
'L4a':(430,1210,760,1320),'L4b':(740,1210,1090,1320),'L5a':(430,1300,760,1430),'L5b':(700,1300,1090,1430),
'L6a':(430,1400,760,1520),'L6b':(740,1400,1090,1520),'L7':(660,1480,1090,1640)}
for k,b in B.items():
    c=im.crop(b); c=c.resize((c.width*3,c.height*3),Image.LANCZOS); c.save(f'c_{k}.png')
