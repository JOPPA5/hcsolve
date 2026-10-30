from PIL import Image
im=Image.open('hires/pc_hcp_24_adr.JPG').convert('L')
s=1785/1400
def c(b,Z=5):
    r=im.crop([int(x*s) for x in b]);return r.resize((r.width*Z,r.height*Z),Image.LANCZOS)
L=[c((48,48,300,88)),c((300,45,560,85)),c((560,45,800,85)),c((780,45,990,85)),
   c((48,80,300,120)),c((300,78,560,118))]
M=[c((560,78,780,118)),c((770,78,950,118)),c((48,108,300,148)),c((300,108,560,150)),c((560,110,800,150)),c((780,108,1000,150))]
N=[c((48,138,300,178)),c((300,138,560,178)),c((560,135,800,175)),c((800,135,1030,175)),c((48,165,300,205)),c((300,165,420,205))]
O=[c((48,195,300,235)),c((300,195,560,235)),c((540,195,800,235)),c((780,195,1020,235)),c((625,215,810,250))]
for n,S in zip('LMNO',[L,M,N,O]):
    H=sum(i.height+6 for i in S);W=max(i.width for i in S)
    m=Image.new('L',(W,H),255);y=0
    for i in S: m.paste(i,(0,y));y+=i.height+6
    m.save('crops/Q%s.png'%n);print(m.size)
