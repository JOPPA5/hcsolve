"""Preserve manual, explicitly partial readings; this is not image recognition."""
from pathlib import Path
import hashlib, json, html

ROOT = Path(__file__).resolve().parents[2]
DATA = {
1218: {
 'title': 'Sunday and a masons’ dance',
 'reading': '''Kedves édes Jolánkám! Kívánom, hogy a legjob[b] kedvében és egésségben találja soraim. Édesem, hogy mulatott […] remélem […] most is jól telt el a vasárnap. Ami engem illet, én el voltam foglalva, mert első vasárnap volt, este pedig a kőműves mulatság volt […] de még ilyen rosszul nem mulattam soha […]. Azt az egyet megjegyzem, hogy […] nég[y] leán[n]yal […]. Táncolni egyáltalán nem táncoltam. Mikor megy Berénybe? Azzal bezárom soraim, sorait várva.

Stamp area: Tiéd vagyok […].''',
 'english': '''My dear, sweet Jolánka! I hope my lines find you in the best of spirits and in good health. My darling, how did you enjoy yourself? […] I hope […] Sunday went well again. As for me, I was busy, because it was the first Sunday; in the evening there was a masons’ dance […], but I have never enjoyed myself so little […]. I will just mention that […] four girls […]. I did not dance at all. When are you going to Berény? With that I close my lines, awaiting yours.

Stamp area: I am yours […].''',
 'gaps': 'The phrase after the question, the venue/name after “mulatság”, the middle anecdote (including possible literal digits), and most of the stamp text remain unresolved. A tentative “33 times married” reading was rejected as insufficiently grounded. The small annotation near the address also remains unread. This is a selected continuous reading with gaps, not a complete diplomatic transcript.',
},
1217: {
 'title': 'Pest, Sándor, the dance school and billiards',
 'reading': '''Kedves Jolánkám! Kívánom, hogy jó kedvében találja soraim. Hogy mulatott vasárnap? Én délelőtt bementem Pestre, voltam Sándornál, de a többivel nem beszélhettem, mert Újpesten voltak. Délután [utra/újra?] elmentem, és ekkor jöttem a táncziskolából, és elmentünk egy [ki…] biliárdozni. Abból lett a vasárnap, és [azzal?] bezárom soraim. Isten vele, édesem.

Stamp area: Isten vele, édesem! Jó mulatást kívánok, és gondoljon néha rám, hű kedvesére.''',
 'english': '''My dear Jolánka! I hope my lines find you in good spirits. How did you enjoy yourself on Sunday? In the morning I went into Pest and visited Sándor, but I could not speak with the others, because they were in Újpest. In the afternoon I went out [again?], and then I came from the dance school, and we went […] to play billiards. That was my Sunday, and [with that?] I close my lines. Farewell, my darling.

Stamp area: Farewell, my darling! I wish you a pleasant time, and think sometimes of me, your faithful sweetheart.''',
 'gaps': 'Almost all of the main message and the stamp-area message are readable, but the first word of main row 12, the short sequence before “biliárdozni” in row 16, and the connector in row 18 need glyph-level resolution. Do not silently expand “ki” to “kicsit”. Accents, missing doubled consonants and punctuation are editorial in the readable version. No DONE marker until the whole symbol transcript has been checked.',
 'rows': '''kedvesjolánkám
kívánomhogyjó
kedvébentalálja
soraimhogymu
latotvasárnap
éndélelőtbemen
tempestrevoltam
sándornáldeatob
bivelnembeszél
hettemmertujpesten
voltakdélután
u[t/j?]raelmentem
ésekkorjöttem
atáncziskolából
éselmentünkegy
ki[…]biliárdozni
abóllettavasár
nap[azzal?]bezárom
soraimistenveleédesem

[stamp]
istenvele
édesemjo
mulatást
kivánok
ésgondol
jonnéha
rámhűked
vesére''',
},
1216: {
 'title': 'Waiting for a letter and hoping to meet again',
 'reading': '''Opening: Szeretett édes Jolánkám! Nem tudom mire vélni, hogy nem ír […].

Middle: […] reményem, hogy van egésséges […] várom, hogy viszontlássam. Múlt héten beszéltem Sándorral, mondta, hogy jól néz ki, mer[t] bizony régen nem láttam […].

Stamp opening: Csókolom számtalanszor […].''',
 'english': '''Opening: My beloved, sweet Jolánka! I do not know what to make of your not writing […].

Middle: […] I hope you are in good health […] I am waiting to see you again. Last week I spoke with Sándor; he said that you look well, for indeed I have not seen you for a long time […].

Stamp opening: I kiss you countless times […].''',
 'gaps': 'Only the quoted passages are claimed. The passage about the Wednesday post, the lower-half travel narrative and the remainder of the stamp text need transcription. A possible place name Györk and a proposed later journey are not established and are omitted from the translation. The green hand is dense; separate tall strokes, short strokes and their accents before adding further words.',
},
1213: {
 'title': 'Easter, Szolnok and visiting the neighbours',
 'reading': '''Szeretet[t] édes Jolánkám! Kívánom, hogy a legjobb egésségben találja soraim. Hogy […] a húsvéti ünnepek? Remélem jól, jobban mint nekem. Első nap voltam Szolnokon, második napon szabad voltam, és így voltam öntöz[ködni?] […] szomszédoknál […].

Later: Sajnálom, édesem, hogy magát nem öntözhettem meg […].''',
 'english': '''My beloved, sweet Jolánka! I hope my lines find you in the best of health. How […] the Easter holidays? Well, I hope—better than for me. On the first day I was in Szolnok; on the second day I was free, so I went [Easter sprinkling?] […] at the neighbours’ […].

Later: I am sorry, my darling, that I could not sprinkle you […].''',
 'gaps': 'The opening question has an uncertain verb. The activity at the row 8 break is not fully transcribed; “Easter sprinkling” is a contextual interpretation supported by the later “öntözhettem”. Most of the lower half and the stamp-area message remain unread. Do not count these omissions as deciphered text. The printed picture-side verse is not an encrypted continuation.',
},
1212: {
 'title': 'Thanks for a letter, a love verse and a dinner',
 'reading': '''Édes Jolánkám! Becses sorait köszönettel megkaptam, melyek örömemre szolgáltak, és az alat[t]i sorokban válaszolok.

[Kivel?] bizonyítsam,
hogy téged szeretlek?
Tanúm […]
mindenséget.
Hogy csak érted élek,
s érted szenvedek,
és [mindennél?] a földön
jobban szeretlek.

A vacsora elég kedélyes volt, és hogy mit […] azt nem értem. Isten vele […].''',
 'english': '''My sweet Jolánka! I have received your valued lines with thanks; they gave me joy, and I reply in the lines below.

[How/with whom?] shall I prove
that I love you?
My witness […]
the universe.
That I live only for you,
and suffer for you,
and love you more
than [anything?] on earth.

The dinner was quite pleasant, and what […] I do not understand. Farewell […].''',
 'gaps': 'The first word of the verse looks like “kivel” under the working key; do not replace it by the grammatically expected “mivel” without a glyph explanation. The line beginning “tanúm” is unresolved and has not been restored from a presumed quotation. The comparative line, the last dinner clause, the footer and the short encrypted annotation by the address remain uncertain. Ordinary cursive annotations are distinct from the cipher. No complete-message claim.',
},
}

if any((ROOT/f'ciphers/hcp-{n}/work/reading.json').exists() for n in DATA):
 raise SystemExit('Initial-pass generator: existing readings must not be overwritten')

key=json.loads((ROOT/'ciphers/hcp-1301/work/graphic-key.json').read_text())
for n,d in DATA.items():
 p=ROOT/f'ciphers/hcp-{n}'
 hashes={f.name:hashlib.sha256(f.read_bytes()).hexdigest() for f in (p/'source').iterdir() if f.is_file()}
 (p/'work/graphic-key.json').write_text(json.dumps(key,ensure_ascii=False,indent=2)+'\n')
 (p/'work/reading.json').write_text(json.dumps({'id':n,'status':'partial','method':'manual visual reading; not OCR or independent verification','source_sha256':hashes,**d},ensure_ascii=False,indent=2)+'\n')
 if 'rows' in d:(p/'work/provisional-rows.txt').write_text(d['rows']+'\n')
 keytable='\n'.join(f'| {shape} | {letter} |' for shape,letter in key.items())
 report=f'''# HCP{n} — {d['title']}

**Status: partial decipherment, not independently reviewed.** Work date: 2026-10-12.

## Source and method

[HC Portal record](https://crypto.hcportal.eu/dashboard/cryptograms/{n}) was visibly **Not solved**. General, Description and Attachments were read. Both postcard sides are preserved in `source/`; the portal supplied no transcription or solution. See `SOURCES.md` for attachment URLs and hashes.

The text is Hungarian written with a graphic monoalphabetic substitution. The working alphabet was transferred from this workspace’s HCP1301/HCP1243 readings and tested manually against this separate card. Repeated greetings and unrelated coherent passages support the transfer; they do not resolve every handwritten symbol. Accents can modify the same base symbol; joined `gy` and `cs` require care.

The following is an editorial reading with spaces and punctuation, not an exact symbol-by-symbol transcript. Square brackets mark alternatives, supplied letters or gaps. No external plaintext was used for these passages. The AI Register search for `jolanka` returned “No matching contributions” among 37 contributions on the work date; that limited check does not prove that no historical solution exists elsewhere.

## Hungarian reading

{d['reading']}

## English translation

{d['english']}

## Uncertainty and remaining work

{d['gaps']}

All five new cards remain partial. No DONE, FINAL, review, or register entry is created by this batch. The picture side was inspected; no handwritten encrypted continuation was identified there.

## Working key

At this scan resolution h/p are near-homographs and sometimes require linguistic context; d/n can also differ only by stroke length. The shape names below describe tendencies, not a guaranteed visual classifier.

| Named graphic class | Letter |
|---|---|
{keytable}

## Reproduction boundary

Run from the repository root:

```sh
python3 batches/jolanka-next-five-2026-10-12/check_readings.py {n}
```

This verifies the archived files against the recorded hashes and prints the saved manual reading. It **does not decipher pixels** or independently validate the proposed text. `work/reading.json` records the claim; `work/top.png`, `bottom.png` and `stamp.png` are enlarged source crops for visual comparison. Full automated reproduction is not yet available, which is another reason not to create a completion marker.
'''
 (p/'SOLUTION.md').write_text(report)
 with (p/'NOTES.md').open('a') as out:
  out.write('\n2026-10-12: Applied the HCP1301/1243 graphic key to the main text and inspected the stamp and both source sides. Saved the partial Hungarian reading and English translation in SOLUTION.md and work/reading.json. '+d['gaps']+'\n')
 (p/'work/source-comparison.html').write_text('<!doctype html><meta charset="utf-8"><title>HCP'+str(n)+' partial reading</title><style>body{font:18px system-ui;margin:25px}img{max-width:100%}pre{white-space:pre-wrap;line-height:1.7}</style><h1>HCP'+str(n)+' — partial manual reading</h1><img src="../source/address.jpg"><pre>'+html.escape(d['reading'])+'</pre><h2>English</h2><pre>'+html.escape(d['english'])+'</pre><h2>Unresolved</h2><p>'+html.escape(d['gaps'])+'</p>')
print('Saved five partial editions with English translations, source hashes and comparison pages.')
