from pathlib import Path
import subprocess,re,json,sys
w=Path(__file__).resolve().parent
out=w/sys.argv[1] if len(sys.argv)>1 else w;out.mkdir(exist_ok=True)
records=json.loads(w.joinpath('controls.json').read_text())
for rec in records:
 name=rec['label'];ct=w/(name+'.txt')
 # Top four published-IDP candidates for complete first stage; one for incomplete stage.
 lines=out.joinpath(name+'.physical-results.txt').read_text().splitlines()[:4 if name.endswith('240') else 1]
 for i,line in enumerate(lines):
  prefix=out/f'{name}.pipeline-{i}';outer=re.search(r'outer=([0-9,]+)',line)[1];mid=line.split()[-1]
  middle=Path(str(prefix)+'.middle.txt');middle.write_text(mid+'\n');k2=Path(str(prefix)+'.outer.txt');k2.write_text(outer+'\n')
  with Path(str(prefix)+'.single.txt').open('w') as out,Path(str(prefix)+'.single-progress.txt').open('w') as err:
   subprocess.run([str(w/'single'),'batches/scoring-sol61','ciphers/hcp-363/work/segmented/bigrams.tsv',str(middle),'20'],stdout=out,stderr=err,check=True)
  inner=re.search(r'key=([0-9,]+)',Path(str(prefix)+'.single.txt').read_text())[1];k1=Path(str(prefix)+'.inner.txt');k1.write_text(inner+'\n')
  with Path(str(prefix)+'.refined.txt').open('w') as out,Path(str(prefix)+'.refine-progress.txt').open('w') as err:
   subprocess.run([str(w/'refine'),'batches/scoring-sol61',str(ct),str(k1),str(k2)],stdout=out,stderr=err,check=True)
  result=Path(str(prefix)+'.refined.txt').read_text().split()[-1];print(name,i,'matches',sum(a==b for a,b in zip(result,rec['plaintext'])),'/',len(result),flush=True)
