from PIL import Image, ImageOps
p=Image.open('work/hires/pc_hcp_63_pic.JPG').convert('L'); s=p.width/1024
x=p.crop((int(130*s),int(510*s),int(230*s),int(625*s)))
x=ImageOps.autocontrast(x,cutoff=1); x=x.resize((x.width*4,x.height*4),Image.LANCZOS)
x.save('review/work/z_picmark.png'); x.rotate(90,expand=True).save('review/work/z_picmark_r.png')
