from pathlib import Path
import subprocess,random,json
p=Path(__file__).parent
plain=Path('batches/scoring-sol61/german/heldout200-plain.txt').read_text().strip()[:150]
model=Path('batches/scoring-sol61/german/quadgrams.tsv')
results=[]
for family in ['vigenere','beaufort','porta']:
 for w in (9,15):
  rng=random.Random(33461+w);key=[rng.randrange(13 if family=='porta' else 26) for _ in range(w)]
  def enc(c,k):
   return (c+k)%26 if family=='vigenere' else (k-c)%26 if family=='beaufort' else (13+(c+k)%13 if c<13 else (c-13-k)%13)
  ct=''.join(chr(97+enc(ord(c)-97,key[i%w])) for i,c in enumerate(plain))
  ct=ct[:70]+'?'+ct[71:94]+'?'+ct[95:]
  path=p/f'german-control-{family}-{w}.txt';path.write_text(ct+'\n')
  args=[str(p/'poly-erasures'),str(model),str(path),family,str(w),str(w),'50','30000']
  out=subprocess.check_output(args,text=True);(p/f'german-control-{family}-{w}-results.txt').write_text(out)
  recovered=out.split()[-1];expected=plain[:70]+'?'+plain[71:94]+'?'+plain[95:]
  row={'family':family,'width':w,'key':key,'exact_plaintext':recovered==expected,'known_positions':sum(a==b for a,b in zip(recovered,expected) if b!='?')};results.append(row);print(row,flush=True)
(p/'german-poly-control-results.json').write_text(json.dumps(results,indent=2)+'\n')
if not all(r['exact_plaintext'] for r in results):raise SystemExit('Control gate failed; no targets attempted')
for family in ['vigenere','beaufort','porta']:
 for offset in range(5):
  args=[str(p/'poly-erasures'),str(model),str(p/f'target-phase-{offset}.txt'),family,'1','24','30','20000']
  out=subprocess.check_output(args,text=True);(p/f'german-{family}-phase-{offset}-results.txt').write_text(out)
  print(f'completed {family} gap position {offset}',flush=True)
