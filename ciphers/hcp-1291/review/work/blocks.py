import sys; sys.path.insert(0,'/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1291/review/work')
from crop import crop
ys=[(90,370),(350,640),(620,890),(860,1120),(1090,1320),(1300,1520),(1490,1720),(1700,2120)]
for i,(a,b) in enumerate(ys):
    crop(f'bl{i}a',60,a,900,b,1.8); crop(f'bl{i}b',820,a,1720,b,1.7)
