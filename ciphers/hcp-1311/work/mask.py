from PIL import Image
im=Image.open('hires/cpc_--_HU__HU_Jasz-Arokszalas_jolanka-81_adr.jpg').convert('RGB')
box=(2680,340,3220,880)
r=im.crop(box); px=r.load(); 
o=Image.new('L',r.size,255); q=o.load()
for x in range(r.width):
  for y in range(r.height):
    R,G,B=px[x,y]
    d=G-R
    q[x,y]=max(0,min(255,255-(d+10)*9)) if R<175 else 255
o.resize((1620,1620),Image.LANCZOS).save('crops/st_mask.png')
