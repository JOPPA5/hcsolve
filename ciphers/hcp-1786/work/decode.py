#!/usr/bin/env python3
"""hcp-1786: mechanical decoder. Run from the repo root:
  python3 -I ciphers/hcp-1786/work/decode.py
It checks the source hashes, decodes the transcription T with no free vowel insertion
(only signs written on the card give letters), prints the literal text, compares each
word with the reading, and fails on any difference outside the listed EXCEPTIONS.
Comparison folds what the cipher does not distinguish: b/p, d/t, h/ch, i/y, accents.

Notation: 0 1 2 3 4 5 6 8 9 x j(zeta-shaped) c(e-shaped) v a = signs.
After a sign: / crossed = +o; # heavy stroke = +a; ^ caron or ring on the consonant;
* a stroke or blot on the sign, read through (no value).
Marks: - e; . i/y; : u; ^- e with caron (ě); ^~ caron on the consonant, then e;
' accent on the e (no value). = writer's line-end hyphen. + at the start of a word =
written above the line with a curled insertion mark."""
import hashlib, os, re, sys, unicodedata
here = os.path.dirname(os.path.abspath(__file__)); d = os.path.dirname(here)
H = {'source/picture-large.jpg': '6b20e0635cc534536df68105f873570b31d1a84ea4e7fefd8999c24e7a8ecb3f',
     'source/address-large.jpg': 'a92ab46bd6c2cbdd4725949ab4ba53215a5619217c44b40bd4b249a9b905815a',
     'work/hires/pc_hcp_467_pic.JPG': '4ec5a1fd89e6f35e339a1e01f279591e7cee1aeac3ede366d18fbf5d187a9864',
     'work/hires/pc_hcp_467_adr.JPG': 'c68d9f60a357ec10169e8e59fed56d677c420fc36ca79b8c1fcd62fcc8b35cff'}
for f, h in H.items():
    if hashlib.sha256(open(os.path.join(d, f), 'rb').read()).hexdigest() != h:
        sys.exit('HASH MISMATCH ' + f)
print('source hashes OK')
V = {'0':'l','1':'d','2':'n','3':'m','4':'r','5':'s','6':'p','8':'h','9':'k','x':'z','j':'j','c':'c','v':'v','a':'a'}
CARON = {'4':'ř','5':'š','x':'ž','c':'č','1':'ď'}
T = """64^.*j3^-1- 64/x#1.3 1.31/ 1.9.
x# 65#2.c^9/ 2-53.5^ 5- x0#1c^9/
x0/6.1. vx^1.1^ j5-3 1. 65#0 x^~
j5/: 1/ 90-6.
1.2-5 j5-3 v 9:12- 8/4^ 64/ 4^~=
6/v-' 5-3-2/ x#5-1/ j.x^ 3#3- j-5^1^-
9/:5-9 4^~6. a 6:1- 8/1/v/
1^-5^.3 5*- x^ 6*4^.j-1-1- 14^.v- 1/3:
j5/: x1- 80#12# a0- x0#1- 50:2.c^9/
64^~c- 01-v.4# 4.80- +94#5: 64.4/1.""".split('\n')
R = """Přijměte prozatím tímto díky
za psaníčko, nesmíš se, zlatíčko,
zlobiti, vždyť jsem ti psal, že
jsou to klepy.
Dnes jsem v Kutné Hoře, pro ře=
pové semeno. Zaseto již máme, ještě
kousek řepy a bude hotovo.
Těším se, až přijedete dříve domů.
Jsou zde chladna, ale zlaté sluníčko
přece otevírá rychle krásu přírody.""".split('\n')
# word (folded form of the reading): why the literal differs
EXCEPTIONS = {'zladicko': 'no i written in zlatíčko', 'dnes': 'a dot stands after the 1 (literal dines): slip or stray',
              'hore': 'no e written in Hoře', 'az': 'bare x with ring: no heavy stroke, so literal ž',
              'odevira': 'bare 0 as initial o: literal l; word-sense call'}
tok = re.compile(r"([0-9xjcva])(/?)(#?)(\*?)(\^(?![-~]))?|(\^-)|(\^~)|([-.:])|(')|(\*)")
def dec(w):
    w = w.lstrip('+').rstrip('='); o = ''; n = 0; pos = 0
    for m in tok.finditer(w):
        if m.start() != pos: sys.exit('TOKEN ERROR ' + w)
        pos = m.end(); s, cr, hv, st, car, he, cn, mk, ac, bl = m.groups(); n += 1
        if s:
            o += CARON[s] if car and s in CARON else V[s]
            o += 'o' if cr else ''; o += 'a' if hv else ''
        elif he: o += 'ě'
        elif cn: o = o[:-1] + {'r':'ř','z':'ž'}[o[-1]] + 'e'
        elif mk: o += {'-': 'e', '.': 'i', ':': 'u'}[mk]
        elif ac: o = o[:-1] + 'é'
    if pos != len(w): sys.exit('TOKEN ERROR ' + w)
    return o, n
def fold(t):
    t = unicodedata.normalize('NFD', t.lower())
    t = ''.join(c for c in t if not unicodedata.combining(c))
    return t.replace('ch', 'h').replace('y', 'i').replace('b', 'p').replace('t', 'd')
words = signs = bad = 0; used = []
for tl, rl in zip(T, R):
    tw = tl.split(); rw = rl.split(); assert len(tw) == len(rw), (tw, rw)
    lit = []
    for c, w in zip(tw, rw):
        l, n = dec(c); lit.append(l); signs += n; words += 1
        f = fold(re.sub(r'[.,=]', '', w))
        if fold(l) != f:
            if f in EXCEPTIONS: used.append((w, l, EXCEPTIONS[f]))
            else: print('MISMATCH', c, l, w); bad += 1
    print(' '.join(lit))
print('signs/marks:', signs, 'words:', words, 'mismatches:', bad)
print('listed exceptions (%d of %d):' % (len(used), len(EXCEPTIONS)))
for u in used: print('  %s: literal %s; %s' % u)
heavy = sum(c.count('#') for c in T); print('heavy signs:', heavy)
if len(used) != len(EXCEPTIONS): bad += 1; print('UNUSED EXCEPTION')
print()
print(' '.join(R).replace('ře= pové', 'řepové'))
sys.exit(1 if bad else 0)
