from PIL import Image, ImageOps
im=Image.open('../../work/hires/cpc_1912-05-12_HU__HU_Jasz-Arokszalas_jolanka-20_adr.jpg').convert('RGB')
g=im.split()[1]
def s(n,b,sc=7):
    c=ImageOps.autocontrast(g.crop(b)); c.resize((c.width*sc,c.height*sc),Image.BICUBIC).save('crops/%s.png'%n)
s('blot_g',(290,2055,375,2140))
# comparison sheet at same scale: blot, row1 cs, row1 s, row20 s-in-beszelte, row7 s, a row 13 '6', row20 '6', row 12 k
boxes={'blot':(285,2050,380,2145),'cs_r1':(470,70,585,175),'cs_r1b':(1290,75,1400,175),'s_r20':(620,2050,715,2145),'6_r20':(530,2050,625,2145)}
W=Image.new('RGB',(120*5*4,130*4),'white')
x=0
for k,b in boxes.items():
    c=im.crop(b); c=c.resize((c.width*4,c.height*4),Image.BICUBIC); W.paste(c,(x,0)); x+=120*4
W.save('crops/compare.png')
