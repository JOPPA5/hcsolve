# HCP 1266 (cpc_--09_HU__HU_Jasz Arokszalas_jolanka-83): a railwayman's cipher postcard to Jolánka Tóth

Human solver: Tomáš Pavuk

**Status: deciphered in full except one overwritten sign; independent review 1 verdict REVISE, all findings addressed, no sign value changed.** Report dated 2026-11-01.

## Origin and context

The cryptogram is record 1266 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1266), portal name cpc_--09_HU__HU_Jasz Arokszalas_jolanka-83, part of Tobias Schrödel's collection of cryptographic postcards (private collection). When it was captured on 2026-11-01 the portal listed it as **Not solved**, tagged Postcard and T. Schrödel Collection, category Substitution, language Unknown, location Europe, sender Unknown, recipient Tóth Jolánka, with no date and no transcription or solution attached. No published solution of this card was found or used.

The picture side is a tinted photograph of a couple, with a printed series caption: Szerelem törvénye. 1. §. Bár merre jársz, hű maradj! ("The law of love, § 1: wherever you go, stay faithful!"). It carries no cipher.

The address side is in plain writing in green ink: Szép reményű / Tóth Jolánka / úrleánynak / Jászárokszállás ("To the young lady of fair promise, Jolánka Tóth, Jászárokszállás"). The first line is a reading of a flourished word. The stamp is missing. Inside its printed box and on the left half of the card stands the cipher text: 21 main rows and 6 rows in the stamp box, 330 signs in all, in the same green ink.

Other marks, none of them in cipher: two postmarks, one showing ...OKSZÁLL[ÁS] and an hour or day 9 C. The second has fragments at the top edge, including a rotated numeral (6 or 9), but is not legible as a date. Two lines of purple crayon stand at the upper left; the second probably reads Ferencz, and the first is unread. The year of the card is not known.

![Address side with the cipher text (source/address-large.jpg)](../source/address-large.jpg)

![Picture side (source/picture-large.jpg)](../source/picture-large.jpg)

The card belongs to the family of cipher postcards addressed to Jolánka Tóth, several of which are deciphered in this repository (for example HCP 1212, 1213, 1216, 1217, 1218, 1243 and 1301). HCP 1216 is signed Feri, and its cancellation place is Rákospalota, which also comes up in this card's plaintext. This card itself has no cipher signature. The purple Ferencz and Rákospalota may point to the same man, but the hands were not compared and his identity is not proven.

## Method

The key was **transferred, not reconstructed**. The solver read all 27 rows sign by sign from enlarged crops of the un-converted high-resolution scan, with no OCR. The family key turned the text into Hungarian at once; the first anchors were ne haragudjon, hogy and nagyon el vagyok foglalva. The result is a sign ledger (one token for each written sign), and a short script checks the hashes of the image files and decodes the ledger.

On enlargement, three things differ from HCP 1216. The g sign has a lightning shape here, and its value is fixed by haragudjon, hogy, nagyon, vagyok, vizsgát, megkezdem. The combinations gy, sz and cs are written as two signs. A few signs are used against their usual value, as listed under Uncertainties.

Hungarian word division and most accents are not in the text and are the editor's. The writer does mark ö, ő and some acutes.

## Key

Cipher type: **MASC + Steganography** (updated 2026-11-03): monoalphabetic substitution, with part of the message hidden in the stamp box under the stamp (now lifted).

Monoalphabetic substitution with invented graphic signs. The names below are conventional labels for handwritten shapes.

| Sign | Letter | Sign | Letter | Sign | Letter |
|---|---|---|---|---|---|
| two bars | a | section mark (S shape) | k | F-like | r |
| six | b | wave | l | right bowl | s |
| left bowl | c | three strokes | m | gamma | t |
| short stroke upper left + long stroke | d | two strokes | n | plain cross X | u |
| three bars | e | cursive loop | o (dots ö, double mark ő) | chevron | v |
| upright cross | f | tall stroke + short tick right | h / p | low or looped descender | y |
| lightning sign | g | dotted crossed curve | i | crossed diagonal with tail | z |
| inverted T | j | | | | |

h and p share one sign, and the choice rests on word sense. d and n are told apart by stroke length.

## Plaintext

Literal decipherment, row by row. `{d=p}` is a d-shaped sign read p, `{h=d}` an h-shaped sign read d, `{?}` the overwritten sign.

```text
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

**Hungarian (normalized).** [ ] marks letters the writer left out, < > a sign read on word sense.

Szeretet[t] édes Jolánkám! Ne haragudjon, hogy soká írok, de nagyon el vagyok foglalva a vasút[t]al. Ma vo[l]tam orvosi vizitán, délután ka<p>om [a] <p>iros zászlót, holnap teszem le [a] fékezői vizsgát, és már csütö[r]tökön utazok is. Evvel megkezdem az új jövőt, édesem. A héten még i[tt] lakom, de jövő hét[en] Rákospalota, <d>e a címet még nem tudom megírni, majd legközelebb bővebben. Isten ve{?}desem (read as: Isten vele, édesem).

In the stamp box (hidden under the stamp, which is now lifted; re-read from the scan on 2026-11-03, every sign confirmed): Gondoljon néha rám, min[t] én önre. Csókolom.

**English.** My beloved sweet Jolánka! Do not be angry that I am so slow to write, but I am very busy with the railway. Today I was at the medical inspection; this afternoon I get the red flag, tomorrow I take the brakeman's exam, and as early as Thursday I am already leaving. With this I begin the new future, my sweet. This week I am still living here, but next week Rákospalota; but I cannot give the address yet, more next time. God be with you, my sweet.

Stamp box: Think of me sometimes, as I do of you. I kiss you.

**Slovak.** Moja milovaná, sladká Jolánka! Nehnevajte sa, že píšem tak neskoro, ale som veľmi zaneprázdnený železnicou. Dnes som bol na lekárskej prehliadke, popoludní dostanem červenú zástavku, zajtra skladám brzdársku skúšku a už vo štvrtok aj cestujem. Tým začínam novú budúcnosť, drahá. Tento týždeň ešte bývam tu, ale budúci týždeň Rákospalota, adresu však ešte neviem napísať, viac nabudúce. S Bohom, drahá.

V rámčeku na známku: Myslite niekedy na mňa, ako ja na Vás. Bozkávam.

## Uncertainties

- **Row 21, the sign after ve.** It is overwritten and heavy, with bars crossed by a stem and a dot above, and it may be a correction of another sign. It gets no value. Isten vele, édesem is an inference from sense: at most one sign stands between ve and desem, so l, e and é cannot all be written there. veled is also possible, though the card otherwise uses formal address.
- **Row 15, még i[tt] lakom.** After the i comes a pale wave ending in a small dot-and-dash that neither solver nor reviewer can explain. The tt is an emendation. mégis lakom is an alternative with a similar sense.
- **Rows 7 and 8, kapom, piros.** Both p's are written with the d-shaped sign, literally kadom, diros. The writer uses the h/p sign for p elsewhere. Word sense and the railway context force p.
- **Row 17, de.** Written with the h-shaped sign. HCP 1216 has the same slip.
- **h/p and d/n.** holnap, palota against haragudjon, hogy, héten, néha, hét rest on word sense. All d/n calls rest on stroke length.
- **Stamp box, min[t].** There is no t and no visible dot on the i, so the i is a shape call.
- **Row 5.** The first sign is smeared at the edge (f by shape and by foglalva). In vasutal two bars touch the gamma, read a from sense.
- **Sentence division at rows 12–13.** The cipher has no word breaks. utazok is. Evvel megkezdem az új jövőt is preferred; utazok is evvel. Megkezdem… ("travelling with it") uses the same signs and is strained.
- **Spellings.** votam is probably the colloquial form vótam, not a slip. czimet is an old spelling, a weak hint at an early date and no evidence for one. Omitted letters and missing ö dots (kozelebb, bovebben, csütötökön) are normalized.
- **Interpretation.** piros zászló is taken as a railwayman's red signal flag. This is plausible but was not checked against a source on period railway practice.
- **Not established.** The date, the first purple line, and the sender's identity.

## Review and what changed

An independent Claude Opus 5.5 reviewer re-ran the reproduction, read all 27 rows itself and decoded them with its own script. All 27 rows matched, 330 signs of 28 types with one unvalued sign; the reviewer had seen the solver's text first, so this was a sighted check. It confirmed the key, the transcription and every disclosed sign call. Its verdict was **REVISE**, because the normalization and translations needed correction:

1. The word ma ("today") was not on the card (row 19 has only the ma of majd). Removed from the Hungarian and both translations.
2. Row 18 begins még ("yet"), with a visible acute, not meg. Corrected; "I cannot give the address yet". Rows 13 and 19 were rechecked and have no acute. The ledger now records the acutes of rows 15 and 18.
3. The sentence was redivided to utazok is. Evvel megkezdem…, replacing a strained "travelling with it". The signs are unchanged.
4. Row 21 now keeps `ve{?}desem`, with vele, édesem stated as an inference.
5. The remaining four minor findings were wording: vótam noted as colloquial, czimet noted as an old spelling, the second postmark described as not legible as a date, and the key described as sharing the letter values of HCP 1216 rather than as unchanged.

No sign value changed.
