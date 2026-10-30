"""hcp-1479: decode the PARTIAL dot-position (Rosicrucian-style) Pigpen transcription.

Run from the repo root:
    python3 -I ciphers/hcp-1479/work/decode.py

Grid (cell shape -> three letters; the dot's horizontal position L/C/R picks one):
    ABC | DEF | GHI
    JKL | MNO | PQR
    STU | VWX | YZ
"""
import hashlib
import pathlib
import sys

D = pathlib.Path(__file__).resolve().parent.parent
HASHES = {
    'source/address-large.jpg': '1e848022cd2f29cd181c2f6fddd83fcb7a35839b6e255c7ab17e91ef903bcff0',
    'source/picture-large.jpg': '088a8e6477e8eca0386a15fc07563298967c5a63d325aaa7cf5e24f5ea1105eb',
    'source/metadata.md': 'd805435d3ec1fb2f4834490d80efa7a9ea29632ced7eac4eb067bef4f43922e6',
}
CELLS = {  # shape token -> letters for dot Left, Centre, Right
    'BR': 'ABC', 'B': 'DEF', 'BL': 'GHI',
    'R': 'JKL', 'C': 'MNO', 'L': 'PQR',
    'TR': 'STU', 'T': 'VWX', 'TL': 'YZ',
}
POS = {'L': 0, 'C': 1, 'R': 2}


def main():
    bad = [p for p, h in HASHES.items()
           if hashlib.sha256((D / p).read_bytes()).hexdigest() != h]
    if bad:
        sys.exit('source hash mismatch: ' + ', '.join(bad))
    print('source hashes OK')
    n = unread = 0
    for line in (D / 'work/transcription.txt').read_text().splitlines():
        if not line.strip() or line.startswith('#'):
            continue
        label, body = line.split(':', 1)
        words = []
        for w in body.split('|'):
            out = ''
            for tok in w.split():
                if tok == '?':
                    out += '?'
                    unread += 1
                    continue
                weak = tok.endswith('*')
                shape, pos = tok.rstrip('*').split('.')
                out += CELLS[shape][POS[pos]].lower() if weak else CELLS[shape][POS[pos]]
                n += 1
            words.append(out)
        print(f'{label}: ' + ' '.join(words))
    print(f'{n} glyphs decoded (lowercase = weak reading), {unread}+ glyph slots unread '
          '(R2 street segment count unknown) -> PARTIAL')


if __name__ == '__main__':
    main()
