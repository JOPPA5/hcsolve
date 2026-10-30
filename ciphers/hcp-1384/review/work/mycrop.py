from PIL import Image
im=Image.open('ciphers/hcp-1384/work/hires/pc_hcp_65_adr.JPG');print(im.size)
print(Image.open('ciphers/hcp-1384/work/reading.jpg').size)
im.thumbnail((1400,1400));im.save('ciphers/hcp-1384/review/work/adr_small.jpg')
