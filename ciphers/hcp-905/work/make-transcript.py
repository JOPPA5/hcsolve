"""Materialize the MANUAL glyph classification; not OCR or cryptanalysis.
Coordinates are approximate original-image centers. The operator classified each
shape against source crops, using the disclosed transferred Pigpen key. Readable
letters below are an economical notation for those human shape classes.
"""
import json,hashlib
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
key={'SE':'A','S':'B','SW':'C','E':'D','O':'E','W':'F','NE':'G','N':'H','NW':'I','SE.':'K','S.':'L','SW.':'M','E.':'N','O.':'O','W.':'P','N.':'R','NW.':'S','I':'T','V':'U','LT':'V','UP':'W','UP.':'Z','SEum':'Ä','Vum':'Ü'}
inv={v:k for k,v in key.items()};inv['J']='NW'
# Each center array was manually placed using the original coordinates; boxes
# intentionally provide context rather than claim pixel-perfect segmentation.
rows=[
(63,[('JA',[322,347]),('VERD',[397,425,457,489]),('NICHT',[655,674,701,734,755]),('EINMAL',[815,840,875,899,927,951])],"JA - VERD....! NICHT - EINMAL -"),
(119,[('DIR',[320,340,366]),('KANN',[412,435,455,479]),("ICH'S",[534,561,589,623]),('MEHR',[673,702,735,762]),('RECHT',[805,836,868,900,926])],"DIR - KANN - ICH'S - MEHR - RECHT -"),
(165,[('MACHEN',[318,348,370,401,429,460]),('WIE',[509,533,566]),('DEINE',[625,656,683,706,738]),('LETZTE',[796,823,853,872,898,924])],"MACHEN, WIE - DEINE - LETZTE, -"),
(217,[('IM',[299,324]),('ÜBRIGEN',[375,408,437,466,488,507,541]),('JA',[586,611]),('WIE',[656,677,706]),('AUCH',[764,792,812,842]),('DIE',[901,925,956])],"IM - ÜBRIGEN - JA, - WIE - AUCH - DIE -"),
(257,[('ANDERN',[294,322,347,381,410,435]),('ZWEI',[490,520,550,576]),('KÜNSTLERKARTEN',[617,644,676,699,721,747,776,807,822,849,876,897,924,953])],"ANDERN - ZWEI - KÜNSTLERKARTEN, -"),
(299,[('SEHR',[292,314,341,369]),('HÜBSCHE',[420,450,483,509,535,567,600]),('[CANCELLED]',[630]),('UND',[664,698,725]),('DAHER',[780,808,836,865,892]),('VON',[934,957,982])],"SEHR - HÜBSCHE [CANCELLED] - UND - DAHER - VON -"),
(343,[('MIR',[290,312,337]),('MIT',[389,411,434]),('HERZLICHEM',[483,510,539,563,590,614,637,659,693,721]),('DANK',[780,806,839,857]),('ENT',[907,940,960])],"MIR - MIT - HERZLICHEM - DANK - ENT="),
(385,[('GEGENGEDOMMENE',[290,310,336,361,398,427,450,480,515,542,570,596,625,652]),('IN',[692,724]),('ETWAS',[776,805,824,850,872]),('MERK',[906,940,960,984])],"GEGENGEDOMMENE, IN - ETWAS - MERK="),
(428,[('WÜRDIGEM',[327,350,377,400,425,456,480,502]),('TONE',[550,575,602,630]),('ABGEFASSTE',[681,712,751,781,813,836,867,895,920,950])],"WÜRDIGEM - TONE - ABGEFASSTE -"),
(470,[('SONNENKARTE',[45,80,113,140,169,199,216,240,265,288,313]),('ICH',[370,395,425]),('BIN',[494,518,550]),('FROH',[602,640,674,698]),('DASS',[760,785,815,840]),('ICH',[903,926,956])],"SONNENKARTE. ICH - BIN - FROH, DASS - ICH -"),
(512,[('SIE',[44,73,102]),('SELBST',[164,195,228,256,274,296]),('VOM',[350,386,410]),('POSTBOTEN',[472,506,535,563,594,622,648,678,710]),('ENTGEGEN',[775,805,829,855,885,910,941,966])],"SIE - SELBST - VOM - POSTBOTEN - ENTGEGEN="),
(551,[('NAHM',[46,75,101,126]),('AUHSERDEM',[182,199,226,250,285,321,355,384,411]),('MUHS',[459,488,519,544]),('ICH',[603,630,658]),('JEDE',[722,751,795,818]),('VER',[874,901,936])],"NAHM. - AUHSERDEM - MUHS - ICH - JEDE - VER="),
(590,[('ANTWORTUNG',[44,68,90,110,136,169,192,212,235,266]),('FÜR',[315,345,378]),('KÜDINGHOVENER',[407,426,448,475,505,541,566,591,622,641,666,694,718]),('FILIAL',[805,832,861,888,911,946])],"ANTWORTUNG - FÜR - KÜDINGHOVENER - FILIAL="),
(626,[('POSTVERHÄBTNISSE',[36,68,91,108,125,151,180,207,231,261,284,307,334,359,389,423]),('ABLEHNEN',[478,503,530,559,587,608,635,660]),('SCHLUHS',[700,726,752,774,799,820,843]),('U',[880]),('KUHS',[920,938,958,982])],"POSTVERHÄBTNISSE - ABLEHNEN. SCHLUHS - U. - KUHS")]
result=[];pos=0
for ri,(y,words,literal) in enumerate(rows,1):
 out=[]
 for word,xs in words:
  chars=['?'] if word=='[CANCELLED]' else [c for c in word if c.isalpha()]
  assert len(chars)==len(xs),(ri,word,len(chars),len(xs))
  glyphs=[]
  for char,x in zip(chars,xs):
   pos+=1
   g={'id':pos,'shape':None if char=='?' else inv[char],'center':[x,y],'bbox':[max(x-14,0),y-20,min(x+14,1024),y+21],'status':'cancelled' if char=='?' else 'active'}
   if char=='?':g['note']='Two heavy vertical cancellation strokes cross a geometric field. Top/right/bottom strokes remain visible, of the E/O (⊐/□) family; no interior dot visible. Left boundary and underlying letter unasserted. Not an active plaintext letter.'
   if pos==156:
    assert char=='D'
    g['note']='Undotted E/⊐ cell, literal D. Position153 provides a dotted N control. GEGENGEDOMMENE is retained; GEGENGENOMMENE only editorially restores the dropped dot.'
   if ri==14 and char=='B' and x==261:g['note']='Undotted cup. Literal B, not L; editorial reading of compound is POSTVERHÄLTNISSE.'
   if ri in (12,14) and char=='H' and x in (226,519,820,958):g['note']='Undotted cap: literal H. Repeated HS sequence is not silently repaired to SS or sharp s.'
   glyphs.append(g)
  out.append({'notation':word,'glyphs':glyphs})
 result.append({'row':ri,'y':y,'literal_with_editorial_J':literal,'words':out})
d={'provenance':'Manual shape transcription of own source scans; transferred omitted-J Pigpen key from HCP995/HCP1016 disclosed. No OCR. J is editorial choice for shared I/J cell. Coordinates approximate; bounding boxes may overlap.','sha256':{name:json.loads((ROOT.parents[1]/'batches/easy-2026-10-28/source-sha256.json').read_text())[f'ciphers/hcp-905/source/{name}'] for name in ('picture.jpg','address.jpg','metadata.md')},'key':key,'rows':result}
for name,expected in d['sha256'].items():
 assert hashlib.sha256((ROOT/'source'/name).read_bytes()).hexdigest()==expected,(name,'source hash changed')
(ROOT/'work'/'transcript.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
print(f'{pos} positions materialized')
