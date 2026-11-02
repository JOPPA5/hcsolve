from PIL import Image
for n,f in (('ov_adr','adr'),('ov_pic','pic')):
    im=Image.open(f'hires/cpc_--_HU__HU_Jasz-Arokszalas_jolanka-65_{f}.jpg').convert('RGB')
    im.thumbnail((1400,1000)); im.save(f'crops/{n}.png')
