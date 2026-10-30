from PIL import Image, ImageOps
i=Image.open('work/hires/pc_hcp_56_adr.JPG').convert('L')
r=i.crop((90,50,840,1110)).rotate(90,expand=True)
r=ImageOps.autocontrast(r,cutoff=1)
print(r.size)
r.save('review/work/rot.png')
W,H=r.size
# overview
r.resize((W*2,H*2),Image.LANCZOS).crop((0,0,W*2,H*2)).save('review/work/rot2x.png')
for k in range(3):
    h=H//3
    c=r.crop((0,k*h-20 if k else 0,W,(k+1)*h+20))
    c.resize((c.width*2,c.height*2),Image.LANCZOS).save(f'review/work/band{k}.png')
