from PIL import Image, ImageOps, ImageFilter
s=1785/1024
p=Image.open('hires/pc_hcp_467_pic.JPG').convert('RGB')
R,G,B=p.split()
g=Image.blend(R,G,0.3)  # red channel hides cyan-ish sky differently
g=R.filter(ImageFilter.GaussianBlur(0.8))
c=g.crop((int(400*s),int(55*s),int(680*s),int(305*s)))
c=ImageOps.autocontrast(c,cutoff=1)
c=c.resize((c.width*2,c.height*2),Image.BICUBIC); c.save('crops/pall.png'); print(c.size)
