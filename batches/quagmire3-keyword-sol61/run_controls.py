from pathlib import Path
import json,subprocess,time,hashlib
P=Path(__file__).resolve().parent;R=P.parents[1];M=R/'ciphers/hcp-350/work';models={n:{g:float(v) for g,v in (line.split() for line in (M/f'ring-{n}grams.tsv').read_text().splitlines())} for n in [4,5]}
def enc(p,slots,shifts):
 A={c:i for i,c in enumerate(slots)};return ''.join('?' if c=='?' else slots[(A[c]+shifts[i%len(shifts)])%26] for i,c in enumerate(p))
def dec(c,slots,shifts):return enc(c,slots,[(-r)%26 for r in shifts])
def parse(file,ct,n):
 rows=[]
 for line in file.read_text().splitlines():
  score,keyword,slots,rs,p=line.split();shifts=[int(r) for r in rs.split(',') if r];assert len(set(slots))==26 and set(slots)==set('abcdefghijklmnopqrstuvwxyz');assert dec(ct,slots,shifts)==p and enc(p,slots,shifts)==ct;sc=sum(models[n].get(p[i:i+n],-n) for i in range(len(p)-n+1) if '?' not in p[i:i+n]);assert abs(sc-float(score))<.03;rows.append(dict(score=float(score),keyword=keyword,alphabet_slots=slots,absolute_shifts=shifts,plaintext=p,independent_cipher_inverse_exact=True))
 return rows
results=[]
for T in [3,9]:
 folder=P/f'controlT{T}';fixture=json.loads((folder/'planted.json').read_text());start=time.monotonic();prefix=folder/'candidates'
 if not (folder/'candidates-five.txt').exists():
  with (folder/'progress.txt').open('w') as f:subprocess.run([str(P/'search'),str(M),str(folder/'cipher.txt'),str(T),str(P/'alphabets.tsv'),str(prefix)],stdout=f,stderr=f,check=True)
 stages={label:parse(folder/f'candidates-{label}.txt',fixture['erased_ciphertext'],n) for label,n in [('screen',4),('four',4),('five',5)]};chosen=stages['five'][0];expected=fixture['expected_readable_plaintext'];matches=sum(a==b for a,b in zip(chosen['plaintext'],expected) if b!='?');equivalent=all(enc('abcdefghijklmnopqrstuvwxyz',chosen['alphabet_slots'],[chosen['absolute_shifts'][i]])==enc('abcdefghijklmnopqrstuvwxyz',fixture['alphabet_slots'],[fixture['absolute_shifts'][i]]) for i in range(T));r=dict(**chosen,period=T,matching_readable_letters=matches,readable_letters=148,exact_readable_plaintext=matches==148,full_substitution_maps_equal_to_planted=equivalent,erased_plaintext_not_claimed=True,seconds=time.monotonic()-start,truth_used_for_search=False,selection='highest5gram amongtop64fourgramrefinedTRAINkeywordalphabets',planted=fixture,stages=stages);results.append(r);(folder/'result.json').write_text(json.dumps(r,indent=2)+'\n');(P/'results.json').write_text(json.dumps(results,indent=2)+'\n');print(T,matches,r['score'],r['keyword'],r['full_substitution_maps_equal_to_planted'],r['seconds'],flush=True)
manifest=json.loads((P/'manifest.json').read_text());manifest.update(screen='all18098TRAINalphabets, perphaseall26unigrammax then6passfourgramcoordinate',four='top128screen,4starts5000shiftproposals+coordinate',five='top64fourgram,4starts10000shiftproposals+coordinate, topLANGUAGEscore',absolute_shifts='all26possibleineveryclass includingR0; nevernormalized',erasure_positions0=[70,94]);(P/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
