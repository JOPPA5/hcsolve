from PIL import Image, ImageEnhance
im=Image.open('work/hires/cpc_--_HU__HU_Jasz-Arokszalas_jolanka-77_adr.jpg').convert('RGB')
im.crop((60,200,1640,330)).resize((1975,162)).save('review/work/r2/row3w.png')
x=im.crop((800,190,1640,330));x=x.resize((1848,308),Image.LANCZOS);ImageEnhance.Contrast(x).enhance(1.7).save('review/work/r2/r3soraim.png')
