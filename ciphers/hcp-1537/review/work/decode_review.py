"""Reviewer's independent decoder for HCP 1537 (no solver code imported)."""
import sys, json, pathlib
KEY = {'6':'a','p':'b','s':'c','t':'d','5':'e','F':'f','g':'k','r':'h','4':'i','y':'j','8':'l',
       'n':'m','m':'n','3':'o','b':'p','h':'r','c':'s','d':'t','2':'u','f':'v','1':'y','q':'z','H':'ch'}
def dec(line): return ''.join(KEY.get(ch, ch) for ch in line)
src = pathlib.Path(sys.argv[1])
rows = [l.rstrip('\n') for l in src.read_text().splitlines() if l and not l.startswith('#')]
n = 0; used = {}
for r in rows:
    for ch in r:
        if ch in KEY: n += 1; used[ch] = used.get(ch, 0) + 1
        elif ch not in ' .,?-': print('UNMAPPED', repr(ch), file=sys.stderr)
    print(dec(r))
print(f'# rows={len(rows)} signs={n}', file=sys.stderr)
print('# counts', dict(sorted(used.items())), file=sys.stderr)
