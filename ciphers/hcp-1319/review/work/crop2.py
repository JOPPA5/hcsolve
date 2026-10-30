from PIL import Image, ImageEnhance
D='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1319/'
im=Image.open(D+'work/hires/cpc_1912-09-_HU__HU_Jasz-Arokszalas_jolanka-107_adr.jpg').convert('RGB')
s=3445/1024
R={'r7word':(120,250,300,292,4),'r7bad':(195,252,250,292,10),'r3ha':(275,95,345,150,7),'r9start':(25,305,130,362,6),'r9m':(165,335,240,362,8),'r9mid':(175,330,245,365,8),'r8d':(310,305,420,350,6),'r3son':(120,100,190,150,6),'r7hol':(300,225,450,290,5),'stamp':(800,70,950,240,5),'pm':(440,50,640,260,4)}
for k,(a,b,c,d,z) in R.items():
    x=im.crop((int(a*s),int(b*s),int(c*s),int(d*s)))
    x=x.resize((x.width*z//1,x.height*z//1),Image.LANCZOS) if z<=4 else x.resize((x.width*z//3,x.height*z//3),Image.LANCZOS)
    x=ImageEnhance.Contrast(x).enhance(1.4); x.save(D+f'review/work/crops/z_{k}.png')
x=im.crop((int(800*s),int(70*s),int(950*s),int(240*s))).rotate(0); x.save(D+'review/work/crops/z_stamp0.png')
