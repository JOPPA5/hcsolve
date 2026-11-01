from PIL import Image, ImageEnhance
src='work/hires/cpc_1912-04-10_HU__HU_Jasz-Arokszalas_jolanka-16_adr.jpg'
im=Image.open(src).convert('RGB')
ys=[90,420,720,1020,1320,1620,1760]
n=0
for i in range(6):
    y0=ys[i]; y1=min(ys[i]+ 400,2090)
    for side,(x0,x1) in enumerate([(60,860),(780,1600)]):
        c=im.crop((x0,y0,x1,y1)); c=c.resize((c.width*2,c.height*2),Image.LANCZOS)
        c=ImageEnhance.Contrast(c).enhance(1.5)
        c.save(f'review/work/crops/t{i}{"LR"[side]}.png')
