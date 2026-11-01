from PIL import Image
im=Image.open('hires/cpc_1914-04-12_HU__HU_Jasz-Arokszalas_jolanka-52_adr.jpg').convert('RGB')
regs={'r7st':(60,545,620,640),'r7m':(560,560,1000,650),'r9e':(1500,650,1760,790),'r10':(60,790,640,870),'r14':(500,1040,1200,1120),'r14b':(1050,1020,1500,1100),'r16':(560,1180,1160,1250),'r2e':(1480,150,1730,250)}
for k,b in regs.items():
    c=im.crop(b); s=min(5,1640/c.width); c.resize((int(c.width*s),int(c.height*s)),Image.LANCZOS).save(f'tiles/z_{k}.png')
