"""Prepare bounded substitution scouts; transcripts are NOT source-verified."""
from pathlib import Path
from collections import Counter
import unicodedata, math, json, random, hashlib

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
def fold(s):
    return ''.join(c for c in unicodedata.normalize('NFD',s.lower().replace('ß','ss')) if 'a' <= c <= 'z')
model = HERE/'models/hu'
sentences = [fold(x[9:]) for x in (model/'source/train.conllu').read_text().splitlines() if x.startswith('# text = ')]
for n in (3,4,5):
    counts = Counter()
    for s in sentences: counts.update(s[i:i+n] for i in range(len(s)-n+1))
    den = sum(counts.values()) + .1*26**n
    (model/f'model{n}.tsv').write_text(f'#floor {math.log(.1/den)}\n'+''.join(f'{g}\t{math.log((v+.1)/den)}\n' for g,v in sorted(counts.items())))

# Graphic labels, NOT a claimed Latin-letter transcription. E/A and I/D/N
# distinctions require a further glyph-by-glyph image pass. No ciphertext
# is generated from guessed plaintext. UPPERCASE labels are graphic names.
samples = {
 1243: [
  'S Z E R E T E T T E D E S J O L A N',
  'K E M T U N A T O M D O G S Z E',
  'R E N C S E S E N M E G E R K E Z',
  'T E M M I N D J A R T A Z U T B A',
  'T A L A L K O Z T A M A V V A L',
  'A Z E G E N N E L K I N E K A Z T',
  'A L A D O T A N T A M D E O Z A Z T',
  'A L I R J A D O G O B E N O B',
  'T A Z T A L A N O T L A D A T',
  'D O G M E G M E G K A N J A',
  'L E N E T T O G N E M'],
 1301: [
  'K E D V E S J O L E N K A M D O G',
  'T E L T A L A V A S A R H A D J A',
  'R E M E L E M J O L A M I N D E M',
  'O L E T E L E Q J O L T A L T M E R T',
  'N E M V O L E G Q D E R C Z S Z A',
  'B E D I D O M D E L U T E N S O L',
  'O T I Q V A L A S Z T M E N Q Z U E S'],
 917: [
  '##θΠ42 42**4-y##44*',
  'H614221e 11 4884e θ2θ612 1e*θ6 e15θ* HLee1-1*1 f1*2θe',
  'xθf4h4e Π3e19θ H6f4h4e Π3e19θ* 3ee15θ21# 22444*',
  '2*3-64-Π3e19 223e*1-θθ6 Π1-1θ4 121-yθ2θ6e19 2244e45θ ###244',
  '3912 θ123-64 2244e45#56#4e 69y *4e422θθ-6θe*θ212L']
}
for n,rows in samples.items():
    path=ROOT/f'ciphers/hcp-{n}/work'
    raw = '\n'.join(rows)+'\n'
    (path/'graphic-scout.txt').write_text(raw)
    chars = sorted(set(c for c in raw if not c.isspace() and c!='-'))
    alphabet = {c:chr(97+i) for i,c in enumerate(chars)}
    assert len(chars)<=26, (n,len(chars))
    ct = ''.join(alphabet[c] for c in raw if c in alphabet)
    (path/'scout.txt').write_text(ct+'\n')
    (path/'scout-labels.json').write_text(json.dumps({'labels':alphabet,'length':len(ct),'status':'tentative graphic transcription, not verified','coverage':'selected rows only; remaining rows not transcribed'},ensure_ascii=False,indent=2)+'\n')
    if n==917:
        body=''.join(alphabet[c] for row in rows[1:] for c in row if c in alphabet)
        (path/'scout-body.txt').write_text(body+'\n')
        (path/'scout-reverse.txt').write_text(ct[::-1]+'\n')

test = [fold(x[9:]) for x in (model/'source/test.conllu').read_text().splitlines() if x.startswith('# text = ')]
pt=''.join(test[:5])[:260]
key=list('abcdefghijklmnopqrstuvwxyz');random.Random(9171243).shuffle(key)
ct=''.join(key[ord(c)-97] for c in pt)
(HERE/'control.txt').write_text(ct+'\n')
(HERE/'control-plain.txt').write_text(pt+'\n')
(HERE/'provenance.json').write_text(json.dumps({'model':'UniversalDependencies/UD_Hungarian-Szeged/master, training split only','test':'test split, first 5 sentences, first 260 folded letters','control_seed':9171243,'control_encryption_key':''.join(key),'scouts':'Graphic labels assigned manually from images; known bad/ambiguous glyph distinctions prevent a final claim. Search results are hypotheses only.','source_hashes':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in (model/'source').glob('*.conllu')}},indent=2)+'\n')
print([(n,json.loads((ROOT/f'ciphers/hcp-{n}/work/scout-labels.json').read_text())['length']) for n in samples])
