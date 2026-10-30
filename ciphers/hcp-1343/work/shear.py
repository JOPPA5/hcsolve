from PIL import Image
im=Image.open('hires/pc_hcp_24_adr.JPG').convert('L')
s=1785/1400
p=im.crop([int(x*s) for x in (40,290,625,880)])
k=0.04
q=p.transform(p.size,Image.AFFINE,(1,0,0,k,1,-5),Image.BICUBIC,fillcolor=230)
q=q.resize((q.width*3,q.height*3),Image.LANCZOS)
print(q.size)
n=4;H=q.height//n
for i in range(n):
    q.crop((0,max(0,i*H-40),q.width,(i+1)*H+40)).save('crops/S%d.png'%i)
