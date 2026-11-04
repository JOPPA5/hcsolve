# Independent reviewer decode of hcp-1097: my own line reading from the hires scan.
K={'1':'a','2':'e','3':'i','4':'o','5':'u'}
lines=["y45 g4t b1ck h2r2","3n th3s c45ntry 1g13n","3 g4t y45r p4st c1rd",
"t4 l1t2 t4 1nsw2r2d","3t s4 3 w3ll s2nd y45","th1s 4n2. 3 sp4s2","y45r v2ry b3sy!",
"h5sk3ng c4rn n4w","3 1m 1t w4lsl2b2n","n4w h4w l4ng 1r2","y45 1g41ng t4 st1y?","(m15d)"]
for l in lines: print(f"{l:28s}-> {''.join(K.get(c,c) for c in l)}")
