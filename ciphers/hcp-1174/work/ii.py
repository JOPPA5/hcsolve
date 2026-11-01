from PIL import Image
im=Image.open('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1174/work/hires/cpc_1916-02-15_HU_Mezokovesd_HU_Szomolya_szomolya-18_adr.jpg').convert('RGB')
print(im.size)
c=im.crop((0,880,1650,1950)); c.resize((c.width*2//3*1,c.height*2//3)).save('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1174/work/crops/ii_over.png')
