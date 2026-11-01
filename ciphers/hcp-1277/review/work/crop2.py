from PIL import Image, ImageEnhance
im=Image.open('work/hires/cpc_1914-03-01_HU__HU_Jasz-Arokszalas_jolanka-48_adr.jpg').convert('RGB')
ys=[50,330,610,890,1170,1450,1730]
for i,y in enumerate(ys):
  for j,(a,b) in enumerate([(50,830),(790,1570)]):
    c=im.crop((a,y,b,y+330 if i<6 else 2110)); c=c.resize((c.width*2,c.height*2),Image.LANCZOS)
    ImageEnhance.Contrast(c).enhance(1.5).save(f'review/work/g{i}{j}.png')
c=im.crop((1600,50,2800,520)); c=c.resize((c.width*1,c.height*1)).transpose(Image.ROTATE_180).save('review/work/pm180.png')
im.crop((1600,50,2800,520)).save('review/work/pm.png')
c=im.crop((2650,180,3200,800)); c=c.resize((c.width*2,c.height*2),Image.LANCZOS); c.save('review/work/stamp.png'); 
b=c.split()[2]; ImageEnhance.Contrast(b).enhance(2.5).save('review/work/stampb.png')
c=im.crop((400,1900,2000,2110)); c.save('review/work/bottom.png'); c.transpose(Image.ROTATE_180).save('review/work/bottom180.png')
