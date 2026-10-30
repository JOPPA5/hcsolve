from PIL import Image
W='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1289/work/'
im=Image.open(W+'hires/cpc_--22_HU__HU_Jasz-Arokszalas_jolanka-87_adr.jpg')
S=1.72
def crop(name,x0,y0,x1,y1,z):
    c=im.crop(tuple(int(v*S) for v in (x0,y0,x1,y1)))
    c.resize((int(c.width*z),int(c.height*z)),Image.LANCZOS).save(W+'crops2/'+name+'.png')
for i,y in enumerate(range(40,1000,130)):
    crop(f'A{i:02d}',35,y,950,y+150,1.25)
for i,y in enumerate([1040,1140]):
    crop(f'B{i}L',35,y,700,y+90,1.7); crop(f'B{i}M',680,y,1320,y+90,1.7); crop(f'B{i}R',1300,y,1920,y+90,1.7)
crop('stamp',1550,140,1810,420,3.5)
