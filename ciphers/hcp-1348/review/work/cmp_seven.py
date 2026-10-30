# side-by-side: final year digit hcp-1348 vs "Feb. 7th 1907" on hcp-1353
from PIL import Image,ImageOps
im=Image.open('hcp-1353/work/hires/pc_hcp_34_adr.JPG').convert('L').rotate(90,expand=True)
a=ImageOps.autocontrast(im.crop((500,1490,1070,1630))); a=a.resize((a.width*3,a.height*3),Image.LANCZOS)
b=Image.open('hcp-1348/review/work/r_year.png'); b=b.resize((a.width,int(b.height*a.width/b.width)))
o=Image.new('L',(a.width,a.height+b.height+10),255); o.paste(a,(0,0)); o.paste(b,(0,a.height+10)); o.save('hcp-1348/review/work/cmp_seven.png'); print(o.size)
