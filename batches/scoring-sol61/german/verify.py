from pathlib import Path
import json,hashlib
p=Path(__file__).resolve().parent
out={}
for name in ['control40','holdout43','flat40']:
 pt=(p/(name+'-plain.txt')).read_text();ct=(p/(name+'-cipher.txt')).read_text()
 result=(p/(name+'-result.txt')).read_text().split();key=result[-2];found=result[-1]
 dec=''.join(key[ord(c)-97] for c in ct)
 assert dec==found and len(set(key))==26
 out[name]={'length':len(pt),'exact_plaintext_recovered':found==pt,'correct_characters':sum(a==b for a,b in zip(pt,found)),'whole_result_matches_its_key':True,'score':float(result[0]),'result':found}
report=p/'build-report.json';r=json.loads(report.read_text());r['sources']['de_gsd-ud-test.conllu']=hashlib.sha256((p/'source/de_gsd-ud-test.conllu').read_bytes()).hexdigest();report.write_text(json.dumps(r,indent=2)+'\n')
(p/'verification.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
