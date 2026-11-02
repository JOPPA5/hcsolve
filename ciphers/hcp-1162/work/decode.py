#!/usr/bin/env python3
"""hcp-1162: run from repo root: python3 -I ciphers/hcp-1162/work/decode.py"""
import collections, hashlib, pathlib, re
D = pathlib.Path('ciphers/hcp-1162')
H = {'source/picture-large.jpg': 'f94ef51d6855537885f57fa3eb31f8288c2b269fa2d5ce2c75025ad90720639b',
     'source/address-large.jpg': 'fb7f54d9792e1ec68fe356d83d7d47bb9fe0b61d529af156789843562e928cb3',
     'work/hires/cpc_1916-03-28_HU_Mezokovesd_HU_Szomolya_szomolya-25_pic.jpg': 'a98b2e7166a9bc8e4addf7db8be36625cfc42b3178caa5acf05245094b031429',
     'work/hires/cpc_1916-03-28_HU_Mezokovesd_HU_Szomolya_szomolya-25_adr.jpg': '6eb1c803fd0d1c210b36f2310e175eb07464ba35d6c3b7287a6e6a3fce1cc98b'}
for f, h in H.items():
    assert hashlib.sha256((D / f).read_bytes()).hexdigest() == h, f
print('source hashes OK')
KEY = {'1': 'i', '1.': 'a', '1:': 'e', "1'": 'á', '.1': 'u', ':1': 'ü', '1,': 'b',
       '0': 'o', '0,': 'ö', '2': 'c', '2,': 'cs', '2.': 'é',
       '3': 'd', '3,': 'r', '3.': 'v', '4': 'f', '4,': 'g', '4.': 'gy',
       '5': 'h', '5,': 'l', '5.': 'ly', '6': 'j', '6,': 'n', '6.': 'ny',
       '7': 'k', '7,': 's', '7.': 'sz', '8': 'm', '8,': 't', '9': 'p', '9,': 'z'}
lines = [l for l in (D / 'work/transcription.txt').read_text().splitlines() if l and l[0] != '#']
words, n, odd, used = [], 0, [], collections.Counter()
for l in lines:
    for w in l.split(' / '):
        out = ''
        for t in w.split():
            if t in '!()-':
                continue
            m = re.fullmatch(r'(.+)\{(.+)\}', t)
            n += 1
            if m:
                used[m[1]] += 1; odd.append((m[1], KEY[m[1]], m[2])); out += m[2]
            else:
                used[t] += 1; out += KEY[t]
        words.append(out + ('-' if w.endswith('-') else ''))
txt = ' '.join(words).replace('- ', '')
# Two words cross a line end with no hyphen on the card (lines 19-20, 21-22); joined here by sense.
for a, b in (('édes anyám', 'édesanyám'), ('kedve sed', 'kedvesed')):
    assert txt.count(a) == 1, a
    txt = txt.replace(a, b)
print('decoded (card spelling, no accents beyond the cipher, hyphens joined):')
print(txt)
PT = ("Édes Margitkám! Nagyon fájt a szívem hogy olyan kevés időt tölthettem veled de máskép nem tehettem már a "
      "pontosságot muszáj betartani míg ebe a pokolba leszek mert tudod hogy ez valóságos pokol) Tudod e édesem hogy "
      "gyalog hamarab haza értem volna mint kocsin három negyed nyolcra értünk le) a fuvaros két koronát kért tőlem "
      "de csak egy korona hatvan filért adtam neki) most többet nem írok ha majd írsz írd meg hogy mit beszélt az után "
      "édesanyám számtalanszor ölel és csókol szerető kedvesed (Árpád)")
FOLD = str.maketrans('íóőúű', 'ioöuü')
norm = lambda s: re.sub(r'[^a-záéöü ]', '', s.lower().translate(FOLD)).split()
assert norm(PT) == norm(txt), (norm(PT), norm(txt))
print('\nplaintext (cipher-folded accents restored; compared word by word with the decoded text, card word breaks kept):')
print(PT)
print('Open on card: Mezőkövesd, 1916 [III]/28.')
print('Address (open): Őnsg. / Szépreményű / Sziber Margitka / kisasszonynak / Szomolya / (Borsodm.) u. p. Bogács')
print(f'\n{n} cipher signs, {len(used)} distinct; {n-len(odd)} decode by the table, {len(odd)} off the table, read by sense: {odd}')
print('sign counts:', ' '.join(f'{k}={v}' for k, v in sorted(used.items())))
assert set(used) <= set(KEY) and len(odd) == 1
