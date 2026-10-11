exec((__import__('pathlib').Path(__file__).parent/'base.py').read_text())
import sys
controls=[]
for N in [43,40]:
 for k in [1,2,3]:
  for T in [3,9]:
   rng=random.Random(332610061+N*1000+k*100+T);w,s=rng.choice(eligible);r=[rng.randrange(1,26) for _ in range(T)];offset=50+N*13+k*9+T;p=''.join(held[offset:])[:N];ct=enc(p,s,r,k);assert dec(ct,s,r,k)==p
   folder=P/f'control-N{N}-Q{k}-T{T}';folder.mkdir(exist_ok=True);fixture=dict(keyword=w,slots=s,shifts=r,plaintext=p,ciphertext=ct,heldout_offset=offset,seed=332610061+N*1000+k*100+T,length=N,erasure_positions=[]);(folder/'planted.json').write_text(json.dumps(fixture,indent=2))
   z=search(folder,ct,T,k);z.update(length=N,matches=sum(a==b for a,b in zip(z['plaintext'],p)),full_maps_equal=all(enc(string.ascii_lowercase,z['slots'],[z['shifts'][i]],k)==enc(string.ascii_lowercase,s,[r[i]],k) for i in range(T)),fixture=fixture,truth_used_for_search=False);(folder/'result.json').write_text(json.dumps(z,indent=2));controls.append(z);print('CONTROL',N,k,T,z['matches'],z['full_maps_equal'],z['keyword'],flush=True)
(P/'controls-summary.json').write_text(json.dumps([{key:v for key,v in z.items() if key!='stages'} for z in controls],indent=2))
source=ROOT/'ciphers/hcp-332/work/transcription.txt';ct=''.join(source.read_text().split()).lower();assert len(ct)==43 and ct.startswith('trc');hashes={str(f):hashlib.sha256(f.read_bytes()).hexdigest() for f in [source,ROOT/'ciphers/hcp-332/source/cryptogram.jpg']}
results=[]
for gate in controls:
 N,k,T=gate['length'],gate['kind'],gate['period']
 if gate['matches']!=N:continue
 for glyph in ['o','d']:
  variant=ct if N==43 else ct[3:];pos=30 if N==43 else 27;assert variant[pos]=='o';variant=variant[:pos]+glyph+variant[pos+1:];folder=P/'targets'/f'N{N}-Q{k}-T{T}-glyph{glyph}';z=search(folder,variant,T,k);z.update(length=N,glyph=glyph,conditional_prefix_omission=N==40,ciphertext=variant);(folder/'result.json').write_text(json.dumps(z,indent=2));results.append({key:v for key,v in z.items() if key!='stages'});print('TARGET',N,k,T,glyph,z['score'],z['keyword'],z['plaintext'],flush=True)
assert hashes=={f:hashlib.sha256(Path(f).read_bytes()).hexdigest() for f in hashes}
(P/'target-summary.json').write_text(json.dumps(results,indent=2));(P/'manifest.json').write_text(json.dumps(dict(source_hashes=hashes,source_unchanged=True,dictionary_count=len(alph),dictionary_hash=hashlib.sha256((P/'alphabets.tsv').read_bytes()).hexdigest(),split=bound,all_absolute_shifts_free=True,no_erasures=True,control_gate='highest language-score plaintext exact wholeN; full26 maps additionally disclosed',restricted_family=True),indent=2))
