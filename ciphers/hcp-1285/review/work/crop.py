from PIL import Image
im=Image.open('../../work/hires/cpc_1912-01-14_HU__HU_Jasz-Arokszalas_jolanka-02_adr.jpg').convert('RGB')
print(im.size)
r=im.rotate(-90,expand=True); print(r.size)
r.save('rot.png')
W,H=r.size
z=1900/W
r.resize((1900,int(H*z)),Image.LANCZOS).save('all.png')
im.resize((im.width*1500//im.height if 0 else 1400,int(im.height*1400/im.width)),Image.LANCZOS).save('upright.png')
