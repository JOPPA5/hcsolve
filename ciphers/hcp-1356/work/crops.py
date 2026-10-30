from PIL import Image, ImageOps
im=Image.open('hires/pc_hcp_37_adr.JPG').convert('RGB')
m=im.crop((200,360,890,1085)).rotate(90,expand=True)
print(m.size); m.save('crops/message.png')
m2=m.resize((m.width*2,m.height*2),Image.LANCZOS); m2.save('crops/message2x.png')
W,H=m.size
# rows: strips
n=0
for y0 in range(0,H-120,110):
    s=m.crop((0,y0,W,min(H,y0+170))).resize((W*3//1,(min(H,y0+170)-y0)*3),Image.LANCZOS)
    for i,x0 in enumerate((0,W*3//2-200)):
        s.crop((x0,0,x0+W*3//2+200,s.height)).save(f'crops/r{n}_{i}.png')
    n+=1
print(n)
