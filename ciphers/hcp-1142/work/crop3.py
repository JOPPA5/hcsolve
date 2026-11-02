from PIL import Image, ImageOps
im=Image.open('hires/cpc_1906--_HU_Mezokovesd_HU_Szomolya_szomolya-41_adr.jpg').convert('RGB')
f=1.73
c=im.crop(tuple(int(v*f) for v in (440,1125,720,1195))); c=c.resize((c.width*3,c.height*3),Image.LANCZOS); c.save('crops/word1.png')
g=ImageOps.autocontrast(c.split()[0]); g.save('crops/word1r.png')
c=im.crop(tuple(int(v*f) for v in (650,1125,960,1195))); c=c.resize((c.width*3,c.height*3),Image.LANCZOS); c.save('crops/word2.png')
c=im.crop(tuple(int(v*f) for v in (690,1050,880,1130))); c=c.resize((c.width*3,c.height*3),Image.LANCZOS); c.save('crops/sig.png')
