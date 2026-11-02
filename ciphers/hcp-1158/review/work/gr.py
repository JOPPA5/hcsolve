from PIL import Image, ImageEnhance
im=Image.open('work/hires/cpc_1915--12_HU_Mezokovesd_HU_Szomolya_szomolya-44_adr.jpg').convert('RGB')
f=2.1675
G=[(10,70),(195,365),(380,555),(555,735),(730,890),(880,975)]
for i,(t,b) in enumerate(G):
    for j,(l,r) in enumerate([(30,390),(360,740)]):
        c=im.crop((int(l*f),int(t*f),int(r*f),int(b*f)))
        s=2.4
        c=c.resize((int(c.width*s),int(c.height*s)),Image.LANCZOS)
        c=ImageEnhance.Contrast(c).enhance(1.5)
        c.save(f'review/work/g{i}_{j}.png'); print(i,j,c.size)
