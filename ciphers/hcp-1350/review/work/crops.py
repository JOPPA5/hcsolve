from PIL import Image
im=Image.open('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1350/work/hires/pc_hcp_31_adr.JPG').rotate(90,expand=True)
r={'L1a':(330,1010,720,1130),'L1b':(680,1010,1090,1130),'L2a':(330,1090,720,1210),'L2b':(700,1090,1090,1240),
'L3':(330,1200,900,1320),'L4':(330,1290,950,1400),'L5':(340,1370,1010,1520),'L6a':(340,1470,720,1600),'L6b':(690,1460,1090,1610),'L7':(370,1560,1080,1660),'pm':(100,120,450,500)}
for k,b in r.items():
    c=im.crop(b);s=4 if k!='pm' else 3
    c.resize((c.width*s,c.height*s),Image.LANCZOS).save(k+'.png')
