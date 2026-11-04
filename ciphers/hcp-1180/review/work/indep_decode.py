# Independent reviewer decoder for hcp-1180 (Claude Opus 5.5, review round 1).
# Tokenises the transcription differently: regex tokens, fractions first; reports sign stats.
import re, sys, collections
V = {'1':'a','2':'e','3':'i','4':'o','5':'u','1/1':'ä','5/5':'ü'}
src = open(sys.argv[1], encoding='utf-8').read().splitlines()
lines = [l for l in src if l and not l.startswith('#')]
tok = re.compile(r'\[struck:[^\]]*\]|#\d+|\d/\d|[0-9]|[a-zA-Z]|[^\s]')
stats = collections.Counter(); out=[]
for l in lines:
    s=''
    for t in tok.findall(l):
        if t.startswith('[struck'): continue
        if t.startswith('#'): s += t[1:]; continue
        if t in V: s += V[t]; stats[t]+=1; continue
        if t=='V': stats['root']+=1; continue
        if t.isalpha(): s += t; stats['letter']+=1; continue
        if t == '|': s += ' '; continue
        if t == '~': s += '~'; continue
        if t == '!': s += '!'; continue
        stats['null:'+t]+=1
    out.append(s)
text = ' '.join(out).replace('~ ','')
print(' '.join(text.split()))
print(dict(stats), file=sys.stderr)
bad = [d for d in re.findall(r'\d', ' '.join(lines)) if d not in '12345']
print('digits outside 1-5 (excluding #date):', bad, file=sys.stderr)
