# Independent reviewer decode of hcp-1186 (own transcription from enlarged crops of work/hires adr scan).
# Codes: digits as seen; Y=Y-sign; a=round a; d=a with tall stem; w=w-sign; u=u-sign; e=e-sign; o=filled oval;
# n=n-sign; j=dotted iota; K=l/k sign; E=hooked E/t sign; Z=hooked 2-like sign; _=overbar on preceding base (R)
lines = """4Y 4a a1wu 6 2385
Y4Z9 a48w9 4 a98Y j31
6 w65_n Yu6Y 4 8966_2j
o36_53Y u3e Y3 e6_4Y9 K1Y
6a 2385 6a 4 u6d9 83Y
o31_53Y98 u3e Y3 E4aa &
u15
868""".split('\n')
import re
key = {'6':'A','K':'B','w':'C','n':'D','9':'E','o':'F','5':'G','u':'H','4':'I','E':'K','2':'L','Z':'M',
       '8':'N','3':'O','a':'S','Y':'T','1':'U','d':'V','e':'W','j':'Y','&':'&'}
from collections import Counter
cnt = Counter()
for L in lines:
    words = []
    for w in L.split():
        toks = re.findall(r'._|.', w)
        out = ''
        for t in toks:
            out += 'R' if t.endswith('_') else key[t]
            cnt[t if not t.endswith('_') else 'R(' + t[0] + ')'] += 1
        words.append(out)
    print(L.ljust(28), ' '.join(words))
print(sorted(cnt.items()))
vals = list(key.values()); assert len(vals) == len(set(vals))
