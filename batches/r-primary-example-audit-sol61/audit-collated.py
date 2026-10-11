from pathlib import Path
import json
b=Path(__file__).resolve().parent;data=json.load(open(b/'collated-transcription.json'))
def enc(text,labels):
 assert sorted(labels)==list(range(1,len(labels)+1));w=len(labels);columns=[text[j::w]for j in range(w)];return ''.join(columns[labels.index(rank)]for rank in range(1,w+1))
records=[]
for a,c in [('stage1','stage2'),('stage2','stage3')]:
 source=''.join(data[a]['rows']);got=enc(source,data[a]['labels']);expected=''.join(data[c]['rows']);records.append(dict(from_stage=a,to_stage=c,length=len(got),computed_rows=[got[i:i+len(data[c]['labels'])]for i in range(0,len(got),len(data[c]['labels']))],scan_rows=data[c]['rows'],exact=got==expected,differences=[dict(index=i,computed=x,scan=y)for i,(x,y)in enumerate(zip(got,expected))if x!=y]));print(records[-1])
final=enc(''.join(data['stage3']['rows']),data['stage3']['labels']);print('final',' '.join(final[i:i+5]for i in range(0,len(final),5)));(b/'collated-stage-check.json').write_text(json.dumps(dict(stages=records,computed_final_ciphertext=final,computed_final_groups=[final[i:i+5]for i in range(0,len(final),5)]),indent=2)+'\n')
