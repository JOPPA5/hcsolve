"""Independent reviewer decoder for hcp-1010 (Claude Opus 5.5, reviewer, 2026-11-03).
Transcription re-read by the reviewer from work/hires/cpc_--_DE__DE_Hier__pic.jpg (crops in review/work/).
Key built independently: A..M without J ascending 1..12, N..Z descending 25..13.
Run: python3 -I ciphers/hcp-1010/review/work/decode_review.py
"""
import string
letters = [c for c in string.ascii_uppercase if c != 'J']
key = {}
for i, c in enumerate(letters[:12]):
    key[i + 1] = c
for i, c in enumerate(letters[12:]):
    key[25 - i] = c
UML = {'A': 'AE', 'U': 'UE', 'O': 'OE'}

T = {
    'A (bottom, upside down)': "4 ?5 21 / 2 18 21 20 ?3 8 5 / 9 20 19 / 10 18u 8 25 5 21 / 8 9 5 21 / 16 9 5 / 20 9 5 / 20 5 8 5 25",
    'B (bottom, upside down)': "16 1 20 / 16 9 21 4 / 16 24 8 11 / 9 12 / 25 1u 3 8 20 19 5 25 / 12 24 12 5 25 19 / 8 9 5 21 / 7 5 20 3 8 5 8 5 25",
    'C (fence boards)': "17 5 21 / 2 24 19 / 5 25 / 5 21 16 5 7",
    # Not in the solver's transcription: digits on the boy's hat brim (read with the card turned 90 deg).
    'D (hat brim, reviewer reading, tentative)': "7 21 18 20 ?20",
    'D-alt (hat brim, if 2nd group is 24)': "7 24 18 20 ?20",
}
for tag, s in T.items():
    words = []
    for w in s.split('/'):
        out = ''
        for tok in w.split():
            unc = tok.startswith('?')
            u = tok.endswith('u')
            n = int(tok.strip('?u'))
            c = key[n]
            if u:
                c = UML[c]
            out += c.lower() if unc else c
        words.append(out)
    print(f'{tag}: {" ".join(words)}')
used = set()
for s in T.values():
    for tok in s.replace('/', ' ').split():
        used.add(int(tok.strip('?u')))
print('numbers used:', sorted(used))
print('(lower case = reviewer could not see the sign clearly)')
