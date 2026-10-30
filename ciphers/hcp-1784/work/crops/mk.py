from PIL import Image, ImageOps
im=Image.open('hires/pc_hcp_465_adr.JPG').convert('RGB')
c=im.crop((40,280,900,1120)).rotate(90,expand=True)
c.save('crops/rot.png'); print(c.size)
# split in thirds, top half then bottom halves, 3x
w,h=c.size
n=0
for y0,y1 in [(0,250),(220,470),(440,700),(650,840)]:
  for x0,x1 in [(0,460),(400,860)]:
    d=c.crop((x0,y0,x1,y1)); d=d.resize((d.width*3,d.height*3),Image.LANCZOS); d.save(f'crops/r{n}.png'); n+=1
