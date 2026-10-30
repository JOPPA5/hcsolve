from PIL import Image,ImageOps
im=Image.open('work/hires/pc_hcp_30_adr.JPG').convert('RGB')
c=im.crop((1390,120,1660,430)); 
for a,n in ((0,'pm0'),(-30,'pm1'),(270,'pm2')):
    d=ImageOps.autocontrast(c.rotate(a,expand=True),cutoff=0.5); d.resize((d.width*3,d.height*3),Image.BICUBIC).save(f'work/crops/{n}.jpg',quality=90)
