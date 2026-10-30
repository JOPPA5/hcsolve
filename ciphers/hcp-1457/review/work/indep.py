# Independent reviewer decoder: own Morse table built from the alphabet order string,
# reads the solver's stroke transcription and a reviewer-written pig-Latin list.
import sys, re
codes = ".- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. --- .--. --.- .-. ... - ..- ...- .-- -..- -.-- --..".split()
T = dict(zip(codes, "ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
n = 0
for line in open(sys.argv[1]):
    line = line.split('#')[0].strip()
    if not line: continue
    tag, body = line.split(':', 1)
    out = []
    for tok in body.split():
        if tok == '/': out.append(' ')
        elif tok == 'STOP': out.append('.')
        else: out.append(T[tok]); n += 1
    print(tag, ''.join(out))
print('letter groups:', n)
# Margin: reviewer's own literal reading; decode by moving the trailing consonant cluster before the final 'a'
lit = "anyma ankstha orfa P.C. istha orningma aveha ou?a eensa attha iewva eba orefa eryva ettypra"
def un(w):
    if w == 'P.C.': return w
    m = re.fullmatch(r'(.*[aeiouy])([^aeiouy]+)a', w)
    return m.group(2) + m.group(1) if m else '<'+w+'>'
print(' '.join(un(w) for w in lit.split()))
