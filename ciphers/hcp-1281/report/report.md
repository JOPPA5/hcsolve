# HCP 1281: a Hungarian love note from Feri to Jolánka Tóth, 10 June 1914

Human solver: Tomáš Pavuk

**Status: deciphered; independent review 1 verdict REVISE, all ten findings addressed.** The message reads from start to finish. One line lost under the stamp is unread, one word in row 7 is unidentified, and the hour in row 22 is uncertain. Report dated 2026-11-01.

## Origin and context

The cryptogram is record 1281 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1281), portal name cpc_1914-06-10_HU__HU_Jasz Arokszalas_jolanka-54, part of Tobias Schrödel's collection of cryptographic postcards (private collection). When it was captured on 2026-11-01 the portal listed it as **Not solved**, with tags Postcard and T. Schrödel Collection, category Substitution, language Unknown, recipient Tóth Jolánka, and no transcription or solution attached. The portal cites https://ecp.ep.liu.se/index.php/histocrypt/article/view/166.

The cipher text fills the address side around the address. The plain address reads Tóth Jolánka úrleánynak, Helyben, István út 5 ("To Miss Jolánka Tóth, local, István street 5"), with a cursive line above it that is probably Szépreményű but is not firmly read. The right cancel reads [1]914 JUN. 10 N4, Budapest. Helyben means a local address, so the card was posted in the town of delivery. The portal's file name says Jászárokszállás, which this card does not show. The picture side has only a printed caption about a "love thermometer" and no cipher.

The card belongs to the family of Hungarian postcards to Jolánka Tóth signed by Feri. Several are deciphered in this repository (HCP 1212, 1213, 1216, 1217, 1218, 1243, 1301). The key was **transferred unchanged** from those cards, so this is not a new key recovery. No published reading of this card was found or used, and no earlier AI work exists on this number.

![Address side with the cipher text (source/address-large.jpg)](../source/address-large.jpg)

![Picture side (source/picture-large.jpg)](../source/picture-large.jpg)

## Method

The solver read the 24 main rows and 7 rows under the stamp sign by sign from enlarged crops of the un-converted original scan. No OCR was used. The result is a ledger of key values, row by row, in `work/ledger.txt`. The command `python3 -I ciphers/hcp-1281/work/decode.py` checks the scan hashes and prints the ledger and the normalized text. It proves consistency only, because the signs were read by eye, and word sense guided the doubtful signs listed below.

The reviewer made separate crops and its own shape transcription with the published family key. That transcription was not blind, because the reviewer had read the ledger first. It agreed on 453 of 463 tokens, and the differences produced the corrections below.

## Key

Simple monoalphabetic substitution with invented graphic signs. Full family table: `ciphers/hcp-1216/SOLUTION.md`. Signs used on this card:

| Plain | Sign | Plain | Sign |
|---|---|---|---|
| a | two bars | m | three strokes |
| b | six | n | two strokes |
| cs | opposed bowls | o | cursive loop |
| d | long stroke + left tick | ö | loop with ticks or dots |
| e | three bars | r | F-like |
| f | upright cross | s | right bowl |
| g | open loop with descender | t | gamma |
| h / p | tall stroke + right tick | u / ű | plain cross |
| i | dotted crossed curve | v | chevron |
| j | inverted T | y | low descender |
| k | section mark | z | crossed diagonal |
| l | wave | | |

The digits 2, 1/4, 10 and 30 are written in clear. Gy is written as g + y. Hogy is once shortened to h (row 5), and de once to d (row 7). Accents on a, e, i, o and u are mostly not shown and are supplied in normalization.

## Plaintext

Literal decipherment, row by row (h stands for the h/p sign; brackets mark a doubtful or unexplained sign):

```text
01 szeretetedesjolankam
02 kivanomhogyalegjobked
03 vebentalaljasoraim
04 neharagudjonramede
05 semhtegnahnemtetem
06 tiszteletemetkedves
07 samönneldalegnagyob
08 sajnalatomrae[z]sleg
09 nagyobbosszusagom
10 2orakesseselerkez
11 tem[||,]vagyis1/410orakor
12 erkeztemhazaiga
13 zansajnalomhogy
14 nemmehettemelmert
15 bizonyötnahignem
16 latnon[t]agateznagy
17 dologazenehöszi
18 vemnekdebiztatazare
19 menyhogy30oramul
20 vaviszontlatjokegy
21 azazholnahdelutan
22 fogom[ö][t]okkorfogom
23 tiszteletemetezelbezaromsormarado[k]imado
24 f[t]eri (up the right edge)
S1-S7 csokol / jaszam / talan / szor / sirig / hűferi / f[e][...]
```

**Hungarian (normalized):** Szeretet[t] édes Jolánkám! Kívánom, hogy a legjob[b] kedvében találja soraim. Ne haragudjon rám, édesem, h[ogy] tegnap nem tettem tiszteletemet kedves S[…]nél (written samönnél, unidentified), d[e] a legnagyob[b] sajnálatomra és legnagyobb bosszúságom[ra] 2 óra késéssel érkeztem, vagyis 1/4 10 órakor érkeztem haza. Igazán sajnálom, hogy nem mehettem el, mert bizony öt napig nem látnom magát, ez nagy dolog az én ep[ed]ő (or: hő) szívemnek, de biztat az a remény, hogy 30 óra múlva viszontlátjuk egy[mást], azaz holnap délután fogom, [öt?] okkor (hour uncertain) fogom tiszteletemet [tenni]. Ezzel bezárom sor[ai]m. Maradok imádó Feri.

Under the stamp: Csókolja számtalanszor, sírig hű Feri. [one more line lost]

**English:** My beloved sweet Jolánka! I hope my lines find you in the best of spirits. Do not be angry with me, my darling, that I did not pay my respects yesterday at dear S…'s (unidentified name or word in -nél), but to my greatest regret and greatest annoyance I arrived with a 2-hour delay, that is, I got home at a quarter past nine. I am truly sorry that I could not go, because not seeing you for five days, surely, that is a great thing for my yearning (or: ardent) heart, but I am encouraged by the hope that in 30 hours we shall see each other again, that is, tomorrow afternoon, at five(?) o'clock (the hour is uncertain), I shall pay my respects. With this I close my lines. I remain your adoring Feri.

Under the stamp: He kisses you countless times, faithful unto the grave, Feri. [one more line lost]

**Slovak:** Moja milovaná, sladká Jolánka! Želám si, aby Vás moje riadky našli v najlepšej nálade. Nehnevajte sa na mňa, drahá, že som včera neurobil svoju návštevu u milého S… (neurčené meno alebo slovo na -nél), ale na moju najväčšiu ľútosť a najväčšiu mrzutosť som mal 2 hodiny meškanie, teda domov som prišiel štvrť na desať. Naozaj ľutujem, že som nemohol ísť, lebo veru päť dní Vás nevidieť, to je veľká vec pre moje túžiace (alebo: vrúcne) srdce, ale povzbudzuje ma nádej, že o 30 hodín sa znova uvidíme, teda zajtra popoludní, o piatej(?) (hodina je neistá) sa prídem pokloniť. Tým končím svoje riadky. Zostávam Váš zbožňujúci Feri.

Pod známkou: Bozkáva Vás nespočetnekrát, do hrobu verný Feri. [jeden ďalší riadok je stratený]

Hungarian 1/4 10 (negyed tíz) means 9:15, as does Slovak štvrť na desať.

## What remains uncertain

- **Row S7:** a cross (f), two faint bars, then a tear and stamp residue. It is unread. Rows S4 to S6 lie partly on stamp residue and are weaker than the main rows.
- **Row 7, samönnel:** an unidentified word or name, read only as "at someone's". The strokes lie across the postmark ring.
- **Row 22, the hour:** a rewritten loop with marks above it and a rewritten gamma, then o k k o r. Ötkor ("at five") is the nearest form, but "five" rests on shape and sense, and a corrected digit or word cannot be excluded. The infinitive tenni is supplied.
- **Row 17:** ep[ed]ő (yearning) or hő (ardent). The sense is the same.
- **Row 16:** látnom magát is an emendation: the card has two strokes and a gamma (n, t).
- **Row 23:** the k of maradok has a g-like shape. Sor[ai]m is supplied.
- **Row 8:** the sign read és has a cross written through it. **Row 11:** two strokes with a short mark after erkeztem are unexplained and left out. **Row 24:** the extra sign in Feri is unexplained and dropped.
- **Rows 20 to 21:** viszontlátjok egy is normalized to viszontlátjuk egy[mást]; egy, azaz is not excluded.
- **Context:** the identity of S…, the journey behind the delay, the time of writing and the meaning of `N` in the cancel are not known. The 30 hours fit a meeting on 11 June, but that is consistency only, not independent support for "five".

## Review and what changed

A separate Claude Opus 5.5 agent reviewed the solution and returned REVISE. It confirmed the key, the plot and the language, and it found no use of a published solution. All ten findings were accepted after a check on the crops:

- The stamp text was wrongly said to lack -ja: csókol|ja runs across two rows.
- [ór]akor was withdrawn, and the hour is marked uncertain in all versions.
- The name Sámon was withdrawn: two ticks over the loop were missed, and the suffix would not fit that name.
- Row 22 begins fogom, not fogo[n].
- Hő was added as an alternative in row 17.
- The literal gamma in row 16, the g-shaped k in row 23 and the unclear mark in row 11 are now in the ledger.
- Gy is now recorded as two signs.
- The timing argument is now stated as consistency only.

The key and the sense of the message did not change.
