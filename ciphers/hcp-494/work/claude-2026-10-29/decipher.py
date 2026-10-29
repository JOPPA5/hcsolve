"""HCP 494: decipher the two letter-cipher passages and list the nomenclator codes.

Single reproduction command (from the repository root):

    python3 ciphers/hcp-494/work/claude-2026-10-29/decipher.py

Inputs, all unchanged files in source/:
  source/bourdeau/ct.txt     Bourdeau's token transcription of the two letter-cipher passages
  source/bourdeau/codes.txt  the 26 numeric nomenclator codes with the manuscript glosses

Key: HCP key 255 (HStAM 4 d Nr. 1234, 1666), letter table only. Each letter has five
numeric homophones (base + 10*r, r = 0..4), a doubled-capital homophone, and there are
syllable signs; 1-19 are nulls. The key's own word list (180-407) does not fit this
letter, so the numeric codes are reported with their manuscript glosses, not decoded.

Three glyph decisions override Bourdeau's transcription, each documented in SOLUTION.md
(sections "Passage 1", "Passage 2") and in work/claude-2026-10-29/panel-summary.md:
  passage 1 token 16  BB -> PP   (= n, not z)   single-bow P, as "Proposition"/"Praedicat"
  passage 2 token 1   55 -> II   (= g, not h)   two tall descending strokes, no numeral bowl
  passage 2 token 19  XX as drawn (= u); the intended text is ff (ablauff), one letter slip
The script prints both the literal decipherment (signs as drawn) and the intended reading.
"""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[2]          # ciphers/hcp-494
SRC = ROOT / 'source' / 'bourdeau'

# --- key 255 letter table ---------------------------------------------------
LETTERS = 'abcdefghiklmnopqrstuwxyz'
BASES = [20, 22, 24, 26, 28, 21, 23, 25, 27, 29, 70, 72, 74, 76, 78, 71, 73, 75, 77, 79, 120, 122, 124, 126]
KEY = {str(b + 10 * r): L for L, b in zip(LETTERS, BASES) for r in range(5)}
KEY.update(dict(zip('CC DD EE FF GG HH II KK LL MM NN OO PP QQ RR SS TT UU WW XX YY ZZ AA BB'.split(), LETTERS)))
KEY.update({str(n): '' for n in range(1, 20)})      # nulls
KEY.update({'[st]': 'st', '[tt]': 'tt', '[I]': 'll', '[ll]': 'll', '[au]': 'au', '[ff]': 'ff'})

# --- glyph decisions (passage index, token index): (token as drawn, intended token) ----
DRAWN = {(0, 16): 'PP', (1, 1): 'II', (1, 18): '[au]'}   # re-identified signs, as drawn
INTENDED = {(1, 19): '[ff]'}                            # terminal XX read as the intended ff


def passages():
    rows = [l.split() for l in (SRC / 'ct.txt').read_text().splitlines()
            if l.strip() and not l.startswith('#')]
    assert rows[0][16] == 'BB' and rows[1][1] == '55' and rows[1][18] == '8' and rows[1][19] == 'XX', rows
    return rows


def decode(row, p, intended):
    out = []
    for i, tok in enumerate(row):
        tok = DRAWN.get((p, i), tok)
        if intended:
            tok = INTENDED.get((p, i), tok)
        if re.fullmatch(r'\[\d+\]', tok):
            out.append('<%s>' % tok.strip('[]'))
        else:
            out.append(KEY[tok])
    return ''.join(out)


def codes():
    for l in (SRC / 'codes.txt').read_text().splitlines():
        if l.startswith('#') or not l.strip():
            continue
        m = re.match(r'(\S+)\s+(\d+)\s+(.*?)\s{2,}(.*?)\s{2,}(\S.*)$', l)
        yield m.group(1), m.group(2), m.group(3).strip(), m.group(4).strip()


if __name__ == '__main__':
    rows = passages()
    print('# Letter-cipher passages, key 255 letter table')
    for p, row in enumerate(rows):
        print(f'passage {p + 1} literal  : {decode(row, p, False)}')
        print(f'passage {p + 1} intended : {decode(row, p, True)}')
    print()
    print('# Reading (clear text in plain type, deciphered in brackets, codes with their glosses)')
    print('Totaliter [disgustirt. Undertan in] <634 Holstein>, nun so wohl als in <601 Dennemarck> Adell, Bürger und Bauren ...')
    print('... insidiosus hostis <768 Sueco>: [Gott geb das all wol ablauff]   (last sign drawn as XX = u)')
    print()
    print('# Nomenclator codes in order (value = manuscript gloss, not key 255; see SOLUTION.md for 447/602)')
    for page, code, gloss, reading in codes():
        print(f'{page:4} {code:>4}  {reading:32} gloss: {gloss}')
    sys.exit(0)
