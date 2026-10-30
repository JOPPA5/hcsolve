#!/usr/bin/env python3
"""HCP 1457: verify source hashes, decode the Morse stroke text and the pig-Latin margin.
Run from the repo root:
  python3 -I ciphers/hcp-1457/work/decode.py
"""
import hashlib, os, re, sys

D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
HASHES = {
    'source/address-large.jpg': '68150dbf7c77154b688ece2db724f377ad6d684004b400944f8d05a9c6557f21',
    'source/picture-large.jpg': 'c6cac8ce4c650c822c47a6f30ee9139b512a9ff893e9577e669785ecd92a633a',
}
MORSE = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G',
    '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N',
    '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U',
    '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y', '--..': 'Z',
}

def check_hashes():
    ok = True
    for rel, h in HASHES.items():
        got = hashlib.sha256(open(os.path.join(D, rel), 'rb').read()).hexdigest()
        print(('OK   ' if got == h else 'FAIL ') + rel)
        ok &= got == h
    return ok

def lines(name):
    for raw in open(os.path.join(D, 'work', name), encoding='utf-8'):
        raw = raw.split('#', 1)[0].strip()
        if raw:
            tag, body = raw.split(':', 1)
            yield tag.strip(), body.strip()

def decode_morse():
    out = []
    for tag, body in lines('transcription-morse.txt'):
        words = []
        for w in body.split('/'):
            letters = []
            for tok in w.split():
                if tok == 'STOP':
                    letters.append('.')
                elif tok in MORSE:
                    letters.append(MORSE[tok])
                else:
                    sys.exit(f'unknown Morse group {tok!r} in {tag}')
            words.append(''.join(letters))
        txt = ' '.join(words)
        print(f'{tag}: {txt}')
        out.append(txt)
    return ' '.join(out)

def unpig(seg):
    """stem+moved+a  ->  moved+stem  (pig-Latin variant with suffix 'a')."""
    stem, moved, a = seg.split('+')
    assert a == 'a', seg
    assert re.fullmatch(r'[^aeiou\[\]]+|\[[^aeiou]\]', moved), seg
    return (moved + stem).replace('[', '').replace(']', '')

def decode_margin():
    out = []
    for tag, body in lines('transcription-margin.txt'):
        words, lit = [], []
        for tok in body.split():
            core = tok.rstrip('.,?')
            tail = '' if tok == 'P.C.' else tok[len(core):]
            if tok == 'P.C.':
                words.append(tok); lit.append(tok); continue
            parts = core.split('-')                      # syllable-wise words (eba-orefa)
            words.append(''.join(unpig(p) for p in parts) + tail)
            lit.append('-'.join(p.replace('+', '') for p in parts) + tail)
        txt = ' '.join(words)
        print(f'{tag}: {" ".join(lit)}\n    -> {txt}')
        out.append(txt)
    s = ' '.join(out)
    return re.sub(r'(^|\. )([a-z])', lambda m: m.group(1) + m.group(2).upper(), s)

if __name__ == '__main__':
    if not check_hashes():
        sys.exit('source hash mismatch')
    print('\n== Address side (Morse strokes) ==')
    a = decode_morse()
    print('\n== Picture side margin (pig Latin) ==')
    b = decode_margin()
    print('\n== Full plaintext ==')
    print(a.replace(' .', '.'))
    print(b.replace('P.C. This', 'P.C. this'))
