from PIL import Image
im=Image.open('hires/cpc_1915--12_HU_Mezokovesd_HU_Szomolya_szomolya-44_adr.jpg').convert('RGB')
f=1.734
T={'reten':(180,325,340,405),'virag':(130,760,350,825),'blot':(440,480,600,560),'sziv':(170,520,420,590),'csok':(180,1150,420,1215),'be':(340,650,520,730),'meg':(30,650,200,730),'open':(30,70,900,255),'ket':(30,890,300,1000),'ertek':(30,1000,330,1060),'gond':(620,1020,780,1100)}
for k,(l,t,r,b) in T.items():
    c=im.crop((int(l*f),int(t*f),int(r*f),int(b*f)))
    s=2 if k=='open' else 5 if r-l<200 else 4
    c=c.resize((c.width*s,c.height*s),Image.LANCZOS); c.save(f'crops/t_{k}.png')
