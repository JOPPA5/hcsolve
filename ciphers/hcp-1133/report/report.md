# HCP 1133 (cpc_1902-12-18_HU__HU_Helyben_): a Hungarian postcard from Temesvár with two Morse passages

Human solver: Tomáš Pavuk

**Status: deciphered in full (all 17 Morse lines, 105 letter groups, no unknown group); independent review 1 verdict ACCEPT, no change to the decoded letters.** Report dated 2026-11-03.

## Origin and context

The cryptogram is record 1133 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1133), portal name cpc_1902-12-18_HU__HU_Helyben_, part of Tobias Schrödel's collection of cryptographic postcards (private collection). When it was captured on 2026-11-03 the portal listed it as **Not solved**, tagged Postcard and T. Schrödel Collection, language Unknown, sender Unknown, recipient Márthé Ilona, with no transcription or solution attached.

It is a photo postcard of an actress in a long coat (photographer's mark "SARONY"). The picture side, turned 90° counter-clockwise, is written over in ink in Hungarian: a dateline, a left column, a right column and a bottom block of plain text, with **two passages in Morse code** inside the right column. The card is signed "Üdvözlettel Richter Antal" ("With greetings, Antal Richter").

The address side reads "Levelező lap. Szépreményű Márthé Ilona kisasszonynak, Helyben, Jr. Eötvös utcza 7 sz." ("Postcard. To the promising Miss Ilona Márthé, local, Jr. Eötvös Street No. 7"). "Helyben" ("local") means the card was posted within the same town, Temesvár (today Timișoara, Romania). A 4-filler Turul stamp of the Hungarian Royal Post is still attached; the postmark (upside down) reads "…02 DEC 18", that is 18 December 1902, which agrees with the portal file name. The dateline on the picture side clearly reads "1900", one day before the postmark's day and month; both are reported as written.

![Picture side turned upright (90° counter-clockwise): plain text in the left column and at the bottom, two Morse blocks in the right column (work/picture-ccw.jpg)](../work/picture-ccw.jpg)

![Address side: Márthé Ilona, Helyben, Eötvös utcza 7; Turul stamp and postmark (source/address-large.jpg)](../source/address-large.jpg)

No published solution was found. A web search for the names on the card (Márthé Ilona, Richter Antal, Temesvár) found nothing about this card.

## Method

The transcription is manual, from the un-converted high-resolution scan of the picture side, rotated and cut into per-line crops enlarged 3x to 5x. Every Morse line (3 lines in the first passage B1, 14 in the second passage B2) was transcribed sign by sign into work/morse_transcription.txt. The writer puts a slanted stroke "/" after every letter and does not separate words, so letter boundaries are certain and word division is editorial.

Decoding is a direct table lookup (work/decode.py), which also checks the SHA-256 of the scans. In review, a second agent rotated and cropped the scan independently, checked all 17 lines against the transcription, and decoded them with its own Morse table (review/work/indep_decode.py); it got the same two strings.

## Key

**Morse code**, International Morse plus two accented letters:

| Sign | Letter | Note |
|---|---|---|
| `..-..` | É | standard Hungarian Morse |
| `.-.--` | Á | the writer's own sign (standard is `.--.-`); used twice, in vÁrtam and délutÁn, both confirmed by the word |

All other letters are standard International Morse. Ú is written as plain U (lesUjtott). Register type: MASC/Morse.

## Reproduction

From the repository root:

```
python3 -I ciphers/hcp-1133/work/decode.py
```

Output:

```
B1 joined: VISELKENÉSELESUJTOTTTELJESEN
B2 joined: REGGELVÁRTAMDÉLUTÁNHOGYÉRTSEMEZTKÉREMIRJONAZONNALAZÉGREKÉREMIRJONEGYLEVELET
```

## Ciphertext

As transcribed (one written line per row; "/" ends each letter):

```
[B1]
...-/../.../ ./.-../-.-/./-./..-../.../
./.-.././.../..-/.---/-/---/-/-/
-/./.-../.---/./.../ ./-./
[B2]
.-././--./--././
.-../...-/.-.--/.-./
-/.-/--/-../..-../
.-../..-/-/.-.--/-./
..../---/--./-.--/
..-../.-./-/.../ ./--/
./--../-/-.-/..-../.-./
./--/../.-./.---/---/
-./.-/--../---/-./
-./.-/.-../.-/--../
..-../--./.-././-.-/..-../
.-././--/../.-./.---/
---/-././--./-.--/
.-.././...-/./.-.././-/
```

## Plaintext

Morse passage B1: **viselkenése [= viselkedése] lesújtott teljesen**

Morse passage B2: **reggel vártam délután, hogy értsem ezt. Kérem írjon azonnal, az égre kérem, írjon egy levelet**

The whole card in reading order (left column, right column, bottom block); the Morse text is in capitals:

> Kelt Temesvár 1900 év December hó 17 napján.
> Azt kérem egészen nyugodtan elhiheti, hogy nem egyáltalában nem szoktam mondani sem most sem máskor, hogy már nem fogadom szívesen lapját. Én szokva vagyok mindent szívesen fogadni, és hogy beteg voltam, azt a legnagyobb lelki nyugalommal ismétlem.
> VISELKENÉSE LESUJTOTT TELJESEN, márpedig ezt nem hittem volna. Csoda, hogy nem találtak több vádat ellenem. REGGEL VÁRTAM DÉLUTÁN HOGY ÉRTSEM EZT. KÉREM ÍRJON AZONNAL, AZ ÉGRE KÉREM ÍRJON EGY LEVELET, levelezőlapot azt írta, már nem küld. Szépe(?) nagyon szép.
> De ne méltóztassék hinni, hogy én ily dolgokat egyhamar elfelejtek. Öles betűkkel irotatt [íratott] az bizonyos helyre.
> Üdvözlettel Richter Antal.

**English.** Dated Temesvár, 17 December 1900. I ask you: you may quite calmly believe that I am not at all in the habit of saying, now or at any other time, that I no longer gladly receive your card. I am used to receiving everything gladly, and that I was ill I repeat with the greatest peace of mind. YOUR BEHAVIOUR STRUCK ME DOWN COMPLETELY, and I would never have believed that. It is a wonder they did not find more accusations against me. I WAITED FROM MORNING TO AFTERNOON TO UNDERSTAND THIS. PLEASE WRITE AT ONCE, FOR HEAVEN'S SAKE, PLEASE WRITE A LETTER. As for a postcard, you wrote that you will not send one any more. Its (?) is very pretty. But please do not believe that I forget such things quickly. It was written in huge ("fathom-high") letters onto that certain place. With greetings, Antal Richter.

**Slovensky.** Dané v Temešvári 17. decembra 1900. Prosím, môžete celkom pokojne veriť, že vôbec nemám vo zvyku hovoriť, ani teraz ani inokedy, že už neprijímam Váš lístok rád. Som zvyknutý všetko prijímať rád, a že som bol chorý, to opakujem s najväčším duševným pokojom. VAŠE SPRÁVANIE MA ÚPLNE ZDRVILO, a to by som nikdy nebol veril. Div, že proti mne nenašli viac obvinení. ČAKAL SOM OD RÁNA DO POPOLUDNIA, ABY SOM TOMU POROZUMEL. PROSÍM, NAPÍŠTE HNEĎ, PROBOHA PROSÍM, NAPÍŠTE LIST. Korešpondenčný lístok vraj už nepošlete. Jeho (?) je veľmi pekný. Ale neráčte si myslieť, že také veci rýchlo zabúdam. Bolo to napísané obrovskými písmenami na isté miesto. S pozdravom Antal Richter.

Both Morse passages run on grammatically from the plain sentences around them: the writer protests against an accusation in plain words and hides the most emotional lines in Morse.

## Uncertainties

1. **"viselkenése" for "viselkedése".** The pixels show `-.` (N) where the word needs `-..` (D); the dash and the single dot are clear and nothing is hidden under the portal watermark. This is a writer's slip of one dot.
2. **Faint dashes.** Seven marks are a faint thin tail ending in a dot or blob, as if the pen started dry: in B2 line 7 (middle of the final R), line 9 (dash of A, first sign of Z), line 10 (first sign of N), line 11 (third sign of É, start of G) and line 12 (middle of R). All are read as dashes, and each is confirmed by the word; as dots they give no words.
3. **Calls resting partly on word sense.** In B2 line 5 (H `....`) and line 6 (S `...`) one dot is slightly elongated; in B2 line 7 the last mark of Z `--..` in "ezt" is a short blob that, read as a dash, would give Q. "hogy", "értsem" and "ezt" decide these.
4. **Word division and punctuation** in the Morse text are editorial.
5. **Plain text, single words:** "irotatt" (most likely a slip for "íratott", "was written"); "Szépe(?)" (possibly "Szép-e?", "is it pretty?"); "szívesen" (a long-s and z ligature makes it look like "kivessem"); "Jr." in the address, left unexpanded (possibly a Temesvár district such as Józsefváros, hypothesis only). Each is a single word, and the clause around it reads.
6. **Year.** The dateline says 1900, the postmark 1902.
7. **Under the stamp.** The stamp is still attached, so whether anything is hidden under it cannot be checked. No hidden writing was found in the picture or along the edges.

## Review summary

An independent reviewer (a separate Claude Opus 5.5 agent) ran the reproduction command, decoded the transcription with its own Morse table, and checked all 17 Morse lines against its own 3x to 5x crops of the high-resolution scan, as well as the plain text, the address and the postmark. Verdict **ACCEPT**, with five minor findings:

1. The Z of "ezt" rests partly on word sense: now listed (uncertainty 3).
2. The list of faint dashes was incomplete: two more (R in line 7, A in line 9) added (uncertainty 2).
3. The Slovak "na tom istom mieste" was corrected to "na isté miesto"; the English now says "onto".
4. The Józsefváros hypothesis for "Jr." was added as a hypothesis only.
5. Steganography: nothing can be checked under the attached stamp and nothing hidden is visible elsewhere; this card is not part of the Jolánka series, where hidden writing under the stamp is common, so no Steganography label is used.

No decoded letter changed.

## Credits

Transcription, decipherment and this report by Claude Opus 5.5 (Anthropic); independent review by a separate Claude Opus 5.5 agent. No earlier work by another model exists on this card. Human solver: Tomáš Pavuk.
