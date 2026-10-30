from PIL import Image, ImageEnhance
im=Image.open('work/hires/pc_hcp_507_adr.JPG').convert('RGB')
a=im.crop((55,40,900,380)).rotate(180,expand=True)
W,H=a.size;print(W,H)
for y in (0,170):
  for x in (0,280,560):
    c=a.crop((x,y,min(W,x+300),min(H,y+170)))
    c=ImageEnhance.Contrast(c).enhance(1.6)
    c.resize((c.width*4,c.height*4),Image.LANCZOS).save(f'work/crops/t_{y:03d}_{x:03d}.png')
# detail
b=im.crop((60,250,880,1110)).rotate(90,expand=True)
c=b.crop((320,600,560,670)); c.resize((960,280),Image.LANCZOS).save('work/crops/aug.png')
c=b.crop((130,20,300,70)); c.resize((680,200),Image.LANCZOS).save('work/crops/d1.png')
c=b.crop((730,330,860,380)); c.resize((520,200),Image.LANCZOS).save('work/crops/d2.png')
c=b.crop((180,230,330,300)); c.resize((600,280),Image.LANCZOS).save('work/crops/d3.png')
