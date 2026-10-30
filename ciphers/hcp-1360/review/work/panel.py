from PIL import Image, ImageDraw
R='/Users/tomaspavuk/Desktop/hcsolve/ciphers/'
s=1175/1053
me=Image.open('rot.png').convert('RGB').crop(tuple(int(v*s) for v in (660,850,890,925)))
items=[('hcp-1360 (this card, native crop x6) - Mpwf+h. per solver, read here as Mpwjoh',me.resize((me.width*6,me.height*6),Image.LANCZOS)),
('hcp-1361 accepted Mpwjoh',Image.open(R+'hcp-1361/work/crops/l2b.png').convert('RGB').crop((0,20,1030,370))),
('hcp-1367 accepted Mpwjoh',Image.open(R+'hcp-1367/work/crops/l1b.png').convert('RGB').crop((0,20,1000,420))),
('hcp-1363 Mpwfs per solver',Image.open(R+'hcp-1363/work/crops/w2.jpg').convert('RGB')),
]
W=1300;rows=[]
for t,i in items:
    z=min(W/i.width,1.0) if i.width>W else 1
    i=i.resize((int(i.width*z),int(i.height*z)))
    rows.append((t,i))
H=sum(i.height+26 for _,i in rows)
o=Image.new('RGB',(W,H),'white');d=ImageDraw.Draw(o);y=0
for t,i in rows:
    d.text((6,y+6),t,fill='black');y+=26;o.paste(i,(0,y));y+=i.height
o.save('cmp_mpwjoh.png');print(o.size)
