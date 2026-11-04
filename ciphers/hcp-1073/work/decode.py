"""hcp-1073 decoder. Run from repo root:
   python3 -I ciphers/hcp-1073/work/decode.py
Checks source hashes, then decodes work/transcription.txt with the key below."""
import hashlib, os, sys
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
HASHES = {
 'source/address-large.jpg': 'a71876de47479a27fbad706b970aabcc8731b1063b8b3ef29944c9f80f4cdb3d',
 'source/picture-large.jpg': 'df6ec1a7b69ca22615be7c030109a4fddce19e12f2c4cedfc0dfccef8e6915ad',
 'work/hires/cpc_1910-07-13_DE_Aschersleben_DE_Hier_hugocarl-01_adr.jpg': '5c66bb0d6b256987f7d82dcdf353ca3f2e1db721608789dce2a784f298e14a04',
 'work/hires/cpc_1910-07-13_DE_Aschersleben_DE_Hier_hugocarl-01_pic.jpg': '121f2e1b6b6a1fcee83069b4977e43ed40e85e386fdfb97846e827063a46009a',
}
for p, h in HASHES.items():
    got = hashlib.sha256(open(os.path.join(D, p), 'rb').read()).hexdigest()
    print(('OK   ' if got == h else 'FAIL ') + p)
    if got != h: sys.exit(1)
# digits: c..l with j omitted -> 1..9 (d=2 e=3 f=4 g=5 h=6 i=7 k=8 l=9); 6 also used for b (see SOLUTION.md)
KEY = {'2':'d','3':'e','4':'f','5':'g','7':'i','8':'k','9':'l',
       '6':'h|b',   # homograph: H in Hoffentlich, b in bist / bischen (resolved by sense)
       'R':'r','S':'s','Sd':'s','a':'a','N':'n','+':'ch','T':'t','W':'w','B':'b','P':'st',
       'o':'o','u':'u','ü':'ü','{1000}':'1000', ',':',', '.':'.', '!':'!'}
# 6 resolved by position (line, index of token in line) -> letter
SIX = {(5,0):'h', (5,11):'b', (8,0):'b'}
out = []
for ln, line in enumerate((l for l in open(os.path.join(D,'work/transcription.txt'), encoding='utf-8')
                           if l.strip() and not l.startswith('#')), 1):
    toks = line.split(); s = ''
    for i, t in enumerate(toks):
        v = SIX[(ln, i)] if t == '6' else KEY[t]
        s += v + (' ' if t in ',.!' else '')
    out.append(s.strip())
print('\nLetter-by-letter (separators kept):')
for s in out: print('  ' + s)
print('\nWord-divided plaintext (word division from the separators and sense):')
print(PLAIN := '1000 Grüsse u. Küsse sendet Dir Dein Dissel. Hoffentlich bist du gesund! '
      'Wenn nicht, dann langweile dich bitte nicht so u. denk ein bischen an deine Trude.')
# check: the word-divided text uses exactly the decoded letters
flat = lambda x: ''.join(c for c in x.lower() if c.isalnum())
assert flat(' '.join(out)) == flat(PLAIN), (flat(' '.join(out)), flat(PLAIN))
print('\nCheck: decoded letter stream == word-divided plaintext: OK')
