# Independent decode. Key tables are parsed (not imported) from FINAL cards hcp-1174 and hcp-1178;
# the tokens below were typed from review/work/top.png and sig.png, not copied from the solver's script.
import re, ast
tbl={}
for card in ('hcp-1174','hcp-1178'):
    s=open(f'../../../{card}/work/decode.py',encoding='utf8').read()
    for k,v in ast.literal_eval('{'+re.search(r'KEY = \{(.*?)\}',s,re.S).group(1)+'}').items():
        tbl.setdefault(k,set()).add(v)
print('conflicts between the two cards:',{k:v for k,v in tbl.items() if len(v)>1})
for line in ["7 1: 3 3. 1: 7, | 8 1. 3, 4, 1 8, 7 1' 8","1' 3, 9 1' 3"]:
    print(' '.join(''.join(sorted(tbl[t])[0] for t in w.split()) for w in line.split('|')))
print('signs',sum(len(l.replace('|',' ').split()) for l in ["7 1: 3 3. 1: 7, | 8 1. 3, 4, 1 8, 7 1' 8","1' 3, 9 1' 3"]))
