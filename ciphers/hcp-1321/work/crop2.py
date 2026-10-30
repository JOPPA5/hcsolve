from PIL import Image
r=Image.open('hires/pc_hcp_2_adr.JPG').convert('RGB').crop((180,150,930,1100)).rotate(90,expand=True)
# r is 950x750 ; msg2x coords /2
for n,b in {'L1a':(120,205,450,290),'L1b':(490,220,700,300),'L2a':(115,300,490,385),'L2b':(570,315,845,385),'L3':(120,395,430,470)}.items():
    c=r.crop(b); c.resize((c.width*5,c.height*5),Image.BICUBIC).save(f'crops/{n}.png')
