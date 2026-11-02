from PIL import Image,ImageOps
src='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1229/work/hires/cpc_1914-01-07_HU__HU_Jasz-Arokszalas_jolanka-46_adr.jpg'
im=Image.open(src).convert('RGB')
n=0
for j,y in enumerate(range(55,2130,140)):
  for k,x in enumerate((60,540,1020)):
    c=im.crop((x,y,x+520,y+175))
    c=ImageOps.autocontrast(c.convert('L'),cutoff=0.5).resize((1560,525),Image.LANCZOS)
    c.save(f'crops/z{j:02d}{"abc"[k]}.png');n+=1
print(n)
