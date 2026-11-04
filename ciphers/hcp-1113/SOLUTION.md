# hcp-1113 – Solution (round 1)

Card: HC Portal cryptogram 1113, `cpc_1909-07-30_DE_Freiburg-(Schlesien)_DE_Hier_fritzlehmann-06`, T. Schrödel collection.
Picture side: printed photo card "Gretchen" with the Faust caption "Was ist das? Gott im Himmel! Schau, Ein Schmuck!" (no handwriting).
Address side: Germania 5 Pf stamp, postmark FREIBURG (SCHLESIEN) 30.7.09; addressed in plain Kurrent "Herrn Fritz Lehmann, Hier,
Alte ...straße" (the street name is one unread Kurrent word, see uncertainty 6; it is not part of the cipher). The message is in pencil, written sideways on the left half.
Portal status: Not solved; no transcription or solution attached. Transcription and decipherment are my own (Claude Opus 5.5),
from the high-resolution scan in work/hires/. No earlier work existed in this directory. One web search (2026-11-03) found no
published solution of this card (the closest hit, Klausis Krypto Kolumne 2018-11-28, is a different 1909 card from Newport RI).
The key is the same as on the sister card hcp-1134 (same recipient, same signature "Susi"), which I compared with this card.

## Cipher type and key

Number substitution (MASC), German. The 25-letter alphabet without J, numbered from 2:

| A | B | C | D | E | F | G | H | I | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |10 |11 |12 |13 |14 |15 |16 |17 |18 |19 |20 |21 |22 |23 |24 |25 |26 |

Dots separate numbers, dashes separate words. A bar over a number doubles the letter (13 with bar = MM). The two 19s that begin
nouns (Schatz, Stunde) carry an extra diagonal stroke of unknown purpose (a capital marker or a correction stroke are both possible); they decode as plain 19 = S either way.
Numbers used: 2 3 4 5 6 8 9 10 12 13 14 18 19 20 21 26 – all decode under the one table.

## Transcription (work/transcription.txt)

```
8.6.12.10.6.3.20.6.18.
19x.4.9.2.20.26! -
3.10.14. - 26.21.18. -
3.6.19.20.10.13=.20.6.14.
19x.20.21.14.5.6. -
3.6.10. - 5.10.18.
5.6.10.14.6. -
19.21.19.10.
```

## Plaintext

German: GELIEBTER SCHATZ! BIN ZUR BESTIMMTEN STUNDE BEI DIR. DEINE SUSI

Normalised: "Geliebter Schatz! Bin zur bestimmten Stunde bei dir. Deine Susi."

English: "Beloved darling! I will be with you at the appointed hour. Your Susi."

Slovak: "Milovaný poklad! V dohodnutú hodinu budem u teba. Tvoja Susi."

## Command (from repo root)

```
python3 -I ciphers/hcp-1113/work/decode.py
```

It checks the SHA-256 of both source scans and the hi-res address scan, then decodes work/transcription.txt with the key above.

## Uncertainties

1. First number (G of GELIEBTER): an open S-shaped numeral with a separate top stroke. It does not match this writer's 5 (three 5s on
   the card have a straight upright and a flat flag, see work/crops/cmp5.png), so I read it as an open-written 8. Word sense supports
   it (5 would give "DELIEBTER", not a word); the pixels alone are not fully decisive. There is no other 8 on the card to compare.
2. The two 19s with a crossing diagonal (work/crops/cmp19.png): the underlying 1 and 9 are clear; on the STUNDE one the 9 is faint
   and the diagonal is darker. The stroke appears only at the two noun-initial S; it may be a capital marker or a correction/over-writing
   stroke, and its purpose is unknown. Reading it as a deletion would leave "CHATZ" / "TUNDE", which is impossible, so the 19 stands
   whatever the stroke means.
3. Last number of BESTIMMTEN is 14 with a heavily retraced 1 (overwritten); 13 carries a clear bar = doubled M.
4. Signature "SUSI": a name/nickname; identity unknown (same signature as hcp-1134).
5. Steganography check: the stamp is still affixed, so anything under it cannot be inspected on these scans; no ink traces show at its
   edges. The picture side carries only the printed caption, title "Gretchen" and a publisher number; no handwriting found.
6. Address: the street name after "Alte" (plain Kurrent pencil, crossed by the portal watermark, work/crops/street.png) is not read.
   It begins with L and ends in -straße; the middle letters cannot be read with confidence. It is a single word of the address,
   not of the message.

## Why I believe it is correct

One fixed table (identical to hcp-1134 to the same recipient) decodes all 8 lines (44 numbers) into fluent German with no leftover
signs: a short love note confirming a rendezvous, signed Susi. The doubling bar falls exactly on the MM of BESTIMMTEN, and the
punctuation (! after SCHATZ) fits the salutation. Nothing was adjusted beyond the disclosed reading of the first 8.

## Response to review 1

Verdict ACCEPT, four minor findings. No decoded letter changed.

1. First numeral 8 vs 5 – agreed; the disclosure stays as written (uncertainty 1) and is repeated in the report.
2. Diagonal strokes on the two 19s – agreed. The "capital marker" wording is replaced throughout (key section, uncertainty 2) by
   "purpose unknown: capital marker or correction stroke"; the decoding 19 = S is unaffected.
3. Street name – agreed. Re-examined at 2x on the hi-res scan (work/crops/street.png): "Alte L...straße", the middle letters
   are crossed by the watermark and not legible with confidence. Stated as one unread address word (uncertainty 6), not "read loosely".
4. Register type – agreed: MASC. No steganography was found on this card (stamp affixed with no ink at its edges, picture side
   only printed text); the human's remark about stamp-box messages concerns the Jolánka (Arokszállás) cards, not this one.

Re-ran `python3 -I ciphers/hcp-1113/work/decode.py` after the edits: three hash checks OK, output unchanged
(GELIEBTER SCHATZ! BIN ZUR BESTIMMTEN STUNDE BEI DIR DEINE SUSI).
