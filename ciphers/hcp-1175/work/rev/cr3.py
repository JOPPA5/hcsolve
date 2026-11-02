from PIL import Image, ImageOps, ImageChops
im=Image.open('../hires/cpc_1915-10-25_HU_Mezokovesd_HU_Szomolya_szomolya-03_adr.jpg').convert('RGB')
b=(450,1940,1520,2040)
x=im.crop(b); R,G,B=x.split()
# blue-black ink: dark in R; brown overstrike is much lighter in R than in B
d=ImageOps.autocontrast(R,cutoff=0.5).point(lambda v:0 if v<95 else 255 if v>150 else (v-95)*4)
x.resize((x.width*2,x.height*2),Image.LANCZOS).save('dots.png')
d.resize((x.width*2,x.height*2),Image.LANCZOS).save('dots_r.png')
