# HCP 914: a "spell-it-out" name-grid postcard from Linz to Kremsmünster (1900)

Human solver: Tomáš Pavuk

**Status: read in full (12 of 12 name positions, 4 of 4 place positions); independent review 1 verdict ACCEPT, no change to the reading.** Report dated 2026-11-03.

## Origin and context

The cryptogram is record 914 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/914), portal name cpc_1900-06-25_AT_Linz_AT_Kremsmunster_, part of Tobias Schrödel's collection of cryptographic postcards (private collection; the portal links the HistoCrypt article https://ecp.ep.liu.se/index.php/histocrypt/article/view/166). When it was captured on 2026-11-03 the portal listed it as **Not solved**, language Unknown, sender Unknown, recipient Käthe Mayrhöfer, with no transcription or solution attached. A short web search found no published solution of this card.

The address side is written in German Kurrent: **Wolgeboren Fräulein Käthi Mayrhofer in Kremsmünster, Herrnstrasse** ("Miss Käthi Mayrhofer, Herrnstrasse, Kremsmünster", Upper Austria). It carries an Austrian 5-heller Franz Joseph stamp, still attached, with a partial duplex cancellation, and an arrival postmark KREMSMÜNSTER 25 6. The portal's file name gives the date 1900-06-25 and the route Linz to Kremsmünster (about 35 km).

The picture side is a printed commercial puzzle card, "Herzlichen Gruss aus der Ferne sendet ..." ("Cordial greetings from afar are sent by ..."), printed by Fritz Schemm, Kunstanstalt, Nürnberg, and marked "Gesetzlich geschützt" (registered design). It carries a short printed verse, a printed explanation ("Erklärung") with a worked example, and two grids of Fraktur letters, one headed "Name des Absenders" (sender's name) and one headed "Ort" (place). The sender fills in the grids by hand.

![Picture side: the printed name grid, the "Ort" grid and the explanation column (source/picture-large.jpg)](../source/picture-large.jpg)

![Address side: Käthi Mayrhofer, Kremsmünster (source/address-large.jpg)](../source/address-large.jpg)

This is not a secret cipher with a private key. The rule is printed on the card itself, and the "secret" is only a little puzzle for the recipient, as the verse says: to learn who sent the card, she must "begin spelling".

## Method

The printed explanation shows how the grid works: under each printed letter the sender writes the position (or positions) that letter takes in the name. The printed example is filled in for "Carl Meier": A 2, C 1, E 6 and 8, J 7, L 4, M 5, R 3 and 9. Writing the letters in the order of their numbers gives CARLMEIER.

Cryptographically this is a transposition: the letters of the name are given in alphabetical order, and the handwritten numbers give their true order. The grid has one cell for I/J (Fraktur J), one cell for the trigraph Sch, and separate cells for Ä, Ö and Ü.

The handwritten numbers were read from the full-resolution scan (3410 x 2265 pixels) with enlarged crops, cell by cell across both grids. A small script (work/decode.py) checks the hashes of the source images, checks that the positions form a complete run with no gap or duplicate, and prints the result. The reviewer read all cells again independently from its own crops, built its own decoder, and also decoded the printed "Carl Meier" example with it to confirm the rule.

Reproduction, from the repository root:

    python3 -I ciphers/hcp-914/work/decode.py

Output: `source hashes OK`, `name_des_absenders: LOUISEKALUSCHA`, `ort: LINZ`.

## Key (the filled-in grids)

Name des Absenders (all other cells empty, including B C D F G H M N P Q R T V W X Y Z Ä Ö Ü):

| Letter | A | E | I/J | K | L | O | S | Sch | U |
|---|---|---|---|---|---|---|---|---|---|
| Positions | 8, 12 | 6 | 4 | 7 | 1, 9 | 2 | 5 | 11 | 3, 10 |

Ort (all other cells empty):

| Letter | I/J | L | N | Z |
|---|---|---|---|---|
| Positions | 2 | 1 | 3 | 4 |

The positions run exactly 1 to 12 and 1 to 4 with no gap and no duplicate, which is an internal check of the transcription.

## Plaintext and translation

Name: L O U I S E K A L U SCH A, giving **Louise Kaluscha**

Place: L I N Z, giving **Linz**

Full message with the printed heading (German): **"Herzlichen Gruss aus der Ferne sendet Louise Kaluscha, Linz."**

English: "Louise Kaluscha [from] Linz sends cordial greetings from afar."

Slovak: "Srdečný pozdrav z diaľky posiela Louise Kaluscha, Linz."

The printed verse (not ciphertext): "In der Ferne hab' ich Deiner gedacht, / Beweis soll die Karte hier bringen, / Doch willst Du wissen wer sie Dir gebracht, / Musst mit dem Buchstabieren beginnen."

English: "Far away I thought of you; this card shall be the proof; but if you want to know who sent it, you must begin by spelling."

Slovak: "V diaľke som na teba myslel(a); dôkazom nech je táto karta; ak však chceš vedieť, kto ti ju poslal, musíš začať hláskovať."

## What remains uncertain

- I or J: the grid has one I/J cell; I is chosen by word sense in both fields (Louise, Linz).
- The word division Louise | Kaluscha is by sense; the grid has no space. "Kaluscha" is a plausible Germanised spelling of the Slavic surname Kaluža; it cannot be checked against outside records.
- Digit shapes: the 7 under K has a hooked stroke and the 1s under L have a flag; both read clearly, and the complete 1 to 12 sequence confirms them.
- In the Ort grid, cells C and D (and the edge of E) show faint grey specks and short strokes. They are much lighter than the real numbers, form no digit shape and look like ink set-off or smudging; they are not read as numbers. The Ort positions are complete without them.
- The stamp is still on the card, so nothing can be said about the area under it. No hidden or extra writing was found anywhere else on either side (picture, edges, explanation column). The card is therefore not labelled as steganography. The pencil "25 €" at the bottom right is a modern dealer's price.
- Linz as the place of posting rests on the deciphered "Ort", the portal's file name and fragments of a partial cancellation, not on a clean postmark.

## Review and what changed

An independent reviewer (a separate Claude Opus 5.5 agent) ran the reproduction command, re-read every cell of both grids from its own enlargements of the full-resolution scan, decoded them with its own script, and confirmed the reading rule with the printed "Carl Meier" example. Its reading agreed in every cell. Verdict: **ACCEPT**.

The review made four minor points: (1) the faint specks in the Ort grid should be mentioned; (2) the stamp area cannot be checked and the card should not be labelled "+ Steganography"; (3) the report should say plainly that this is a commercial puzzle card with a printed rule and no secret key; (4) the surname and word division rest on sense. All four are now stated in this report. The decoded name and place did not change.

## Credits

Transcription and decipherment by Claude Opus 5.5 (Anthropic), 2026-11-03; independent review by a separate Claude Opus 5.5 agent. Human solver: Tomáš Pavuk. Source images: HC Portal, T. Schrödel collection.
