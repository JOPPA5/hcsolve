# hcp-1044 – Solution (round 1)

Card: HC Portal cryptogram 1044, `cpc_--___DE_Hier_fritzlehmann-16`, T. Schrödel collection. Undated; no stamp and no postmark
(the stamp box is empty, so nothing can be hidden under a stamp). Addressed in plain Kurrent "Herrn Fritz Lehmann, Hier."
Picture side: printed photo card "Lieb' mich, und die Welt ist mein!" with a four-line verse (publisher KVG 2130/5); no handwriting
seen on the picture side or along its edges. The message is 6 lines of pencil numbers plus a signature, written sideways on the
left half of the address side.
Portal status: Not solved; no transcription or solution attached. Transcription and decipherment are my own (Claude Opus 5.5,
2026-11-03) from the high-resolution scan in work/hires/. No earlier work existed in this directory. One short web search
(2026-11-03, query on "fritzlehmann" / Schrödel / Lehmann cipher postcard) found no published solution of this card; the hits were
Klausis Krypto Kolumne posts about other Schrödel cards. The key is the one used on the Lehmann sister cards hcp-1113, hcp-1134
and hcp-1051 (same recipient; at DONE1 time these were still in review, they have since been closed FINAL); I tested it here on
its own evidence and it decodes every number on the card.

## Cipher type and key

Number substitution (MASC), German. The 25-letter alphabet without J, numbered from 2:

| A | B | C | D | E | F | G | H | I | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |10 |11 |12 |13 |14 |15 |16 |17 |18 |19 |20 |21 |22 |23 |24 |25 |26 |

Dots separate numbers, dashes separate words; ß is written SZ (19.26). Two dots over a number mark an umlaut (2" = Ä).
The bar seen over every 5 (and 15) is just this writer's detached top stroke of the digit 5, not a doubling mark.
Numbers used: 2 3 4 5 6 7 9 10 11 12 13 14 15 16 18 19 20 21 23 26.

## Transcription (work/transcription.txt)

```
2.4.9 - 7.18.10.20.26.6 - 13.2.4.9 - 13.10.18 -
3.12.15.19.26 - 11.6.10.14 - 11.10.14.5 -
5.6.14.14 - 5.21 - 23.6.10.19.26.20 - 23.10.6
13.6.10.14.6 - 6.12.20.6.18.14 - 19.10.14.5 - 13.2.4.9 -
13.10.18.19 - 19.16.2".20.6.18 - 15.5.6.18 - 7.18.14".9.6.18
13.10.20 - 5.6.13 - 2.12.20.6.14 - 14".3.6.18.26.10.6.9.6.14
12.10.6.19.6
```

## Command

```
python3 -I ciphers/hcp-1044/work/decode.py
```
(run from the repo root; checks the SHA-256 of the four source images, then prints the literal decode and a normalised line)

## Plaintext

As decoded:
```
ACH FRITZE MACH MIR / BLOSZ KEIN KIND / DENN DU WEISZT WIE / MEINE ELTERN SIND MACH /
MIRS SPA"TER ODER FRN"HER / MIT DEM ALTEN N"BERZIEHEN / LIESE
```

German, normalised: "Ach Fritze, mach mir bloß kein Kind, denn du weißt, wie meine Eltern sind. Mach mir's später oder früher
mit dem Alten überziehen. Liese." (punctuation and sentence division are mine; the card has none beyond dots and dashes).
Alternative division: "... Mach mir's später oder früher mit dem Alten. Überziehen!" The letters are not in doubt; the division
is editorial.

English: "Oh Fritz, just don't give me a baby, because you know what my parents are like. Do it for me sooner or later with the
old one [the old thing?] pulled over. Liese." (alternative: "... with the old one. Pull it on!"; the exact sense of "später oder
früher" and "mit dem Alten" is unclear)

Slovak: "Ach Fritz, len mi nerob dieťa, veď vieš, akí sú moji rodičia. Urob mi to neskôr alebo skôr s tým starým natiahnutým.
Liese." (alternatíva: "... s tým starým. Natiahnuť!")

The last sentence is literal; "überziehen" (to pull over) and "Überzieher" were period slang for a condom, which fits the
content of the first sentence. Whether "mit dem Alten" means "with the old one" (an object) or something else is interpretation;
the letters themselves are all read.

## Uncertainties

1. Ü written as 14" (N with umlaut) twice: FRÜHER = 7.18.14".9.6.18 and ÜBERZIEHEN = 14".3.6.18.26.10.6.9.6.14. The sign under
   the dots is the same open, crossed "14" as in DENN/KEIN/ELTERN, not the clearly written 21 of DU. I read it as the writer's
   own convention or slip (in Kurrent n and u are the same shape apart from the u-bow), and normalise it to Ü by word sense.
2. Line 5, group 1 = 13.10.18.19 (MIRS): the third number has the closed lower loop of this writer's 18 and the fourth the closed
   upper loop of 19 (enlarged crop work/crops/l5_first.png); the first look suggested 14.14 ("MINN"), which gives no word.
3. Signature 12.10.6.19.6 = LIESE: the fourth number has the closed 9-loop; 14 (LIENE) is the weaker alternative. Name read literally.
4. MEINE: the 14 is overwritten by a heavy blot (correction); a "1" and a crossed 4-shape are visible under it, so 14 is supported
   by the strokes, but the call also rests partly on word sense (MEINE fits; no other value gives a word). MIR (line 1): the 13 is retraced.
   KIND: the final 5 is written very large and retraced; it is still a 5.
5. No sender, date or place on the card; "Hier" = local delivery (Lehmann sister cards are from Schweidnitz/Freiburg in Silesia).

## Why I believe it is correct

One fixed table, taken unchanged from the sister cards, turns every number group on the card into German words that form
connected, grammatical sentences fitting a love-card correspondence with Fritz Lehmann. The only deviation (14" for Ü) is
systematic (twice, same word-initial/inner position as Ü) and disclosed.

## Response to review 1

Verdict ACCEPT, four minor findings; the decoded letters are unchanged.

1. Sister cards called "finished" – fixed. The header now says the key is the one used on sister cards hcp-1113, hcp-1134 and
   hcp-1051, which were in review at DONE1 time and are now FINAL, and that it was tested on this card on its own evidence.
2. Sentence division of lines 5–6 – fixed. The normalised German now gives the one-clause reading ("... mit dem Alten
   überziehen") as primary and the two-sentence division ("... mit dem Alten. Überziehen!") as alternative, both labelled
   editorial; the English and Slovak say that the sense of "später oder früher" and "mit dem Alten" is unclear.
3. MEINE partly by word sense – fixed in Uncertainty 4: the strokes under the blot support 14, but the call also rests on word sense.
4. Web search – done (2026-11-03): one short search on "fritzlehmann" / Schrödel / Lehmann postcard cipher returned only Klausis
   Krypto Kolumne posts about other Schrödel cards; no published solution of this card. Recorded in the header.

Re-checked: the stamp box on the address side is empty and printed only (no stamp, so nothing under it), and the picture side has
no handwriting (re-viewed source/address-large.jpg and source/picture-large.jpg). No steganographic part on this card; type stays MASC.
`python3 -I ciphers/hcp-1044/work/decode.py` re-run after the edits: all four hashes OK, output unchanged.
