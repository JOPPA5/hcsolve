from PIL import Image
D='ciphers/hcp-1294/'
im=Image.open(D+'work/hires/cpc_1912-03-26_HU__HU_Jasz-Arokszalas_jolanka-12_adr.jpg').convert('RGB')
S=3445/1024
def c(n,b,z):
    r=im.crop(tuple(int(v*S) for v in b)); r=r.resize((r.width*z,r.height*z),Image.LANCZOS); r.save(D+'review/work/crops/'+n+'.png')
c('stamp',(785,85,925,215),2)
c('pm1',(470,45,700,280),1)
c('pm2',(710,50,890,270),1)
c('addr',(480,100,960,530),1)
c('r8signs',(180,265,260,305),4)
# o and i and d-comparison
c('o_r08b',(305,262,345,305),4)
c('o_r02',(205,55,245,100),4)
c('i_r02',(315,50,355,100),4)
