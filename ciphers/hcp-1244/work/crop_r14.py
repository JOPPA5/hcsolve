from PIL import Image, ImageEnhance
im=Image.open('work/hires/cpc_1912-04-10_HU__HU_Jasz-Arokszalas_jolanka-16_adr.jpg').convert('RGB')
b=(1200,1610,1340,1740)
x=im.crop(b); s=7
r,g,bl=x.split()
out=Image.new('L',(x.width*s*2+10,x.height*s),255)
out.paste(ImageEnhance.Contrast(g.resize((x.width*s,x.height*s),Image.BICUBIC)).enhance(2),(0,0))
out.paste(ImageEnhance.Contrast(bl.resize((x.width*s,x.height*s),Image.BICUBIC)).enhance(2),(x.width*s+10,0))
out.save('work/crops2/r14end_gb.png')
im.crop((700,1600,1340,1880)).resize((1920,840),Image.LANCZOS).save('work/crops2/r14_15_end.png')
