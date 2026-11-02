from PIL import Image
im=Image.open('work/hires/cpc_1912-06-_HU__HU_Jasz-Arokszalas_jolanka-105_adr.jpg').convert('RGB')
S=1.72
R=[('a',40,240),('b',230,430),('c',420,620),('d',610,810),('e',800,1000),('f',990,1215)]
for n,a,b in R:
    for j,(l,r) in enumerate([(40,500),(470,950)]):
        c=im.crop((int(l*S),int(a*S),int(r*S),int(b*S))); c.resize((int(c.width*1.3),int(c.height*1.3)),Image.LANCZOS).save(f'review/work/crops2/{n}{j}.png')
