from PIL import Image
im=Image.open('hires/cpc_1915--12_HU_Mezokovesd_HU_Szomolya_szomolya-44_adr.jpg').convert('RGB')
f=1.734
for k,(l,t,r,b) in {'reten':(370,325,660,395),'hu':(320,1150,470,1200)}.items():
    c=im.crop((int(l*f),int(t*f),int(r*f),int(b*f))); c=c.resize((c.width*4,c.height*4),Image.LANCZOS); c.save(f'crops/v_{k}.png')
