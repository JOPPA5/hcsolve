from PIL import Image,ImageOps
im=Image.open('review/work/try2.png')
z={'r_l1a':(0,40,240,145),'r_l1b':(230,40,480,145),'r_l1c':(470,40,780,145),'r_kiss':(30,145,280,250),'r_from':(240,145,480,260),'r_ours':(490,145,780,260),'r_ini':(150,250,540,396)}
for k,b in z.items():
    c=ImageOps.autocontrast(im.crop(b)); c.resize((c.width*4,c.height*4),Image.LANCZOS).save(f'review/work/{k}.png')
