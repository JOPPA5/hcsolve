import run_pair as r
import json,collections
out=[]
for j in range(3):
 folder=r.P/f'control{j}'
 if not(folder/'plant.json').exists():continue
 p=json.loads((folder/'plant.json').read_text());phase=p['phase'];rows=[]
 for filename,order,table in [('result.json',4,r.quad),('result5.json',5,r.five)]:
  f=folder/f'phase{phase}'/filename
  if not f.exists():continue
  v=json.loads(f.read_text());trueP=p['input_slots']if p['sign']==1 else[p['input_slots'][(-i)%26]for i in range(26)];trueO=p['output_positions']if p['sign']==1 else[(-x)%26 for x in p['output_positions']];g=(v['output_positions'][0]-trueO[0])%26;normalO=[(x+g)%26 for x in trueO];normalP=[trueP[(i-g)%26]for i in range(26)];truth=''.join(p['plaintext_messages']);pairs=collections.Counter(a+'>'+b for a,b in zip(truth,v['plaintext_joined'])if a!=b);rows.append(dict(result=filename,exact_plaintext_both=v['plaintext_messages']==p['plaintext_messages'],matching_letters=sum(a==b for a,b in zip(truth,v['plaintext_joined'])),wrong_symbol_pairs=dict(pairs),true_output_positions_matching_up_global_rotation=sum(a==b for a,b in zip(normalO,v['output_positions'])),true_input_slots_matching_up_global_rotation=sum(a==b for a,b in zip(normalP,v['input_slots'])),observed_plaintext_symbols=''.join(sorted(set(truth))),unused_input_letters=''.join(chr(97+i)for i in range(26)if chr(97+i)not in truth),true_frozen_score=sum(table.get(t[i:i+order],-order)for t in p['plaintext_messages']for i in range(len(t)-order+1)),selected_frozen_score=v['language_score'],truth_used_for_search=False))
 out.append(dict(label=f'control{j}',phase=phase,original_sign=p['sign'],diagnostics=rows))
(r.P/'control-diagnostics.json').write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2))
