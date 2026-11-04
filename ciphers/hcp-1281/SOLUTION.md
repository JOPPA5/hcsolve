# HCP1281 — Feri to Jolánka Tóth: missed visit, late train, "in 30 hours"

**Status: complete reading of the message, revised after review 1 (verdict REVISE).** One damaged line under the stamp is unread (item 1), one word is unidentified (item 2), and the hour in row 22 is uncertain (item 8). Written 2026-11-01 by Claude Opus 5.5. No earlier work on this number was used; the portal shows *Not solved* and attaches no transcription or solution. No published solution of this card turned up. The orchestrator's AI-register check of 2026-11-01 found no record.

## Cipher type and key

Hungarian, simple monoalphabetic substitution with invented graphic signs: the "Jolánka" postcard family.

*Type note 2026-11-03:* register type is now **MASC + Steganography**, because part of the message (rows S1-S7) is written in the cipher signs in the stamp box, hidden under the stamp, which is now lifted. The key was transferred unchanged from the finished cards HCP1216, 1212, 1213, 1217, 1218, 1243, 1301; see the sign table in `ciphers/hcp-1216/SOLUTION.md`. Nothing was changed or added to it. Digits in rows 10, 11 and 19 (2, 1/4, 10, 30) are written in clear inside the cipher text. The word *hogy* is once shortened to the h sign (row 5) and *de* once to d (row 7).

Sign values used on this card: a two bars, b six, cs opposed bowls, d long stroke + left tick, e three bars, f upright cross, g open loop with descender (*gy* is written here as g + y, two signs), h/p tall stroke + right tick, i dotted crossed curve, j inverted T, k section mark, l wave, m three strokes, n two strokes, o cursive loop, r F-like, s right bowl, t gamma, u/ű plain cross, v chevron, y low descender, z crossed diagonal. Dots or ticks on o give ö. Accents on a, e, i, o, u are mostly not visible and are supplied in normalization.

## Reproduction (one command, from the repository root)

```sh
python3 -I ciphers/hcp-1281/work/decode.py
```

It checks the SHA-256 of both scans in `source/` and both originals in `work/hires/`, prints `work/ledger.txt` row by row, then `work/normalized.txt`. The ledger is a manual transcription from enlarged pixels. It is not OCR. It holds key values rather than shape names, so the computer proves no reading of pixels; it was not a blind reading either, because word sense guided the doubtful signs listed below.

## Literal decipherment (as printed by the command)

```
01 szeretetedesjolankam          13 zansajnalomhogy
02 kivanomhogyalegjobked         14 nemmehettemelmert
03 vebentalaljasoraim            15 bizonyötnahignem
04 neharagudjonramede            16 latnon[t]agateznagy
05 semhtegnahnemtetem            17 dologazenehöszi
06 tiszteletemetkedves           18 vemnekdebiztatazare
07 samönneldalegnagyob           19 menyhogy30oramul
08 sajnalatomrae[z]sleg          20 vaviszontlatjokegy
09 nagyobbosszusagom             21 azazholnahdelutan
10 2orakesseselerkez             22 fogom[ö][t]okkorfogom
11 tem[||,]vagyis1/410orakor       23 tiszteletemetezelbezaromsormarado[k]imado
12 erkeztemhazaiga               24 f[t]eri  (up the right edge)
stamp: csokol / jaszam / talan / szor / sirig / hűferi / f[e][...]
```

## Hungarian (normalized)

Szeretet[t] édes Jolánkám! Kívánom, hogy a legjob[b] kedvében találja soraim. Ne haragudjon rám, édesem, h[ogy] tegnap nem tettem tiszteletemet kedves S[…]nél (written *samönnél*, unidentified), d[e] a legnagyob[b] sajnálatomra és legnagyobb bosszúságom[ra] 2 óra késéssel érkeztem, vagyis 1/4 10 órakor érkeztem haza. Igazán sajnálom, hogy nem mehettem el, mert bizony öt napig nem látnom magát, ez nagy dolog az én ep[ed]ő (or: hő) szívemnek, de biztat az a remény, hogy 30 óra múlva viszontlátjuk egy[mást], azaz holnap délután fogom, [öt?] *okkor* (hour uncertain) fogom tiszteletemet [tenni]. Ezzel bezárom sor[ai]m. Maradok imádó Feri.

Under the stamp: Csókolja számtalanszor, sírig hű Feri. [one more line, f…, destroyed where the stamp was torn off]

## English

My beloved sweet Jolánka! I hope my lines find you in the best of spirits. Do not be angry with me, my darling, that I did not pay my respects yesterday at dear S…'s (unidentified name or word in -nél), but to my greatest regret and greatest annoyance I arrived with a 2-hour delay, that is, I got home at a quarter past nine. I am truly sorry that I could not go, because not seeing you for five days, surely, that is a great thing for my yearning (or: ardent) heart, but I am encouraged by the hope that in 30 hours we shall see each other again, that is, tomorrow afternoon, at five(?) o'clock (the hour is uncertain), I shall pay my respects. With this I close my lines. I remain your adoring Feri.

Under the stamp: He kisses you countless times, faithful unto the grave, Feri. [one more line lost]

## Slovak

Moja milovaná, sladká Jolánka! Želám si, aby Vás moje riadky našli v najlepšej nálade. Nehnevajte sa na mňa, drahá, že som včera neurobil svoju návštevu u milého S… (neurčené meno alebo slovo na -nél), ale na moju najväčšiu ľútosť a najväčšiu mrzutosť som mal 2 hodiny meškanie, teda domov som prišiel štvrť na desať. Naozaj ľutujem, že som nemohol ísť, lebo veru päť dní Vás nevidieť, to je veľká vec pre moje túžiace (alebo: vrúcne) srdce, ale povzbudzuje ma nádej, že o 30 hodín sa znova uvidíme, teda zajtra popoludní, o piatej(?) (hodina je neistá) sa prídem pokloniť. Tým končím svoje riadky. Zostávam Váš zbožňujúci Feri.

Pod známkou: Bozkáva Vás nespočetnekrát, do hrobu verný Feri. [jeden ďalší riadok je stratený]

Hungarian *1/4 10* (*negyed tíz*) means 9:15, as does Slovak *štvrť na desať*.

## Uncertainties

1. **Last line under the stamp (S7)**: a clear cross (f), then two faint bars, then stains, a tear and stamp residue. It is unread and not restored. It is one short line in a physically destroyed spot; the closing formula is complete without it. S5 *sirig* and S4 *szor* lie partly on the green stamp residue and are weaker than the main rows. The word *csókolja* runs across rows S1 and S2.
2. **Row 7, *samönnel***: literal s a m ö n n e l. Two ticks stand above the loop, as on the ö of rows 15 and 17; the four strokes after it lie across the postmark ring, so their grouping is less sure than elsewhere. An unidentified word or name, normalized S[…]nél. The earlier form *Sámon* is withdrawn: a back-vowel name would take *-nál*, and no other card in the repository has it. Only the sense "at someone's" rests on word sense. The final d (left tick) is read as short *de*.
3. **Row 8, sign after *-ra***: three bars with a cross written through the middle bar, then s. Read *és* from sense, and the cross ledgered as `[z]` (unexplained, possibly a correction). *Az este* ("the evening") was considered: the next word, *leg-nagyobb*, fits *és* better.
4. **Row 11, mark after *erkeztem*** (`[||,]`): two strokes with a short mark at the base, not a clean m. No word needs it. It is left out of the normalization, as a false start or a stray; a comma after *erkeztem* is also possible.
5. **Row 16, *látnom magát***: literal l a t n o n t a g a t: two strokes, then a clean full-size gamma. *Látnom magát* (with the two m's written as one) is an emendation of a miswritten sign and rests on word sense; it is the only reading found.
6. **Row 17, *e h ö***: normalized *az én ep[ed]ő* (yearning), which inserts two letters and takes the sign as p. *Az én[e] hő szívemnek* ("my ardent heart") is an alternative: it needs one stray e and takes the sign at its h value. The call is not forced and the sense is the same. Elsewhere h/p is resolved by sense: p in *tegnap, napig, holnap*, h elsewhere.
7. **Rows 20–21**: *viszontlátjok egy* is normalized *viszontlátjuk egy[mást]* (o for u, -mást not written). The verb form is unusual. The alternative *egy, azaz* ("one, that is") is not excluded and does not change the sense.
8. **Row 22, the time**: the row runs *fogom* (the arm of the o runs into the first of the three strokes), a heavily rewritten loop with two or three marks above and an extra stroke at its right tail, a gamma rewritten with a second arc, then *o k k o r*. The word is printed as read. The loop is read ö only from shape and sense, so **"five" is uncertain**, and a corrected digit or word cannot be excluded. *Órakor* would need r and a, which are not there; *ötkor* ("at five") is closer to the letters, and *akkor* ("then") would need o for a. The sentence has *fogom* twice, and the infinitive *tenni* is missing and supplied.
9. **Row 23**: *ezel* = ezzel; *sorm* = sor[ai]m, supplied. The sign after *marado* has the descending shape of the g sign, not the k shapes of rows 1, 12, 18 and 22; k rests on sense (*maradok*).
10. **Signature (row 24)**: f, then a gamma with a tick across its top, then e r i. The extra sign is unexplained and is dropped; *Feri* is confirmed by the stamp row and by sister cards.
11. Other spellings normalized: *szeretet, legjob, legnagyob, tetem*, *kessesel* (signs k e s s e s e l, for *késéssel*), *bosszusagom* (-ra omitted, supplied). Row 10's first sign is read as the digit 2 from sense.
12. **Plain text** in the address, not cipher: *Tóth Jolánka úrleánynak, Helyben, István út 5*, and a cursive top line, probably *Szépreményű* (not firmly read). *Helyben* means a local address, so the card was posted in the town of delivery, and the postmark reads BUDAPEST, JÚN. 10. The portal's file name says Jászárokszállás; this card does not show that. The picture side has only the printed caption about the "love thermometer"; no cipher there.

## Why it is correct

- The key comes unchanged from reviewed sister cards, and it turns all 24 main rows and the first six stamp rows into Hungarian, with only the doubtful signs listed above.
- The text is coherent, with one plot: a missed visit, a 2-hour delay, home at 9:15, five days apart, reunion in 30 hours "tomorrow afternoon". The numbers fit each other: if the card was written on 10 June (the postmark date; the hour of writing is an assumption), 30 hours later falls on 11 June. This is consistency only and is no independent support for "five": 30 hours before 17:00 on 11 June is 11:00 on 10 June, and the sense of `N4` in the cancel is not established.
- Formulas match the family: *kívánom hogy… találja soraim* (HCP1213), *számtalanszor, sírig hű* (HCP1216), signature Feri, formal *Ön* address (*haragudjon, magát*).
- Repeated words decode identically: *hogy* ×3, *tiszteletemet* ×2, *fogom* ×2, *nagy* forms ×3, *erkez-* ×2.

## Response to review 1

Review verdict REVISE. All ten findings were re-checked on the reviewer's crops of the hi-res scan (`review/work/crops/`). All are accepted. The reading of the message is not substantially changed: the key, the plot and the translations stand, except that one word is now unidentified and the hour is marked uncertain. `python3 -I ciphers/hcp-1281/work/decode.py` was re-run after the changes: 4 hashes OK, and rows and normalization match this file.

1. **Stamp -ja (accepted, fixed).** `zs.png`: row S2 begins with j, a. The brackets and the remark are gone from the normalization and item 1.
2. **Row 22 hour (accepted, fixed).** `r22.png`, `r22z.png`: after the rewritten loop and gamma stand o, k, k, o, r, with no r or a in the middle. *[ór]akor* is withdrawn. The word is printed as read and the hour is marked uncertain in Hungarian, English and Slovak; see item 8.
3. **Row 7 (accepted, fixed).** `pm1.png`, `r7a.png` show the two ticks above the loop. The ledger now has ö. *Sámon* is withdrawn; the word stands as S[…]nél, unidentified, in all three versions; see item 2.
4. **`fogom` (accepted, fixed).** `z22.png`: the arm of the o turns down into a full stroke, and two free strokes follow. The ledger has `f o g o m`; item 8 is adjusted.
5. **Row 17 *hő* (accepted, fixed).** *Hő* is listed as an alternative in item 6 and in all three versions. I keep *ep[ed]ő* as the printed form without claiming it is forced.
6. **Row 16 gamma (accepted, fixed).** `zm.png`: two strokes and a clean gamma. The ledger now gives `n [t]`, and item 5 states it as an emendation.
7. **Row 23 *maradok* (accepted, fixed).** `zk.png`: the sign is g-shaped. The ledger has `[k]`, disclosed in item 9.
8. **`gy` (accepted, fixed).** The ledger tokens are split into g and y, and the sign list and a header line are corrected.
9. **Row 11 (accepted, fixed).** `e.png`: two strokes with a short base mark. The ledger token is now `[||,]`, and item 4 names the comma option.
10. **Timing (accepted, fixed).** *Why it is correct* now says this is consistency only.

## Stamp-box message (2026-11-03)

Audit by Claude Opus 5.5 at the human's request. The stamp box of the original (`work/hires/..._adr.jpg`) was cropped again at 2x and 3x, with a red-channel version (`work/stamp-2026-11-03/`). The stamp has been lifted. Only torn paper, a green perforated frame and a green triangular cancel-like patch remain. Under it are seven short rows in the **cipher signs** (no plain Hungarian). The rows were already read in the first solution and are in the ledger and `decode.py` output (`stamp:` line). This audit re-read them from the pixels and found nothing to change.

- Literal: `csokol / jaszam / talan / szor / sirig / hűferi / f[e][...]`
- Hungarian: Csókolja számtalanszor, sírig hű Feri. [last line f… unread]
- English: He kisses you countless times, faithful unto the grave, Feri. [last line unread]
- Slovak: Bozkáva Vás nespočetnekrát, do hrobu verný Feri. [posledný riadok neprečítaný]

Unread: row S7. It has a clear upright cross (f), then two or three faint bars, then a tear with stamp residue. It is one short line, probably a few letters, and it is not restored. Rows S4 and S5 lie on the green residue and are weaker, but each sign can still be seen.

