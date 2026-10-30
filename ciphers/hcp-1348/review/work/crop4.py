from PIL import Image,ImageOps
im=Image.open('work/hires/pc_hcp_29_adr.JPG').convert('L')
r=im.rotate(90,expand=True)  # CCW
s=1785/1488
# date band: adr_small x 190-300, y 410-890
c=im.crop((int(190*s),int(600*s),int(300*s),int(900*s))).rotate(90,expand=True)
c=ImageOps.autocontrast(c); c.resize((c.width*5,c.height*5),Image.LANCZOS).save('review/work/r_year.png')
p=im.crop((int(1040*s),int(150*s),int(1300*s),int(370*s)))
p=ImageOps.autocontrast(p); p.resize((p.width*3,p.height*3),Image.LANCZOS).save('review/work/r_postmark.png')
