from PIL import Image
im=Image.open('work/hires/pc_hcp_507_adr.JPG').convert('RGB')
# top block upside down lines, y 40-370
a=im.crop((60,40,900,370)).rotate(180,expand=True)
for i,(x0,x1) in enumerate([(0,430),(410,840)]):
    c=a.crop((x0,0,x1,330)); c.resize((c.width*3,c.height*3),Image.LANCZOS).save(f'work/crops/top{i}.png')
# side block rotate 90 ccw? 
b=im.crop((60,370,880,1110)).rotate(90,expand=True)
print(b.size)
b.save('work/crops/side.png')
b=im.crop((60,370,880,1110)).rotate(-90,expand=True)
b.save('work/crops/side2.png')
