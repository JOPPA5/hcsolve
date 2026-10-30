# Independent reading: my own transcription keyed from review/work crops, not from work/transcription.json.
import string, json, sys
mine = """Nz Efbsftu Cpz
uxfmwf Xfflt up ebz
uijoht Xjmm Cf
Mppljoh Vq
Gspn Zpvs Mpwjoh
Hjsm Mpp"""
tr = str.maketrans(string.ascii_lowercase, 'zabcdefghijklmnopqrstuvwxy')
n = 0
for l in mine.splitlines():
    n += sum(c.isalpha() for c in l)
    print(l.ljust(24), l.lower().translate(tr).upper())
print('letters', n)
T = json.load(open(sys.argv[1]))
sol = "\n".join(" ".join(w.rstrip('.') for w in l) for l in T['lines'])
print('identical to solver transcription:', sol == mine)
for k in range(26):
    d = str.maketrans(string.ascii_lowercase, string.ascii_lowercase[-k:] + string.ascii_lowercase[:-k] if k else string.ascii_lowercase)
    p = mine.lower().translate(d)
    if k in (0, 1, 2): print(k, p.replace('\n', ' / '))
