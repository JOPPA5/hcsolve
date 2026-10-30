from PIL import Image
im=Image.open('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1377/work/hires/pc_hcp_58_adr.JPG')
print(im.size)
im.thumbnail((1600,1600)); im.save('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1377/review/work/adr_small.png')
