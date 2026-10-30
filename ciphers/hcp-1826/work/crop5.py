from PIL import Image, ImageEnhance
im=Image.open('work/hires/pc_hcp_507_adr.JPG').convert('RGB')
def s(box,name,rot,z):
    c=im.crop(box).rotate(rot,expand=True); c=ImageEnhance.Contrast(c).enhance(1.5)
    c.resize((c.width*z,c.height*z),Image.LANCZOS).save('work/crops/'+name)
s((55,40,330,130),'corner.png',180,5)
s((330,40,650,130),'top_mid.png',180,4)
# soon region in hires coords: approx
s((470,85,640,130),'soon.png',180,6)
s((640,40,880,170),'topstart.png',180,4)
