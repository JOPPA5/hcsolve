from PIL import Image
d='crops2/'
# strip of signs: rows with s: full rows at 1x for search
im=Image.open('hires/cpc_--_HU__HU_Jasz-Arokszalas_jolanka-78_adr.jpg').convert('RGB')
im.crop((60,40,1600,1040)).resize((2000,1299)).save(d+'top.png')
im.crop((60,1020,1600,2110)).resize((2000,1416)).save(d+'bot.png')
