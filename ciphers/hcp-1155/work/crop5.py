import glob
from PIL import Image
im=Image.open(glob.glob('hires/*_pic.jpg')[0]).convert('RGB')
r=im.crop((40,380,450,1950)).rotate(-90,expand=True); r.save('crops/verse.png')
