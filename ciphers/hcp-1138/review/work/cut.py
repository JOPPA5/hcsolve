from PIL import Image
import sys
r=Image.open('crops/rot51w.png')
Z=float(sys.argv[1]);name=sys.argv[2];box=tuple(int(v) for v in sys.argv[3:7])
c=r.crop(box);c=c.resize((int(c.width*Z),int(c.height*Z)),Image.LANCZOS);c.save('crops/%s.png'%name);print(c.size)
