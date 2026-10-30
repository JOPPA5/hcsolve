import sys
from PIL import Image
im = Image.open(sys.argv[1]).convert('L')
for i,(y0,y1) in enumerate([(35,240),(220,430),(410,630)]):
    c = im.crop((28,y0,85,y1)).rotate(90, expand=True)
    c = c.resize((c.width*4, c.height*4), Image.LANCZOS)
    c.save(f'{sys.argv[2]}/mg{i}.png')
