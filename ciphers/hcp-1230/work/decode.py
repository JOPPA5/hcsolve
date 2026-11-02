"""HCP1230: verify source hashes, decode the sign ledger with the Jolanka key. From repo root:
   python3 -I ciphers/hcp-1230/work/decode.py"""
import hashlib, os, sys, unicodedata
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
N = 'cpc_1913-12-_HU__HU_Jasz-Arokszalas_jolanka-116_'
HASH = {'source/picture-large.jpg': 'f805df0c22122954f0caf2f7fcbb929560adf340f234b9a48b64a4ae2c7a1e66',
        'source/address-large.jpg': 'df9988954aa5519f2458c41a7046b7e36252ed03b528d5612bdfcfebaaf8ec26',
        'work/hires/' + N + 'pic.jpg': '60fbd2a00d1b37bba8d69f0004c71de2ff1fbeb94526d06e801bf59c98f26b63',
        'work/hires/' + N + 'adr.jpg': 'c3c75b66e733a462f1c652d5e709fc2eb4b8b17a2e9f0ce8b60f28bd1bdb1cb9'}
for f, h in HASH.items():
    got = hashlib.sha256(open(os.path.join(D, f), 'rb').read()).hexdigest()
    print(('OK  ' if got == h else 'BAD ') + f)
    if got != h: sys.exit(1)
KEY = {'A': 'a', 'E': 'e', 'F': 'r', ')': 's', 'K': 'k', '6': 'b', '+': 'f', 'X': 'u', 'Z': 'z', 'G': 'g', 'Y': 'y',
       'CS': 'cs', 'O': 'o', 'I': 'i', 'T': 't', 'J': 'j', 'V': 'v', 'L': 'l', 'M': 'm', 'N': 'n', 'H': 'h', 'D': 'd', 'P': 'p'}
MARK = {'acute': '́', 'diaeresis': '̈', 'double': '̋'}
def dec(tok):
    res = tok.startswith('[') and tok.endswith(']')
    base, _, acc = tok.strip('[]').partition(':')
    if base not in KEY: raise SystemExit('unknown token ' + tok)
    s = unicodedata.normalize('NFC', KEY[base] + MARK[acc]) if acc else KEY[base]
    return f'[{s}]' if res else s
print('\nLiteral decipherment, one row per written line ([x] = restoration):')
n = 0
for line in open(os.path.join(D, 'work/ledger.txt'), encoding='utf-8'):
    if not line.strip() or line.startswith('#'): continue
    lab, *toks = line.split(); n += len(toks)
    print(lab, ''.join(dec(t) for t in toks))
print(f'\n{n} signs decoded')
print('\nNormalized Hungarian (editorial word division, accents and spelling; see SOLUTION.md):')
print(open(os.path.join(D, 'work/normalized.txt'), encoding='utf-8').read())
