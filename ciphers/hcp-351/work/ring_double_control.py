from pathlib import Path
import json,subprocess,time
p=Path(__file__).resolve().parent;steps=[7,6,7,5,6,7,6,8,6,10,5,6,5,7,6,5,9];body=(p/'double-control-cipher.txt').read_text().strip();assert len(body)==385
(p/'double-control-cipher.txt').write_text(body+'\n');summary=json.loads((p/'double-control-summary.json').read_text()) if (p/'double-control-summary.json').exists() else []
def parse(out):
 lines=out.splitlines();return dict(language_score=float(lines[0].split()[0]),plaintext=lines[0].split()[1],input_slots=[int(x)for x in lines[1].split(',')if x],output_positions=[int(x)for x in lines[2].split(',')if x])
def verify(r,phase,sign):
 I={letter:slot for slot,letter in enumerate(r['input_slots'])};O={slot:letter for letter,slot in enumerate(r['output_positions'])};d=0;ct=[]
 for i,c in enumerate(r['plaintext']):ct.append(chr(97+O[(I[ord(c)-97]+d)%26]));d=(d+sign*(steps[(phase+2*i)%17]+steps[(phase+2*i+1)%17]))%26
 assert ''.join(ct)==body;r['independent_reencryption_exact']=True
for phase in [9]:
 for sign in (1,):
  if any(r['phase']==phase and r['sign']==sign for r in summary):continue
  start=time.monotonic();label=f'double-control-phase{phase}-sign{sign}';folder=p/label;folder.mkdir(exist_ok=True);ic=(folder/'ic-candidates.txt').read_text() if (folder/'ic-candidates.txt').exists() else subprocess.check_output([str(p/'ring_ic_double'),str(p/'double-control-cipher.txt'),str(phase),str(sign),'3000'],text=True);(folder/'ic-candidates.txt').write_text(ic);rows=[]
  missing=[(i,line)for i,line in enumerate(ic.splitlines())if not (folder/f'masc-{i:03}.txt').exists()]
  if missing:
   (folder/'missing-ic-candidates.txt').write_text('\n'.join(line for i,line in missing)+'\n');batch=subprocess.check_output([str(p/'ring_ic_masc_batch_double'),str(p),str(p/'double-control-cipher.txt'),str(phase),str(sign),str(folder/'missing-ic-candidates.txt')],text=True);(folder/'masc-batch-output.txt').write_text(batch);lines=batch.splitlines();assert len(lines)==4*len(missing)
   for j,(i,line) in enumerate(missing):
    assert int(lines[4*j].split()[0])==j;(folder/f'masc-{i:03}.txt').write_text('\n'.join(lines[4*j+1:4*j+4])+'\n')
  for i,line in enumerate(ic.splitlines()):
   parts=line.split();O=[int(x)for x in parts[1].split(',')if x];key=folder/f'output-{i:03}.txt';key.write_text(' '.join(map(str,O))+'\n');out=(folder/f'masc-{i:03}.txt').read_text();r=parse(out);r.update(ic_candidate_index=i,concentration=int(parts[0]));verify(r,phase,sign);rows.append(r)
  rows.sort(key=lambda r:r['language_score'],reverse=True);(folder/'language-reranked.json').write_text(json.dumps(rows,indent=2));row=rows[0];key=folder/'refine-seed-000.txt';key.write_text(' '.join(map(str,row['input_slots']+row['output_positions']))+'\n');out=subprocess.check_output([str(p/'ring_ic_refine_double'),str(p),str(p/'double-control-cipher.txt'),str(phase),str(sign),str(key)],text=True);(folder/'refine-000.txt').write_text(out);r=parse(out);r.update(phase=phase,sign=sign,seed_language_rank=0,ic_candidate_index=row['ic_candidate_index'],masc_score=row['language_score'],candidate_count=len(rows),seconds=time.monotonic()-start);verify(r,phase,sign);summary.append(r);(folder/'refined.json').write_text(json.dumps([r],indent=2));(p/'double-control-summary.json').write_text(json.dumps(sorted(summary,key=lambda r:r['language_score'],reverse=True),indent=2));print('TARGET',phase,sign,'candidates',len(rows),'MASC',row['language_score'],'REFINE',r['language_score'],'seconds',r['seconds'],flush=True)

plain=(p/"double-control-plain.txt").read_text().strip();result=summary[0];result["exact_control"]=result["plaintext"]==plain;result["match_count"]=sum(a==b for a,b in zip(plain,result["plaintext"]));(p/"double-control-verified.json").write_text(json.dumps(result,indent=2));print("CONTROL",result["match_count"],result["exact_control"],flush=True)
