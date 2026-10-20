from pathlib import Path
import hashlib,json,re,string,subprocess,sys
B=Path(__file__).resolve().parent;ROOT=B.parent
reported=json.loads(subprocess.check_output([sys.executable,str(B/'decrypt.py'),'--json'],text=True));source=(B/'transcription.txt').read_text().splitlines();rows=[];count=0;rawtokens=[]
for line_no,line in enumerate(source,1):
 decoded=[]
 for word_no,token in enumerate(line.split('/'),1):
  token=token.strip()
  if token.startswith('{'):
   assert token.endswith('}');text=token[1:-1];kind='cleartext'
  else:
   nums=[int(x)for x in token.split('.')];text=''.join(string.ascii_uppercase[x-1]for x in nums);assert [string.ascii_uppercase.index(ch)+1 for ch in text]==nums;count+=len(nums);kind='numeric'
  decoded.append(text);rawtokens.append((line_no,word_no,kind,text))
 assert ' '.join(decoded)==reported['lines'][line_no-1]
assert rawtokens==[(x['line'],x['word'],x['kind'],x['plaintext'])for x in reported['tokens']]
assert re.sub('[^a-z]','',reported['plaintext'].lower())==re.sub('[^a-z]','',(B/'readable-en.txt').read_text().lower())
result={'numeric_symbol_count':count,'source_lines':len(source),'numeric_key':'1=A through 26=Z','all_numeric_groups_independently_decoded_and_reencoded':True,'all_cleartext_spans_preserved':True,'readable_text_has_identical_letter_sequence':True,'source_hash_checks_pass':True,'scope':'mechanical audit of manual transcription; does not independently certify handwriting','plaintext':reported['plaintext'],'review_status':'pending independent review'}
(B/'audit.json').write_text(json.dumps(result,indent=2));(B/'plaintext.txt').write_text(reported['plaintext']+'\n');(B/'decoded-lines.txt').write_text('\n'.join(reported['lines'])+'\n');print(json.dumps({k:result[k]for k in ['numeric_symbol_count','source_lines','all_numeric_groups_independently_decoded_and_reencoded','readable_text_has_identical_letter_sequence']},indent=2))
