from PIL import Image, ImageDraw
m=Image.open('msg.png')
s=Image.open('../../../hcp-1363/work/hires/pc_hcp_44_adr.JPG').convert('RGB').rotate(90,expand=True)
W=1785
s=s.crop((340,W-1000,1150,W-150))
# 1366 field; 1363 Cpz; 1366 Mpwfs end; 1363 Mpwfs end
parts=[('1366 upper-right field',m.crop((540,60,760,170))),
       ('1363 line 1 Cpz',s.crop((620,190,740,290))),
       ('1366 Mpwf + ending',m.crop((400,140,680,260))),
       ('1363 Mpwf + ending',s.crop((340,175,640,275)))]
ims=[(t,p.resize((p.size[0]*4,p.size[1]*4),Image.LANCZOS)) for t,p in parts]
w=max(p.size[0] for _,p in ims); h=sum(p.size[1]+24 for _,p in ims)
o=Image.new('RGB',(w,h),'white'); d=ImageDraw.Draw(o); y=0
for t,p in ims:
    d.text((4,y+4),t,fill='black'); y+=24; o.paste(p,(0,y)); y+=p.size[1]
o.save('cmp_cpz_lover.png'); print(o.size)
