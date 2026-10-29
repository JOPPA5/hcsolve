"""A separately acquired Lincker letter as a key-family control, not a solve of 494.

Transcriptions were made visually after seeing the manuscript interlinear glosses.
No claim of blind decipherment or independent palaeographic review is made.
"""
from pathlib import Path
import hashlib, json

ROOT = Path(__file__).resolve().parents[1]
ALPHABET = 'abcdefghiklmnopqrstuwxyz'
KEY1235 = {str(41 + 4*i + r): c for i,c in enumerate(ALPHABET) for r in range(4)}
KEY1235['320'] = '<General>'
BASE255 = [20,22,24,26,28,21,23,25,27,29,70,72,74,76,78,71,73,75,77,79,120,122,124,126]
KEY255 = {str(b+10*r): c for b,c in zip(BASE255,ALPHABET) for r in range(5)}
ROWS = [
    ('p3', '45 57 109 44 65 113 55 107 320 46 43 117 54 73 113 133', 'besagter<General>bauditz'),
    ('p4', '47 43 120 56 76 116 135', 'bauditz'),
]
out = []
for page, ciphertext, gloss in ROWS:
    tokens = ciphertext.split()
    literal = ''.join(KEY1235.get(t,'?') for t in tokens)
    alternate = ''.join(KEY255.get(t,'?') for t in tokens)
    out.append({'page':page,'tokens':tokens,'literal_key1235':literal,
                'manuscript_gloss_reading':gloss,'wrong_key255_control':alternate,
                'note':'p3 final number preferred 133; 135 would also decode z in this table.' if page=='p3' else ''})

# Do not silently correct the cipher. Record the one letter discrepancy.
expected = list('besagterbauditzbauditz')
tokens = [t for _,s,_ in ROWS for t in s.split() if t!='320']
assert len(expected)==len(tokens)==22
differences = [{'position':i+1,'token':t,'key1235':KEY1235[t],'gloss':g}
               for i,(t,g) in enumerate(zip(tokens,expected)) if KEY1235[t]!=g]
sources = ['source/arcinsys/key1235-0001.jpg',
           'source/arcinsys/daenemark145-mets.xml'] + [
           f'source/arcinsys/daenemark145-{i:04}.jpg' for i in range(1,6)]
result = {
    'status':'AUXILIARY KEY MATCH; HCP 494 remains unresolved',
    'archive':'HStAM 4 f Staaten D, Daenemark 145, Copenhagen 3 March 1677 (preferred date reading)',
    'catalogue':'https://arcinsys.hessen.de/arcinsys/showArchivalDescriptionDetails.action?archivalDescriptionId=2283126',
    'key':'HStAM 4 d 1235, circa 1670',
    'alphabet':ALPHABET,'key1235':KEY1235,'passages':out,
    'literal_letter_matches_to_gloss':22-len(differences),'letter_tokens':22,
    'differences':differences,
    'interpretation':'Repeated bauditz uses different homophones; 320=General also agrees. The 55 mismatch (d versus gloss e) is explicit, not corrected in literal output. It supports a local copying/enciphering-error hypothesis, but a changed cell is not excluded.',
    'transfer_limit':'This is a different letter alphabet and word list. Do not transfer 55=e or 117=u to HCP 494. Its ERTAZ gap and expanded nomenclator remain unresolved.',
    'source_sha256':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in sources},
}
(ROOT/'work/compare-1677.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(result,ensure_ascii=False,indent=2))
