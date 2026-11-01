from PIL import Image, ImageEnhance, ImageDraw
im=Image.open('work/hires/cpc_1914-03-01_HU__HU_Jasz-Arokszalas_jolanka-48_adr.jpg').convert('RGB')
W=Image.new('RGB',(1530,212*3),'white')
L=[('r03',3,23,26,-60),('r06',6,22,25,-65),('r08',8,21,22,-65),('r19',19,4,20,50),('r20',20,2,20,30),('r16',16,8,20,0)]
for j,(n,r,i,l,d) in enumerate(L):
    y=165+70.4*(r-2)+d; x=60+(i+.5)*(1500/l)
    c=im.crop((int(x-190),int(y-52),int(x+190),int(y+52))).resize((760,208),Image.LANCZOS)
    c=ImageEnhance.Contrast(c).enhance(1.4); ImageDraw.Draw(c).text((4,2),n,fill=(255,0,0))
    W.paste(c,((j%2)*770,(j//2)*212))
W.save('work/crops2/gy2.png')
