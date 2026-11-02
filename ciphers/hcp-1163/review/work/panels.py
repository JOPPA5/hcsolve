from PIL import Image
P='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1163/'
im=Image.open(P+'work/hires/cpc_1916-02-26_HU_Mezokovesd_HU_Szomolya_szomolya-20_adr.jpg').convert('RGB')
ys=[(50,540),(520,1000),(980,1300),(1270,1800),(1760,2170)]
for i,(a,b) in enumerate(ys):
    for j,(x,y) in enumerate([(30,800),(780,1600)]):
        c=im.crop((x,a,y,b)); c=c.resize((c.width*2,c.height*2),Image.LANCZOS); c.save(P+f'review/work/crops/p{i}{j}.png')
