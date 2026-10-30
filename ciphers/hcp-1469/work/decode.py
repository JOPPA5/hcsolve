#!/usr/bin/env python3
"""HCP1469 decoder: checks source hashes, decodes work/transcription.txt with the key.
Run from the repo root:  python3 -I ciphers/hcp-1469/work/decode.py
"""
import hashlib, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
CDIR = os.path.dirname(HERE)

KEY = {  # sign code -> letter
    'O': 'a', '3': 'b', 'C': 'c', ')': 'd', '.': 'e', 'F': 'f', 'G': 'g', 'H': 'h',
    ':': 'i', 'J': 'j', 'K': 'k', 'L': 'l', 'M': 'm', 'V': 'n', 'Q': 'o', 'P': 'p',
    'X': 'q', '7': 'r', '2': 's', 'T': 't', 'U': 'u', '>': 'v', 'Y': 'y',
}

def check_hashes():
    ref = json.load(open(os.path.join(HERE, 'source-sha256.json')))
    for rel, h in ref.items():
        got = hashlib.sha256(open(os.path.join(CDIR, rel), 'rb').read()).hexdigest()
        if got != h:
            sys.exit('HASH MISMATCH: %s' % rel)
    print('source hashes OK (%d files)' % len(ref))

def decode_token(tok):
    if '=' in tok:                      # contextual reading of the caret sign
        sign, reading = tok.split('=')
        assert sign == 'V', tok
        reading = reading.rstrip('?')
        return reading.upper() if tok.endswith('?') else reading
    if tok not in KEY:
        sys.exit('unknown sign %r' % tok)
    return KEY[tok]

def main():
    check_hashes()
    lines = []
    ntok = nwords = nw = nr = 0
    for raw in open(os.path.join(HERE, 'transcription.txt'), encoding='utf-8'):
        raw = raw.strip()
        if not raw or raw.startswith('#'):
            continue
        label, body = raw.split(' ', 1)
        toks = [w.split() for w in body.split(' / ')]
        ntok += sum(len(w) for w in toks); nwords += len(toks)
        nw += sum(t == 'V=w' for w in toks for t in w); nr += sum(t == 'V=r?' for w in toks for t in w)
        words = [''.join(decode_token(t) for t in w) for w in toks]
        lines.append((label, ' '.join(words)))
    for label, text in lines:
        print('%-4s %s' % (label, text))
    print()
    print('FULL:', ' '.join(t for _, t in lines))
    print('STATS: %d lines, %d words, %d sign tokens, unknown=0, caret read as w=%d, caret read as r=%d'
          % (len(lines), nwords, ntok, nw, nr))
    print('(upper-case R = caret sign read as r by context; see SOLUTION.md)')

if __name__ == '__main__':
    main()
