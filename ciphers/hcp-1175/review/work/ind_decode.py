#!/usr/bin/env python3
# independent decoder: own key literal from hcp-1174 table text + own reading of the five lines
import re
R="""5|1.|8|2.|4,|1:|4.|7.|1:|3,|1:|5,
1|6,|3|.1|5,|0|7|2.|7,|0|3|1.|6,|1:|8
2.|3,|5|1:|8,|1:|7|1.|7|0|3,|1.|9,
.1|8,|0|6,|4|0,|1,|5,|0,|3.|0,|8
8|1.|4,|1.|8"""
tab=open('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1174/SOLUTION.md',encoding='utf-8').read()
K={}
for s,l in re.findall(r'`([^`]+?)`[^|]*\| ([^|]+?) \|',tab):
    K[s]=l.split(',')[0].strip()
K['1\'']='á'
print(K)
out=[];miss=[]
for line in R.split('\n'):
    w=''
    for s in line.split('|'):
        if s in K: w+=K[s]
        else: w+='['+s+']'; miss.append(s)
    out.append(w)
print(' / '.join(out)); print('not in hcp-1174 table:',miss)
sol=[l.split() for l in open('/Users/tomaspavuk/Desktop/hcsolve/ciphers/hcp-1175/work/transcription2.txt',encoding='utf-8') if not l.startswith('#')]
print('solver transcription identical to mine:', sol==[l.split('|') for l in R.split('\n')])
