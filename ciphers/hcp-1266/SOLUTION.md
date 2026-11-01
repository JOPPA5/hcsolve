# HCP1266 — Unsigned (Feri?) to Jolánka Tóth: brakeman's exam, new future on the railway, a move to Rákospalota

**Status: complete reading, review 1 (REVISE) addressed.** Claude Opus 5.5, 2026-11-01. No earlier work exists on this number. The portal shows *Not solved* with no transcription or solution; no published solution of this card was found. The transcription here is mine, made from `work/hires/*_adr.jpg` (`source/` holds no transcription).

## Cipher type and key

Hungarian, simple substitution with invented graphic signs: the Jolánka postcard family key, with the same letter values as finished HCP1216 (also 1213, 1217, 1218, 1243, 1301); the writing of digraphs and the shape of g differ (see below the table). The key was transferred, not reconstructed.

| sign | letter | sign | letter | sign | letter |
|---|---|---|---|---|---|
| two bars | a | section mark (S shape) | k | F-like | r |
| six | b | wave | l | right bowl | s |
| left bowl | c | three strokes | m | gamma | t |
| short stroke upper left + long stroke | d | two strokes | n | plain cross X | u |
| three bars | e | cursive loop | o (dots ö, double mark ő) | chevron | v |
| upright cross | f | tall stroke + short tick right | h / p | low descender / looped descender | y |
| lightning sign | g | dotted crossed curve | i | crossed diagonal with tail | z |
| inverted T | j | | | | |

On this card *gy*, *sz*, *cs* are written as two signs (g+y, s+z, c+s). The g sign has the lightning shape; that value is fixed here by *haragudjon, hogy, nagyon, vagyok, fékezői vizsgát, megkezdem*.

## Reproduction (one command, from the repository root)

```sh
python3 -I ciphers/hcp-1266/work/decode.py
```

It checks the SHA-256 of all four image files, decodes `work/ledger.txt` (manual sign-by-sign transcription, 21 main rows plus 6 rows in the stamp box) and prints the literal rows, then `work/normalized.txt`. The crops I read from are in `work/crops/`.

## Literal decipherment (as printed)

```
01 szeretetedesjolan              12 utazokisevel
02 kamneharagudjon                13 megkezdemazuj
03 hogysokairokde                 14 jövötedesemahe
04 nagyonelvagyok                 15 tenmégilakom
05 foglalvaavasutal               16 dejövöhetrakos
06 mavotamorvosivi                17 palota{h=d}eaczimet
07 zitandelutanka{d=p}om          18 mégnemtudom
08 {d=p}iroszaszlot               19 megirnimajdleg
09 holnapteszemle                 20 kozelebbbovebben
10 fekezőivizsgat                 21 istenve{?}desem
11 esmarcsutötokön
stamp box: gondol / jonne / haram / minen / önre / csokolom
```

## Hungarian (normalized)

Szeretet[t] édes Jolánkám! Ne haragudjon, hogy soká írok, de nagyon el vagyok foglalva a vasút[t]al. Ma vo[l]tam orvosi vizitán, délután ka<p>om [a] <p>iros zászlót, holnap teszem le [a] fékezői vizsgát, és már csütö[r]tökön utazok is. Evvel megkezdem az új jövőt, édesem. A héten még i[tt] lakom, de jövő hét[en] Rákospalota, <d>e a címet még nem tudom megírni, majd legközelebb bővebben. Isten ve{?}desem (read as: Isten vele, édesem).

Stamp box: Gondoljon néha rám, min[t] én önre. Csókolom.

([ ] letters the writer left out, supplied; < > a sign read against its usual value on word sense; {?} overwritten sign, kept in place. *vele, édesem* is an inference: l, e and the first é are not written as such; see item 5.)

## English

My beloved sweet Jolánka! Do not be angry that I am so slow to write, but I am very busy with the railway. Today I was at the medical inspection; this afternoon I get the red flag, tomorrow I take the brakeman's exam, and as early as Thursday I am already leaving. With this I begin the new future, my sweet. This week I am still living here, but next week Rákospalota; but I cannot give the address yet, more next time. God be with you, my sweet.
Stamp box: Think of me sometimes, as I do of you. I kiss you.

## Slovak

Moja milovaná, sladká Jolánka! Nehnevajte sa, že píšem tak neskoro, ale som veľmi zaneprázdnený železnicou. Dnes som bol na lekárskej prehliadke, popoludní dostanem červenú zástavku, zajtra skladám brzdársku skúšku a už vo štvrtok aj cestujem. Tým začínam novú budúcnosť, drahá. Tento týždeň ešte bývam tu, ale budúci týždeň Rákospalota, adresu však ešte neviem napísať, viac nabudúce. S Bohom, drahá.
V rámčeku na známku: Myslite niekedy na mňa, ako ja na Vás. Bozkávam.

## Clear text on the card

Address (green ink, plain script): *Szép reményű / Tóth Jolánka / úrleánynak / Jászárokszállás* ("To the young lady of fair promise, Jolánka Tóth"); the first line is my reading of a flourished word and is not part of the cipher. Purple crayon at upper left, two lines: second line reads *Ferencz* probably, first line unread (roughly *Ilole*); it is not in the writer's cipher and I do not claim it. Printed on the picture side: *Szerelem törvénye. 1. §. Bár merre jársz, hű maradj!* The postmarks show ...OKSZÁLL[ÁS] and an hour/day 9 C; year not legible. The second cancellation shows fragments at the top edge, including a rotated numeral (6 or 9), but is not legible as a date.

## Uncertainties

Word-sense calls, stated as the brief asks:

1. **Rows 7, 8: *kapom*, *piros*.** Both p's are written with the d-shaped sign (short stroke left, long right): literally *kadom*, *diros*. The same writer uses the h/p sign for p in *holnap* and *palota*. *piros zászlót* ("red flag") and the railway context force p, but this is a sign used against its usual value in two places.
2. **Row 17: *de*.** Written with the h-shaped sign (literally *he*). *de a címet* is the only reading that gives sense. HCP1216 has the same slip, row 5.
3. **Row 3 etc., h vs p:** *holnap, palota* p and *haragudjon, hogy, héten, néha, hét* h rest on word sense (near-homograph, as in the family).
4. **d vs n:** all d/n calls were made on stroke length (one short plus one long vs two equal). The S4 word *minen* has two short equal strokes, read n.

Other points:

5. **Row 21, the sign after *ve*:** overwritten, heavy, three bars crossed by a stem, with a dot above. I give it no value and keep it in place as `ve{?}desem`. *Isten vele, édesem* is what the sense requires, but that is an inference: at most one sign stands between *ve* and *desem*, so l, e and é cannot all be written there. The sign may be a correction of another sign. *veled* is also possible, though the rest of the card uses formal address. Only this one sign is affected.
6. **Row 15, *mégi lakom*:** after i comes a pale wave (l) ending in a small dot-and-dash I cannot explain; it may be a pen blot or a correction. Normalized *még i[tt] lakom* ("still living here"), which supplies *tt* and is an emendation. An acute stands over the e of *még* (now in the ledger). The alternative *mégis lakom* does not change the sense much.
7. **S4 *min[t]*:** no t and no visible dot on the i. *mint én önre* is the reading; the omitted t is supplied. The i sign's dot is not visible, so i is a shape call.
8. **Row 5 first sign** sits at the very edge and is smeared; f from shape and from *foglalva*. **Row 5, *vasutal*:** the two bars touch the gamma's top bar; read a, not e, from sense.
9. **Row 6 *votam*** is probably not a slip: *vótam* is an ordinary colloquial or dialect form of *voltam*. **Row 17 *czimet*** is an old spelling of *címet*, normalized; it weakly suggests a date before the spelling reform and is not evidence for a date. **Row 1 *szeretet*, *vasutal*, *csütötökön* (row 11: r omitted, u and second o undotted), *kozelebb, bovebben* (row 20, dots not written), *evvel* spelled *evel*:** writer's spellings, normalized. Row 7 and 9 *[a]* are supplied articles. *jövő hét[en]* supplies the ending.
10. **Sense of *piros zászlót*:** I take it as the railwayman's red signal flag; this is interpretation. The sentence division is an editorial choice, since the cipher has no word breaks: *utazok is. Evvel megkezdem az új jövőt* ("With this I begin the new future") is preferred; the alternative *utazok is evvel. Megkezdem…* ("travelling with it") uses the same signs and is strained. The writer marks acutes at some places (*dé-, hé-, még, hét, né, én*), though not everywhere; only the two *még* are recorded in the literal rows. All other acutes are supplied in the normalization.
11. **Sender:** no signature in cipher. Same key as the *Feri* of HCP1216, and the purple *Ferencz* and Rákospalota may fit, but I did not compare the hands and identity is not proven.
12. **Date:** not legible.

## Why it is correct

- The family key's letter values turn every sign into Hungarian except one overwritten sign (item 5) and the marks of item 6; only the g shape needed fixing, and it is consistent at every occurrence.
- The content is specific and internally coherent (railway, medical inspection, signal flag, exam for *fékező*, Thursday travel, move, address to follow), not generic love-letter formula that a forced reading could supply.
- Rákospalota is the cancellation place of HCP1216 in the same correspondence; it is decoded here independently.
- Repeats decode identically: *hogy, vagyok, nagyon*, *megirni/megkezdem*, *jövőt/jövő*, *desem* ×2.

## Response to review 1

Verdict REVISE. All eight findings accepted and fixed. No sign value changed; the only ledger change adds two acute marks. I checked each point on the hires scan.

1. ***ma* not on the card: fixed.** Row 19 is `megirnimajdleg`, one *ma* only, inside *majd*. The Hungarian is now *megírni, majd legközelebb bővebben*; "today" and "dnes" are gone from the translations.
2. **Row 18 *még*: fixed.** The acute over the first e is clear on `review/work/crops/z18.png`. Text and translations now read *a címet még nem tudom megírni*, "I cannot give the address yet". The ledger records `E:acute` in row 18, `work/decode.py` got an acute mark, and *megnem* left the list of repeats. I rechecked the other cases on `work/crops/rev13.png` and z18: row 13 *megkezdem* and row 19 *megírni* have no acute. Row 15 has one, slightly to the right of the e, and is now also in the ledger.
3. **Sentence division: changed as proposed.** *és már csütörtökön utazok is. Evvel megkezdem az új jövőt, édesem.* The signs are unchanged. The earlier division is kept in item 10 as the alternative.
4. **Row 21: fixed.** The normalization now keeps `ve{?}desem` and states *Isten vele, édesem* as an inference; item 5 explains it.
5. ***vo[l]tam*: noted** in item 9 as probably colloquial *vótam*. I keep the bracket form in the normalization because the standard spelling helps the reader.
6. ***czimet*: added** to item 9, with the weak dating remark.
7. **Second cancellation: reworded** to "not legible as a date"; the rotated numeral is mentioned.
8. **"Unchanged": softened** in the key section and in "Why it is correct".

The reviewer's unverified points stay open and are disclosed: the row 15 marks and the *tt* emendation, the row 21 sign, the date, the first purple line, the sender's identity, and the railway sense of *piros zászló*. The command was re-run after the edits: all four hashes OK, and the output matches this file.
