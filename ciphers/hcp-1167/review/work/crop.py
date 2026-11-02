from PIL import Image
im=Image.open('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1167/work/hires/cpc_1916-03-11_HU_Mezokovesd_HU_Szomolya_szomolya-22_adr.jpg')
s=3468/1400
# bands in overview coords
bands=[(20,185),(170,330),(290,450),(400,560),(520,690),(640,790),(700,880)]
for i,(a,b) in enumerate(bands):
    for j,(l,r) in enumerate([(20,350),(320,680)]):
        c=im.crop((int(l*s),int(a*s),int(r*s),int(b*s)))
        c=c.resize((int(c.width*1.5),int(c.height*1.5)),Image.LANCZOS)
        c.save(f'/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1167/review/work/b{i}{"ab"[j]}.png')
