# hcp-951 – Solution (round 1)

Solver: Claude Opus 5.5 (claude-opus-5-5), 2026-11-03. No earlier work exists on this number; nothing published was found (short web search, 2026-11-03: no hit for Hugo Dunkel / Stürzbach / this card). The portal attaches no transcription or solution; the transcription below is my own, read from `work/hires/cpc_1940-01-05_DE__DE_Sturzbach__adr.jpg` (enlarged crops in `work/crops/`).

Card: picture postcard "Döbeln – Bürgergarten mit Blick auf die Kaserne", 6 Pf Hindenburg stamp (Deutsches Reich), slogan cancel "Vermeidet Rundfunk-Störungen!", portal date 1940-01-05. Addressed to Herrn Hugo Dunkel, Stürzbach, Thüringer Wald. German, Kurrent hand.

## Cipher type and key

Number substitution, A=1, B=2 … Z=26 (a monoalphabetic substitution; register label MASC). Commas separate letters; a comma with a short downward tick marks the end of a word. Umlaut ö is written as plain O (4,15,2,5,12,14 = DOBELN for Döbeln) and ß as a single S (STRASE). The house number 19 is written as a plain number and is not enciphered.

No steganography found: the picture side carries no writing (contrast-enhanced crops `work/crops/pictop.png`, `picbot.png`); the stamp could not be lifted, so nothing under it can be checked.

## Transcription (ciphertext, all of it)

```
9,12,19,5, 19,3,8,23,1,18,26,5
4,15,2,5,12,14
2,18,5,9,20,5,
19,20,18,1,19,5, 14,18, 19
```

## Plaintext

Decoded: `ILSE SCHWARZE / DOBELN / BREITE / STRASE NR 19`
Normalised German: Ilse Schwarze, Döbeln, Breitestraße Nr. 19
English: Ilse Schwarze, Döbeln, Breite Street no. 19 (the sender's name and address).
Slovak: Ilse Schwarze, Döbeln, Breitestraße (Široká ulica) č. 19.

### Whole card (plain parts included)

Ink, sender (Kurrent):
"Viele Grüße von hier, sendet Ihnen wohl bekannt, doch rätselhaft genannt." [cipher block] "Noch alles Gute zum Jahreswechsel."
EN: "Many greetings from here, sent to you by one well known, yet called puzzling. [name and address] All the best for the turn of the year."
SK: "Veľa pozdravov odtiaľto vám posiela dobre známa, no záhadná nazvaná. [meno a adresa] Ešte všetko dobré k prelomu roka."

Ink, middle of card, plain (looks like the decoded address written out, perhaps by the recipient): "Ilse Schwarze / Döbeln i/S [= in Sachsen] / Breitestr. 19". It confirms the decryption independently.

Pencil, bottom edge, a different, later remark: "Kennst du das/die […]fräulein [aus] Döbeln? !?" – "Do you know the […] young lady (from) Döbeln?" / SK "Poznáš tú […] slečnu (z) Döbelnu?". The first half of one compound word (perhaps "Probe-" or "Post-") is unread (see below).

Address: "Herrn Hugo Dunkel, Stürzbach, Thüringer Wald". "Stürzbach" is written clearly; the place meant is almost certainly Stützerbach in the Thuringian Forest (no locality "Stürzbach" is attested there), so the spelling is the writer's.

## Command

From the repo root:

```
python3 -I ciphers/hcp-951/work/decode.py
```

It checks the SHA-256 of all four source images and decodes `work/transcription.txt` with the A=1..Z=26 key. Output: `ILSE SCHWARZE / DOBELN / BREITE / STRASE NR 19`.

## Uncertainties

1. Line 1 ends "1,18265" with no commas between 18, 26 and 5; split by spacing. 18,26,5 = RZE is the only split giving a word (1,82,65 is impossible).
2. Line 3 first sign is a looped "2" (B); compared with the "2" in "2,5" on line 2 it fits, but "9" (I → IREITE) is the alternative; B rests partly on word sense and on the plain "Breitestr." note.
3. "3,8" in line 1: the 8 is drawn open, like "&"; read 8 = H (SCH).
4. The final "19" is taken as a literal house number (decoding it gives S, "Nr. S"); the plain note says "Breitestr. 19".
5. Plain ink note: the surname is written "Schwarze" followed by a long flourish or strike-through that runs into the ruled line; the letters after "z" could be read as "-emann" struck out. The cipher fixes the name as SCHWARZE.
6. Pencil note: the compound word after the article ends clearly in "-fräulein" (ä with two dots, then u-l-e-i-n); its first part (p with long descender, r/o, a looped letter: "Probe-" or "Post-" are possible) is unread. The article ("das"/"die") is half covered by an ink descender from the line above. It is a later remark in pencil, not part of the sender's message; only this one half-word is unread.
7. The stamp area could not be inspected underneath.
8. Faint marks above the slogan cancel and left of the stamp (hires scan roughly x 2140–2200 and 2600–2750, y 60–420): a pale N-like and v-like stroke and a short diagonal stroke beside the perforation. On enhanced crops they form no letters or digits; they look like ink transfer or stray marks, not a hidden message.

## Why I believe it is correct

- Every number decodes under the trivial A=1..Z=26 key with no exceptions, to a name, a town and a street: 100% coverage of the 30 enciphered numbers.
- The town (Döbeln, Saxony) matches the picture side and the plain note "Döbeln i/S"; the plain note "Ilse Schwarze / Döbeln i/S / Breitestr. 19" on the card matches the decryption word for word.
- The text frames it: "sent by one well known, yet called puzzling" – the sender hides her name and address in numbers.

## Response to review 1

Review 1 verdict: ACCEPT, four minor findings. All addressed; the decoded text is unchanged. Reproduction command re-run on 2026-11-03: all four SHA-256 checks OK, output `ILSE SCHWARZE / DOBELN / BREITE / STRASE NR 19`.

1. Pencil word (minor) – fixed. I agree with the reviewer's crop (`review/work/pencil_word.png`): the word ends in "-fräulein" with a dotted ä. The pencil line is now given as "Kennst du das/die […]fräulein [aus] Döbeln? !?" with only the first half of the compound ("Probe-"/"Post-"?) unread (Plaintext and Uncertainty 6).
2. Destination town (minor) – fixed. Added a note that "Stürzbach" is the writer's spelling and the place meant is almost certainly Stützerbach, Thuringian Forest.
3. Faint violet marks (minor) – fixed. Made my own autocontrast crop of the hires scan (x 1900–2800, y 0–450): a pale N-like and v-like stroke and a diagonal stroke by the perforation, no letters or digits. Added as Uncertainty 8.
4. Register type (minor) – agreed. No steganographic text was found on either side (the stamp cannot be lifted), so the type is MASC, not "MASC + Steganography".
