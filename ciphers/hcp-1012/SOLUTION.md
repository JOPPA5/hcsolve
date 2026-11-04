# SOLUTION hcp-1012 (cpc_-11-12_DE_Hof_DE_Selb_) - round 1, revised after review 1

Solver: Claude Opus 5.5 (claude-opus-5-5), 2026-11-03. No earlier work exists on this number; no published solution was found or used. The portal attaches no transcription, so the transcription in `work/transcription.txt` is my own, read from the un-converted scans in `work/hires/`.

## The card

Picture postcard, Serie "Liebesträume" (art-nouveau lady with book, printed four-line verse). Address side: "Wohlgeboren / Fräulein Rosa Lang / Selb / Kirchplatz" (Kurrent). Bavarian 5 Pf stamp, postmark Hof 12 NOV (year illegible), arrival Selb 13 NOV. Message in pencil on the picture side, written across the card (rotate the picture side 90 degrees counter-clockwise to read). In that reading orientation a short postscript runs up the left margin (it appears upside down at the top edge of the scan as delivered). German, Kurrent hand.

## Cipher type and key

Number substitution (MASC) mixed with plain Kurrent. Each letter is replaced by its position in the 25-letter alphabet without J, plus 6 (A=7 ... Z=31). Words are written as dot-separated numbers; some words are plain Kurrent, and inside cipher words a few letters are left in plain Kurrent (f, u, nn, ch, h). Ä is written as the cipher number 7 with an umlaut mark above it.

| A | B | C | D | E | F | G | H | I | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | 25 | 26 | 27 | 28 | 29 | 30 | 31 |

Numbers attested on the card: 7 8 11 12 13 14 15 16 17 19 20 23 24 25 26 31 (A B E F G H I K L N O R S T U Z). Every attested number fits the single rule; no number is left over.

Register type: `MASC`. No steganographic message was found (see uncertainty 9).

## Command (from the repo root)

```
python3 -I ciphers/hcp-1012/work/decode.py
```

It checks SHA-256 of both source images and both hi-res originals, then decodes `work/transcription.txt` (numbers through the key, `N^` = number N with an umlaut mark, `{x}` plain letters inside cipher words, `[word]` plain words).

## Transcription (card line by line, reading orientation)

```
8.23.15.12, 11.23.14.7.17.25.11.19, 8: 11.24.25.11.19
Dank für 7.26.f.16.17.7^.23.u.19.13,
Entschuldigen Diese(n?) Karte!
8.23.15.11.12, 12.20.17.13.25, 24.20.nn.25.7.13,
(F) der 19.15.ch.25 11.h.11.23, 31.11.15.25,
der 7.17.17.11 25.7.13.11
Stunden! H. Gruss.   [monogram signature]
(left margin, running upward:) Freundlichst auch ihre(?),
```

## Plaintext (German)

Brif [sic] erhalten, besten Dank für Aufklärung. Entschuldigen [Sie] diese(n?) Karte! Brief folgt Sonntag, der [= da] nicht eher Zeit, der [= da] alle Tage Stunden! H[erzlichen] Gruss. [monogram]
Left margin: Freundlichst auch Ihre(?),

([Sie] is an editorial supply; it is not written on the card.)

## English

Letter received, many thanks for the explanation. [Please] excuse this card! A letter will follow on Sunday, since [I have] no time earlier, since [I have] lessons every day! Warm regards. [monogram]
Margin: two possible readings. (a) "Ihre" (formal, matching the "Sie" form of the card): "Most kindly, also your ..." - a closing formula leading into the monogram (preferred). (b) "ihr(e)" = "her": "Kindest [regards] to her too."

## Slovak

List som dostal(a), srdečná vďaka za vysvetlenie. Prepáčte [mi] túto pohľadnicu! List príde v nedeľu, keďže skôr nemám čas, lebo mám každý deň hodiny! Srdečný pozdrav. [monogram]
Okraj: dve možné čítania. (a) "Ihre": "Najsrdečnejšie, aj Vaša ..." (záverečná formula pred monogramom; preferované). (b) "ihr(e)": "Najsrdečnejšie aj jej."

## Uncertainties

1. First word is 8.23.15.12 = BRIF (no E); the same word later is written in full 8.23.15.11.12 = BRIEF. I report BRIF as written (writer's slip or abbreviation). Dots above some "1" digits on the card are the writer's habit of dotting 1s (seen on 11, 13, 15) and are not read as signs.
2. "8: 11.24..." - the colon after 8 is read as a separator plus a stray dot; 8 + 11.24.25.11.19 = BESTEN.
3. The two plain words before "nicht eher" and before "alle Tage" are read from the pixels as Kurrent "der" (d-loop, then e and r spikes). The sense requires "da" (since); I keep "der" as written and translate as "since". A reading "da" would rest on word sense only. Before the first "der" stands a separate F-shaped mark with two crossbars, detached from the d; it is unexplained (perhaps a false start or correction) and is not read as part of the text.
4. Plain letters inside cipher words: f in AUFKLÄRUNG (crossed Kurrent f), u (with u-bow), nn in SONNTAG (four minims), ch in NICHT, h in EHER. "nn" and "ch" are small glyphs; their reading is supported by the words they complete. The Ä of AUFKLÄRUNG is the cipher number 7 (crossed, as elsewhere for A) with a Kurrent e-shaped umlaut mark above it.
5. "H. Gruss": H. read as an abbreviation of Herzlichen (word sense).
6. Signature: a looped monogram (looks like "Ad." or "Ht."); not resolved, reported as an unread monogram (a single signature item).
7. "Entschuldigen Diese(n?) Karte": the word after Entschuldigen is one word with a looped capital D (Diese + final n or r stroke); "Sie" is not written and is supplied editorially. Whether the final stroke is n or r is open; the meaning does not change.
8. Postscript: "Freundlichst auch ihre" is clear except the end of the last word (ihr / ihre, followed by a comma-like stroke); the two readings are given above. One word, rest reads.
9. The printed verse ("Ich fühle Deinen Odem / Mich überall umwehn / Wohin die Augen schweifen / Wähn ich Dein Bild zu sehn!") is rubbed and partly struck through in pencil. I found no pattern in the strike-outs that forms a message; recorded as observation only. Steganography check: the stamp is affixed and the scan shows no writing around or through it; the picture side and edges were inspected, nothing hidden beyond the margin postscript (plain text). The space under the stamp cannot be inspected from the scan, so a hidden note there cannot be excluded.
10. Year: postmarks do not show a legible year; Bavarian 5 Pf arms stamp suggests about 1900-1910 (unproven).

## Why I believe it is correct

- One arithmetic rule (position in J-less alphabet + 6) explains all 16 distinct numbers on the card; nothing is forced. K=16 next to L=17 in AUFKLÄRUNG confirms that J is omitted.
- Every cipher word decodes to a German word that fits its neighbours: erhalten, besten (Dank), Aufklärung, Brief, folgt, Sonntag, nicht, eher, Zeit, alle, Tage. The same word BRIEF appears twice, and the plain-language parts join seamlessly with the cipher parts.
- The message is a coherent short note typical of the period: thanks for an explanation, excuse for using a postcard, letter promised for Sunday.

## Response to review 1

Verdict REVISE; all five findings accepted and addressed. The decoded cipher text is unchanged.

1. (major) "Sie" not on the card - agreed. On `review/work/a3.jpg` / `diese.jpg` the word after "Entschuldigen" is a single word with a looped capital D. Fixed: `work/transcription.txt` now reads `[Entschuldigen] [Diese(n?)] [Karte] !`; the plaintext marks [Sie] as an editorial supply; new uncertainty 7. The end punctuation is "!" as on the card.
2. (minor) Ä is cipher 7 with an umlaut mark - agreed (`review/work/ae3.jpg`: the crossed 7 with an e-shaped mark above). Fixed: transcription token `7^`; `work/decode.py` now handles `N^` (umlaut on the decoded vowel); uncertainty 4 corrected.
3. (minor) Separate F mark - agreed (`review/work/der1.jpg`). Recorded as `[(F)]` in the transcription and as an unexplained separate mark in uncertainty 3; the "lead-in stroke" wording is withdrawn.
4. (minor) Postscript translation - agreed. Both readings now given in English and Slovak, with "Ihre" (formal closing formula) preferred because the card uses the "Sie" form. Orientation now stated: in reading orientation the line runs up the left margin; upside down at the top only in the scan as delivered.
5. (minor) Register type - agreed: `MASC`. I rechecked the stamp box and the edges of both sides on the hi-res scans for a hidden (steganographic) note, as reported for other series in the collection; nothing is visible, and the area under the stamp cannot be inspected, so `MASC + Steganography` is not supported on this card.

Re-ran `python3 -I ciphers/hcp-1012/work/decode.py` after the fixes: all four hashes OK; output
```
brif , erhalten , besten
Dank für aufklärung ,
Entschuldigen Diese(n?) Karte !
brief , folgt , sonntag ,
(F) der nicht eher , zeit ,
der alle tage
Stunden ! H. Gruss . monogram:unread
Freundlichst auch ihre(?) ,
```
