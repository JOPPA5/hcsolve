from PIL import Image, ImageOps
im=Image.open('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1275/work/hires/cpc_1913-08-13_HU__HU_Jasz-Arokszalas_jolanka-40_adr.jpg').convert('RGB')
O='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1275/review/work/crops/'
for n,b in [('rS1',(2720,300,3030,400)),('rS6',(2760,590,3060,740))]:
    r=im.crop(b).split()[0]; r=ImageOps.autocontrast(r,cutoff=1).resize(((b[2]-b[0])*5,(b[3]-b[1])*5),Image.LANCZOS); r.save(O+n+'.png')
