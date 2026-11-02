from PIL import Image
im=Image.open('hires/cpc_1906--_HU_Mezokovesd_HU_Szomolya_szomolya-41_adr.jpg').convert('RGB')
ys=[(40,110),(115,185),(175,245),(235,305),(305,380),(395,455),(455,520),(510,585),(575,650),(695,770),(770,840),(840,900),(925,980),(985,1060),(1060,1190)]
f=1.73
for i,(a,b) in enumerate(ys,1):
    for j,(l,r) in enumerate([(30,470),(440,930)]):
        c=im.crop((int(l*f),int(a*f),int(r*f),int(b*f)))
        c=c.resize((c.width*2,c.height*2),Image.LANCZOS)
        c.save(f'crops/L{i:02d}{"ab"[j]}.png')
