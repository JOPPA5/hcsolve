from PIL import Image,ImageOps
im=Image.open('work/hires/pc_hcp_39_adr.JPG').convert('RGB')
c=im.crop((1330,130,1680,370)); c=ImageOps.autocontrast(c,cutoff=0.5).resize((c.width*3,c.height*3),Image.BICUBIC); c.save('work/crops/z_postmark.png')
