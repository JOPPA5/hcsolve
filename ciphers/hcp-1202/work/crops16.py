import sys,os; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from crops import *
for i,y in enumerate([1740,1900,2030]):
    crop(f'n{i}a',(2100,y,2800,y+200),2.15)
    crop(f'n{i}b',(2750,y,3450,y+200),2.15)
