#!/usr/bin/env python3
"""Round-2 manual transcription of HCP 1528 (all 18 rows, re-read from 3-5x crops
after review 1). Gaps: {H#} = ink hidden under printed foliage (unknown length,
possibly zero); {Q#} = a visible sign whose identity is not secured."""
from pathlib import Path
import json,hashlib,csv,re
R=Path(__file__).resolve().parents[1];W=R/'work'
key=json.loads((W/'key.json').read_text())
data=[
 'fh581 t4g q6 th6r1 84cd5g. b3c85ř8 7c5n cf5 cht5sg3 6 q2cd68 7c5n',
 '75cd5 t3n6. 75 n4 74q 3 r3tm5 85b5, 6fc6g t3c2t b84s5 6 ghg{Q1} m5-',
 '7c32 2b8m5 f b3h6tg2. f b3mt584 q5bd6n c5 85g6h5, qt6 n4 t3f384',
 '74q 74d4 t3 2h6t2. 73 n4 m1m4 m5n3s f5h2c5 m5fr3t. 6p1 n5 cht5sg3',
 'cd3m683 g5 nm5, p1ř q6 q6tm32 s5m2 m5řd58. 4 p18 p1ř c4 fc6g bh68',
 'gt1q nm5 d6g r86f6 p38586, 6p1 nm5 {H1} p183 n5 cht5sg3 6cb3m',
 'm6 řf484 p183, b383q483 cf32 h2sg2',
 'm6 r86f2, p186 p1 nm5 74cd5 p385cd4',
 'bh5cd686. r5qg1 c5 f5 cf4m5ř p6f{H2}',
 '6 f1h4t, bh3c4n, c85sm6 76mg3f6',
 'n5 2sd4f5 b3h2s5m4. m5b3c84',
 'n4 fc6g q5 cf4m 3b5d d6g3f1',
 '84cd5g, 76g3 b3c85tm5, gd5h1 nm5',
 'q6hn32d48. cht5sm1 b3qth6f6',
 'd4c4s t832r1ř, f6cm4f1ř b2c',
 'b3c486 d4 df27 b5b32c,',
 'gd5h1 cd685 fh585',
 'fqb3n4m6.',
]
gaps={'Q1':'R02 last sign of KRK?: g-like sign with trailing hook, not a clear 2/U loop (KRK / KRKU).',
 'H1':'R06 printed foliage blot after ABY MNE; it may or may not hide a sign.',
 'H2':'R09 end of BAV...: ink after p6f runs into the tree at the card edge; ending unknown (bavila? bavíš?).'}
rows=[];positions=[];total=0
for i,cipher in enumerate(data,1):
 out=[];idx=0
 for t in re.findall(r'\{[HQ]\d+\}|.',cipher):
  if t in key: total+=1;idx+=1;positions.append([total,f'R{i:02}',idx,t,key[t]]);out.append(key[t])
  elif t.startswith('{'): out.append('['+t[1:-1]+']')
  else: out.append(t)
 rows.append({'id':f'R{i:02}','cipher':cipher,'plaintext':''.join(out),'units':idx})
rec={'claim':'COMPLETE except three marked gaps','round':2,'manual_transcription':True,
 'notes':'Word spaces/punctuation editorial; diacritics not transcribed. Row boxes of round 1 are in work/v1/transcription.json.',
 'rows':rows,'gaps':gaps}
(W/'transcription.json').write_text(json.dumps(rec,indent=2,ensure_ascii=False)+'\n')
with (W/'positions.csv').open('w') as f:
 w=csv.writer(f);w.writerow(['global_index','row','index_in_row','shape_label','base_plaintext']);w.writerows(positions)
(W/'plaintext.txt').write_text('\n'.join(r['plaintext'] for r in rows)+'\n')
(W/'record-sha256.json').write_text(json.dumps({str((W/f).relative_to(R)):hashlib.sha256((W/f).read_bytes()).hexdigest() for f in ['key.json','transcription.json','positions.csv','plaintext.txt']},indent=2)+'\n')
print(total,'units');print((W/'plaintext.txt').read_text())
