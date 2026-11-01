from PIL import Image
im=Image.open('hires/cpc_--_HU__HU_Jasz-Arokszalas_jolanka-68_adr.jpg').convert('RGB')
Z={'w1':(620,790,1000,890),'w2':(1180,1920,1560,2020),'w3':(1150,240,1400,340),'w4':(40,1940,300,2050)}
ims=[]
for k,b in Z.items():
    c=im.crop(b);ims.append(c.resize((c.width*4,c.height*4),Image.LANCZOS))
o=Image.new('RGB',(1600,sum(i.height+8 for i in ims)),'white');y=0
for i in ims:o.paste(i,(0,y));y+=i.height+8
o.save('crops/W.png')
