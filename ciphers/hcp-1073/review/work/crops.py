import sys
from PIL import Image
src, out = sys.argv[1], sys.argv[2]
im = Image.open(src)
# message area: left ~45% of card
W,H = im.size
msg = im.crop((int(W*0.02), int(H*0.04), int(W*0.42), int(H*0.86))).rotate(90, expand=True)
msg.save(out+'/msg_rot.jpg', quality=92)
w,h = msg.size
# split into 4 horizontal strips x 2 halves, enlarge 2x
n=0
for i in range(4):
    for j in range(2):
        c = msg.crop((j*w//2 - (0 if j==0 else 60), i*h//4, (j+1)*w//2 + (60 if j==0 else 0), (i+1)*h//4))
        c = c.resize((c.width*2, c.height*2), Image.LANCZOS)
        c.save(f'{out}/strip_{i}{j}.jpg', quality=92); n+=1
print(msg.size)
