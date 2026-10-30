from PIL import Image
im=Image.open('hires/pc_hcp_509_adr.JPG').convert('RGB')
# strips by rows (y in hires)
boxes={'a':(280,240,700,400),'b':(240,390,900,510),'c':(40,490,920,630),'d':(40,630,920,800),'e':(40,800,920,960),'f':(40,960,920,1110)}
boxes={'a':(280,240,760,395),'b':(250,395,860,500),'c':(50,500,500,650),'d':(480,500,930,650),
'e':(50,640,500,800),'f':(480,640,930,800),'g':(50,790,500,960),'h':(480,790,930,960),'i':(50,950,500,1110),'j':(480,950,930,1110)}
for k,b in boxes.items():
    c=im.crop(b); c=c.resize((c.width*3,c.height*3),Image.LANCZOS); c.save(f'crops/{k}.png')
