# hcp-1046 – Solution (round 1)

Card: HC Portal cryptogram 1046, `cpc_1909-07-13_DE_-(Schlesien)_DE_Hier_fritzlehmann-04`, T. Schrödel collection.
Picture side: printed photo card "Der Herzensschmied" (a smith hammering a heart, printed verse "Mein Herz ist ganz, o Schmied
dafür Dank ich mein ganzes Leben dir", publisher mark B.N.K., no. 32781/6). No handwriting on the picture side.
Address side: Germania 5 Pf stamp, postmark 13.(7.)09, place name on the postmark not legible on the scan (the file name gives
"...(Schlesien)"; the sister card hcp-1113 is from Freiburg (Schlesien)). Addressed in plain Kurrent:
"An Herrn Fritz Lehmann, Hier, Alte B...hofstraße No 2?, Tischlerm.[eister] H. Franke" (i.e. care of master joiner H. Franke).
The message is two short lines of ink numbers written sideways along the left half.

Portal status: Not solved; no transcription or solution attached. Transcription and decipherment are my own (Claude Opus 5.5),
from the high-resolution scan in work/hires/. No earlier work existed in this directory. One web search (2026-11-03) found no
published solution of this card (the nearest hit, Klausis Krypto Kolumne 2018-11-14, is a different 1909 card in shorthand from
Bartholomäberg). The key is the one established on the sister cards hcp-1113 and hcp-1134 (same recipient Fritz Lehmann, 1909);
I verified it independently here, since every number on this card decodes to a German word under it.

## Cipher type and key

Number substitution (MASC), German. 25-letter alphabet without J, numbered from 2:

| A | B | C | D | E | F | G | H | I | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |10 |11 |12 |13 |14 |15 |16 |17 |18 |19 |20 |21 |22 |23 |24 |25 |26 |

Dots separate numbers, dashes separate words. A word-initial capital is marked by a diagonal stroke across the numeral
(5 and 3 here; 19 on hcp-1113). A double-dot mark over 15 makes it Ö.
Numbers used: 3 4 5 6 9 10 11 12 14 15 18 19 20 21 23.

## Transcription (work/transcription.txt)

```
5x.21. - 11.12.6.10.14.6.18. -
3x.15:.19.6.23.10.4.9.20.
```

## Plaintext

German: DU KLEINER BÖSEWICHT  ->  "Du kleiner Bösewicht!"

English: "You little rascal!" (literally "you little villain")

Slovak: "Ty malý darebák!" (doslova "ty malý zloduch")

The teasing line fits the picture (a lover forging a heart) and the other Lehmann love cards of 1909.

## Command (from repo root)

```
python3 -I ciphers/hcp-1046/work/decode.py
```

It checks the SHA-256 of the two source scans and the hi-res address scan, then decodes work/transcription.txt. Output:
`DU KLEINER BÖSEWICHT`.

## Uncertainties

1. The two word-initial signs (work/crops/msg_a.png). Line 1 begins with a 5 (upright with flat flag and lower bowl) crossed by a
   diagonal stroke; line 2 with a 3 crossed by a diagonal stroke. I read them as 5 = D and 3 = B with the capital marker known from
   hcp-1113. They could also be read as stylised Latin capitals D and B; the plaintext is the same either way. There is no plain 5
   or 3 on this card to compare.
2. Last number of line 2: 20 (T), not 21. In work/crops/cmp21_20.png the second digit is an open looped 0 like the 0 of "10" on
   this card, while the 21 of line 1 ends in a solid 1 stroke. Word sense (BÖSEWICHT) agrees with the pixel reading.
3. The mark over 15 is a small double stroke placed a little above and left of the 15 (between "3." and "15"); I read it as an
   umlaut on 15. Without it the word is "BOSEWICHT", same meaning.
4. No signature or sender. Postmark place not legible on the scan.
5. Unenciphered address: the street name is read only loosely ("Alte B...hofstraße", Kurrent, letters after B uncertain) and the
   house number is 2 followed by an unclear digit (overwritten 1/9). These are address details, not part of the message.
6. Steganography check: stamp box and its margins, picture side (including edges and the printed area) show no hidden writing on
   the scans; what might be under the stamp itself cannot be seen.

## Why I believe it is correct

All 18 numbers decode under one fixed key that was established independently on two sister cards of the same recipient, and they
give a natural three-word German phrase with no leftover signs. The capital-marker stroke matches the convention on hcp-1113.

## Response to review 1

Review 1 (Claude Opus 5.5, separate agent) gave ACCEPT with three minor findings. No decoded letter changes.

1. Faint tilde-like stroke right of the 15 (minor). Agreed. On review/work/z_l2start.png and work/crops/msg.png there is a short,
   very light wavy stroke to the upper right of the 15, before its dot; it is much fainter than the ink of the numbers and has no
   counterpart elsewhere on the card. I take it as a pen trace or touch of the nib, not a sign. Added here as uncertainty 7. If it
   were meant as something, the only plausible role would be a second attempt at the umlaut; the reading BÖSEWICHT is unaffected.
2. House number and street name (minor). Agreed in part. Re-examining review/work/street.png, the number reads "No 29" (a 2 and a
   9, with what may be an earlier 1 under or next to them), so uncertainty 5 now gives "No 29 (possibly corrected)". The street
   name stays unread: it is one Kurrent word, "Alte L/B...hofstraße" or "...ffstraße"; the capital may be the same Kurrent L as on
   sister hcp-1113 ("Alte L...straße"). It is one unread address word, not part of the message.
3. Position of the umlaut (minor). Agreed; the wording in uncertainty 3 was wrong. The double mark stands above the 15 itself
   (slightly left of its centre), as work/crops/msg.png shows.

Corrected uncertainties (supersede items 3 and 5 above; item 7 is new):

3'. The double mark stands directly above the 15 and is read as an umlaut: Ö. Without it the word is BOSEWICHT, same meaning.
5'. Address: house number "No 29", possibly written over a 1; the street name is one unread Kurrent word ("Alte L/B...straße").
7. A very faint short wavy stroke right of the 15 (before its dot) is read as a pen trace, not a sign.

Re-run after the review: `python3 -I ciphers/hcp-1046/work/decode.py` prints `source hashes OK` and `DU KLEINER BÖSEWICHT`.

Steganography: as requested for this batch, the stamp box and its margins and the whole picture side were checked again; no
hidden or extra writing is visible. What may lie under the stamp cannot be seen on the scans. Register type stays MASC.
