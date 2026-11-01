from PIL import Image
d='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1255/'
im=Image.open(d+'work/hires/cpc_1912-03-11_HU__HU_Jasz-Arokszalas_jolanka-08_adr.jpg').convert('RGB')
Z={'r15':(90,1340,620,1440),'r3':(460,250,700,350),'r16':(620,1420,900,1520),'r12s':(90,1060,380,1170),'stampd':(1600,120,2300,960)}
for k,b in Z.items():
    c=im.crop(b); f=max(1,min(6,1900//c.width)); c.resize((c.width*f,c.height*f),Image.LANCZOS).save(d+f'review/work/z_{k}.png')
