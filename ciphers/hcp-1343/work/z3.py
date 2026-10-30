from PIL import Image
im=Image.open('hires/pc_hcp_24_adr.JPG').convert('L')
s=1785/1400
p=im.crop([int(x*s) for x in (40,290,625,880)])
q=p.transform(p.size,Image.AFFINE,(1,0,0,0.04,1,-5),Image.BICUBIC,fillcolor=230)
print(q.size)
# q px; 3x image S offsets: S0 top 0, S1 ~ 525, S2 ~1090, S3 ~1655  ; disp*1.1175
def b(sec,x0,x1,y0,y1,Z=4):
    k=1.1175/3; off=[0,525,1090,1655][sec]
    c=q.crop((int(x0*k),int((y0*1.1175+off)/3),int(x1*k),int((y1*1.1175+off)/3)))
    return c.resize((c.width*Z,c.height*Z),Image.LANCZOS)
L=[b(2,1100,1990,120,220),b(2,20,1000,370,470),b(2,1250,1990,400,500),b(3,20,800,0,90),b(3,700,1900,0,110),b(3,1000,1900,250,330)]
H=sum(i.height+6 for i in L);W=max(i.width for i in L)
m=Image.new('L',(W,H),255);y=0
for i in L: m.paste(i,(0,y));y+=i.height+6
m.save('crops/R.png');print(m.size)
r=im.crop([int(x*s) for x in (615,285,650,580)]).rotate(-90,expand=True);r.resize((r.width*5,r.height*5),Image.LANCZOS).save('crops/s1.png')
r=im.crop([int(x*s) for x in (615,575,650,870)]).rotate(-90,expand=True);r.resize((r.width*5,r.height*5),Image.LANCZOS).save('crops/s2.png')
