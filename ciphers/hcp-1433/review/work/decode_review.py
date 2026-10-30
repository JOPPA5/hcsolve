#!/usr/bin/env python3
"""Reviewer's independent decode of HCP 1433 (written from scratch, round 1).
Marks were re-read by the reviewer from review/work/*.png crops of
source/address.jpg rotated 180 deg; x = approximate pixel column in the
rotated scan of each mark, '/' = separator stroke observed at that point."""
MORSE = {'.-':'A','-...':'B','-.-.':'C','-..':'D','.':'E','..-.':'F','--.':'G',
 '....':'H','..':'I','.---':'J','-.-':'K','.-..':'L','--':'M','-.':'N','---':'O',
 '.--.':'P','--.-':'Q','.-.':'R','...':'S','-':'T','..-':'U','...-':'V','.--':'W',
 '-..-':'X','-.--':'Y','--..':'Z'}
rows = {
 'main1': '... / .... / .- / .-.. / .-..',
 'main2': '.. / ... / . / . / -.-- / --- / ..-',
 'main3': '- / --- / -- / --- / .-. / .-. / ---',
 'main4': '.-- / . / ...- / .',
 # row 5: dot 555, dash 582, [row-4 W|E stroke ends at x601,y435], dot 607,
 # dot 627, / 642, dash 653, dash 675, dash 696 (dark ink), / 712, dot 725,
 # dot 744, dash 770, / 793 (blob on stroke at y441-447), dot 802, dot 828,
 # / 835, dot 854, / 868, then cursive.
 'main5': '.-.. / --- / ..- / .. / .',
 'bot1':  '..-. / --- / -. / -.. / . / ... / -',
 'bot2':  '.-.. / --- / ...- / .',
}
out = {k: ''.join(MORSE[g.strip()] for g in v.split('/')) for k, v in rows.items()}
for k, v in out.items(): print(f'{k:6s} {v}')
print('letters:', sum(map(len, out.values())))
# Alternative segmentations of row 5 considered by the reviewer
alts = {'row-4 stroke also used as row-5 separator': '.- / .. / --- / ..- / .. / .',
        'blob at x~790 = dot after separator': '.-.. / --- / ..- / ... / .',
        'blob at x~790 = dot before separator': '.-.. / --- / ..-. / .. / .',
        'third dash of O taken as print': '.-.. / -- / ..- / .. / .'}
for k, v in alts.items():
    print(f'alt ({k}):', ''.join(MORSE.get(g.strip(), '?') for g in v.split('/')))
