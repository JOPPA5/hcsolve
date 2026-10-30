from PIL import Image
im=Image.open('work/hires/pc_hcp_12_adr.JPG')
print(im.size)
# text area left part, rotated 90 CCW
c=im.crop((50,120,800,1090)).rotate(90,expand=True)
c.save('work/crops/msg.png'); print(c.size)
w,h=c.size
n=0
for y0 in range(0,h,210):
  for x0 in (0,w//2-60):
    s=c.crop((x0,y0,min(w,x0+w//2+60),min(h,y0+260))).resize((1590,780) ,Image.LANCZOS)
    s.save(f'work/crops/p{n:02d}.png');n+=1
print(n)
