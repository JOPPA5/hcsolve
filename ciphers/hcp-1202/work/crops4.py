import sys,os; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from crops import *
# left margin, rotated upright (text runs along left edge)
crop('marginL',(130,1100,330,2200),1.4,rot=-90)
crop('marginR',(130,1100,330,2200),1.4,rot=90)
# right-side of bottom rows
crop('w1',(1400,1500,2300,1720),1.7)
