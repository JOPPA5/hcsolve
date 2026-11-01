from PIL import Image
im=Image.open('../../work/hires/cpc_1913-06-13_HU__HU_Jasz-Arokszalas_jolanka-37_adr.jpg')
for n,b in dict(a=(690,70,1040,180),b=(620,250,1020,330),c=(330,250,700,340),d=(400,405,760,540),e=(2470,50,3020,520)).items():
    c=im.crop(b);c=c.resize((c.width*(2 if n=='e' else 5),c.height*(2 if n=='e' else 5)),Image.LANCZOS);c.save('z'+n+'.png')
