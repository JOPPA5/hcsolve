# Independent review decode of hcp-1150: reviewer's own row-by-row reading from review/work crops.
# Key taken from hcp-1135/1174 tables, not from the solver's decode.py. Run with python3 -I.
import re,subprocess
K={'0':'o','0,':'ö','1':'i','1.':'a',"1'":'á','1:':'e',':1':'ü','1,':'b','2,':'cs','2.':'é','3':'d','3,':'r','3.':'v',
'4':'f','4,':'g','4.':'gy','5':'h','5,':'l','6':'j','6,':'n','6.':'ny','7':'k','7,':'s','7.':'sz','8':'m','8,':'t','9':'p','9,':'z'}
R="""3 3, 1' 4, 1. 8 1. 3, 4, 1 8, 7 1' 8
2. 3, 8, 1: 7, 1 8, 5, 1: 7 5 0 4. 1 6, 1: 8, 5 2. 8, 4 0, 6, 2. 6 6 1: 5, 1: 5, :1 8, 1. 9, 0 8 5 1. 9, 1. 4 1: 5, 2. 1. 9, :1 6, 6, 1: 9 1: 7 1 8, 8,
6, 1. 4. 0 6, 5, 1. 7, 7, 1. 6, 8, 1: 5, 8, 1: 7 6 0 1, 1, 1. 6, 7. 1: 3, 1: 8, 8, 1: 8
3. 0 5, 6, 1. 3. 1: 5, 1: 3 8, 0, 5, 8, 1: 6, 1 6, 0 3 1: 6, 1: 8 7, 0 7 1' 0 8, 8, 5, 1: 7. 1: 7 1: 4. 2. 1, :1 6 7, 1' 4, 0 8, 6, 1: 8
8, :1 3 0 7 1 3, 6, 1 4, 1: 3, 9, 0 6, 5 1. 9, 1. 6 0, 8, 8, 5 1. 8, 5 1. 3 1
7. 1. 1, 1. 3 7, 1' 4, 3, 1. 8 1. 6 3 7. 0 3. 1. 5, 8, 0, 1, 1, 1: 8,
3. 1. 6, 1: 4. 7 1 7, 7. 1: 6, 3 1: 3. 1 3, 1' 4, :1 4. 5 1 3. 6 1' 7 5 0 4. 6, 1: 4 1: 5, 1: 6 2,
1: 9, 1. 3. 1 3, 1' 4, 8, 0 5, 8 1' 2, 0 5, 0 8 5, 1' 6. 7 1. 1: 6, 4, 1: 8 6, 1: 4 1: 5, 1: 6 8, 7,
6, 1: 8 1, 1' 8 :1 5, 0 7 1. 4 2. 6. 1: 7, 2. 4, 3, 1: 3, 1. 4. 0 4, 6, 1. 7 1, 1' 3, 1. 2, 1 5, 5, 1. 4, 0 7
8 1: 3, 8, 1 8, 8, 1. 4 0, 5, 3 0, 6, 3, 1: 1' 3 6, 2. 9, 3. 1: 1: 4. 7. 1: 1, 1, 2, 1 5, 5, 1. 4, 0 8, 5, 1' 8, 5 1. 8, 0 7
7, 0 3, 1. 1 8 1. 8, 9, 1' 3, 3. 1. 7. 1. 8 8, 1. 5, 1. 6, 7. 0 3, 0, 5, 1: 5, 2, 0 7 0 5, 2. 7, :1 3 3. 0, 9, 0, 5, 5 :1 1 8 1. 3 0 3 1' 3, 9 1' 3"""
mine=[t for r in R.split('\n') for t in r.split()]
print(len(mine),'signs;','unknown:',[t for t in mine if t not in K])
print(''.join(K[t] for t in mine))
src=open('../../work/decode.py',encoding='utf8').read().split('T = """')[1].split('"""')[0]
sol=[t for l in src.strip().split('\n') if '|' in l for t in l.split('|')[1].split()]
print('solver',len(sol))
import difflib
sm=difflib.SequenceMatcher(None,sol,mine,autojunk=False)
for op,a,b,c,d in sm.get_opcodes():
    if op!='equal': print(op,sol[a-2:b+2],'->',mine[c-2:d+2])
