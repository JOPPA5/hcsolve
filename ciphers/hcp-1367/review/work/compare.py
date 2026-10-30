from PIL import Image, ImageDraw
r=Image.open('work/hires/pc_hcp_48_adr.JPG').convert('RGB').rotate(90,expand=True)
items=[('Nz (r1)',(445,1030,560,1115)),('group capital (r5)',(840,1420,960,1500)),('group 2nd sign (r5)',(960,1425,1055,1495)),('final h Mpwjoh',(960,1050,1050,1125)),('M of Mpwjoh',(760,1040,850,1120))]
W=sum((b[2]-b[0])*5+10 for _,b in items); H=460
o=Image.new('RGB',(W,H),'white'); d=ImageDraw.Draw(o); x=0
for n,b in items:
    c=r.crop(b); c=c.resize((c.width*5,c.height*5),Image.BICUBIC); o.paste(c,(x,20)); d.text((x+2,2),n,fill='red'); x+=c.width+10
o.save('review/work/compare_signs.png'); print(o.size)
