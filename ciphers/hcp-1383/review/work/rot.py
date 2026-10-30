from PIL import Image
im=Image.open('ciphers/hcp-1383/work/hires/pc_hcp_64_adr.JPG');print(im.size)
m=im.crop((130,70,1000,1120)).rotate(90,expand=True);print(m.size);m.save('ciphers/hcp-1383/review/work/msg.png')
W,H=m.size
for i in range(3):
  x0=i*W//3-40 if i else 0; x1=min(W,(i+1)*W//3+40)
  m.crop((x0,0,x1,H)).resize(((x1-x0)*2,H*2),Image.LANCZOS).save(f'ciphers/hcp-1383/review/work/seg{i}.png')
