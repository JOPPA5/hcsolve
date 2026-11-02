from PIL import Image
d='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1229/work/crops/'
Image.open(d+'eb.png').rotate(-90,expand=True).save(d+'ebr.png')
