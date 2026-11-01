from PIL import Image, ImageOps
im=Image.open('hires/cpc_1912--27_HU__HU_Jasz-Arokszalas_jolanka-103_adr.jpg').convert('RGB')
f=1.72
B={'b16':(42,1105,180,1165,8),'b15':(42,1050,160,1115,8),'b16f':(190,1105,340,1170,6),'c15e':(620,1045,885,1110,3),'st2':(1700,120,1800,250,6)}
for k,(l,t,r,b,s) in B.items():
    c=im.crop((int(l*f),int(t*f),int(r*f),int(b*f)));c=c.resize((c.width*s,c.height*s),Image.BICUBIC)
    # contrast: use green channel
    g=c.split()[1]; ImageOps.autocontrast(g).save(f'crops/{k}.png')
