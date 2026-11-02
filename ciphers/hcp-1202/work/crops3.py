import sys,os; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from crops import *
for i,y in enumerate([1450,1600]):
    crop(f'u{i}',(2000,y,2760,y+215),2.0)
    crop(f'v{i}',(2600,y,3360,y+215),2.0)
