from PIL import Image
im=Image.open('hires/cpc_--_HU__HU_Jasz-Arokszalas_jolanka-68_adr.jpg').convert('RGB')
Z={'z1':(50,1100,450,1230),'z2':(1100,370,1620,480),'z3':(950,780,1350,880),'z4':(1250,780,1620,880),'z5':(800,250,1100,350),'z6':(1250,540,1640,650)}
for k,b in Z.items():
    c=im.crop(b);s=3
    c.resize((c.width*s,c.height*s),Image.LANCZOS).save(f'crops/{k}.png')
ims=[Image.open(f'crops/z{i}.png') for i in range(1,7)]
o=Image.new('RGB',(1600,sum(i.height+8 for i in ims)),'white');y=0
for i in ims:o.paste(i,(0,y));y+=i.height+8
o.save('crops/Z.png')
