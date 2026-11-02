import sys,os; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from crops import *
for i,x in enumerate([140,620,1100,1580,2060,2540,2960]):
    crop(f'C{i}',(x,1740,x+500,2190),2.8)
