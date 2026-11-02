from PIL import Image,ImageOps
im=Image.open('hires/cpc_1914-11-23_HU__HU_Budapest_jolanka-56_adr.jpg').convert('RGB')
def s(n,box,z=3,chan=0):
    c=ImageOps.autocontrast(im.crop(box).split()[chan],cutoff=1)
    c.resize((c.width*z,c.height*z),Image.LANCZOS).save(f'crops/{n}.png')
s('z6',(330,490,1180,680),2); s('z9',(120,680,1000,850),2); s('z5',(330,400,1050,520),3)
s('zend',(3000,1990,3320,2100),4)
s('zst',(2730,300,3180,640),3,chan=2)
