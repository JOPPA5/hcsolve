from PIL import Image, ImageOps
d='ciphers/hcp-1340/'
a=Image.open(d+'work/hires/pc_hcp_21_adr.JPG'); p=Image.open(d+'work/hires/pc_hcp_21_pic.JPG')
print(a.size)
s=1785/1024
# address rows: split in left/right half
rows=[(150,190),(180,225),(215,255),(245,285),(275,315),(305,345),(340,375),(370,410),(405,440),(435,470),(475,515),(510,550),(545,580),(580,615)]
for i,(y0,y1) in enumerate(rows):
    for j,(x0,x1) in enumerate([(30,280),(260,520)]):
        c=a.crop((int(x0*s),int(y0*s),int(x1*s),int(y1*s)))
        c=c.resize((c.width*4,c.height*4),Image.LANCZOS)
        c.save(d+f'review/work/adr_r{i:02d}_{j}.png')
for n,box in {'top1':(50,20,300,60),'top2':(290,20,540,60),'top3':(530,20,780,60),'top4':(770,20,985,90),
 'bot1':(60,465,300,510),'bot2':(290,465,540,510),'bot3':(530,465,790,510),'bot4':(780,465,985,510)}.items():
    c=p.crop(tuple(int(v*s) for v in box)); c=c.resize((c.width*4,c.height*4),Image.LANCZOS); c.save(d+f'review/work/pic_{n}.png')
m=p.crop(tuple(int(v*s) for v in (930,130,985,480))).rotate(90,expand=True)
print(m.size)
for k in range(2):
    c=m.crop((k*m.width//2-(30 if k else 0),0,(k+1)*m.width//2+ (0),m.height)); c=c.resize((c.width*4,c.height*4),Image.LANCZOS); c.save(d+f'review/work/pic_marg{k}.png')
