from PIL import Image,ImageOps,ImageEnhance
im=Image.open('hires/pc_hcp_63_adr.JPG').convert('RGB')
r=im.crop((90,300,830,1100)).rotate(90,expand=True)
print(r.size); r.save('crops/rot.png')
x=ImageOps.autocontrast(r.convert('L'),cutoff=1); x=ImageEnhance.Contrast(x).enhance(1.6); x=x.resize((r.width*2,r.height*2),Image.LANCZOS); x.save('crops/rot2x.jpg',quality=92)
