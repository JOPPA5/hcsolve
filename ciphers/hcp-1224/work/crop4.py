from PIL import Image
im=Image.open('hires/cpc_1912-10-12_HU__HU_Jasz-Arokszalas_jolanka-32_adr.jpg').convert('RGB')
B={'b12':(620,980,1000,1090),'b21':(1000,1660,1500,1780),'b26':(2950,1990,3200,2090),'b2':(860,150,1160,230),'b4':(330,310,640,400),'b24':(780,1860,1120,1970),'b1':(1400,70,1660,170)}
ims=[]
for k,b in B.items():
    r=im.crop(b); ims.append(r.resize((r.width*3,r.height*3),Image.LANCZOS))
W=max(i.width for i in ims);H=sum(i.height+10 for i in ims)
o=Image.new('RGB',(W,H),'white');y=0
for i in ims: o.paste(i,(0,y)); y+=i.height+10
o.save('crops/blots.png');print(o.size)
