#!/usr/bin/env python3
"""hcp-1145: verify scan hashes, decode work/transcription.txt, assert against the stated reading, print the text."""
import hashlib, os, sys
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
H = {'source/picture-large.jpg': 'c7f3f76d4a501ff71b2ef54200ab814cacbd340a31cb8b14a07560970282bd9e',
     'source/address-large.jpg': 'f4e94d5d3b3d9530a182274056e358c22991257b6f318732879d18860d507d62',
     'work/hires/cpc_1916-02-12_HU_Mezokovesd_HU_Szomolya_szomolya-17_pic.jpg': '6c462e2f265cfe5f500bb86341f99078831fe18dc260491c2bdd0237614141a2',
     'work/hires/cpc_1916-02-12_HU_Mezokovesd_HU_Szomolya_szomolya-17_adr.jpg': 'd1bab5a34ec49c008c9770746562850b0a6e9ad1581576b3b3d57075039f5fdd'}
for p, h in H.items():
    if hashlib.sha256(open(os.path.join(D, p), 'rb').read()).hexdigest() != h:
        sys.exit('HASH MISMATCH ' + p)
print('source hashes OK (%d files)' % len(H))
KEY = {'0': 'o', '0,': 'ö', '1': 'i', '1.': 'a', '1:': 'e', "1'": 'á', ':1': 'ü', '1,': 'b',
       '2,': 'cs', '2.': 'é', '3': 'd', '3,': 'r', '3.': 'v', '4': 'f', '4,': 'g', '4.': 'gy',
       '5': 'h', '5,': 'l', '6': 'j', '6,': 'n', '6.': 'ny', '7': 'k', '7,': 's', '7.': 'sz',
       '8': 'm', '8,': 't', '9': 'p', '9,': 'z'}
PUNCT = {'!', ')', '(', '.'}
# Stated reading, spelled as the writer spelled it (single consonants kept); accents are added by me.
READ = """Édes Margitkám
Értesítlek hogy hacsak lehet vasárnap felmegyünk Pistával szerettem volna ha még addig ot let volna édes
anyám nem is gondoltam hogy haza jöjjön legalább nagyot nézet volna mikor betoppantam volna az ajtón
node ezt most hadjuk majd szóval többet
titkon írok csak levelet
titkon szeretlek tégedet
nincsen nagyobb gyötrelem
mint a titkolt szerelem
akár alva akár ébren
mindig te vagy az eszemben
sokszor ölelve és csókolva maradok hüséges kedvesem és imádód Árpád""".split()
FOLD = str.maketrans({'ó': 'o', 'ő': 'ö', 'í': 'i', 'ű': 'ü', 'u': 'ü', 'ú': 'ü'})
words, n, odd, signs = [], 0, [], set()
for line in open(os.path.join(D, 'work/transcription.txt'), encoding='utf-8'):
    if line.startswith('#') or not line.strip():
        continue
    for w in line.split(';'):
        out = ''
        for t in w.split():
            if t == '-' or t in PUNCT:
                continue
            seen, _, used = t.partition('>')
            if used:
                odd.append((seen, used))
            used = used or seen
            out += KEY[used]; n += 1; signs.add(used)
        words.append(out)
if len(words) != len(READ):
    sys.exit('WORD COUNT %d vs %d' % (len(words), len(READ)))
for w, r in zip(words, READ):
    if w != r.lower().translate(FOLD):
        sys.exit('MISMATCH %r vs %r' % (w, r))
print('%d cipher signs, %d distinct, %d words; %d read by sense: %s' % (n, len(signs), len(words), len(odd), odd))
print('raw decode:', ' '.join(words))
print("""
Mezőkövesd, 1916, II/12.   [date in clear]

[all below enciphered]
Édes Margitkám!
Értesítlek hogy hacsak lehet vasárnap felmegyünk Pistával) szerettem volna ha még addig ot[t] let[t] volna
édes anyám nem is gondoltam hogy haza jöjjön legalább nagyot nézet[t] volna mikor betoppantam volna az ajtón)
node ezt most hadjuk majd szóval többet;

Titkon írok csak levelet
Titkon szeretlek tégedet.
Nincsen nagyobb gyötrelem
Mint a titkolt szerelem

I-> Akár alva akár ébren
Mindig te vagy az eszemben.

Sokszor ölelve és csókolva maradok hüséges, kedvesem, és imádód) (Árpád)

[address in clear] Őnsg. Szépreményű Sziber Margitka kisasszonynak, Borsod m., Szomolya, u. p. (Bogács)""")
