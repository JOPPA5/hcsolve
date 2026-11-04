"""hcp-904: German written in Greek letters. Run from repo root: python3 -I ciphers/hcp-904/work/decode.py"""
import hashlib, os, sys
D = os.path.dirname(os.path.abspath(__file__))
C = os.path.dirname(D)
HASHES = {
 'source/picture-large.jpg': 'b91bac89c03ea243817bc47e8ef55cfdc7ef69438a929fc7c8ec78981d035282',
 'source/address-large.jpg': '67a86ceaa97ffa4e4dfcfe382798dafd8b7fe5371198f43a54ff0f7c5d53a4a9',
 'work/hires/cpc_1902--_DE_Leipzig_DE_Wolferode-bei-Eisleben__pic.jpg': 'ba4a2c5b4d8ebea90ef8a5d662df499e1f8f48b7b14f198e919e9853dfd37623',
 'work/hires/cpc_1902--_DE_Leipzig_DE_Wolferode-bei-Eisleben__adr.jpg': '397038cf9309cfe8ff4f9cb6c47d790550a3119a854c2a634bbe58cdee228374',
}
for p, h in HASHES.items():
    got = hashlib.sha256(open(os.path.join(C, p), 'rb').read()).hexdigest()
    print(('OK   ' if got == h else 'FAIL ') + p)
    if got != h: sys.exit(1)
KEY = {'α':'a','β':'b','γ':'g','δ':'d','ε':'e','ζ':'z','ʽ':'h','ι':'i','κ':'k','λ':'l','μ':'m',
       'ν':'n','ο':'o','ρ':'r','σ':'s','τ':'t','υ':'u','φ':'f','χ':'ch','Ϝ':'W',
       'Α':'A','Β':'B','Γ':'G','Δ':'D','Ι':'J','Κ':'K','Λ':'L','Μ':'M'}
print()
for line in open(os.path.join(D, 'transcription.txt'), encoding='utf-8'):
    if line.startswith('#'): continue
    out = ''.join(KEY.get(ch, ch) for ch in line.rstrip('\n'))
    print(out)
