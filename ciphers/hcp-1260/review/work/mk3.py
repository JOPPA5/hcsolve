from PIL import Image
im=Image.open('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1260/work/hires/cpc_--25_HU__HU_Jasz-Arokszalas_jolanka-90_adr.jpg')
r=im.crop((430,230,640,330)); r.resize((r.width*5,r.height*5)).save('crops/r3j.png')
r=im.crop((1500,1600,2000,2000)) 
p=Image.open('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1260/work/hires/cpc_--25_HU__HU_Jasz-Arokszalas_jolanka-90_pic.jpg'); p.thumbnail((1000,1000)); p.convert('RGB').save('crops/pic.png')
