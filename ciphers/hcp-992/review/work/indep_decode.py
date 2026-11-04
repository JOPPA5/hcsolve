# Independent check of hcp-992 by the reviewer. My own sign-by-sign reading of the
# picture side (hires scan), own sign names, own key derived from cribs.
# phi = oval/filled loop on a descender (A), phi: = with diaeresis, cup = U-shaped,
# cup: = with diaeresis, v = pointed V, Z = capital-I sign, arc = arch with dot below,
# rc = reversed-c curve, hk = hook/open-6 (R), dx = double-crossed sign, 2b = 2 with
# ink blob on top (final sign of the signature).
READ = [
 "3 4 arc 2 | 8 4 hk Z arc 2 2 arc 9 9 4 1 arc 4 6 7 4 5 | 8 4 hk Z 4 2 5",
 "9 cup 2 dx 7 4",
 "v arc rc 8 | phi 6 4 hk | cup 3 phi hk 3 7",
 "3 arc 7 | cup 2 Z phi: 8 1 arc 9 4 2 | 9 hk cup: 5 5 4 2 | cup 2 v | dx cup 5 5 4 2 | v 4 arc 2 | 5 arc rc 8 | 5 4 8 hk | 2 phi rc 8 | v arc hk | 5 4 8 2 4 2 v 4 5 | 4 hk arc rc 2b",
]
KEY = {'1':'l','2':'n','3':'m','4':'e','5':'s','6':'b','7':'t','8':'h','9':'g','phi':'a','phi:':'ä',
       'cup':'u','cup:':'ü','v':'d','Z':'z','arc':'i','rc':'c','hk':'r','dx':'k','2b':'?'}
from collections import Counter
cnt = Counter()
for l in READ:
    words = []
    for w in l.split('|'):
        toks = w.split(); cnt.update(toks)
        words.append(''.join(KEY[t] for t in toks))
    print(' '.join(words))
print('signs', len(cnt), 'tokens', sum(cnt.values()))
print(sorted(cnt.items(), key=lambda x: -x[1]))
