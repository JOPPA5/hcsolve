import sys,os; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from crops import *
crop('top1',(1500,115,2300,290),1.9,rot=180)
crop('top2',(2250,115,2800,290),2,rot=180)
crop('pen',(1950,350,2800,1050),1.7)
crop('pen2',(2300,280,3000,1050),1.8,rot=90)
crop('z3',(1800,1180,2250,1330),3)
crop('z14',(1250,1180,1800,1330),2.6)
crop('addr',(1850,1000,3300,1820),1.0)
