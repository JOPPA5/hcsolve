from PIL import Image, ImageOps
im=Image.open('../../work/hires/cpc_1912-03-20_HU__HU_Jasz-Arokszalas_jolanka-11_adr.jpg').convert('RGB')
c=im.crop((205,830,345,985)); r,g,b=c.split()
# green channel contrast-stretched shows ink density; blue likewise; dark overlaps reveal a second stroke
out=Image.new('RGB',(3*560,620),'white')
out.paste(c.resize((560,620),Image.LANCZOS),(0,0))
out.paste(ImageOps.autocontrast(r,cutoff=1).convert('RGB').resize((560,620),Image.LANCZOS),(560,0))
out.paste(ImageOps.autocontrast(g,cutoff=1).convert('RGB').resize((560,620),Image.LANCZOS),(1120,0))
out.save('sign_row7.png')
