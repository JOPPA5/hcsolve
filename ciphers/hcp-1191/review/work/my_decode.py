"""Reviewer's independent decoder for hcp-1191: own key table (from reviewer's reading
of the hi-res scan), applied to the solver's sign-code transcription."""
import sys, collections
MYKEY = {  # code -> plain, written by the reviewer from the pixels, not copied from key.tsv
 'Ad':'A','Bt':'B','Ct':'C','cr':'D','Ec':'E','f4':'F','G3':'G','Hc':'H','X':'I',
 'st':'J','kk':'K','dv':'L','Mv':'M','Nb':'N','Qc':'O','p7':'P','pl':'R','Ss':'S',
 'dm':'T','bw':'T','Uc':'U','Wc':'W','pc':'Y','Yq':'?','[I]':'I','[#]':''}
cnt = collections.Counter(); lines = []
for ln in open(sys.argv[1], encoding='utf-8'):
    if ln.startswith('#') or not ln.strip(): continue
    ws = []
    for w in ln.split(' / '):
        s = ''
        for t in w.split():
            if t.isdigit(): s += ' ' + t; continue
            cnt[t] += 1; s += MYKEY[t]
        ws.append(s.strip())
    lines.append(' '.join(ws))
print('\n'.join(lines))
print('signs:', sum(cnt.values()), dict(cnt.most_common()), file=sys.stderr)
