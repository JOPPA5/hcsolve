from pathlib import Path
import json,subprocess,time
P=Path(__file__).resolve().parent;R=P.parents[1];M=R/'ciphers/hcp-350/work';model={g:float(v) for g,v in (line.split() for line in (M/'ring-5grams.tsv').read_text().splitlines())}
def enc(p,A,R):
 inv={v:i for i,v in enumerate(A)};return ''.join('?' if c=='?' else chr(97+inv[(A[ord(c)-97]+R[i%len(R)])%26]) for i,c in enumerate(p))
def dec(c,A,R):return enc(c,A,[(-x)%26 for x in R])
rows=[]
for source in json.loads((P/'results.json').read_text()):
 T=source['period'];folder=P/f'controlT{T}'/'post5';folder.mkdir(exist_ok=True);seed=folder/'seed.txt';seed.write_text(' '.join(map(str,source['recovered_alphabet_positions']+source['recovered_absolute_shifts']))+'\n');outfile=folder/'search.txt';start=time.monotonic()
 with outfile.open('w') as f,(folder/'progress.txt').open('w') as log:subprocess.run([str(P/'refine5'),str(M/'ring-5grams.tsv'),str(P/f'controlT{T}'/'cipher.txt'),str(T),'16','50000',str(334350500+T),str(seed)],stdout=f,stderr=log,check=True)
 lines=outfile.read_text().splitlines();A=[int(x) for x in lines[1].split(',') if x];shifts=[int(x) for x in lines[2].split(',') if x];plain=lines[3];assert dec(source['erased_ciphertext'],A,shifts)==plain and enc(plain,A,shifts)==source['erased_ciphertext'];sc=sum(model.get(plain[i:i+5],-5) for i in range(len(plain)-4) if '?' not in plain[i:i+5]);assert abs(float(lines[0].split()[0])-sc)<.025;expected=source['expected_readable_plaintext'];correct=sum(a==b for a,b in zip(plain,expected) if b!='?');r=dict(period=T,alphabet_positions=A,absolute_shifts=shifts,plaintext=plain,matching_readable_letters=correct,readable_letters=148,exact_readable_plaintext=correct==148,score=sc,true_score=sum(model.get(expected[i:i+5],-5) for i in range(len(expected)-4) if '?' not in expected[i:i+5]),seconds=time.monotonic()-start,seed_selection='fixed operative4gram winner for eachcontrol; no truthbasedchoice',independent_cipher_inverse_exact=True,erasures_not_recovered=True);rows.append(r);(folder/'result.json').write_text(json.dumps(r,indent=2)+'\n');print(T,correct,sc,r['true_score'],r['seconds'],flush=True)
(P/'results5.json').write_text(json.dumps(rows,indent=2)+'\n')
