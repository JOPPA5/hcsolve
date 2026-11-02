from PIL import Image, ImageDraw
d='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1148/'
im=Image.open(d+'work/hires/cpc_1916-05-09_HU_Mezokovesd_HU_Szomolya_szomolya-34_adr.jpg')
P=[('hazaertunk',1570,195),('indult1',325,312),('indult2',580,312),('ertunk',1890,290),('nadragunk',2165,385),('ugrani',370,850),
('kereszt',830,950),('tudom',1395,1195),('egyutt',675,1465),('bu',1050,1707),('udvoz',125,1812),('hu',1135,1902)]
W=Image.new('RGB',(4*440,3*380),'white')
for i,(n,x,y) in enumerate(P):
    c=im.crop((x-65,y-55,x+45,y+40)).resize((440,380),Image.LANCZOS)
    ImageDraw.Draw(c).text((4,4),n,fill='red')
    W.paste(c,((i%4)*440,(i//4)*380))
W.save(d+'review/work/c/dotleft.png')
