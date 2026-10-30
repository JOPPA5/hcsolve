from PIL import Image, ImageEnhance
im=Image.open('work/hires/pc_hcp_507_adr.JPG').convert('RGB')
b=im.crop((60,250,880,1110)).rotate(90,expand=True)  # size 860x820
print(b.size)
b.save('work/crops/sidefull.png')
W,H=b.size
# left and right halves in strips of 170 px height
n=0
for y in range(0,H-100,150):
  for x,w in ((0,450),(410,450)):
    c=b.crop((x,y,x+w,min(H,y+190)))
    c=ImageEnhance.Contrast(c).enhance(1.5)
    c.resize((c.width*3,c.height*3),Image.LANCZOS).save(f'work/crops/s_{y:03d}_{x:03d}.png')
