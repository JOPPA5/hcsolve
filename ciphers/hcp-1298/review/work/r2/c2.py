from PIL import Image, ImageEnhance, ImageDraw
im=Image.open('work/hires/cpc_--_HU__HU_Jasz-Arokszalas_jolanka-77_adr.jpg').convert('RGB')
def g(b,s=6,k=1.8):
    x=im.crop(b);x=x.resize((int(x.width*s),int(x.height*s)),Image.LANCZOS)
    return ImageEnhance.Contrast(x).enhance(k)
g((1360,1480,1600,1590),6).save('review/work/r2/z20end.png')
g((80,1590,260,1710),6).save('review/work/r2/z21start.png')
# comparison: row 1, row 3 soraim, row 11 i, row 4 tailx
