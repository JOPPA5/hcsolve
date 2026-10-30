"""hcp-1797: verify source hashes, decode work/transcription.json (Caesar -1). Run from repo root."""
import hashlib, json, os, datetime
D = 'ciphers/hcp-1797/'
H = {
 'source/picture-large.jpg': 'bb2137002503390d7b85268bec4819e3c2737336a0bd340f372cf9bf0d3728ff',
 'source/address-large.jpg': 'e439192b573b5c1074fb5eae7c1da7a625c23ee987824339985cd4efc0885fd2',
 'work/hires/pc_hcp_478_pic.JPG': 'ac7a9d7b3e36ff418def085c1b303cbc6b0daeef621c02421f8f17427e1c4169',
 'work/hires/pc_hcp_478_adr.JPG': 'abb7574bd0d6cfd7ec7a82444adde9df9b3e68e73f15689dc32f8928dd18cfb8',
}
for f, h in H.items():
    assert hashlib.sha256(open(D + f, 'rb').read()).hexdigest() == h, f
print('source hashes OK:', len(H))
def dec(s):
    return ''.join(chr((ord(c.upper()) - 66) % 26 + 65) if c.isalpha() else c for c in s)
def enc(s):
    return ''.join(chr((ord(c) - 64) % 26 + 65) if c.isalpha() else c for c in s)
n = 0
for line in json.load(open(D + 'work/transcription.json'))['lines']:
    out = []
    for kind, t in line:
        if kind == 'c':
            p = dec(t); assert enc(p).lower() == t.lower(); n += sum(c.isalpha() for c in t); out.append(p)
        elif kind == 'p':
            out.append(t)
        elif kind == 'l':
            out.append('[' + t + ']')
        else:
            out.append('[UNRESOLVED ' + t + ' = ' + dec(t) + ' if shifted]')
    print(' '.join(out))
print('enciphered letters decoded:', n)
print('unresolved group alternative: Wbn =', dec('Wbn'), 'if shifted')
print('1908-01-29 weekday:', datetime.date(1908, 1, 29).strftime('%A'))
