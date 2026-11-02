"""HCP1227: verify source hashes and decode the sign ledger. Run from repo root:
   python3 -I ciphers/hcp-1227/work/decode.py"""
import hashlib, os, sys
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
H = {'source/address-large.jpg': '3cbf2ec3e0d7c581e7ff6a140a1d822f393d8f0bf708a499595c71857b7dd2cf',
     'source/picture-large.jpg': 'cec8a08dca52d64f9113b336c92eec54959fa967bc63c578d4ba2641f994fe7d',
     'work/hires/cpc_-09-26_HU__HU_Jasz-Arokszalas_jolanka-95_adr.jpg': '0283a539ab92d24d068076aa4a28db7648aa1e28921b996bfe67b7ad3f002464',
     'work/hires/cpc_-09-26_HU__HU_Jasz-Arokszalas_jolanka-95_pic.jpg': '182c7bda9d1932901e841471cf8e7fd69d6ff0164795db5f219fe04451082b54'}
for f, h in H.items():
    ok = hashlib.sha256(open(os.path.join(D, f), 'rb').read()).hexdigest() == h
    print(('OK  ' if ok else 'BAD ') + f)
    if not ok: sys.exit(1)
ACC = {':"': {'o': 'ö', 'u': 'ü'}, ":'": {'a': 'á', 'e': 'é'}}
VALID = set('abdefghijklmnoprstuvyz') | {'cs', '2', '8'}
def dec(t):
    if t == '|': return '{|}'
    if t == '?': return '·'
    if t[0] == '[': return t
    if t[-2:] in ACC: return ACC[t[-2:]][t[:-2]]
    if t not in VALID: raise SystemExit('unknown token ' + t)
    return t
print('\nLiteral decipherment, one row per written line (· = sign lost, [x] = restored):')
n = lost = rest = 0
for line in open(os.path.join(D, 'work/ledger.txt'), encoding='utf-8'):
    if not line.strip() or line.startswith('#'): continue
    lab, *toks = line.split()
    n += len(toks); lost += toks.count('?'); rest += sum(t[0] == '[' for t in toks)
    print(f'{lab:>3} ' + ''.join(dec(t) for t in toks))
print(f'\n{n} tokens, {rest} of them restored, {lost} lost without restoration.')
print('\nNormalized Hungarian (editorial; see SOLUTION.md):')
print(open(os.path.join(D, 'work/normalized.txt'), encoding='utf-8').read())
