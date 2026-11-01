from PIL import Image, ImageEnhance
src='work/hires/cpc_1912-04-10_HU__HU_Jasz-Arokszalas_jolanka-16_adr.jpg'
im=Image.open(src).convert('RGB')
R={'stamp':(2680,210,3200,760,3),'a1':(1600,1440,2400,1560,2),'r5e':(780,620,1450,760,2),'r7e':(780,890,1450,1020,2),'pm':(1600,180,2450,700,2)}
for k,(a,b,c,d,s) in R.items():
    x=im.crop((a,b,c,d)); x=x.resize((x.width*s,x.height*s),Image.LANCZOS)
    ImageEnhance.Contrast(x).enhance(1.4).save(f'review/work/crops/{k}.png')
