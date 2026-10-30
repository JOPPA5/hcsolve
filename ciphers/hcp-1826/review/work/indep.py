#!/usr/bin/env python3
"""Reviewer's own decode of hcp-1826. Rows typed from review/work/crops, undivided.
Notation: Z crossed sign, O left box, U right box, ' raised dot, () circle = capital, literal 1:48 as #.
Run from the repo root: python3 -I ciphers/hcp-1826/review/work/indep.py"""
import re, sys, subprocess, difflib
ROWS = """0OU6 18Z617 62'18 2'1'32'17
0'Z5 811Z91'915 O9 15O1'915
O9 4142' 46Z1'9 414Z4
152'45 4O (19) Z4 #
0'2'1792'517Z0 19U4 1'16 0OU
17O 9O4 0'Z94 102' 4O 18O102'
4142'9 13U54 5Z0 5O Z5 16O6
4142' O4142'6 31'51'4 (1') 17O 9O4
0'Z94 4O 15O 9O0' U941'11 4142'
11Z54 O16 (Z)U15. 4142'9 (4). 18Z9
15O 0'1'4 14 102' Z917 4142'62' 1'5
Z9O4142' 62'Z5O9. (11)2'4 102'
1292'0' 1'16 0OU
0'Z94 102' 4O 18O102' 0'2'17. O6
0'OU1117 6Z4142'6 (1') 0'OU1117
18O102' 5O102' O4142'6 41'102'
(1') 13U54 Z5 5OU9 142'118 0OU 0'14Z4
(1') 18Z9 Z90 0'Z0. 11O32' (18)Z661'2'."""
L = {"Z":"a","2'":"e","1'":"i","O":"o","U":"u","0'":"w","0":"y","#":"[1:48]"}
for i,c in enumerate("bcdfghjklmn", 0): L[str(19-i)] = c
L.update({"8":"p","6":"r","5":"s","4":"t","3":"v"})
def dec(s):
    out=''; i=0
    while i<len(s):
        m=re.compile(r"\(([^)]+)\)|1[0-9](?!')|[012]'|[ZOU#034569 8.]").match(s,i)
        if not m: sys.exit(f'unparsed at {s[i:]}')
        t=m.group(0); i=m.end()
        if m.group(1): out+=L[m.group(1)].upper()
        elif t in ' .': out+=t
        else: out+=L[t]
    return out
txt=' '.join(dec(r) for r in ROWS.splitlines())
print(txt)
n=lambda s: re.sub(r'[^a-z0-9]','',s.lower()).replace('148','')
sol=subprocess.run(['python3','-I','ciphers/hcp-1826/work/decode.py'],capture_output=True,text=True).stdout.split('Literal plaintext:\n')[1]
a,b=n(txt),n(sol)
print('letters mine/solver',len(a),len(b))
for op,i,j,k,l in difflib.SequenceMatcher(None,a,b,autojunk=False).get_opcodes():
    if op!='equal': print(op,repr(a[i-6:j+6]),'vs',repr(b[k-6:l+6]))
