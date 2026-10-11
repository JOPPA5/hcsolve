from pathlib import Path
import json,collections,math
b=Path(__file__).resolve().parent;r=b.parents[1];f=b/'template355';t=json.load(open(b/'framing355-control/control.json'));cts=(f/'ciphertexts.txt').read_text().split();logs=sorted(float(l.split()[1]) for l in (r/'ciphers/hcp-350/work/ring-unigrams.tsv').read_text().splitlines());rows=[]
for line in (f/'template-output.tsv').read_text().splitlines():
 label,sc,key,sh=line.split('\t');O=list(map(int,key.rstrip(',').split(',')));sh=list(map(int,sh.rstrip(',').split(',')));assert sorted(O)==list(range(26)) and sh[0]==0;N=collections.Counter()
 for ct in cts:
  for i,c in enumerate(ct):N[(O[ord(c)-97]-23*(i//26)-sh[i%26])%26]+=1
 counts=sorted(N[i] for i in range(26));v=sum(n*l-math.lgamma(n+1) for n,l in zip(counts,logs));assert abs(v-float(sc))<.012;rows.append(dict(label=label,score=v,overlap=max(sum(o==(p+k)%26 for o,p in zip(O,t['output_positions'])) for k in range(26))))
selected=json.load(open(f/'selected-profile-seeds.json'));sel={z['label'] for z in selected};report=dict(rows_checked=len(rows),max_all_ring_overlap=max(z['overlap'] for z in rows),max_selected_ring_overlap=max(z['overlap'] for z in rows if z['label'] in sel),refined_max=max(z['score'] for z in rows if z['label'].endswith('refined')),rows=rows,diagnostic_only=True);(f/'template-diagnostic.json').write_text(json.dumps(report,indent=2)+'\n');print({k:v for k,v in report.items() if k!='rows'})
