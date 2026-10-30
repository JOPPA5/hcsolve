# Independent check: reflect the address side left-right with PIL and save
# enlarged crops of the message, the edge word and the address.
import sys
from PIL import Image
src, out = sys.argv[1], sys.argv[2]
im = Image.open(src)
f = im.transpose(Image.FLIP_LEFT_RIGHT)
f.save(out + '/flip_pil.png')
f.crop((620, 270, 1024, 540)).resize((1212, 810), Image.LANCZOS).save(out + '/msg_flip_3x.png')
im.crop((0, 360, 140, 425)).resize((700, 325), Image.LANCZOS).save(out + '/edge_orig_5x.png')
im.crop((420, 270, 980, 600)).resize((1120, 660), Image.LANCZOS).save(out + '/addr_orig_2x.png')
print('ok')
