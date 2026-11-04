# hcp-1045 – Solution (round 1)

Card: HC Portal cryptogram 1045, `cpc_1909-10-12_DE_-(Schlesien)_DE_Hier_fritzlehmann-09`, T. Schrödel collection.
Picture side: printed photo card "Gretchen" (Faust caption "Nach ihm nur schau' ich zum Fenster hinaus, / Nach ihm nur geh' ich aus
dem Haus.", publisher no. 4034-6); no handwriting on it. Address side: Germania 5 Pf stamp, postmark ...(SCHLESIEN) 12.10.09; addressed in
plain Kurrent "An Herrn Fritz Lehmann, Hier, Alte ...straße" (street name not part of the cipher; tentative reading "Alte
Landschaftstraße"). The message is a pencil
number block written sideways on the left half, plus a three-line note squeezed diagonally into the top-left corner of the block.
Portal status: Not solved; no transcription or solution attached. Transcription and decipherment are my own (Claude Opus 5.5) from the
high-resolution scan in work/hires/. No earlier work existed in this directory. One web search (2026-11-03) found no published
solution of this card. The key is the one used on the sister cards hcp-1113 and hcp-1134 (same recipient, same signature "Susi"; both were still in review
when this card was handed over and are FINAL since 2026-11-03); the key stands on this card alone, since it fits every number here.

## Cipher type and key

Number substitution (MASC), German. 25-letter alphabet without J, numbered from 2:

| A | B | C | D | E | F | G | H | I | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |10 |11 |12 |13 |14 |15 |16 |17 |18 |19 |20 |21 |22 |23 |24 |25 |26 |

Dots separate numbers, dashes separate words. Double tick = umlaut (2" = Ä, 21" = Ü); the Ü of ÜBER is not marked and is supplied
by word sense (notation 21^). Bar over a number = doubled letter (14 with bar
= NN). A darker diagonal cross stroke over the first number of a noun/name (7 F of Fritz and Freude, 11 K of Karte, 8 G of Gezanke,
Gesundheit, Gruß) marks a capital, as on hcp-1113; it does not change the letter. ß is written SZ. `!` and `?` are written as plain
punctuation (the `?` marks in darker pencil). Numbers used: 2 3 5 6 7 8 9 10 11 12 13 14 15 18 19 20 21 23 26 – all decode under the
one table.

## Transcription (work/transcription.txt)

```
[corner note]  23.15. - 3.10.19.20. - 5.21. - 9.6.21.20 ?
12.10.6.3.6.18. 7x.18.10.20.26. !
6.3.6.14. - 5.6.10.6.14.6. - 11x.2.18.
20.6. - 6.18.9.2.12.20.6.14. - 21^x.3.6.18.
23.2.19. - 10.19.20. - 5.6.14=. - 5.2|19.26. -
7.21".18. - 6.10.14. - 7.15.18.20.23.2".18.
6.14.5.6.19. - 8x.6.26.2.14.11.6. ?
10.19.20. - 5.2.19. - 5.10.6. -
7x.18.6.21.5.6. - 2.21.7. - 13.6.10.
14.6. - 8x.6.19.21.14.5.9.6|10.20. ?
13.10.20. - 8x.18.21.19.26. -
19.21.19.10.
```

## Plaintext

German, as written:
WO BIST DU HEUT? – LIEBER FRITZ! EBEN DEIENE KARTE ERHALTEN. ÜBER WAS IST DENN DASZ FÜR EIN FORTWÄRENDES GEZANKE? IST DAS DIE
FREUDE AUF MEINE GESUNDHEIT? MIT GRUSZ SUSI

Normalised: "Lieber Fritz! Eben deine Karte erhalten. Über was ist denn das für ein fortwährendes Gezanke? Ist das die Freude auf meine
Gesundheit? Mit Gruß, Susi. – Wo bist du heut?"

English: "Dear Fritz! Just received your card. What is all this constant bickering about? Is that the joy over my health?
With greetings, Susi. – Where are you today?"

Slovak: "Milý Fritz! Práve som dostala tvoj lístok. O čom je to ustavičné hašterenie? To je tá radosť z môjho zdravia? S pozdravom
Susi. – Kde si dnes?"

"Freude auf meine Gesundheit" echoes the toast formula "auf meine Gesundheit" ("to my health"), so the question may be ironic:
"Is that how you celebrate / drink to my health?" (Slovak: "To je tá oslava / pripíjanie na moje zdravie?"). The neutral rendering
above is kept; the alternative is noted.

The corner note "WO BIST DU HEUT?" is written above the first line in the free corner; it may be a postscript or a heading – its
position in the reading order is not certain, its text is.

## Command (from repo root)

```
python3 -I ciphers/hcp-1045/work/decode.py
```

It checks the SHA-256 of both source scans and of the hi-res address scan, then decodes work/transcription.txt with the key above.

## Uncertainties

1. DASZ (line 4): the digits read 5 . 2 1 9 . 2 6 with no dot inside "219" (crop work/crops/w_dasz.png). Only the split 2|19 gives a
   word (D-A-S-Z, "daß" written for "das" in "was ist denn das für ein..."); 21|9 would give DUHZ. The split rests on word sense; the
   digits themselves are clear.
2. MIT (line 10, first number): the sign has a long 1-stroke with a small looped foot like the foot of this writer's 2, so it could be
   23 overwritten to 13 or a 13 with a flourish (comparison work/crops/cmp_23_13.png, next to a clean 23 in WAS). 13 = M gives MIT
   GRUSZ; 23 would give "WIT". M rests partly on word sense.
3. DEIENE (line 2): clearly 5.6.10.6.14.6 (work/crops/w_deine.png) – an extra E, a writer's slip for DEINE, kept as written.
4. HEUT (corner note): the last number runs to the card's left edge; the 2 is clear, the 0 joined to it is faint
   (work/crops/heut3.png). 20 = T makes HEUT; nothing else fits after HEU. Treat as a near-restoration of one letter.
5. Ü of ÜBER: not marked on the card. The 21 of ÜBER stands at the end of line 3 and is overwritten in darker pencil, with no ticks over
   it. The double tick at the far right between lines 2 and 3 stands after KAR (end of line 2, above the final 18 of ÜBER) and is
   best read as the Kurrent double hyphen dividing KAR-TE. The literal reading is UBER; Ü rests on word sense (notation 21^).
6. The `?` after GEZANKE and after GESUNDHEIT are dark marks that resemble a 2 over a dash (GEZANKE) or a smudged hook with a dot
   (GESUNDHEIT); I take them as question marks, like the clear `?.` closing the corner note, because a trailing A would make no word.
7. FORTWÄRENDES is written without H (fortwährendes) – the writer's spelling. The last 18 of FORTWÄR is partly on the printed
   "Levelező" text but readable.
8. A separate dark pencil cross on the printed "Cartões Postaes / Briefkaart" line carries no number and is not part of the message.
9. Steganography check: the picture side has no handwriting beyond the printed caption. The stamp is still affixed, so anything under it
   cannot be inspected on these scans; no ink or pencil traces show at the stamp edges.
10. "Susi" is a nickname; identity unknown.

## Why I believe it is correct

One fixed table, the same as on two sister cards to the same man signed by the same Susi, decodes all 11 lines and the corner note
(about 90 numbers) into fluent colloquial German without any adjustment of the key; the only interventions are two missing separator
dots (DASZ 2|19, GESUNDHEIT 6|10), one ambiguous overwritten numeral and one unmarked umlaut (ÜBER), all disclosed. Umlaut
ticks fall on Ä/Ü exactly where German needs them (für, fortwährendes), the bar falls on the double N of DENN, and the capital crosses fall on nouns and the name. The content (a reply to his card,
complaining about constant quarrelling, signed Susi) fits the love-letter correspondence of hcp-1113 and hcp-1134.

## Response to review 1

Verdict ACCEPT, five minor findings; none changes the decoded text. `python3 -I ciphers/hcp-1045/work/decode.py` was re-run after the
changes: all three SHA-256 checks OK, output identical to round 1.

1. ÜBER umlaut misdescribed – agreed and fixed. On review/work/uber2.png and the full block the double tick stands at the right end
   of line 2, directly after the 18 of KAR, and the word continues as TE on line 3. I now read it as the Kurrent word-division mark
   (double hyphen) for KAR-TE. The 21 of ÜBER carries no ticks. Uncertainty 5 is rewritten, the transcription now writes 21^x (new
   notation: umlaut supplied by word sense), decode.py accepts ^, and the key paragraph says so. Literal reading UBER; meaning unchanged.
2. Second missing separator – agreed and fixed. GESUNDHEIT is written 9.610.20 on the card; the transcription now writes 9.6|10.20
   and "Why I believe it is correct" names both missing dots (DASZ and GESUNDHEIT).
3. "Freude auf meine Gesundheit" – agreed. The English now reads "the joy over my health" (neutral), and the ironic toast reading
   ("is that how you drink to my health?") is given as an alternative in English and Slovak.
4. Street name – tentative reading added: "Alte Landschaftstraße" (Kurrent, only partly legible under the portal watermark). It is a
   single word of the plain address, not part of the message; marked tentative.
5. Sister-card status – wording fixed: the key is "the same as on" hcp-1113 and hcp-1134, which have since reached FINAL; the claim
   of correctness rests on this card's own decryption.

Steganography (the human's remark about stamp-box messages on the Jolánka cards): checked again for this card. The stamp is still
affixed and shows no pencil at its edges; the picture side carries only print. No hidden message is visible on the scans, so the
type stays MASC (number substitution); the underside of the stamp remains unverifiable.
