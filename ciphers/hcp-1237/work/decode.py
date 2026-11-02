"""HCP1237: check source hashes, decode work/ledger.txt with the Jolanka key. Run from repo root:
   python3 -I ciphers/hcp-1237/work/decode.py"""
import hashlib, os, sys
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
H = {'source/picture-large.jpg': '1e0b12ede3bccfff5076ee98bbc497ba720df76deca7ff7e26b9df7f9952f927',
     'source/address-large.jpg': '4c085248ac439638b814179ebb39e59a067a27a630df7ea36f41864a51d606cd',
     'work/hires/cpc_1912-06-30_HU__HU_Jasz-Arokszalas_jolanka-26_pic.jpg': '0486d69be329fb2e5bc85a4e65e68b4a9d094d5851601a8d615e9b107e759370',
     'work/hires/cpc_1912-06-30_HU__HU_Jasz-Arokszalas_jolanka-26_adr.jpg': '4171787131cb8e226dd5a9b5cafe1d8f45f3ca765bb24fa8ab39be6fb7cb720e'}
for f, h in H.items():
    ok = hashlib.sha256(open(os.path.join(D, f), 'rb').read()).hexdigest() == h
    print(('OK  ' if ok else 'BAD ') + f)
    if not ok: sys.exit(1)
print('\nLiteral decipherment, one row per written line (:m = accent mark seen):')
for line in open(os.path.join(D, 'work/ledger.txt'), encoding='utf-8'):
    if not line.strip() or line.startswith('#'): continue
    lab, *toks = line.split()
    out = ''
    for t in toks:
        if t == 'X?': out += '[?]'; continue
        base, _, m = t.partition(':')
        if base not in set('ABCDEFGHIJKLMNOPRSTUVYZ') | {'GY'}: sys.exit('unknown token ' + t)
        out += base.lower() + ("'" if m else '')
    print(f'{lab:>3} {out}')
print('\nNormalized Hungarian (editorial; see SOLUTION.md):')
print(open(os.path.join(D, 'work/normalized.txt'), encoding='utf-8').read())
