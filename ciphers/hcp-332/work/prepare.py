from pathlib import Path
p=Path(__file__).parent
s=''.join((p/'transcription.txt').read_text().lower().split())
for reading in ['o','d']:
 x=s.replace('ugozr','ug'+reading+'zr')
 for prefix in [True,False]:
  y=x if prefix else x[3:]
  (p/f'target-{reading}-{len(y)}.txt').write_text(y)
# Explicitly invented synthetic control, not historical plaintext or a target crib.
plain=('ziadameopakovaniepredoslehotelegramubezodkladu'+'x')[:43]
assert len(plain)==43
(p/'control-plain.txt').write_text(plain)
key=[7,13,2]
(p/'control-key.txt').write_text('7 13 2')
(p/'control-cipher.txt').write_text(''.join(chr(97+(ord(c)-97+key[i%3])%26) for i,c in enumerate(plain)))
