from PIL import Image
im=Image.open('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1167/work/hires/cpc_1916-03-11_HU_Mezokovesd_HU_Szomolya_szomolya-22_adr.jpg')
print(im.size)
im.resize((1400,int(1400*im.size[1]/im.size[0]))).save('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1167/review/work/overview.png')
