from PIL import Image
im=Image.open('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1167/work/hires/cpc_1916-03-11_HU_Mezokovesd_HU_Szomolya_szomolya-22_adr.jpg')
s=3468/1400
z={'l16':(170,600,420,650,3),'l7e':(380,240,500,290,4),'word':(30,745,260,800,4),'pm':(980,120,1300,340,1.5),'date2':(30,800,620,860,2)}
for k,(l,a,r,b,f) in z.items():
    c=im.crop((int(l*s),int(a*s),int(r*s),int(b*s)))
    c.resize((int(c.width*f),int(c.height*f)),Image.LANCZOS).save(f'/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1167/review/work/y_{k}.png')
p=Image.open('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1167/work/hires/cpc_1916-03-11_HU_Mezokovesd_HU_Szomolya_szomolya-22_pic.jpg')
p.resize((900,int(900*p.size[1]/p.size[0]))).save('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1167/review/work/y_pic.png')
