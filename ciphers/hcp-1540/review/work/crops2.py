import sys
from PIL import Image
im = Image.open(sys.argv[1]); out=sys.argv[2]
for name,box in [("b03",(30,738,674,782)),("b04",(30,764,674,806)),("b10",(30,940,674,990)),
                 ("b03L",(30,738,360,782)),("b03R",(280,738,674,782)),("b04R",(330,764,674,806)),("b10L",(30,940,360,990)),
                 ("b07",(30,862,674,900)),("b05",(30,792,674,835)),("b01",(30,680,674,722)),("b09",(30,880,674,925))]:
    c=im.crop(box); s=4 if box[2]-box[0]<400 else 3
    c.resize((c.width*s,c.height*s),Image.LANCZOS).save(f"{out}/{name}.png")
