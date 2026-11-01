from PIL import Image, ImageEnhance
src='work/hires/cpc_1912-04-10_HU__HU_Jasz-Arokszalas_jolanka-16_adr.jpg'
im=Image.open(src).convert('RGB')
R={'r14end':(1130,1615,1340,1740,5),'r17end':(1230,1900,1560,2020,4),
 'r15blot':(400,1770,680,1880,5),'r11vela':(770,1330,1030,1410,5),'r06tick':(60,770,500,890,3),
 'r13pale':(600,1560,860,1680,5),'r15h':(600,1770,760,1880,5),'r14h':(520,1660,660,1760,5)}
for k,(a,b,c,d,s) in R.items():
    x=im.crop((a,b,c,d)); x=x.resize((x.width*s,x.height*s),Image.LANCZOS)
    ImageEnhance.Contrast(x).enhance(1.4).save(f'review/work/crops/{k}.png')
# blue channel stretch for faint ink
g=im.crop((770,1330,1030,1410)).split()[1].resize((1300,400),Image.LANCZOS)
ImageEnhance.Contrast(g).enhance(2.5).save('review/work/crops/r11vela_g.png')
