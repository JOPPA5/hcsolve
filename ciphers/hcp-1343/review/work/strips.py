from PIL import Image, ImageOps
im=Image.open('work/hires/pc_hcp_24_adr.JPG').convert('L')
W,H=im.size
# left panel, deslant, split in rows with overlap
s=1785/1400
p=im.crop((int(30*s),int(285*s),int(640*s),int(880*s)))
p=ImageOps.autocontrast(p,cutoff=1)
k=0.04
q=p.transform(p.size,Image.AFFINE,(1,0,0,k,1,-5),Image.BICUBIC,fillcolor=230)
n=8;h=q.height//n
for i in range(n):
    r=q.crop((0,max(0,i*h-25),q.width,(i+1)*h+25)); r=r.resize((r.width*2,r.height*2),Image.LANCZOS)
    # split into left/right half for zoom
    r.crop((0,0,r.width*6//10,r.height)).resize((int(r.width*6/10*1.6),int(r.height*1.6)),Image.LANCZOS).save('review/work/P%dL.png'%i)
    r.crop((r.width*4//10,0,r.width,r.height)).resize((int(r.width*6/10*1.6),int(r.height*1.6)),Image.LANCZOS).save('review/work/P%dR.png'%i)
t=im.crop((int(40*s),int(40*s),int(1040*s),int(260*s)))
t=ImageOps.autocontrast(t,cutoff=1)
t=t.transform(t.size,Image.AFFINE,(1,0,0,0.0,1,0),Image.BICUBIC,fillcolor=230)
n=4;h=t.height//n
for i in range(n):
  for j in range(2):
    r=t.crop((j*t.width*45//100,max(0,i*h-15),j*t.width*45//100+t.width*55//100,(i+1)*h+15)); r=r.resize((r.width*3,r.height*3),Image.LANCZOS); r.save('review/work/T%d%s.png'%(i,'LR'[j]))
im.resize((1400,921)).save('review/work/whole.png')
