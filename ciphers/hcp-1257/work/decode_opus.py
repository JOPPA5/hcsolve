"""HCP1257: verify source hashes and decode the sign ledger. Run from repo root:
   python3 -I ciphers/hcp-1257/work/decode_opus.py"""
import hashlib, os, sys, unicodedata
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
HASH = {'source/picture-large.jpg': 'ab307a51e775583c4ddae03df107111409ba1873c7cb1923ce25d4bbb361e511',
        'source/address-large.jpg': '31c23fb7ed0fafa529bd1dbf01bbe44c8ae9c037abab5fbce4fb4bddfc371176',
        'work/hires/cpc_--_HU__HU_Jasz-Arokszalas_jolanka-69_pic.jpg': '11acb9444b2d902f1fedcb7207a1bd059a4fb99aa5badf81c49e081e434c920c',
        'work/hires/cpc_--_HU__HU_Jasz-Arokszalas_jolanka-69_adr.jpg': 'b82819aa1c0ecacbad71280ee686f4407fafbe49dbe83e194af05e48c1b87489'}
for f, h in HASH.items():
    got = hashlib.sha256(open(os.path.join(D, f), 'rb').read()).hexdigest()
    print(('OK  ' if got == h else 'BAD ') + f)
    if got != h: sys.exit(1)
KEY = {'F': 'r', ')': 's', 'X': 'u', '6': 'b', '+': 'f', 'H': 'h', 'CS': 'cs',
       'N?': '{n}', 'E?': '{e}', 'L?': '{l}', 'I?': '{i}', 'Y?': '{y?}', 'L~': '{l}', 'A~': '{a}',
       '[blot]': '{blot}', '[o?]': '{o}', '[646]': '{646}', '[D]': '[d]'}
MARK = {'diaeresis': '̈'}
def dec(tok):
    base, _, acc = tok.partition(':')
    s = KEY.get(base, base.lower() if base.isalpha() else None)
    if s is None: raise SystemExit('unknown token ' + tok)
    return unicodedata.normalize('NFC', s + MARK[acc]) if acc else s
print('\nLiteral decipherment, one row per written line (h stands for the h/p sign; {..} = see SOLUTION.md):')
for line in open(os.path.join(D, 'work/ledger-opus.txt'), encoding='utf-8'):
    if not line.strip() or line.startswith('#'): continue
    lab, *toks = line.split()
    print(f'{lab:>3} ' + ''.join(dec(t) for t in toks))
print('\nNormalized Hungarian (editorial; see SOLUTION.md):')
print(open(os.path.join(D, 'work/normalized-opus.txt'), encoding='utf-8').read())
