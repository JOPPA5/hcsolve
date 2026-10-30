# HCP 1340 (pc_hcp_21): a German love note from Bubi to Rosa, 1905

Human solver: Tomáš Pavuk

**Status: deciphered in full (347 of 347 cipher signs read); independent review 1 verdict REVISE, all findings addressed, no sign value changed.** Report dated 2026-10-30.

## Origin and context

The cryptogram is record 1340 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1340), portal name pc_hcp_21, part of the HCPortal collection of cryptographic postcards. When it was captured on 2026-10-30 the portal listed it as **Not solved**, tagged Postcard, HCPortal collection, category Substitution, date 1905-06-09, language Unknown, location Europe, sender Unknown, recipient Rosa Duffuer, with no transcription or solution attached.

It is a hand-coloured picture postcard of a river or woodland scene with birch trunks and a blossoming tree. The address side is in plain Kurrent handwriting: **Fräulein Rosa Duffuer** (portal spelling; the handwriting may equally be Duffner), **Villa Waldlust, Schönwald, bad. Schwarzw.** It carries a German Reich 5-pfennig stamp and a postmark SCHÖNWALD (BADEN) 9.6.05. Above the cipher the writer put the plain date **Den 8. Juni 05.**, a Thursday.

The cipher text fills the left half of the address side (thirteen rows) and continues on the picture side along the top edge, down the corner, under the picture and up the right margin. Plain greetings stand beside it on the picture side, under the picture, roughly: "Bitte auch freundliche Grüsse an deine lieben Eltern und an deinen lieben Bruder. Wie geht es deinem lieben Vater? Wünsche gute Besserung. Gruss Euer Hermann"; the left margin has **Frohes Wiedersehen!** So the card shows a polite open face, for anyone who might read it, and a private ciphered one. The word "Eltern" in the plain text is less certain. The ciphered signature "Bubi" is presumably the Hermann of the plain text, but that is an inference.

![Address side: thirteen cipher rows under the date, plain address, Schönwald (Baden) postmark 9.6.05 (source/address-large.jpg)](../source/address-large.jpg)

![Picture side: cipher along the top edge, corner and right margin and under the picture; plain Kurrent greetings at the bottom and in the left margin (source/picture-large.jpg)](../source/picture-large.jpg)

Other marks, none of them cipher: the printed postcard headings, "Series 678. 3." with a heart emblem, a large pen flourish above "Fräulein", the stamp, the postmark and the HCPortal watermark on both sides.

## Method

The transcription is **manual**, made from the un-converted originals of the scans enlarged 3 to 9 times. No OCR was used and the portal gave no transcription. Each sign received a token; `work/transcription.txt` holds the sixteen blocks (adr1 to adr13, pic-top, pic-bottom, pic-margin).

Word spaces are kept on the card, so the key came from recurring short words. Testing German gave #26#6 = einen, 62c10 = nicht, 2c1 = ich, 05 = du and 270 = ist. Those values then read the remaining text without any change. The writer's digits and signs do not match any other card in this repository, so nothing was transferred from a sister card. Two early misreadings were corrected from the enlargements: the a sign was first confused with the b sign, and "kome" was taken for "kam".

## Key

Monoalphabetic substitution of German letters by digits and invented signs. The labels describe handwritten shapes. There is one merger: the sign 0 stands for both d and t.

| Plain | Sign | Plain | Sign |
|---|---|---|---|
| a | slash, dot on right, dot or tick on left | m | ### (three bars crossed by one long stroke) |
| b | slash, dot on right only | n | 6 |
| c | c-shape (only in ch, sch) | o / ö | 9 / 9 with two ticks |
| d, t | 0 | p | p-shape (once) |
| e | # (two bars crossed by two) | r | two ticks ,, |
| f | 4 | s | 7 with hook and bar |
| g | 8 | u / ü | 5 / 5 with two ticks |
| h | 1 | v | v-shape (once) |
| i | 2 | w | W-shape |
| k | slashed 0 | z | looped a-like sign with a foot, after 0 only (twice) |
| l | 3 | | |

ä and äu are written with e and eu. Sign counts (347 in all): e 46, d/t 36, s 34, i 32, n 31, h 20, r 18, c 18, u 17, a 16, b 15, m 11, o 10, g 10, l 9, k 8, w 5, ü 3, f 3, z 2, p 1, ö 1, v 1.

The a and b signs differ only by the left mark. In "war" of row adr8 that mark merges with the tail of the W, and in the corner "war" it is only a small kink on the slash. Those two a signs rest on the word as well as the glyph.

## Plaintext

Literal German, as the key gives it, with a d or t chosen for each 0 and nothing else changed:

```text
adr1        libste rosa: hast du
adr2        meine karte bekomen?
adr3        wie get es dir? bist du
adr4        wider gesund? süsser schatz
adr5        ich hae mich ein bischen er=
adr6        keltet und bekome einen
adr7        kleinen schnupfen. macht
adr8        aber nichts war doch netz
adr9        gell süsses breutchen.
adr10       ob ich nun am freitag
adr11       kome ist noch nicht sicher
adr12       da ich noch mals nach triberg
adr13       muss.
pic-top     gell du bist mir nicht böse, weil ich dinstag so unartig war.
pic-bottom  sei nun fest geküsst von deinem treuen bubi.
pic-margin  gruss und kuss dein bubi.
```

Reading (four edits against the literal text: hae > ha[b]e, keltet > kältet, netz > nett, breutchen > bräutchen; capitals and part of the punctuation are editorial; the writer's other spellings are kept):

**Libste Rosa: Hast du meine Karte bekomen? Wie get es dir? Bist du wider gesund? Süsser Schatz. Ich ha[b]e mich ein bischen er=kältet und bekome einen kleinen Schnupfen. Macht aber nichts. War doch nett, gell süsses Bräutchen. Ob ich nun am Freitag kome, ist noch nicht sicher, da ich noch mals nach Triberg muss.**

**Gell du bist mir nicht böse, weil ich Dinstag so unartig war.**

**Sei nun fest geküsst von deinem treuen Bubi.**

**Gruss und Kuss dein Bubi.**

English translation: **Dearest Rosa: Did you get my card? How are you? Are you well again? Sweet treasure. I have caught a bit of a cold and am getting a little sniffle. It does not matter, though. It was nice after all, wasn't it, sweet little bride. Whether I shall come on Friday now is not yet certain, as I have to go to Triberg once more.**

**Don't be cross with me, will you, because I was so naughty on Tuesday.**

**Be kissed hard now by your faithful Bubi.**

**A greeting and a kiss, your Bubi.**

Slovak translation: **Najdrahšia Rosa: Dostala si moju pohľadnicu? Ako sa máš? Si už zase zdravá? Sladký poklad. Trochu som sa nachladil a dostávam malú nádchu. To však nevadí. Veď bolo pekne, však, sladká nevestička. Či teraz prídem v piatok, ešte nie je isté, lebo musím ešte raz do Tribergu.**

**Však sa na mňa nehneváš, že som bol v utorok taký nezbedný.**

**Buď teraz pevne pobozkaná od svojho verného Bubiho.**

**Pozdrav a bozk, tvoj Bubi.**

Notes on the reading:

- **gell** is the south German tag "isn't it, right?". The private spellings are consistent and fit a south-west German writer: Libste, wider, Dinstag (dropped e of ie), bekomen, kome (one m), get (no h).
- **Triberg** is the Black Forest town next to Schönwald, today Triberg im Schwarzwald. The Tuesday and Friday fit a card written on Thursday 8 June 1905.
- **er=kältet** is divided over rows adr5 and adr6, with an = sign on the card.

## Reproduction

From the repository root:

```sh
python3 -I ciphers/hcp-1340/work/decode.py
```

The script uses only the standard library and writes no files. It checks the SHA-256 hashes of the four scans, decodes `work/transcription.txt` with `work/key.json`, prints the literal text and then the edited reading, and ends with the sign count (347) and token types (23). Its table can only choose d or t for each 0. The four edits sit in a separate table named on the output. The script does not read the images; the transcription step is manual and was checked in review.

## Uncertainties

- **ha[b]e.** The card has 1, a sign, #, literally "hae". No b sign is there. Treated as a slip of the pen.
- **Z and "nett".** Z rests on two occurrences that do not agree cleanly. Schatz fits z, but adr8 is literally 6 # 0 Z, "netz". The context forces the word "nett", not the key. A faint separate stroke below that sign has no value that could be assigned.
- **P and V** occur once each (Schnupfen, von).
- **R of Rosa.** The two ticks stand between Libste and Rosa. They could belong to the first word ("Libster"); the addressee settles it as Rosa.
- **d/t.** One sign for both; each of the 36 is chosen by the word.
- **muss** (adr13). The second 7 runs through the printed heart emblem. Its stroke stays visible, so it is read, not restored.
- **Bräutchen.** The 0 has a heavily inked left side, with no bar through it; k would give no word. The word is an endearment; whether the pair were engaged is unknown.
- **Order of the picture-side blocks** is assumed; the sense does not depend on it.
- **Persons.** Bubi as Hermann is an inference, and the family name Duffuer or Duffner is open.
- **Earlier publication.** The portal showed Not solved with no attachment, the AI Decipherment Register had no entry for this card on 2026-10-30, and the repository holds no reading of it. No wider web search was made.

## Review summary

Reviewer: a separate Claude Opus 5.5 agent, round 1, verdict **REVISE**. It ran the command, checked the hashes, read every row of both sides at 4x from the originals, the contested signs at 6 to 8x, and decoded its own transcription with its own script (not blind, as it had seen the solver's file). It found 347 signs and the same sixteen blocks; only four words differed, and those were the points below. It tried and failed to refute the key, the transcription and the sense.

Changes because of the review:

- **Libste (major).** The first version printed "Liebste" under the heading "spelling as ciphered", through a word table that added a letter. The card has no e after the i. It now stands as Libste and is disclosed.
- **Decoding table.** It now only chooses d or t, and the editing is a separate, visible step. The literal output therefore shows netz, keltet and breutchen.
- **Left margin.** Corrected from "Liebes" to "Frohes Wiedersehen!" (plain text, not cipher).
- **Gruss and Kuss.** A doubt about the second 7 was withdrawn: the mark is the ordinary crossbar.
- **a/b signs and the blotted 0.** Both now disclosed.

No token of the transcription and no key value changed.

## Sources

- HC Portal record 1340, General, Description and Attachments tabs, captured 2026-10-30: https://crypto.hcportal.eu/dashboard/cryptograms/1340 (source/metadata.md).
- Picture side: https://api.hcportal.eu/media/4080/conversions/pc_hcp_21_pic-large.jpg, original https://api.hcportal.eu/media/4080/pc_hcp_21_pic.JPG
- Address side: https://api.hcportal.eu/media/4081/conversions/pc_hcp_21_adr-large.jpg, original https://api.hcportal.eu/media/4081/pc_hcp_21_adr.JPG
- AI Decipherment Register (https://ai.hcportal.eu/register/), checked by the orchestrator 2026-10-30.
