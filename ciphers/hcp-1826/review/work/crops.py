from PIL import Image, ImageEnhance
im=Image.open('work/hires/pc_hcp_507_adr.JPG').convert('RGB')
b=im.crop((60,250,890,1120)).rotate(90,expand=True)
b=ImageEnhance.Contrast(b).enhance(1.7)
print(b.size)
W,H=b.size
b.save('review/work/crops/side_all.png')
# tiles
n=0
for y in range(0,H,210):
  for x,xe in ((0,470),(420,W)):
    c=b.crop((x,y,xe,min(H,y+240)))
    c.resize((c.width*3,c.height*3),Image.LANCZOS).save(f'review/work/crops/side_{y:03d}_{x:03d}.png')
a=im.crop((55,40,900,390)).rotate(180,expand=True)
a=ImageEnhance.Contrast(a).enhance(1.7)
W,H=a.size;print(W,H)
a.save('review/work/crops/top_all.png')
for y in (0,175):
  for x in (0,290,560):
    c=a.crop((x,y,min(W,x+310),min(H,y+185)))
    c.resize((c.width*4,c.height*4),Image.LANCZOS).save(f'review/work/crops/top_{y:03d}_{x:03d}.png')
