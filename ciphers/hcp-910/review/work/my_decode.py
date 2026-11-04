# Independent reviewer decode of hcp-910 from the reviewer's own reading of the hires scan.
import re
K=dict(zip("1234567890","aeioulnmrs"))
mine = """568 d27 | 2372 k61372 b3tt2 | h1:tt2 3ch 74ch 177 25ch | 72863ch 20 w5:9d2 | 83ch 029 f92527 |
w177 J29 8329 | 237 P1k2t Z5ck29 | sch3ck27 k4:7t d277 | 3ch w230 73cht w177 3ch | 37 59615b k4882"""
def dec(s):
    s=s.replace('1:','ä').replace('4:','ö').replace('5:','ü')
    return ''.join(K.get(c,c) for c in s)
print(dec(mine))
digits=re.findall(r'\d', mine)
print('digit signs:',len(digits), {d:digits.count(d) for d in sorted(set(digits))})
