from PIL import Image
im=Image.open('hires/cpc_1915--12_HU_Mezokovesd_HU_Szomolya_szomolya-44_adr.jpg').convert('RGB')
f=1.734
T={'ret2':(180,355,350,410) ,'udv':(560,1115,800,1185),'first':(25,585,130,650),'val':(240,1115,560,1185),'pm2':(1480,180,1720,300),'bak':(25,1015,360,1065),'end':(620,1160,920,1205)}
for k,(l,t,r,b) in T.items():
    c=im.crop((int(l*f),int(t*f),int(r*f),int(b*f)))
    s=4
    c=c.resize((c.width*s,c.height*s),Image.LANCZOS); c.save(f'crops/u_{k}.png')
