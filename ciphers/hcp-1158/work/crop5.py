from PIL import Image
im=Image.open('hires/cpc_1915--12_HU_Mezokovesd_HU_Szomolya_szomolya-44_adr.jpg').convert('RGB')
f=1.734
for k,(l,t,r,b) in {'hu':(255,1160,345,1205),'udv':(335,1120,400,1170),'ent':(780,720,880,790)}.items():
    c=im.crop((int(l*f),int(t*f),int(r*f),int(b*f))); c=c.resize((c.width*6,c.height*6),Image.LANCZOS); c.save(f'crops/w_{k}.png')
