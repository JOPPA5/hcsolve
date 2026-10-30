from PIL import Image, ImageOps
o=Image.open('work/hires/pc_hcp_12_adr.JPG').convert('RGB')
a=o.rotate(90,expand=True)
S=1785/1600
reg={'first_l':(255,1150,420,1275,8),'n_hook':(405,1195,560,1270,10),'nine54':(270,1105,560,1190,6),
'P_Pole':(240,1395,470,1465,7),'R_Reh':(640,1270,800,1350,7),'P_Reh2':(230,1395,350,1460,8),'but':(240,1320,560,1410,4),'have':(600,1330,900,1420,4)}
for k,(x0,y0,x1,y1,z) in reg.items():
    c=a.crop(tuple(int(v*S) for v in (x0,y0,x1,y1)))
    c=c.resize((c.width*z,c.height*z),Image.LANCZOS); ImageOps.autocontrast(c,cutoff=0.5).save(f'review/work/{k}.png')
# unrotated: postmark, address
for k,b,z in (('pm',(1230,160,1480,430),5),('name',(1180,500,1640,680),4)):
    c=o.crop(b); c=c.resize((c.width*z,c.height*z),Image.LANCZOS); ImageOps.autocontrast(c,cutoff=0.5).save(f'review/work/{k}.png')
p=Image.open('work/hires/pc_hcp_12_pic.JPG'); p.thumbnail((1400,1400)); p.save('review/work/pic.png')
