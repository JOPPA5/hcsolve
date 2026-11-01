from PIL import Image
im=Image.open('hires/cpc_1912-01-17_HU__HU_Jasz-Arokszalas_jolanka-03_adr.jpg').convert('RGB')
s=1.72
B={'z6end':(690,450,900,530,6),'z8mid':(340,585,560,655,6),'addr':(1150,1090,1650,1230,3),'pm':(1090,50,1480,400,2)}
for k,(a,b,c,d,z) in B.items():
    x=im.crop((int(a*s),int(b*s),int(c*s),int(d*s))); x.resize((x.width*z//2,x.height*z//2),Image.LANCZOS).save(f'crops/{k}.png')
