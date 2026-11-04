# HCP 1302 (cpc_--_HU__HU_Jasz Arokszalas_jolanka-78): Feri to Jolánka Tóth

Human solver: Tomáš Pavuk

**Status: deciphered; all 19 main rows and the 6 rows under the stamp read, with one damaged word (népség) restored from sense and disclosed. Independent review 1 verdict ACCEPT, no plaintext word changed.** Report dated 2026-11-02.

## Origin and context

The cryptogram is record 1302 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1302), portal name cpc_--_HU__HU_Jasz Arokszalas_jolanka-78, part of Tobias Schrödel's collection of cryptographic postcards (private collection; see the HistoCrypt proceedings, https://ecp.ep.liu.se/index.php/histocrypt). When it was captured on 2026-10-30 the portal listed it as **Not solved**, tagged Postcard and T. Schrödel Collection, category Substitution, date, language and sender unknown, recipient Tóth Jolánka, with no transcription or solution attached.

The picture side is a tinted photograph of a couple embracing, with a bouquet; it is scanned sideways, carries the printed number 3071/72, and has no cipher text. The whole message is on the address side, in pink ink: 19 rows down the left half and along the bottom edge, and six short rows on the stamp patch, where the stamp is gone and the writing is partly abraded.

The address, in the same pink hand and unenciphered, reads **Szépremény[ű] Tóth Jolánka úrleánynak, Jász-Árokszállás** ("To the fair-hoped Miss Jolánka Tóth, Jászárokszállás"). The end of Szépreményű runs under the cancel: the y is visible, the ű is not. The place is spelt with a flourish after "Jás", and its end runs under the portal seal.

![Picture side (source/picture-large.jpg)](../source/picture-large.jpg)

![Address side with the cipher text, the plain address, the stamp area and the cancels (source/address-large.jpg)](../source/address-large.jpg)

The card belongs to the "Jolánka" family of Hungarian cipher postcards addressed to Jolánka Tóth, several of which are deciphered in this repository (HCP 1212, 1213, 1216, 1217, 1218, 1243, 1298, 1301). They share one key, so this card was read with a **known, transferred key**, not by a new key recovery. The sender signs Feri, as on HCP 1216.

## Method

- **First reading (2026-10-30), Claude Opus 5.5:** the family key from HCP 1216 and 1301 was applied to a sign-by-sign reading from enlarged crops of the high-resolution scan. About 16 rows gave clean Hungarian; the end of row 18, the middle of row 19 and stamp rows S3 to S5 stayed open. No earlier AI work exists on this number, though the family key itself came from cards with earlier OpenAI GPT-6 Astra / GPT-6.1 Sol work.
- **Second reading (2026-11-02), Claude Opus 5.5:** new crops, separate colour channels and a pink-excess map (red minus green) that lifts the erased ink on the stamp area. This completed row 18 (the numeral 20 plus -ikán, then ot majd nem), corrected row 19 (lesz, not legy; viszontlátásra with one s bowl) and read the stamp rows.
- **Review (2026-11-02), a separate Claude Opus 5.5 agent:** re-ran the command, read all rows and the stamp independently as shape classes, and decoded them with its own script from the key table of HCP 1216. Of 381 letters, 11 differ, and every one is a point the solver had already disclosed. No new key value was needed.

The reading is a manual ledger from the pixels, not OCR, and it is not blind, since sister cards were known. The writer spells carelessly: he drops double letters (ot for ott, Jolánkámal for Jolánkámmal) and writes se for sem. The literal text below is kept as written; the normalized Hungarian is editorial.

## Key

Cipher type: **MASC + Steganography** (type updated 2026-11-03). Hungarian simple monoalphabetic substitution with invented signs; the closing six rows are hidden in the stamp box, under the stamp (now lifted), in the same cipher signs. The names are conventional descriptions of the handwritten shapes.

| Sign | Letter | Sign | Letter | Sign | Letter |
|---|---|---|---|---|---|
| two bars | a | section mark | k | F-like | r |
| six | b | wave | l | right bowl | s |
| left bowl | c | three short strokes | m | gamma / corner | t |
| long stroke + short tick | d | two short strokes | n | plain cross x | u |
| three bars | e | cursive loop | o | chevron | v |
| upright cross + | f | tall stroke + short tick | h / p | low descender | y |
| open loop with descender | g | dotted crossed curve | i | crossed diagonal | z |
| inverted T | j | joined loop + descender | gy | opposed bowls | cs |

One sign serves for both h and p. Dots over o and u give ö and ü, a double mark gives ű. Variants on this card: k appears both as an 8-shape (kám) and as an S-shape (kor, kis), and g has a looped head in row 3. The numerals 6 and 20 stand as written.

## Plaintext

Literal decipherment. (?) = blotted sign with no value; [x] = damaged sign or one read by word sense.

```text
01 (?)szeretetédesjolan
02 kámhogytala[l]tama
03 [g]atvasarnapénelegjól
04 mulattamigazhogy
05 énhamarfeltalalom
06 mag[a]mitvoltarok
07 szalasbólkisangyál
08 kaiseselégjólmu-
09 latotfélötkor
10 mentekelamulat
11 ságbólénis6atkor
12 mentemhazacsakaz
13 fájhogynemjolán
14 kámalmulathattam
15 deezennemsegithe
16 tünkmárminemzar
17 hatjukkiacselédeke[t]
18 seamulatságbóljöjöne20ikánotmajdnem
19 leszkevertné(?)[p][s]égistenveleaviszontlatasra
S1 csóko[l]om
S2 szá[m]ta
S3 lan[s][z][o]r
S4 [s]iri[g][h]ű
S5 imádó
S6 jaferi
```

Normalized Hungarian:

Szeretet[t] édes Jolánkám! Hogy találta magát vasárnap? Én elég jól mulattam, igaz, hogy én hamar feltalálom magam. Itt volt [Á]rokszállásból kis angyalka is, és elég jól mulatott. Fél ötkor mentek el a mulatságból, én is hatkor mentem haza. Csak az fáj, hogy nem Jolánkámmal mulathattam, de ezen nem segíthetünk, már mi nem zárhatjuk ki a cselédeket se a mulatságból. Jöjjön e[l] 20-ikán, ott majd nem lesz kevert né[p][s]ég. Isten vele, a viszontlátásra.

Under the stamp: Csókolom számtalanszor. Sírig [h]ű imádója, Feri.

**English.** Beloved sweet Jolánka of mine! How did you enjoy yourself on Sunday? I had quite a good time; it is true that I quickly find my feet. A little angel from Árokszállás (or a person called Kis Angyalka: the Hungarian allows either) was here too, and she had quite a good time. They left the party at half past four, and I too went home at six. Only it hurts that I could not have my fun with my Jolánka, but this cannot be helped, for we cannot shut the servants out of the party either. Do come on the 20th; there will be no mixed crowd there then. Farewell, until we meet again.

Under the stamp: I kiss you countless times. Your admirer, faithful unto the grave, Feri.

**Slovak.** Milovaná sladká moja Jolánka! Ako ste sa zabavili v nedeľu? Ja som sa zabavil celkom dobre, pravda, ja sa rýchlo nájdem. Bol tu z Árokszállásu aj malý anjelik (alebo osoba menom Kis Angyalka: maďarčina pripúšťa oboje) a zabával sa celkom dobre. O pol piatej odišli zo zábavy, aj ja som o šiestej išiel domov. Len to ma bolí, že som sa nemohol zabávať so svojou Jolánkou, ale tomu nepomôžeme, veď ani služobníctvo nemôžeme vylúčiť zo zábavy. Príďte dvadsiateho, tam potom nebude zmiešaná spoločnosť. S Bohom, dovidenia.

Pod známkou: Bozkávam Vás nespočetnekrát. Váš do hrobu verný ctiteľ, Feri.

## Uncertainties

- **Row 19, népség, is the weakest word.** After n, é come a blot with no value (taken as a false start), a tall stroke with a short stroke beside it (the h/p class, read p), and a heavily inked mass in which no s can be seen; then three bars with a tick above them, and g. The p rests on sense and the s is a restoration: nép?ég gives a word only with s. Kevert népség, "mixed crowd", answers the complaint about the servants, and the reviewer found no better word. The sentence reads without it.
- **Row 19, lesz:** the sign before z is a small closed-headed bowl, unlike the usual open one, but it has no y stroke and the z is clear. Shape plus sense.
- **Row 18, Jöjön e 20-ikán:** one j and no l, normalized Jöjjön el. The alternative e [hó] 20-ikán, "the 20th of this month", gives the same sense. The signs of 20-ikán overlap but are all seen; -ikán with a numeral occurs on HCP 1298.
- **Row 18, majd nem or majdnem:** spacing does not decide; majd nem lesz comes from sense.
- **Stamp rows S3 and S4:** in lan[s][z][o]r and [s]iri[g][h]ű several signs are blots or fragments. Both words rest on the formula, and sírig hű is on HCP 1216, which suggested the reading, so this is not independent. The words themselves are not in doubt.
- **Smaller points:** row 1 opens with a struck sign of no value and has one t in szeretet(t). Rows 2, 3 and 6 have variant signs read by sense (l, g, a). Rows 6 and 7 divide as volt [Á]rokszállásból, sharing a letter. Row 8 reads literally kais es. Row 11 writes the sign 6 before atkor: either the numeral or b for h, normalized hatkor. Row 15 doubles an e. The last sign of row 17 is thick and F-like; t rests on sense, literal r is possible.
- **Who was at the party:** kis angyalka may be a nickname or a person. The identities of Feri and of this person are unknown.
- **Date:** turned 180 degrees, the date block of the upper round cancel shows "…3-N-16", and the rim shows S and O among other letters. A weak second cancel below it shows a two-digit group that looks like 28. Place, format and year are not established, so "Sunday" and "the 20th" cannot be checked against a calendar.

## Review and what changed

The review verdict was **ACCEPT**, with five minor findings, all addressed. No plaintext word changed.

1. The plain word Szépremény[ű] on the address side was missing from the solution; it was added, and needless brackets in the address were removed.
2. "The date is not read" understated the cancels; what is visible is now recorded, without interpretation.
3. The ledger was less cautious than the text in stamp rows S3 and S4; the z, the o and the first s are now bracketed.
4. A tick above the three bars of népség was added to the ledger as é, the spelling the word needs. It is slight support for the restoration, not proof.
5. The translations flattened Jolánkám and did not carry the hedge on kis angyalka; both are corrected.

The review could not recover the value of the blotted signs in row 19 in any colour channel, and could not settle the postmark, the persons, or whether the first sign of row 1 is a false start.

The reading can be reproduced with `python3 -I ciphers/hcp-1302/work/decode_rev2.py`, which checks the scan hashes and prints the ledger and the normalized text. No published solution was found or used.
