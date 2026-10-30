from PIL import Image
im=Image.open('work/hires/pc_hcp_54_adr.JPG').rotate(90,expand=True).convert('RGB')
print(im.size, Image.open('work/reading.jpg').size)
R={'h':(340,930,1040,1110),'r1':(380,1080,1080,1190),'r2':(340,1170,1080,1290),'r3':(380,1260,1080,1400),'r4a':(340,1380,760,1490),'r4b':(700,1380,1110,1500),'r5a':(120,1450,640,1570),'r5b':(600,1470,1090,1570),'r6':(150,1530,1060,1650),'r7':(800,1590,1100,1710)}
for k,b in R.items():
    c=im.crop(b);s=4 if (b[2]-b[0])<520 else 3
    c.resize((c.width*s,c.height*s),Image.LANCZOS).save(f'review/work/{k}.png')
