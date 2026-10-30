#!/usr/bin/env python3
"""HCP1343 decoder: checks file hashes, decodes work/transcription.txt with the key.
Run from the repo root:  python3 -I ciphers/hcp-1343/work/decode.py
"""
import hashlib, json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
CDIR = os.path.dirname(HERE)
KEY = {'O':'a','3':'b','C':'c',')':'d','.':'e','F':'f','G':'g','H':'h',':':'i','J':'j','K':'k',
       'L':'l','M':'m','V':'n','Q':'o','P':'p','X':'q','7':'r','2':'s','T':'t','U':'u','>':'v',
       'Y':'y',"'":"'",'PO':'(','PC':')'}
SPECIAL = {'@=[ea]': '[ea]', '7@=r?': 'r?'}  # the overwritten word of B15, printed as uncertain
def tok(t):
    if t in SPECIAL: return SPECIAL[t]
    if '=' in t:
        s, r = t.split('=')
        return r.rstrip('?').upper() if t.endswith('?') else r.rstrip('?')
    if t not in KEY: sys.exit('unknown sign %r' % t)
    return KEY[t]
ref = json.load(open(os.path.join(HERE, 'source-sha256.json')))
for rel, h in ref.items():
    if hashlib.sha256(open(os.path.join(CDIR, rel), 'rb').read()).hexdigest() != h:
        sys.exit('HASH MISMATCH: ' + rel)
print('source hashes OK (%d files)' % len(ref))
out = []; n = w = 0; cnt = {}
for raw in open(os.path.join(HERE, 'transcription.txt'), encoding='utf-8'):
    raw = raw.strip()
    if not raw or raw.startswith('#'): continue
    label, body = raw.split(' ', 1)
    words = [x.split() for x in body.split(' / ')]
    n += sum(map(len, words)); w += len(words)
    for x in words:
        for t in x:
            if '=' in t: cnt[t] = cnt.get(t, 0) + 1
    text = ' '.join(''.join(tok(t) for t in x) for x in words)
    out.append(text); print('%-4s %s' % (label, text))
print('\nFULL:', ' '.join(out))
print('STATS: %d lines, %d words, %d sign tokens, unmapped=0, contextual=%s' % (len(out), w, n, cnt))
print('(unmapped=0 only means every sign has a key value; contextual signs are readings, not certainties)')
print('(upper-case R = caret or arch sign where r is expected; f[ea]r? = uncertain overwritten word; see SOLUTION.md)')
