from PIL import Image, ImageOps
s=1785/1024
a=Image.open('hires/pc_hcp_467_adr.JPG').convert('L')
rows=[(135,195),(185,240),(232,285),(280,322),(320,372),(358,412),(400,450),(442,490),(490,538),(522,570)]
for i,(t,b) in enumerate(rows):
  for j,(l,r) in enumerate([(60,285),(270,500)]):
    c=a.crop((int(l*s),int(t*s),int(r*s),int(b*s)))
    c=ImageOps.autocontrast(c,cutoff=0.5)
    c=c.resize((c.width*4,c.height*4),Image.BICUBIC); c.save(f'crops/z{i}{"ab"[j]}.png')
