from PIL import Image
im=Image.open('work/hires/pc_hcp_65_adr.JPG')
print(im.size)
r=im.rotate(90,expand=True); print(r.size)
r.save('review/work/rot_full.png')
W,H=r.size
s=r.copy(); s.thumbnail((1000,1400)); s.save('review/work/rot_small.jpg')
