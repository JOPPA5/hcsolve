from PIL import Image, ImageEnhance
im=Image.open('hires/cpc_1914-01-10_HU__HU_Jasz-Arokszalas_jolanka-47_adr.jpg').convert('RGB')
S=1.72
# row baselines (display coords): y at x=60 and x=840
rows={4:(185,160),5:(240,190),6:(288,235),7:(325,285),8:(365,335),9:(408,380),10:(452,420),11:(510,470)}
def strip(n,x0,x1,h=26,s=4.6):
    a,b=rows[n]
    W=int((x1-x0)*S); H=int(2*h*S)
    sl=(b-a)/780
    y0=a+sl*(x0-60)
    q=im.transform((W,H),Image.AFFINE,(1,0,x0*S,sl,1,(y0-h)*S),Image.BICUBIC)
    q=q.resize((int(W*s/1.0*0.6),int(H*s*0.6)),Image.BICUBIC)
    return ImageEnhance.Contrast(q).enhance(1.6)
def sheet(name,rs,x0,x1):
    st=[strip(r,x0,x1) for r in rs]
    W=st[0].width; H=sum(i.height+10 for i in st)
    o=Image.new('RGB',(W,H),'white'); y=0
    for i in st: o.paste(i,(0,y)); y+=i.height+10
    o.save('crops/%s.png'%name)
for a,b,tag in ((270,570,'a'),(550,850,'b')):
    sheet('s45'+tag,(4,5),a,b); sheet('s67'+tag,(6,7),a,b); sheet('s89'+tag,(8,9),a,b); sheet('s1011'+tag,(10,11),a,b)
