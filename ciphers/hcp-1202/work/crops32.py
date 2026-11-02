import sys,os; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from crops import *
crop('T_tail',(1780,2040,2200,2115),3.4)
crop('T_top',(1640,120,2800,300),1.2,rot=180)
crop('T_top2',(1640,120,2800,300),1.2)
# left margin rotated both ways, split
for i,(a,b) in enumerate([(560,1160),(1100,1700),(1640,2190)]):
    crop(f'M{i}a',(120,a,265,b),2.3,rot=90)
    crop(f'M{i}b',(120,a,265,b),2.3,rot=-90)
crop('Rtop',(2780,120,3440,360),2)
crop('Pic',(0,0,10,10),1)
