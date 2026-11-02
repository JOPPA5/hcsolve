from PIL import Image
P='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1163/'
im=Image.open(P+'work/hires/cpc_1916-02-26_HU_Mezokovesd_HU_Szomolya_szomolya-20_adr.jpg').convert('RGB')
# panel coords -> hi: x=base+px/2, y=ybase+py/2
def hi(pan,px,py):
    a=[50,520,980,1270,1760][pan[0]]; b=[30,780][pan[1]]
    return b+px//2,a+py//2
R={'u_csut':((0,1),1050,870-500,140),'u_kuld':((0,0),1100,570,130),'u_cedu':((0,1),1340,520,130),'u_tudom':((0,0),1300,730,130),
'u_ugy':((1,0),1380,720,140),'u_hus':((4,1),1020,310,140),'u_udv':((4,0),100,350,140),
'l_udv':((4,0),880,370,170),'imadod':((4,1),830,470,170),'minden':((3,0),1080,960,170),'mark_gond':((3,1),560,150,190)}
for k,(pan,px,py,r) in R.items():
    x,y=hi(pan,px,py)
    if k=='u_csut': x,y=hi((0,1),1000/1+0,340)
    c=im.crop((x-r,y-r//1,x+r,y+r)); c=c.resize((c.width*4,c.height*4),Image.LANCZOS); c.save(P+f'review/work/crops/{k}.png'); print(k,x,y)
