from PIL import Image
im=Image.open('hires/cpc_-02-04_HU__HU_Jasz-Arokszalas_jolanka-93_adr.jpg').convert('RGB')
s=1.72
J={'y1':(1720,175,1850,225,12),'y20':(45,1020,300,1070,7),'y16':(280,815,480,860,8)}
for k,(a,b,c,d,z) in J.items():
    x=im.crop((int(a*s),int(b*s),int(c*s),int(d*s)));x=x.resize((int(x.width*z),int(x.height*z)),Image.BICUBIC);x.save(f'crops/{k}.png')
