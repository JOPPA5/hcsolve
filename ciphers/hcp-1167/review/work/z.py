from PIL import Image
im=Image.open('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1167/work/hires/cpc_1916-03-11_HU_Mezokovesd_HU_Szomolya_szomolya-22_adr.jpg')
s=3468/1400
z={'iy':(420,425,540,470,5),'megy':(500,350,640,395,5),'szov':(25,440,160,490,5),'l7':(370,245,500,290,5),'hogy':(180,335,270,375,5),'l9e':(460,325,620,365,5),'cl18':(30,690,670,760,3),'open':(30,710,660,800,3),'date':(30,800,620,860,2),'l18r':(170,680,670,735,3)}
for k,(l,a,r,b,f) in z.items():
    c=im.crop((int(l*s),int(a*s),int(r*s),int(b*s)))
    c.resize((int(c.width*f*0.8),int(c.height*f*0.8)),Image.LANCZOS).save(f'/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1167/review/work/z_{k}.png')
