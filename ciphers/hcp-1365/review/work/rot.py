from PIL import Image
im=Image.open('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1365/work/hires/pc_hcp_46_adr.JPG');print(im.size)
r=im.rotate(90,expand=True);print(r.size)
r.save('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1365/review/work/rot.png')
t=r.copy();t.thumbnail((1400,1400));t.save('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1365/review/work/rot_small.png')
