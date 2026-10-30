from PIL import Image
im=Image.open('hires/pc_hcp_2_adr.JPG').convert('RGB')
r=im.crop((180,150,930,1100)).rotate(90,expand=True)
def s(n,b,k,src=r):
    c=src.crop(b); c.resize((c.width*k,c.height*k),Image.LANCZOS).save(f'crops/{n}.png')
s('amp',(375,225,470,285),10)
s('struck',(40,70,350,190),4)
s('sig',(280,540,880,740),3)
s('plain',(30,20,930,230),2)
s('stamp',(1270,110,1720,390),3,im)
