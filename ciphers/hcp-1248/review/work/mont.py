from PIL import Image
im=Image.open('../../work/hires/cpc_1913-09-13_HU__HU_Jasz-Arokszalas_jolanka-43_adr.jpg').convert('RGB')
b=[(1400,1385,1490,1460),(90,1405,170,1480),(1520,1385,1600,1460),(1310,780,1380,860)]
c=Image.new('RGB',(1500,420),'white');x=0
for q in b:
    t=im.crop(q);t=t.resize((t.width*4,t.height*4),Image.LANCZOS);c.paste(t,(x,20));x+=t.width+20
c.save('z_r18_compare.png')
im.crop((1380,465,1520,535)).resize((700,350)).save('z_r6_end2.png')
