from PIL import Image, ImageEnhance
im=Image.open('work/hires/cpc_--_HU__HU_Jasz-Arokszalas_jolanka-81_adr.jpg').convert('RGB')
b=[(2790,600,2930,740,'S6-1'),(1355,2000,1495,2140,'r27-y'),(520,120,660,260,'r2 gy'),(1090,1510,1230,1650,'row20')]
c=Image.new('RGB',(1600,400),'white')
for i,(x0,y0,x1,y1,n) in enumerate(b):
    r=im.crop((x0,y0,x1,y1)).resize((400,400),Image.LANCZOS); c.paste(ImageEnhance.Contrast(r).enhance(1.7),(i*400,0))
c.save('review/work/crops/cmp_y.png')
