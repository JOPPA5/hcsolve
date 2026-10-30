from PIL import Image
im=Image.open('../../work/hires/cpc_1912--_HU__HU_Jasz-Arokszalas_jolanka-98_adr.jpg').convert('RGB')
F=3445/1024
def c(n,a,b,d,e,s,rot=0):
    r=im.crop((int(a*F),int(b*F),int(d*F),int(e*F)))
    if rot: r=r.rotate(rot,expand=True)
    r.resize((int(r.width*s),int(r.height*s)),Image.LANCZOS).save(f'crops/{n}.png')
c('z_hatok',590,565,800,600,2.5)
c('z_nem',480,565,620,600,3.5)
c('z_corner',880,555,985,632,4)
c('z_edge_rot',925,440,985,630,2.8,90)
c('z_postmark',740,75,930,275,1.6)
