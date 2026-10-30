from PIL import Image
im=Image.open('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1828/work/hires/pc_hcp_509_adr.JPG').convert('RGB')
g=im.convert('L')
X,Y=208,1031
for yy in range(Y-22,Y+23,2):
    print(f'{yy:5d}',' '.join(f'{g.getpixel((xx,yy))//10:2d}' for xx in range(X-20,X+21,2)))
print('RGB samples centre row')
for yy in (Y-4,Y,Y+4):
    print([im.getpixel((xx,yy)) for xx in range(X-6,X+7,4)])
