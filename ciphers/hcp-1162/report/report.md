# HCP 1162 (cpc_1916-03-28_HU_Mezokovesd_HU_Szomolya_szomolya-25): a whole Hungarian love letter in digits

Human solver: Tomáš Pavuk

**Status: deciphered in full (388 of 388 cipher signs; 387 by the key as written, 1 by word sense); independent review 1 verdict REVISE, findings addressed, one letter changed.** Report dated 2026-11-02.

## Origin and context

The cryptogram is record 1162 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1162), portal name cpc_1916-03-28_HU_Mezokovesd_HU_Szomolya_szomolya-25, from Tobias Schrödel's cryptographic postcards collection (private collection). When captured on 2026-11-02 the portal listed it as **Not solved**, category Substitution, language Unknown, sender Unknown, recipient Margitka Sziber, with no transcription or solution attached. The portal links a HistoCrypt article (https://ecp.ep.liu.se/index.php/histocrypt/article/view/166). That article was **not checked** for this card, so it is not known whether it treats it. No published solution of this card was met.

The picture side is a coloured romantic print of a couple embracing in a garden, with a child in the tree above them, and has no writing. The message side carries 22 lines of digits on the left and an open address on the right: "Őnsg. Szépreményű Sziber Margitka kisasszonynak, Szomolya (Borsodm.) u. p. Bogács", "To the promising young lady Margitka Sziber, Szomolya (Borsod county), post office Bogács". "Őnsg." is an abbreviated title, read as written. The card was written in wartime. The open words after the signature are the place and date, "Mezőkövesd, 1916 [III]/28". Mezőkövesd and Szomolya are close to each other in north-east Hungary.

It belongs to a correspondence of cards to Margitka Sziber (hcp-1135 to 1179 on the portal). On hcp-1174 the writer enciphers only key words inside plain Hungarian. Here he enciphers the whole message. The signature "Árpád", in digits, also occurs on hcp-1174.

![Message and address side (source/address-large.jpg)](../source/address-large.jpg)

![Picture side, no cipher text (source/picture-large.jpg)](../source/picture-large.jpg)

## Method

The transcription is manual, sign by sign, from the un-converted high-resolution scan, enlarged in strips. No OCR was used.

The key was not recovered from scratch. The table reconstructed on the sister cards hcp-1174, 1178 and 1179 decoded most of the card at once. The signs missing from that table were then fixed by word sense, and each is used in several words or a very clear one: 4 f (fájt, fuvaros, filért), 4. gy (hogy, nagyon, gyalog), 6 j (fájt, muszáj, majd), 6. ny (nyolcra, anyám), 5. ly (olyan), 2 c (nyolcra), .1 u (muszáj, tudod), and more words for 3. v. The new signs slot into a regular scheme, which is good evidence for those that occur only once or twice.

Two points of reading mattered. A digit and its mark are one sign, so the position of a dot decides the letter: at the foot of the stroke it is a, level with the upper stroke it is á. And the sign 1 with a comma, an uncrossed stroke, is b, while the real 7 is always crossed. Taking it for 7 first gave "setartani" and "ese", which corrected to "betartani" and "ebe".

The script work/decode.py checks the scan hashes, decodes the transcription and asserts that the result equals the stated plaintext word by word. Two words cross a line end with no hyphen on the card (édes|anyám, kedve|sed), and the script joins those explicitly. In review the reviewer read all 22 lines again on its own crops and decoded them with its own script and key table (review/work/decode_review.py). All 31 signs are in the key and no key sign is unused.

## Key

Monoalphabetic substitution with a mark as part of the sign. Register label: MASC. The cipher folds i/í, o/ó, ö/ő and writes single letters for each listed digraph.

| plain digit | with comma | with dot | other |
|---|---|---|---|
| 1 = i, í | 1, = b | 1. = a | 1: = e; 1' (high dot) = á; .1 (one dot left) = u; :1 (two dots left) = ü |
| 0 = o, ó | 0, = ö, ő | | |
| 2 = c | 2, = cs | 2. = é | |
| 3 = d | 3, = r | 3. = v | |
| 4 = f | 4, = g | 4. = gy | |
| 5 = h | 5, = l | 5. = ly | |
| 6 = j | 6, = n | 6. = ny | |
| 7 = k | 7, = s | 7. = sz | |
| 8 = m | 8, = t | | |
| 9 = p | 9, = z | | |

The plain digits 2 to 9 run through consonants in alphabet order, c, d, f, h, j, k, m, p, and the dot marks digraphs and the vowels a and é. One difference from a sister card: hcp-1178 lets 5. act as l, but here its one occurrence, in olyan, needs ly.

Sign counts (388 in all): 1: = 41; 8, = 34; 1. = 32; 0 = 32; 8 = 26; 3, = 20; 3 = 18; 6, = 18; 7 = 17; 5, = 17; 1' = 14; 7, = 13; 1 = 13; 2. = 12; 5 = 11; 4. = 8; 7. = 8; 3. = 8; 1, = 7; 4, = 6; 0, = 6; 9 = 5; .1 = 5; 4 = 3; 6 = 3; 9, = 3; 2, = 3; 6. = 2; 5. = 1; 2 = 1; :1 = 1.

## Plaintext

Transcription, card line by card line. Signs are separated by spaces and words by a slash. A trailing hyphen is on the card. 8{t} is the one sign written 8 and read t.

```text
01 2. 3 1: 7, / 8 1. 3, 4, 1 8, 7 1' 8 !
02 6, 1. 4. 0 6, / 4 1' 6 8, / 1. / 7. 1 3. 1: 8 / 5 0 4.
03 0 5. 1. 6, / 7 1: 3. 2. 7, / 1 3 0, 8, / 8{t} 0, 5, 8, -
04 5 1: 8, 8, 1: 8 / 3. 1: 5, 1: 3 / 3 1: / 8 1' 7, -
05 7 2. 9 / 6, 1: 8 / 8, 1: 5 1: 8, 8, 1: 8 / 8 1' 3, / 1.
06 9 0 6, 8, 0 7, 7, 1' 4, 0 8, / 8 .1 7. 1' 6 / 1, 1: 8, 1. 3, -
07 8, 1. 6, 1 / 8 1 4, / 1: 1, 1: / 1. / 9 0 7 0 5, 1, 1.
08 5, 1: 7. 1: 7 / 8 1: 3, 8, / 8, .1 3 0 3 / 5 0 4.
09 1: 9, / 3. 1. 5, 0 7, 1' 4, 0 7, / 9 0 7 0 5, )
10 8, .1 3 0 3 / 1: / 2. 3 1: 7, 1: 8 / 5 0 4. / 4. 1. 5, 0 4,
11 5 1. 8 1. 3, 1. 1, / 5 1. 9, 1. / 2. 3, 8, 1: 8 / 3. 0 5, -
12 6, 1. / 8 1 6, 8, / 7 0 2, 1 6, / 5 1' 3, 0 8 / 6, 1: 4. 1: 3
13 6. 0 5, 2 3, 1. / 2. 3, 8, :1 6, 7 / 5, 1: ) / 1. / 4 .1 3. 1. -
14 3, 0 7, / 7 2. 8, / 7 0 3, 0 6, 1' 8, / 7 2. 3, 8, / 8, 0, -
15 5, 1: 8 / 3 1: / 2, 1. 7 / 1: 4. / 7 0 3, 0 6, 1. / 5 1. 8, -
16 3. 1. 6, / 4 1 5, 2. 3, 8, / 1. 3 8, 1. 8 / 6, 1: 7 1 )
17 8 0 7, 8, / 8, 0, 1, 1, 1: 8, / 6, 1: 8 / 1 3, 0 7
18 5 1. / 8 1. 6 3 / 1 3, 7. / 1 3, 3 / 8 1: 4, / 5 0 4.
19 8 1 8, / 1, 1: 7. 2. 5, 8, / 1. 9, / .1 8, 1' 6, / 2. 3 1: 7,
20 1. 6. 1' 8 / 7. 1' 8 8, 1. 5, 1. 6, 7. 0 3, / 0, 5, 1: 5,
21 2. 7, / 2, 0 7 0 5, / 7. 1: 3, 1: 8, 0, / 7 1: 3 3. 1:
22 7, 1: 3 / ( 1' 3, 9 1' 3 )
```

Hungarian. Spelling and the closing brackets are as on the card; commas, capitals and layout are editorial, and the accents the cipher folds are restored. [= ...] gives the normal form.

Édes Margitkám!

Nagyon fájt a szívem, hogy olyan kevés időt tölthettem veled, de máskép [= másképp] nem tehettem, már a pontosságot muszáj betartani, míg ebe [= ebbe] a pokolba [= pokolban] leszek, mert tudod, hogy ez valóságos pokol) Tudod-e, édesem, hogy gyalog hamarab [= hamarabb] haza értem volna, mint kocsin, három negyed nyolcra értünk le) A fuvaros két koronát kért tőlem, de csak egy korona hatvan filért [= fillért] adtam neki) Most többet nem írok, ha majd írsz, írd meg, hogy mit beszélt az után édesanyám.

Számtalanszor ölel és csókol szerető kedvesed (Árpád)

Open: Mezőkövesd, 1916 [III]/28.

A long pen ruling under card lines 19 and 20 sets the closing formula apart from the body. It carries no signs.

**English.** Sweet Margitka! My heart ached badly that I could spend so little time with you, but I could not do otherwise, since punctuality has to be kept as long as I am in this hell, for you know this is a real hell. Do you know, my sweet, that I would have got home sooner on foot than by carriage? We got down by a quarter to eight. The carter asked two crowns of me, but I gave him only one crown sixty fillér. I will not write more now; when you write, tell me what my mother said afterwards.

Countless times your loving sweetheart embraces and kisses you (Árpád)

Mezőkövesd, 28 [March] 1916.

**Slovak.** Moja sladká Margitka! Veľmi ma bolelo srdce, že som s tebou mohol stráviť tak málo času, ale nemohol som inak, veď presnosť treba dodržiavať, kým budem v tomto pekle, lebo vieš, že je to skutočné peklo. Vieš, moja milá, že pešo by som bol doma skôr než povozom? Dolu sme prišli o trištvrte na osem. Povozník odo mňa pýtal dve koruny, ale dal som mu len jednu korunu šesťdesiat halierov. Teraz už viac nepíšem; keď budeš písať, napíš mi, čo potom hovorila moja mama.

Nespočetnekrát ťa objíma a bozkáva tvoj milujúci milý (Árpád)

Mezőkövesd, 28. [marca] 1916.

## Uncertainties

Cipher signs:

- tölthettem: the first sign is a plain 8 with no comma, which the key makes m. "mölthettem" is no word, so it is read t, as a slip for 8,. This is the only sign off the table.
- Some signs on the table rest partly on word sense. In tölthettem and ölel the 0, has its comma joined to the bowl and looks like 9, and the comma of többet also sits close to the bowl. In értünk the comma of 3, is merged in a heavy tail. In filért the 5, has a closed loop and resembles an 8, but carries the tilde all his 5s have.
- és at the start of card line 21 lies under the red printed figure 3613. The 2. and 7, show through. The red figures, with a further figure right of them, are not part of the message and their meaning is unknown.

Reading:

- édesanyám is literally "my mother" and is translated so. The word is clear, but he asks Margitka what she said, so it may be Margitka's mother, named affectionately. The card does not settle it.
- pokol ("hell"): what he means is not stated. Military service or a strict post in Mezőkövesd in 1916 would fit, but the card does not say so.
- három negyed nyolcra is 7:45; morning or evening is not stated. értünk le, "we got down", presumably means down from Szomolya; the destination is not named.
- The brackets after pokol, le and neki have no opening bracket. He uses them as full stops.
- Tudod-e: the 1: stands alone, joined here as the question particle.
- The month is overwritten. III comes from the portal file name (1916-03-28) and fits the blot. 1916 and 28 are legible. The postmark dateline is mostly under the stamp and does not confirm it.
- The sender is Unknown on the portal; Árpád is the signature decoded here and on hcp-1174.

## Why the reading is believed

One fixed key decodes every line of the card into continuous Hungarian, with no unread word. Most of the key came from other cards, and the new signs fill a regular scheme. The content is concrete and self-consistent: the carter's price of 2 crowns against the 1 crown 60 fillér paid is correct Austro-Hungarian currency. The addressee, place, opening and closing match the sister cards.

## Review and what changed

Review 1 (a separate Claude Opus 5.5 agent) tried to refute the text and could not. It re-ran the command, decoded with its own script, re-read all 22 lines on its own enlargements and checked each sense call. Verdict REVISE, with four findings, all accepted:

1. **Major: utan is után.** The dot in the word after az stands high, not at the foot of the stroke. The sign is 1' and not 1., so a claimed misspelling by the writer disappears. One plaintext letter changed.
2. **Minor: invented hyphens.** Three hyphens at line ends were not pen strokes of the message, one of them the foot of the address bracket. They were removed, and the script now compares word by word, which had hidden a wrong word break at ölel és.
3. **Minor: ruling.** The pen ruling above the closing formula is now disclosed.
4. **Minor: sense count.** The stated count of one sign read by sense is now defined as signs off the table, and signs on the table that rest partly on word sense are listed.

The reviewer could not verify the month, whose mother is meant, what "pokol" refers to, the destination, or the meaning of the red figures. These remain open above.
