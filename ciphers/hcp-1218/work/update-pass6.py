"""Save the sixth-pass editorial claim. This does not decipher the image."""
from pathlib import Path
import json, html
p=Path(__file__).resolve().parents[1]
r=json.loads((p/'work/reading.json').read_text())
main=('Kedves édes Jolánkám! Kívánom, hogy a legjob[b] kedvében és egésségban találja soraim. '
'Édesem, hogy mulatott tegnap? Remélem, [m]int rendesen, most is jól telt el a vasárnap. '
'Ami engem il[l]et, én el voltam foglalva, mert első vasárnap volt, este pedig a kőműves mulatság volt, '
'és pedig szüreti, de még ilyen ro[s]szu[l] nem mulattam soha, csak ép[p]en […] '
'azt az egyet megjegyzem, hogy [33?]-szor nősültem meg négy leán[n]yal. '
'Tánczolni egyáltalán nem tánczoltam. Mikor megy Berénybe? Az[z]al bezárom soraim, sorait várva.')
eng=('My dear, sweet Jolánka! I hope my lines find you in the best of spirits and in good health. '
'My darling, how did you enjoy yourself yesterday? I hope that, as usual, Sunday went well again. '
'As for me, I was busy, because it was the first Sunday; in the evening there was a masons’ dance, '
'specifically a harvest dance, but I have never enjoyed myself so little, just […] '
'I will just mention that I “married” [33?] times with four girls. I did not dance at all. '
'When are you going to Berény? With that I close my lines, awaiting yours.')
stamp='Tiéd vagyok, e szív, e lélek; kit szeretnék, [ha?] téged nem sze[re]tnélek?'
stamp_en='I am yours, this heart, this soul; whom would I love [if] I did not love you?'
uncertainty=('The main text remains partial at A15–A16: after csake{h|p}en the current visual ledger reads '
'ufogy{i|o?}t / me. The earlier unqualified úgy was not supported by a separately transcribed gy at that position '
'and has been withdrawn. The letter sequence is not yet a coherent phrase. A17 has two digit-like signs, '
'provisionally 33. N01 literally gives sze{r|t?}etel; szeretettel requires more than a doubled t and remains an editorial restoration. '
'For the stamp, the opening Tiéd vagyok, e szív, e lélek now follows the unchanged S01–S03 letters exactly '
'(accents and word boundaries editorial). S05 is h/p plus a/e-shaped bars; ha is strongly supported by the '
'published poetic parallel but not established by pixels alone. S07 reads szetnelek on renewed inspection: '
'the middle shapes are a corner and two short strokes. The editorial sze[re]tnélek supplies re; '
'the omitted signs are not visible. The adaptation and possible writing error must not be replaced by '
'an unqualified copy of the published stanza. No independent review, DONE1, FINAL or register entry.')
r.update(status='partial',reading=main+'\n\nSmall annotation by the address: szeretettel? (editorial restoration; literal sze{r|t?}etel).\n\nUnder the stamp, source-assisted editorial reading: '+stamp,
 english=eng+'\n\nSmall annotation by the address: [with love?].\n\nUnder the stamp, source-assisted translation: '+stamp_en,
 gaps=uncertainty,sixth_pass='2026-10-14; full spatial ledger and source-assisted identification of the adapted Honfidal stanza',
 external_parallel={'author':'Sándor Petőfi','title':'Honfidal','url':'https://www.magyarirok.hu/petofi-sandor/h/honfidal','discovered':'2026-10-14','role':'Published poem used to interpret the stamp, not a published solution of HCP1218.'})
(p/'work/reading.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
old=(p/'SOLUTION.md').read_text()
key=old[old.index('## Working key'):old.index('## Reproduction')]
sol=f'''# HCP1218 — Sunday and a masons’ dance

**Status: partial. Updated 2026-10-14.** The stamp quotation has been identified; one main-text clause remains undeciphered. No independent full-text review has taken place.

## Source and method

The [HC Portal record](https://crypto.hcportal.eu/dashboard/cryptograms/1218), named jolanka106 and dated September 1912, was visibly **Not solved** when captured on 2026-10-12. The postcard is addressed to Tóth Jolánka. General, Description and Attachments were read, and both sides are preserved unchanged in `source/`. See `SOURCES.md` for the URLs and hashes. The status has not been rechecked during this local continuation.

The cipher is a Hungarian graphic monoalphabetic substitution. The alphabet was transferred from HCP1301/HCP1243 and tested against this card. The transcription is manual, with prior plaintext hypotheses known; it is neither blind transcription nor OCR. A complete spatial ledger now covers 22 main rows, seven stamp rows and the address annotation. That coverage does not mean every word has been deciphered.

The editorial text supplies spacing, punctuation and most accents. Brackets indicate significant restored letters or unresolved readings. Ordinary source spelling is retained where useful, including egésségban and tánczolni. All literal row output is in `work/as-seen-decoded.txt`; it takes precedence over editorial normalization for exact character claims.

## Hungarian editorial reading

{main}

Small annotation by the address: szeretettel? (editorial restoration; literal sze{{r|t?}}etel).

Under the stamp, source-assisted editorial reading:

{stamp}

## English translation

{eng}

Small annotation by the address: [with love?].

Under the stamp, source-assisted translation:

{stamp_en}

## Identification of the stamp verse

On 2026-10-14 a search for the already-decoded phrases found Sándor Petőfi’s **Honfidal**, written in Debrecen in January–February 1844. The [published text](https://www.magyarirok.hu/petofi-sandor/h/honfidal) opens:

Tied vagyok, tied, hazám! / E szív, e lélek; / Kit szeretnék, ha tégedet / Nem szeretnélek?

This is an external literary source used during decipherment, not an independently obtained complete plaintext or a previously published solution of this postcard. The card appears to adapt the patriotic stanza for a personal addressee. It omits tied, hazám and has téged rather than tégedet. Those words must not be restored to the card merely because they occur in the poem.

The previous interpretation és [s]zívelelek was a word-boundary error. The unchanged letters in S02–S03, okesziv / elelek, divide exactly as the end of vagyok followed by e szív, e lélek. No extra s or e is needed. This resolves that passage directly, while the literary parallel identifies its likely source.

For S05, ha is the source-assisted preferred reading, but h/p and a/e remain explicitly uncertain in the ledger. Two main red bars and a small lower red mark are visible. For S07, the former F T token sequence did not match the enlarged scan: the visible middle forms are T N, giving szetnelek. The editorial restoration sze[re]tnélek explains the intended conditional verb, but the two supplied letters are not visible. Possible copying or enciphering error remains an interpretation.

## Remaining uncertainty

{uncertainty}

The main clause was retested as fogott meg, fogyott and fojt meg. None accounts securely for the observed signs and line break; none has been promoted into the translation. Repeating an enlarged or colour-thresholded view adds no source detail.

{key}
## Reproduction and evidence boundary

Run from the repository root:

```sh
python3 batches/jolanka-next-five-2026-10-12/visual-ledgers/decode.py 1218
```

This checks the archived address image hash and decodes the manually observed shape tokens into literal row text. It preserves uncertain tokens and does not silently supply letters from the poem. It does not itself read pixels or independently prove the manual transcription. The ledger is `work/as-seen.txt`, its coverage and limitations are in `work/as-seen-provenance.json`, and the earlier excerpt ledger is retained unchanged in `work/as-seen-excerpts.txt`.

`python3 batches/jolanka-next-five-2026-10-12/check_readings.py 1218` checks all three archived source hashes and prints the editorial claim. That second command is an integrity check, not cryptanalysis. Earlier readings are retained in the numbered JSON snapshots, including `reading-before-pass6.json`.
'''
(p/'SOLUTION.md').write_text(sol)
(p/'work/source-comparison.html').write_text('<!doctype html><meta charset="utf-8"><style>body{font:18px system-ui;margin:24px;max-width:1200px}img{max-width:100%}pre{white-space:pre-wrap;line-height:1.6}</style><h1>HCP1218 — partial edition, 2026-10-14</h1><img src="../source/address.jpg"><h2>Hungarian editorial reading</h2><pre>'+html.escape(r['reading'])+'</pre><h2>English</h2><pre>'+html.escape(r['english'])+'</pre><h2>Evidence boundary</h2><p>'+html.escape(uncertainty)+'</p><p>Source-assisted identification: <a href="https://www.magyarirok.hu/petofi-sandor/h/honfidal">Petőfi, Honfidal</a>.</p><h2>Literal decoded rows</h2><pre>'+html.escape((p/'work/as-seen-decoded.txt').read_text())+'</pre>')
