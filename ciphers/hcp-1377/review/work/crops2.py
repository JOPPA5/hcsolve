from PIL import Image
r=Image.open('reading.png')
W,H=r.size
n=0
for x0 in range(0,W,230):
    c=r.crop((x0,0,min(W,x0+280),H)).resize((min(280,W-x0)*3,H*3),Image.LANCZOS)
    c.save(f'seg{n}.png'); n+=1
print(n)
im=Image.open('../../work/hires/pc_hcp_58_adr.JPG').convert('RGB')
c=im.crop((1340,80,1660,450)).resize((960,1110),Image.LANCZOS); c.save('stamp.png')
