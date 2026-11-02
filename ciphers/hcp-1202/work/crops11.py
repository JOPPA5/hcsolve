import sys,os; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from crops import *
crop('a1',(950,1250,1750,1370),1.8)
crop('a2',(1650,1280,2000,1380),3)
crop('a3',(1750,1760,2300,1900),2.6)
crop('a4',(600,140,1000,300),3)
crop('a5',(2300,300,3000,1050),1.8,rot=-90)
crop('a6',(1480,105,2800,235),1.1,rot=180)
