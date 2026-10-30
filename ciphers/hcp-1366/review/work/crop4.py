from PIL import Image
i=Image.open('../../../hcp-1363/work/hires/pc_hcp_44_adr.JPG').convert('RGB')
print(i.size)
r=i.rotate(90,expand=True); 
W=i.size[0]
c=r.crop((340,W-1000,1150,W-150)); print(c.size)
c.resize((c.size[0]*2,c.size[1]*2),Image.LANCZOS).save('s1363.png')
