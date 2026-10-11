from pathlib import Path
import random
p=Path(__file__).parent
# Explicitly invented text, not historical plaintext and not target crib.
plain='ministerstvozahranicnychveciziadavyslanectvoabybezodkladneoznamilovysledokrokovaniasprislusnymiuradmiprosimeopreverenieplatnosticestovnychdokladovaoza'
assert len(plain)==150
(p/'control-vig-plain.txt').write_text(plain)
for name,key in [('control-vig',[3,10,21,5,17,1,7,22,4]),('control-vig15',[random.Random(334).randrange(26)])]:
 if name=='control-vig15':
  rng=random.Random(334);key=[rng.randrange(26) for _ in range(15)]
 ct=''.join(chr(97+(ord(c)-97+key[i%len(key)])%26) for i,c in enumerate(plain));ct=ct[:70]+'?'+ct[71:94]+'?'+ct[95:]
 (p/(name+'-cipher.txt')).write_text(ct);(p/(name+'-key.txt')).write_text(' '.join(map(str,key)))
