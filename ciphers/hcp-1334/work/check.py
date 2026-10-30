#!/usr/bin/env python3
"""hcp-1334: verify hashes, print the card's capitals, test what kind of text they are.
Run from repo root: python3 -I ciphers/hcp-1334/work/check.py
This does NOT produce a plaintext: the letters are word initials (see NOTES.md)."""
import hashlib, math, os, re
D = 'ciphers/hcp-1334/'
H = {'source/picture-large.jpg':'aacd7d15685083b8634fdc6949863c8d253a8a947b640a47a102069afd57d2db',
     'source/address-large.jpg':'0b50a8637cb495a55276e55d0f4b1c6f439042918b69c88eaad1851ef0058160',
     'work/hires/pc_hcp_15_pic.JPG':'a117efc68bc68764db06154933e84146fc5bf8e21593c3417eff45760056501d',
     'work/hires/pc_hcp_15_adr.JPG':'51c491eb1d1bae126a0d2ee5cdadd7c5f341015b5173fc469487bbc947c07cdb'}
for p, h in H.items():
    assert hashlib.sha256(open(D + p, 'rb').read()).hexdigest() == h, p
print('hashes ok')
lines = [l.split() for l in open(D + 'work/transcription.txt') if not l.startswith('#')]
card = ''.join(''.join(l) for l in lines)
print('card', len(card), 'capitals:', ' / '.join(' '.join(l) for l in lines))
# Rough readings of the sister cards made from the small previews, for statistics ONLY (not transcriptions of record).
S = {1322:'MODAAHQSDAOHTTDMLAAHASIWNMLDAWYMMHBOTDFYEDAACEMC',
     1338:'MODAAHQSDHAMRDHYAGOADWELTAFKFYEAADC',
     1339:'MODAAHQSDBARRDHYWGODDWELTAEKFYEDC',
     1335:'MODAAHQSDDNFNTWFMDRDHYAFMBOWFLAKFYDC',
     1336:'MODAAHQSDHYGBADHYAFBAWFLTAFKFYEAADC',
     1337:'MODAAHQSDIWSPTSYDHYAGOADWFLAKFYDC'}
pool = card + ''.join(S.values())
# Approximate standard percentages: letters of running English; first letters of English words.
AB = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
TXT = [8.2,1.5,2.8,4.3,12.7,2.2,2.0,6.1,7.0,.15,.77,4.0,2.4,6.7,7.5,1.9,.1,6.0,6.3,9.1,2.8,1.0,2.4,.15,2.0,.07]
INI = [11.7,4.4,5.2,3.2,2.8,4.0,1.6,4.2,7.3,.5,.6,2.4,3.8,2.3,7.6,4.3,.2,2.8,6.7,16.0,1.2,.8,5.5,.05,.8,.05]
def ll(t, f, sh=0):
    s = sum(f)
    return sum(math.log(f[(AB.index(c) - sh) % 26] / s) for c in t)
for name, t in (('card', card), ('7 cards', pool)):
    print(name, 'n=%d' % len(t), 'top', sorted(((t.count(c), c) for c in set(t)), reverse=True)[:7])
    print('  mean log-lik per letter: running text %.3f, word initials %.3f' % (ll(t, TXT)/len(t), ll(t, INI)/len(t)))
    r = sorted(((ll(t, INI, s), s) for s in range(26)), reverse=True)[:3]
    print('  best Caesar shifts under initials model:', [(s, round(x/len(t), 3)) for x, s in r])
    r = sorted(((ll(t, TXT, s), s) for s in range(26)), reverse=True)[:3]
    print('  best Caesar shifts under running-text model:', [(s, round(x/len(t), 3)) for x, s in r])
    print('  vowels AEIOU: %.1f%%' % (100*sum(t.count(c) for c in 'AEIOU')/len(t)), ' E: %.1f%%' % (100*t.count('E')/len(t)))
print('shared opening MODAAHQSD on all 7:', all(s.startswith('MODAAHQSD') for s in S.values()) and card.startswith('MODAAHQSD'))
