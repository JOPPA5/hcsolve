"""HCP1294 row 8: compare oszeholad and its tail with every word of the Jolanka family's SOLUTION.md files.
Run from repo root: python3 -I ciphers/hcp-1294/work/row8_test.py"""
import glob, re, unicodedata, difflib
def base(w): return ''.join(c for c in unicodedata.normalize('NFD', w.lower()) if not unicodedata.combining(c))
vocab = {}
for f in glob.glob('ciphers/hcp-1[23][0-9][0-9]/SOLUTION.md'):
    t = open(f, encoding='utf-8').read()
    if not re.search('jol[aá]nk', t, re.I): continue
    card = f.split('/')[1]
    for w in re.findall(r"[^\W\d_]{3,}", t):
        vocab.setdefault(base(w), set()).add(card)
print(len(vocab), 'distinct words')
for target in ('oszeholad', 'oszepolad', 'oszeholan', 'oszepolan', 'holad', 'polad', 'holan', 'polan'):
    print(target, difflib.get_close_matches(target, list(vocab), n=6, cutoff=.72))
print('prefix ossze/osze:', sorted(w for w in vocab if w.startswith(('ossze', 'osze'))))
print('holnap cards:', sorted(vocab.get('holnap', [])))
