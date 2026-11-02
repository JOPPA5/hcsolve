from PIL import Image, ImageEnhance, ImageOps
im=Image.open('hires/cpc_1912--20_HU__HU_Jasz-Arokszalas_jolanka-101_adr.jpg').convert('RGB')
c=im.crop((920,1370,1130,1510)); c=c.resize((c.width*5,c.height*5),Image.LANCZOS)
r,g,b=c.split()
m=Image.new('RGB',(c.width*3,c.height),'white'); m.paste(c,(0,0))
m.paste(ImageOps.autocontrast(r,cutoff=1).convert('RGB'),(c.width,0))
m.paste(ImageOps.autocontrast(g.point(lambda v:min(v*4,255))).convert('RGB'),(c.width*2,0)); m.save('crops/blob.png')
c=im.crop((60,1960,2050,2050)); c=c.resize((int(c.width*1.08),int(c.height*1.08)*1)); 
d=im.crop((1500,1880,2080,2060)).resize((1740,540),Image.LANCZOS); d.save('crops/end.png')
e=im.crop((60,1360,1600,1570)).resize((2000,273),Image.LANCZOS); e.save('crops/r12_13.png')
