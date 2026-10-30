from PIL import Image,ImageOps
im=Image.open('work/hires/pc_hcp_29_adr.JPG').convert('L')
print(im.size)
# message band on unrotated hires: scale factor from adr_small (1488 wide)
s=1785/1488
box=(370*s,270*s,700*s,920*s)
c=im.crop(tuple(int(x) for x in box)).rotate(-90,expand=True)
print(c.size)
c.save('review/work/try.png')
c2=im.crop(tuple(int(x) for x in box)).rotate(90,expand=True); c2.save('review/work/try2.png')
