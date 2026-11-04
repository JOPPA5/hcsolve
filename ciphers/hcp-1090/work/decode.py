# hcp-1090: decode the Morse transcription. Run from the repo root:
#   python3 -I ciphers/hcp-1090/work/decode.py
# Checks the SHA-256 of the source scans, decodes work/transcription.txt column by column
# (reading order c15 -> c00), prints the literal letter stream and the edited plaintext.
import hashlib, os, re, sys

D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
HASHES = {
    'source/picture-large.jpg': '67a6a5d05161ae15752cefff1cc0cb0648a2d9b2bc81a6c0c5db01803dd37685',
    'source/address-large.jpg': 'b83dc73809b0b8fb3991801ef1fd5331611b5d52033a354f6a25f5c4dd9b234e',
    'work/hires/cpc_1911-04-01_DE_Oppenau_DE_Goggingen__pic.jpg': 'd9b42b690a94e9f115cc8dda7062028318f4298c22db1c9c2d13c94b8a5800b6',
    'work/hires/cpc_1911-04-01_DE_Oppenau_DE_Goggingen__adr.jpg': '713c0f6adff79413966a62329f994de95e7b8ea477f69daddd517f085b99aae6',
}
for p, h in HASHES.items():
    got = hashlib.sha256(open(os.path.join(D, p), 'rb').read()).hexdigest()
    print('hash', 'OK ' if got == h else 'BAD', p)
    if got != h: sys.exit(1)

# German Morse of the period; the writer's own sign "....." (five dots) is used for H
# (six times; standard H "...." never occurs on the card); "----" = CH.
MORSE = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G',
         '.....': 'H', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M',
         '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
         '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y', '--..': 'Z',
         '.-.-': 'Ä', '---.': 'Ö', '..--': 'Ü', '----': 'CH'}

cols = []
for line in open(os.path.join(D, 'work/transcription.txt'), encoding='utf-8'):
    m = re.match(r'(c\d\d): (.*)', line)
    if m: cols.append((m.group(1), m.group(2)))
cols.sort(key=lambda c: -int(c[0][1:]))      # rightmost column first

words = []
for name, body in cols:
    out = []
    for w in body.split(' / '):
        letters = []
        for t in w.split():
            if t == '[u:]': letters.append('u'); continue      # plain-script Kurrent u (hook only; ü inferred), not Morse
            letters.append(MORSE[t.strip('{}')])
        out.append(''.join(letters))
    print('%s  %-40s %s' % (name, body[:40], ' '.join(out)))
    words.append(out)

# words continue across column ends where the line breaks inside a word
literal = ' | '.join(' '.join(w) for w in words)
print('\nLITERAL (| = column end):\n' + literal)

flat = []
joins = {'c06': True, 'c05': True, 'c08': True, 'c07': True, 'c03': True}  # column starts inside a word
for (name, _), w in zip(cols, words):
    if flat and joins.get(name): flat[-1] += w[0]; flat.extend(w[1:])
    else: flat.extend(w)
text = ' '.join(flat)
print('\nLETTER STREAM:\n' + text)

# Editorial emendation, disclosed in SOLUTION.md: GRuHSE -> GRÜSSE (Kurrent u read as ü; the five-dot sign, i.e. Morse 5, stands for S here: writer's slip).
EMEND = [('GRuHSE', 'GRÜSSE')]
for a, b in EMEND: text = text.replace(a, b)
PUNCT = [('ERNST', 'ERNST!'), ('DIR', 'DIR?'), ('HIER', 'HIER!'), ('LANGWEILIG', 'LANGWEILIG.'),
         ('BALD', 'BALD.'), ('WIEDERSEHEN', 'WIEDERSEHEN.'), ('DEINE', 'DEINE')]
t2 = text.split()
for a, b in PUNCT:
    t2 = [b if x == a else x for x in t2]
print('\nPLAINTEXT (emended, punctuation editorial):\n' + ' '.join(t2))
