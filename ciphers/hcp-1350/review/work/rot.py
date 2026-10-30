from PIL import Image
im=Image.open('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1350/work/hires/pc_hcp_31_adr.JPG');print(im.size)
r=im.rotate(90,expand=True);print(r.size)
r2=r.copy();r2.thumbnail((1500,1500));r2.save('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1350/review/work/rot_small.jpg')
