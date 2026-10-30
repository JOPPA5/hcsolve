"""Independent check: own sign-level transcription (read from review crops), expansion by whole-word table, diff vs solver."""
import subprocess, re
T=["D..r O.d B.y","Train arrives at Midhurst","9-54. Did M.ss y.u","l..t n.g.t de...e","I went to the Rehearsal","but we did not have","the Pole last night","rather silly I think","yours with love Ada"]
X={"D..r":"Dear","O.d":"Old","B.y":"Boy","M.ss":"miss","y.u":"you","l..t":"last","n.g.t":"night","de...e":"dearie"}
out=[];n=0
for l in T:
    w=[]
    for t in l.split():
        if t in X:
            assert re.fullmatch(t.lower(),X[t].lower()); n+=t.count('.'); t=X[t]
        w.append(t)
    out.append(' '.join(w))
s=subprocess.run(['python3','-I','ciphers/hcp-1331/work/decode.py'],capture_output=True,text=True,cwd='../..' if False else None).stdout.strip().split('\n')
print('identical' if s==out else ('DIFF',s,out),'dots',n, 'letters',sum(c.isalpha() for c in ''.join(out)))
for m in ['t..t']:
    W=sorted({w.strip().lower() for w in open('/usr/share/dict/words')}); print(m,[w for w in W if re.fullmatch(m,w)])
