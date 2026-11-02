from PIL import Image
im=Image.open('hires/cpc_1916-03-11_HU_Mezokovesd_HU_Szomolya_szomolya-22_adr.jpg').convert('RGB')
s=3468/1800
C=[55,122,178,232,268,305,342,400,445,492,540,590,640,692,745,800,850,905]
for i,c in enumerate(C,1):
    y0=int((c-38)*s);y1=int((c+38)*s)
    for j,(a,b) in enumerate([(50,460),(420,870)]):
        cr=im.crop((int(a*s),y0,int(b*s),y1))
        cr=cr.resize((cr.width*2,cr.height*2),Image.LANCZOS)
        cr.save(f'crops/L{i:02d}{"ab"[j]}.png')
