from PIL import Image,ImageOps,ImageEnhance
im=Image.open('work/hires/pc_hcp_30_adr.JPG').convert('RGB')
m=im.crop((110,420,920,1120)).rotate(90,expand=True)
m.save('work/reading.jpg',quality=92); print(m.size)
g=ImageEnhance.Contrast(ImageOps.grayscale(m)).enhance(1.8)
w,h=g.size
g=g.resize((w*2,h*2),Image.LANCZOS); g.save('work/crops/all2x.jpg',quality=90)
# strips
n=4
for i in range(n):
    y0=int(i*h/n)-15; y1=int((i+1)*h/n)+15
    c=g.crop((0,max(0,y0*2),w*2,min(h,y1)*2)); 
    a=c.crop((0,0,c.width//2+30,c.height)); b=c.crop((c.width//2-30,0,c.width,c.height))
    a.resize((a.width*2//1,a.height*2)).save(f'work/crops/s{i}a.jpg',quality=88); b.resize((b.width*2,b.height*2)).save(f'work/crops/s{i}b.jpg',quality=88)
