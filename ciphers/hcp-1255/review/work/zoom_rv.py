from PIL import Image
d='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1255/'
im=Image.open(d+'work/hires/cpc_1912-03-11_HU__HU_Jasz-Arokszalas_jolanka-08_adr.jpg').convert('RGB')
Z={'r2':(1040,150,1240,250),'r4':(540,350,860,440),'r5':(200,430,500,550),'r7':(740,630,900,740),'r8':(1230,700,1500,790),
'r10':(1040,860,1480,970),'r11':(90,975,640,1075),'r12':(1020,1040,1500,1130),'r18':(1170,1565,1560,1685)}
for k,b in Z.items():
    c=im.crop(b); f=min(6,1900//c.width); c.resize((c.width*f,c.height*f),Image.LANCZOS).save(d+f'review/work/z_{k}.png')
# montage for r5/r7/r4/r2
