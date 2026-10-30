import hashlib, json, sys, collections
B = 'ciphers/hcp-1333/'
H = {'source/address-large.jpg': 'd702018f8a4c181029f1f22e6035d92527b11aa307bd8f0a76c35930bf48d2a8',
     'source/picture-large.jpg': 'abcf1b965f6d5bda238c23b7241451b31164279f077efb1b995dfffe924a9775',
     'work/hires/pc_hcp_14_adr.JPG': 'a55de6010893ca2cd0925858a247debf363137f2021fd82e40f36b566e56429a',
     'work/hires/pc_hcp_14_pic.JPG': '078fdb4a7103f5fa39ecb4dfd9da22ad2b976d6de1367ac5910c73829cf4187b'}
for f, h in H.items():
    assert hashlib.sha256(open(B + f, 'rb').read()).hexdigest() == h, f
print('source hashes OK')
key = json.load(open(B + 'work/key.json', encoding='utf8'))
cnt = collections.Counter(); out = []
for line in open(B + 'work/transcription.txt', encoding='utf8'):
    if line.startswith('#') or not line.strip(): continue
    s = ''
    for t in line.split():
        if t == '/': s += ' '
        elif t == '-': s += '-'
        else:
            sign, val = t.rstrip('!').split('.')
            assert val in key[sign], t
            cnt[sign] += 1; s += val
    out.append(s); print(s)
print('---'); print(' '.join(out).replace('- ', ''))
print('signs:', sum(cnt.values()), dict(cnt.most_common()))
print('signs in classes with two letters:', {k: cnt[k] for k in key if len(key[k]) > 1}, sum(cnt[k] for k in key if len(key[k]) > 1))
