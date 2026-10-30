# Independent reviewer decoder: family key from hcp-1545 (plus y=J alias, shallow v=F),
# applied to the manual_cipher strings, with optional reviewer-verified corrections.
import json, sys, re
base = sys.argv[1]
fam = {k: v.lower() for k, v in json.load(open(base + '/../hcp-1545/work/key.json')).items()}
fam.update({'y': 'j', 'H': 'ch', 'v': 'f'})
lines = json.load(open(base + '/work/transcript.json'))['lines']
corr = '--corrected' in sys.argv
fix = {  # reviewer-verified on pixels / disclosed restorations in [brackets]
 'M03': ('t3f385m5 m5 {G03}', 't3f385m5 n5 '),
 'M06': ('y4m5r {G06}', 'y4m5r[3] '),
 'M07': ('m{G07}4', 'm[3c]d4'),
 'M08': ('bh3{C01}q5d4{G08}', 'bh3r84q5d4'),
 'S01': ('{U01}{G10}d3n', 'm[6] d3n'),
}
unmapped = set()
for l in lines:
    s = l['manual_cipher']
    if corr and l['id'] in fix:
        a, b = fix[l['id']]; assert a in s, (l['id'], a); s = s.replace(a, b)
    if corr: s = re.sub(r' ?\{G0\d\} ?', ' ', s)
    out = []; i = 0
    while i < len(s):
        ch = s[i]
        if ch == '{':
            j = s.index('}', i); out.append(s[i:j+1]); i = j + 1; continue
        if ch in '[]': out.append(ch); i += 1; continue
        if ch in fam: out.append(fam[ch])
        elif ch.isalnum(): out.append('?'); unmapped.add(ch)
        else: out.append(ch)
        i += 1
    print(l['id'], ''.join(out))
print('unmapped glyphs:', unmapped or 'none')
