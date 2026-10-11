# TENTATIVE handwritten example transcription, not a validated known-answer test.
from pathlib import Path
p=Path(__file__).parent
plain='STAHOVANIEVYSLANECTVANUTNEXPOSLITESEMIHNEDSLUZOBNYVOZXX'
keys=[[7,10,21,3,18,6,20,1,19,15,9,13,5,16,2,17,4,12,8,11,14],[7,15,8,6,18,3,10,9,17,14,2,13,1,19,11,5,12,4,16],[7,20,3,12,6,19,8,16,2,17,1,18,11,5,9,4,10,15,14,13]]
s=plain;out=[]
for i,k in enumerate(keys,1):
 assert sorted(k)==list(range(1,len(k)+1))
 out.append(f'Grid{i} width{len(k)} '+repr([s[j:j+len(k)] for j in range(0,len(s),len(k))]))
 s=''.join(s[k.index(rank)::len(k)] for rank in range(1,len(k)+1))
out.append('Payload '+s)
groups=[s[i:i+5] for i in range(0,len(s),5)];groups.insert(4,'JGEMU');out.append('With figure5 manually read indicator JGEMU: '+' '.join(groups))
(p/'paper-example-reconstruction.txt').write_text('\n'.join(out)+'\n');print('\n'.join(out))
