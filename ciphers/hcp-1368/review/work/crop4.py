from PIL import Image, ImageOps
im=Image.open('../../work/hires/pc_hcp_49_adr.JPG').rotate(90,expand=True).convert('L')
B={'amp_N':(655,1325,800,1415),'head':(430,930,720,1040)}
for k,b in B.items():
    c=ImageOps.autocontrast(im.crop(b),cutoff=1); c=c.resize((c.width*6,c.height*6),Image.LANCZOS); c.save('z_'+k+'.png')
