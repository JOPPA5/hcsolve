from PIL import Image, ImageOps
im=Image.open('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1267/work/hires/cpc_1913-07-13_HU__HU_Jasz-Arokszalas_jolanka-39_adr.jpg').convert('RGB')
R='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1267/review/work/'
def mont(n,boxes,s=4,cols=3):
    t=[ImageOps.autocontrast(im.crop(b).resize(((b[2]-b[0])*s,(b[3]-b[1])*s),Image.LANCZOS),cutoff=1) for b in boxes]
    w=max(x.width for x in t)+10;h=max(x.height for x in t)+10
    o=Image.new('RGB',(w*cols,h*((len(t)+cols-1)//cols)),'white')
    for i,x in enumerate(t):o.paste(x,((i%cols)*w,(i//cols)*h))
    o.save(R+n+'.png')
mont('hook',[(1290,490,1430,560),(600,80,720,160),(990,650,1110,720),(280,910,400,980),(220,1400,340,1470),(1360,1150,1480,1230)])
mont('spots',[(280,1040,420,1130),(1270,1080,1500,1160),(880,330,1040,410),(1330,1670,1500,1770),(860,1700,1090,1790),(540,1500,760,1600),(880,1900,1020,1980),(380,1280,520,1350),(1170,1680,1340,1760)],s=3)
mont('sp2',[(940,350,1040,410),(590,1120,810,1200),(930,650,1130,720),(250,1980,420,2040),(2060,1790,2220,1860),(1480,1840,1660,1920)],s=5,cols=2)
