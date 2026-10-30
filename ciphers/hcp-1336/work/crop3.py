from PIL import Image
base='/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1336/work/'
im=Image.open(base+'hires/pc_hcp_17_adr.JPG'); s=1785/1024
for n,b,z in [('s_l2_R',(290,305,345,370),9),('s_l3_B',(205,385,275,440),8)]:
    c=im.crop([int(x*s) for x in b]); c.resize((c.width*z,c.height*z),Image.LANCZOS).save(base+'crops/'+n+'.png')
