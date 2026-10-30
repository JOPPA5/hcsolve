from PIL import Image
im=Image.open('rot.png')
c=im.crop((940,1140,1150,1290)); c.resize((c.size[0]*6,c.size[1]*6),Image.LANCZOS).save('z_pg.png')
c=im.crop((600,960,720,1040)); c.resize((c.size[0]*7,c.size[1]*7),Image.LANCZOS).save('z_pxo.png')
