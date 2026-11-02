"""Reviewer's independent decode: own glyph names, own reading of the enlarged crops, family key from hcp-1216.
Compares with the solver's output. Run: python3 -I ciphers/hcp-1222/review/work/decode_review.py (from repo root)"""
import difflib, os, re, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__))
KEY = dict(bar2='a', bar3='e', six='b', lbowl_rbowl='cs', sl='d', ls='h', ls_p='p', hook='g', hk_y='gy', invT='j', sect='k',
           wave='l', st3='m', st2='n', loop='o', eff='r', rbowl='s', gamma='t', cross='u', chev='v', crz='z', dot='i',
           lbowl='c', plus='f', blot='?', dgl='d', dig7='7', stop='.', gam_r='r')
R = """
rbowl crz bar3 eff bar3 gamma bar3 gamma bar3 sl bar3 rbowl invT loop wave bar2 st2
sect bar2 st3 gamma cross sl bar2 gamma loop st3 ls loop hk_y rbowl crz bar3 eff bar3 st2
lbowl_rbowl bar3 rbowl bar3 st2 st3 bar3 hook bar3 eff sect bar3 crz gamma bar3 st3 six bar2 eff
wave bar3 sect bar3 rbowl gamma bar3 st3 bar2 chev loop st2 bar2 gamma eff loop wave
bar3 rbowl lbowl_rbowl bar2 sect dig7 loop eff bar2 eff bar2 bar3 eff gamma bar3 st3 hk_y loop st2
hk_y loop rbowl eff bar3 stop bar3 sl bar3 rbowl bar3 st3 st3 bar3 hook st2 bar3 st3
gamma cross sl loop st3 st3 dot invT bar2 st2 rbowl loop eff rbowl chev bar2
eff bar2 st3 st3 bar3 hook lbowl_rbowl bar2 sect ls bar3 wave cross gamma bar2 st2
st2 bar3 crz bar3 sect st3 cross st2 sect bar2 stop cross gamma bar2 st2 loop gamma bar2
ls loop st2 dot rbowl chev bar2 st2 st3 cross st2 sect bar2
bar3 rbowl st3 bar3 eff sect dot bar2 sl gamma bar2 bar3 sl bar3 bar2 ls_p bar2 st3
bar2 invT bar3 wave rbowl crz loop gamma ls loop hk_y ls loop wave
hook loop crz blot sect st3 bar3 eff st2 bar3 st3 bar2 sl bar3 st2 dot
dgl bar3 st3 loop rbowl gamma st2 bar3 st3 dot eff loop sect gamma loop six
six bar3 gamma st3 bar2 invT sl bar3 rbowl gamma bar3 eff bar2 six loop chev bar3
six bar3 st2 dot rbowl gamma bar3 st2 chev bar3 wave bar3 bar3 sl bar3 rbowl bar3 st3
chev dot hk_y bar2 crz loop st2 bar3 hook bar3 rbowl rbowl bar3 hook bar3 eff bar3
bar2 sl invT bar2 bar2 gamma dot rbowl crz gamma bar3 wave bar3 gamma bar3 st3 sect bar3 sl chev bar3 rbowl
st3 bar2 st3 bar2 invT bar2 st2 bar2 sect bar3 rbowl gamma bar3 rbowl gamma chev bar3 gam_r bar3 dot st2 bar3 sect
gamma dot rbowl crz gamma bar3 wave gamma bar3 gamma bar3 st3 bar2 st3 bar2 st2 lbowl crz dot sect bar2 gamma dot rbowl
lbowl_rbowl loop sect loop
wave loop st3
rbowl crz bar2 st3
gamma bar2 wave bar2 st2
rbowl crz loop gam_r
plus bar3 eff dot
""".strip().splitlines()
mine = [''.join(KEY[t] for t in r.split()) for r in R]
root = os.path.abspath(os.path.join(HERE, '..', '..', '..', '..'))
out = subprocess.run([sys.executable, '-I', 'ciphers/hcp-1222/work/decode.py'], cwd=root, capture_output=True, text=True).stdout
sol = [m.group(2) for m in re.finditer(r'^\s*(\d\d|c\d) (\S+)$', out, re.M)]
strip = lambda s: re.sub(r'\{t>r\}', 'r', re.sub(r'\{a\|e\}', '?', s.replace('{d?}', 'd'))).replace('é','e').replace('á','a').replace('ö','o').replace('í','i')
print('rows', len(mine), len(sol))
print(sum(map(len, mine)), 'letters (reviewer)', sum(len(strip(s)) for s in sol), 'letters (solver)')
for i, (m, s) in enumerate(zip(mine, sol), 1):
    s = strip(s)
    print(f'{i:02d} {"same" if m == s else "DIFF"} {m}' + ('' if m == s else f'   solver: {s}'))
