from pathlib import Path
import json,subprocess,sys,time
b=Path(__file__).resolve().parent;r=b.parents[1];data=json.load(open(sys.argv[1]));cts=data['ciphertexts'];O=data['O'];K=data['K'];geom=json.load(open(r/'batches/kryha-wheel-sol61/wheel52.json'));H=[[0]*26 for _ in range(23)]
for i in range(len(cts[0])-1):
 H[i%23][(O[ord(cts[0][i])-97]-23*(i//23))%26]+=1
 H[i%23][(O[ord(cts[1][i+1])-97]-23*(i//23)-K[0])%26]+=1
freq={l:float(v) for l,v in (x.split() for x in (r/'ciphers/hcp-350/work/ring-unigrams.tsv').read_text().splitlines())};values=geom['adjacent_distances']+data['delta']+[freq[chr(97+i)] for i in range(26)]+sum(H,[]);t=time.monotonic();run=subprocess.run([str(b/'enumerate-profile'),str(K[0])],input=' '.join(map(str,values)),text=True,capture_output=True,check=True);out=b/sys.argv[2];out.write_text(run.stdout);print(out,time.monotonic()-t,run.stdout.splitlines()[0])
