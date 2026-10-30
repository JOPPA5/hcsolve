from PIL import Image
r=Image.open('reading.png')
B={'row2a':(130,245,330,380),'hpjoh':(420,140,650,260),'nz_nl':(40,460,470,560),'gspn_zpvs':(460,470,910,570),'pxo_el':(20,550,520,650),'hjsm':(570,550,890,690),'npsspx':(180,360,720,500),'bn':(100,140,420,260)}
for k,b in B.items():
    c=r.crop(b); s=5 if c.size[0]<340 else 4
    c.resize((c.size[0]*s,c.size[1]*s),Image.LANCZOS).save(f'z_{k}.png')
im=Image.open('../../work/hires/pc_hcp_58_adr.JPG').convert('RGB')
c=im.crop((1340,80,1660,450)).rotate(90,expand=True)
c.resize((c.size[0]*3,c.size[1]*3),Image.LANCZOS).save('stamp_rot.png')
p=Image.open('../../work/hires/pc_hcp_58_pic.JPG'); print(p.size); p.thumbnail((1000,1000)); p.convert('RGB').save('pic.png')
