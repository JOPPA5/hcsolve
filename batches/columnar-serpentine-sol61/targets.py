from experiment import *
if __name__=='__main__':
 controls=json.loads((P/'controls.json').read_text());assert sum(c['exact_best']for c in controls)>=6;rows=[]
 for num in [363,393,345,396,369]:
  f=REPO/f'ciphers/hcp-{num}/work'/('transcription-raw.txt'if num==363 else'transcription.txt');gs=f.read_text().lower().split();header=gs.pop(0)if gs[0].isdigit()else None;ct=''.join(''.join(c if'a'<=c<='z'else'.'for c in g)for g in gs)
  for rev in [False,True]:
   text=ct[::-1]if rev else ct
   for w in range(2,27):
    rem=len(text)%w;kind='beam'if rem==0 else'one-long'if rem==1 else None
    if kind is None or len(text)//w<2:continue
    for up in [0,1]:
     name=f'target-{num}-whole-reverse{int(rev)}-w{w}';candidates=attack(name,text,w,kind,up);r=dict(cipher=num,length=len(ct),width=w,model=kind,whole_reverse=rev,start_up=up,source_transcription=str(f.relative_to(REPO)),excluded_numeric_header=header,original_ciphertext=ct,working_ciphertext=text,erasures=text.count('.'),scope='whole literal body; no indicator omission or glyph replacement',candidates=candidates,all_retained_working_reencrypt_exact=True)
     # Explicit independent comparison in original stream orientation.
     for c in candidates:
      encrypted=encrypt(c['plaintext'],c['readout_columns'],up);assert(encrypted[::-1]if rev else encrypted)==ct
     rows.append(r);(P/'targets.json').write_text(json.dumps(rows,indent=2));print(num,rev,w,up,candidates[0]['score'],candidates[0]['plaintext'],flush=True)
  print('completed cipher',num,'cases',len(rows),flush=True)
