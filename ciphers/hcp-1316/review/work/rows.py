from PIL import Image
im=Image.open('work/hires/cpc_1912-06-30_HU__HU_Jasz-Arokszalas_jolanka-27_adr.jpg').convert('RGB')
ys=[43,72,100,130,158,193,222,250,283,310,340,375,408,438,472,510,540,570,600]
S=3.364
for i,y in enumerate(ys,1):
    Y=int(y*S); h=70
    x0,x1=70,1900
    if i in(1,2,3,4): pass
    a=im.crop((x0,Y-h,x0+930,Y+h)); b=im.crop((x1-930,Y-h,x1,Y+h))
    W=930*2;H=h*2*2
    o=Image.new('RGB',(W,H*2+8),'white')
    o.paste(a.resize((W,H),Image.LANCZOS),(0,0)); o.paste(b.resize((W,H),Image.LANCZOS),(0,H+8))
    o.save(f'review/work/crops/row{i:02d}.png')
