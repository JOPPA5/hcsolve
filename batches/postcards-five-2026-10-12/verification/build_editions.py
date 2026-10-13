"""Encode the solver's manually read row editions as named graphic classes.
This is editorial serialization, NOT independent OCR or a blind transcription.
"""
from pathlib import Path
import hashlib,json,unicodedata
ROOT=Path(__file__).resolve().parents[3]
classes={'a':'two-bars','b':'six','c':'left-bowl','d':'joined-two-strokes','e':'three-bars','f':'cross','g':'open-loop-descender','h':'two-tall-strokes','i':'dotted-crossed-curve','j':'inverted-T','k':'section-mark','l':'wave','m':'three-short-strokes','n':'two-short-strokes','o':'cursive-loop','p':'tall-short-stroke','r':'F','s':'right-bowl','t':'gamma','u':'x','v':'chevron','y':'low-descender','z':'crossed-diagonal'}
rows={1301:[
'kedvesjolánkámhogy','teltelavasárnapja','remélemjolamiengem','iletelégjolteltmert','nemvolegyperczsza','b{a|e}didőmdélután3tól','5tigválasztmányiülés','5tól7igtűzoltógya','kolatéseste½9től12ig','amozgószínházbanvol','tamőrségenabólislát','hatjajolánkámédesem','nemmehetemlemajd','jövővasárnapokvetlen','lemegyekdehacsakteheti','jojönfelédesemcsü','tö{rt?}ökönepedőszivel','várvamaradokőszinte','imádoj.tisztelemkedves','mamáját','csokol','jaatá','volból','imádója'],
1243:['szeretettédesjolán','kámtudatomhogysze','rencsésenmegérkez','temmindjártazutba','találkoztamavval','azegyénnelkinekazt','alapotadtamdeőazt','alí{t|r}jahogyőbedob','taaztalapotlehet','hogymégmegkapja','lehethogynem.','egypárszóvalkifejezni','hiddelbabámnemlehet','hogyvagyaszivemheznőve','shogymennyireszeretlek.','{i?}ste[n]veleatávolból','ezentulügyeljeabéjegmelett{i|o?}','számr{a|e?}']}
ys={1301:[(23,61),(56,94),(85,126),(114,151),(147,187),(181,222),(212,258),(249,284),(277,315),(303,348),(335,375),(365,405),(395,433),(423,463),(451,486),(480,514),(509,544),(539,577),(570,602),(587,614)],1243:[(16,59),(60,99),(98,141),(138,184),(184,220),(217,262),(260,299),(292,338),(332,369),(365,409),(404,439),(422,463),(457,495),(486,534),(521,565),(558,595),(580,618),(598,620)]}
# y coordinates are review windows, not segmentation boundaries; handwriting slopes.
for n,lines in rows.items():
 w=ROOT/f'ciphers/hcp-{n}/work'
 if (w.parent/'FINAL').exists():raise SystemExit(f'HCP{n} is FINAL; do not regenerate')
 w.mkdir(exist_ok=True)
 key={v:k for k,v in classes.items()}
 for ch in 'áéíóöőúüű':
  base=unicodedata.normalize('NFD',ch)[0]
  key[classes[base]+':'+unicodedata.name(ch).split('WITH ')[1].lower().replace(' ','-')]=ch
 ledger=[]
 for i,line in enumerate(lines):
  # Braces and brackets remain editorial flags, never silently removed.
  toks=[]
  for ch in line:
   if ch in classes:toks.append(classes[ch])
   elif ch in 'áéíóöőúüű':toks.append(next(k for k,v in key.items() if v==ch))
   else:toks.append('literal:'+ch)
  ledger.append({'row':i+1,'source_window':([14,ys[n][i][0],520,ys[n][i][1]] if i<len(ys[n]) else [790,67,942,234]),'graphic_tokens':toks})
 edition={'source':'../source/address.jpg','sha256':hashlib.sha256((w.parent/'source/address.jpg').read_bytes()).hexdigest(),'provenance':'Manual hypothesis-informed visual reading by solver; graphic tokens serialized from that reading. This is not independent OCR. Row windows permit visual audit. Accents are less secure than consonant classes. Explicit editorial flags survive decoding.','rows':ledger}
 (w/'manual-edition.json').write_text(json.dumps(edition,ensure_ascii=False,indent=2)+'\n')
 (w/'graphic-key.json').write_text(json.dumps(key,ensure_ascii=False,indent=2)+'\n')
