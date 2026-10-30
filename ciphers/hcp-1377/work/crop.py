from PIL import Image
im=Image.open('hires/pc_hcp_58_adr.JPG').convert('RGB')
r=im.crop((150,150,860,1140)).rotate(90,expand=True)
print(r.size); r.save('reading.png')
W,H=r.size
r.resize((W*2,H*2),Image.LANCZOS).save('crops/all2x.png')
# split left/right
n=0
for x0 in range(0,W,300):
    c=r.crop((x0,0,min(W,x0+360),H)).resize((min(360,W-x0)*3,H*3),Image.LANCZOS)
    c.save(f'crops/col{n}.png'); n+=1
print(n)
