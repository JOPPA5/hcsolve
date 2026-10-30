from PIL import Image, ImageDraw
import sys
im=Image.open('hires/pc_hcp_14_adr.JPG').convert('RGB')
def sheet(items,out,r=(42,40),z=4,cols=5):
    w=(2*r[0])*z+8;h=(2*r[1])*z+24
    rows=(len(items)+cols-1)//cols
    s=Image.new('RGB',(w*cols,h*rows),'white');d=ImageDraw.Draw(s)
    for i,(n,x,y) in enumerate(items):
        c=im.crop((x-r[0],y-r[1],x+r[0],y+r[1])).resize((2*r[0]*z,2*r[1]*z),Image.LANCZOS)
        X=(i%cols)*w;Y=(i//cols)*h
        s.paste(c,(X,Y+18));d.text((X+3,Y+3),n,fill='red')
    s.save(out);print(s.size)
Q=[('Quinito-i1',217,262),('Quinito-i2',287,262),('cinco-i',263,420),('por-p',707,415),('ir-i',607,477),('pas-p',665,477),('seiar-i',150,527),('pro-p',97,587),('pa-p',763,580),('posto-p',337,727),('beijo-i',167,853),('Luiz-i1',503,850),('Luiz-i2',603,853),('Paulo-p',100,970),('Triz-i',572,1027),('amors-i',645,1080)]
Q2=[('i Quinito1',217,262),('i Quinito2',287,262),('i cinco',245,420),('i ir',580,477),('i seiar',180,527),('i beijo',205,853),('i Luiz1',555,850),('i Luiz2',640,853),('i Triz',572,1027),('i amors',645,1085),
('p por',672,415),('p pas',650,477),('p pro',97,590),('p pa',730,580),('p posto',337,727),('p Paulo',135,965)]
ys=[265,330,415,480,540,600,665,725,790,855,915,970,1030,1085]
def P(n,l,x,dy=-5): return (f'{n} L{l}',x,ys[l-1]+dy)
d=[P('d do',1,395),P('d de',4,462),P('d deve',8,655),P('d sau1',11,243),P('d sau2',11,350),P('d da',13,240)]
r=[P('r cor',1,655),P('r hor',3,520),P('r por',3,722),P('r ir',4,600),P('r sei',5,275),P('r pro',6,147),P('r pa-ra',7,90),P('r lagar',7,480),P('r estar',9,580),P('r Laura',11,725),P('r abra',12,770),P('r Triz',13,520),P('r amor',14,572)]
t=[P('t Quin',1,310),P('t ten',4,237),P('t ment',6,645),P('t post',8,445),P('t est',9,485),P('t Luiz',10,700),P('t tua',13,350),P('t Tri',13,485),P('t ate',13,740),P('t amor',14,682)]

sheet([P('N mama',5,525,0),P('N ment',6,490,0),P('P mama2',5,655,0),P('P meu',1,455,0)],'resp/mN.png',r=(50,40),z=4,cols=4)
