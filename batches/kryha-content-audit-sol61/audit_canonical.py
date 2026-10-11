from pathlib import Path
import json,hashlib,subprocess,re
B=Path(__file__).resolve().parent;R=B.parents[1];variants=json.loads((B/'J-correction-verification.json').read_text())['variants'];expected={x['name']:x for x in variants};records=[]
for n in (350,351):
 folder=R/f'ciphers/hcp-{n}/work/kryha-decipherment';script=folder/'decrypt.py';solution=R/f'ciphers/hcp-{n}/SOLUTION.md';key=json.loads((folder/'key.json').read_text());orig=next(x for x in json.loads((R/'batches/kryha-content-main/proposed-keys.json').read_text())if x['number']==n)
 for k in ['P','O','holes','initial_displacement','adjacent_distances']:assert key[k]==orig[k]
 if n==350:
  src=(R/'batches/kryha-shift23-sol61/350-pixel-strong.txt').read_bytes();assert(folder/'ciphertext.txt').read_bytes()==src;pt=(B/'350-raw-prepared.txt').read_text().strip()
 else:
  assert(folder/'ciphertext.txt').read_bytes()==(B/'351-J-collated-ciphertext.txt').read_bytes();assert(folder/'ciphertext-collated-moderate.txt').read_bytes()==(B/'351-J-collated-I-alternative-ciphertext.txt').read_bytes();assert(folder/'ciphertext-strong.txt').read_bytes()==(R/'batches/kryha-shift23-sol61/351-pixel-strong.txt').read_bytes();pt=expected['J-collated']['raw_prepared']
 cli=subprocess.run(['python3',str(script)],cwd=R,text=True,capture_output=True,check=True).stdout.strip();assert cli.lower()==pt
 literal=re.search(r'```text\s*([A-Z]+)\s*```',solution.read_text()).group(1);assert literal.lower()==pt
 assert (folder/'prepared-plaintext.txt').read_text().strip().lower()==pt
 record=dict(number=n,default_ciphertext_bytes_match_independent_variant=True,functional_key_unchanged=True,default_decoder_exact385=True,SOLUTION_literal_exact385=True,prepared_plaintext_file_exact385=True,default_ciphertext_sha256=hashlib.sha256((folder/'ciphertext.txt').read_bytes()).hexdigest(),key_sha256=hashlib.sha256((folder/'key.json').read_bytes()).hexdigest(),SOLUTION_sha256=hashlib.sha256(solution.read_bytes()).hexdigest())
 if n==351:
  alt=subprocess.run(['python3',str(script),'--variant','collated-moderate'],cwd=R,text=True,capture_output=True,check=True).stdout.strip();assert alt.lower()==expected['J-collated-I-alternative']['raw_prepared'];record['collated_moderate_decoder_exact385']=True
 records.append(record)
(B/'canonical-verification.json').write_text(json.dumps(records,indent=2));print([(r['number'],r['default_decoder_exact385'],r['SOLUTION_literal_exact385'])for r in records])
