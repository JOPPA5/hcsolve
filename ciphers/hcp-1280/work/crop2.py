from PIL import Image, ImageOps
im=Image.open('hires/cpc_1912-03-13_HU__HU_Jasz-Arokszalas_jolanka-09_adr.jpg').convert('RGB')
S=3445/1024
def c(n,l,t,r,b,k=5):
    x=im.crop((int(l*S),int(t*S),int(r*S),int(b*S)));x=x.resize((x.width*k,x.height*k),Image.BICUBIC);x.save(f'crops/z_{n}.png')
c('r2blot',55,55,130,110,4)
c('r3ly',165,95,250,155,4)
c('r6blot',235,175,330,265,4)
c('r7ly',165,255,275,310,4)
c('r8a',15,285,235,340,3)
c('r8b',230,285,455,340,3)
c('r10end',380,360,520,420,3)
c('r11end',350,395,470,445,4)
c('r13blot',170,480,260,540,4)
c('r15gy',100,570,190,620,4)
# stamp red channel: suppress green print, emphasize red ink
x=im.crop((int(830*S),int(50*S),int(970*S),int(200*S)));r,g,b=x.split()
g=ImageOps.autocontrast(g);g=g.resize((g.width*2,g.height*2),Image.BICUBIC);g.save('crops/z_stampG.png')
c('toprt',880,10,985,60,3)
c('addr1',455,130,830,210,2)
c('addr2',470,235,900,320,2)
c('addr3',530,365,920,520,2)
