# hcp-913 – Solution (round 1)

Card: HC Portal cryptogram 913, `cpc_-03-26_DE_Reichen-(Schlesien)_DE_Schneidwitz_fritzlehmann-18`, T. Schrödel collection.
Picture side: printed colour view "Reichenbach i. Schl. – Blick von der Promenade auf das Eulengebirge" (Verlag Rud. Hoefer's Buchhdlg.,
Reichenbach i. Schl., no. 18802); no handwriting on the picture or along its edges (checked on the hi-res scan).
Address side: Germania 5 Pf stamp (still affixed, so nothing under it can be checked), two postmarks REICHENBACH (SCHLES.); the date
reads roughly "26.6.1?" (day 26 clear, month most likely 6, year illegible – the portal file name says "-03-26"; the cherry-picking
invitation fits June better, but the date is not certain). Addressed in plain Kurrent "Herrn Fritz Lehmann, Schweidnitz,
Bögenstraße(?) No. 6" (street read loosely, not part of the cipher). The message is an 18-line ink number block written upside down
(rotated 180 degrees relative to the address) on the left half.

Portal status: Not solved; no transcription or solution attached. Transcription and decipherment are my own (Claude Opus 5.5,
2026-11-03) from the high-resolution scan in work/hires/. No earlier work existed in this directory. No web search for a published
solution was made. The key is the one established on the Lehmann sister cards (reviewed and accepted; FINAL since 2026-11-03) (hcp-1113, hcp-1134, hcp-1044, hcp-1045);
I tested it here and every number decodes under it.

## Cipher type and key

Number substitution (MASC), German. The 25-letter alphabet without J, numbered from 2:

| A | B | C | D | E | F | G | H | I | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |10 |11 |12 |13 |14 |15 |16 |17 |18 |19 |20 |21 |22 |23 |24 |25 |26 |

Dots separate numbers, dashes separate words, a cross "+" ends a sentence (after FRITZ and after HOHENPOSERITZ, i.e. "!").
ß is written SZ. Numbers used: 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 18 19 20 21 22 23 26.
This writer's 5 has a small looped flag on top (looks like a ring); it is the digit 5, not an extra mark (it occurs on DIE, DOCH, KOMME alike).

## Transcription (work/transcription.txt, card rotated 180 degrees)

```
12.10.3.6.18 - [struck 26] 7.18.10.20.26 +
3.10.20.20.6 - 19.6.10 - 5.15.4.9 - 21.15 -
8.15.20 - 21.14.5 - 11.15.13.13.6 -
19.15.14.14.20.2.8 - 13.10.20 - 10.14 -
5.10.6 - 11.10.18.19.4.9.6.14 - 14.2.4.9
9.15.9.6.14.16.15.19.6.18.10.20.26 +
3.10.20.20.6 - 19.4.9.18.6.10.3.6 -
13.10.18 - 15.3 - 5.15 - 11.15.13.13
6.14 - 11.15.13.13.19.20 - 23.21.18.5.6
13.10.4.9 - 19.6.9.18 - 7.18.6.21.6.14 -
5.10.4.9 - 23.10.6.5.6.18 - 26.21 -
19.6.9.6.14 - 21.13 - 23.6.12.4.9.6 -
26.6.10.20 - 10.4.9 - 7.2.9.18.6 - 23.6.10
19.20 - 10.4.9 - 14.15.4.9 - 14.10.4.9.20
23.6.14.14.19 - 8.6.9.20 - 3.10.20.20.6
11.15.13.13.6 5.15.4.9 -
22.10.6.12.6 - 8.13.10".19.26.6 - 22.15.14 -
5.6.10.14.14.6.18 - 6.13.13.2
```

## Command (from the repo root)

```
python3 -I ciphers/hcp-913/work/decode.py
```

It checks the SHA-256 of both source scans and both hi-res originals, then decodes work/transcription.txt literally with the key.

## Plaintext

Literal decode (line by line):
```
LIBER FRITZ ! / BITTE SEI DOCH UO / GOT UND KOMME / SONNTAG MIT IN / DIE KIRSCHEN NACH / HOHENPOSERITZ ! /
BITTE SCHREIBE / MIR OB DO KOMM / EN KOMMST WURDE / MICH SEHR FREUEN / DICH WIEDER ZU / SEHEN UM WELCHE /
ZEIT ICH FAHRE WEI / ST ICH NOCH NICHT / WENNS GEHT BITTE / KOMME DOCH / VIELE GMI"SZE VON / DEINNER EMMA
```

German, normalised (writer's slips corrected, see Uncertainties 1–4): "Lieber Fritz! Bitte sei doch so gut und komme Sonntag mit in
die Kirschen nach Hohenposeritz! Bitte schreibe mir, ob du kommen kannst [lit. 'kommen kommst']. Würde mich sehr freuen, dich wieder
zu sehen. Um welche Zeit ich fahre, weiß ich noch nicht. Wenn's geht, bitte komme doch. Viele Grüße von deiner Emma."

English: "Dear Fritz! Please be so kind as to come along on Sunday to the cherries [cherry picking] in Hohenposeritz! Please write
and tell me whether you are coming. I would be very glad to see you again. I don't know yet what time I am leaving. If it is
possible, please do come. Many greetings from your Emma."

Slovak: "Milý Fritz! Buď taký dobrý a príď v nedeľu so mnou na čerešne do Hohenposeritzu! Prosím, napíš mi, či prídeš. Veľmi by
ma potešilo opäť ťa vidieť. O koľkej pôjdem, ešte neviem. Ak sa dá, príď, prosím. Veľa pozdravov od tvojej Emmy."

Hohenposeritz (today Pożarzysko, Świdnica County, Poland) is a village near Schweidnitz in Silesia (north-east of the town, not on
the road from Reichenbach) – consistent with the postmark and the address.

## Uncertainties

All numbers are read from the pixels; the decode itself is unambiguous. The irregularities are writer's slips, kept literally:

1. "21.15 - 8.15.20" decodes UO GOT, where the sense demands SO GUT (19.15 - 8.21.20). Both numbers are clearly written (work/crops/
   l2end.png); the U and O appear swapped and S replaced. The normalisation "so gut" rests on word sense (the set phrase "sei doch
   so gut und ...").
2. "5.15" decodes DO for DU (clear 15, work/crops/l8.png) – O for U again; "du" by sense.
3. "8.13.10".19.26.6" decodes G M I(") S Z E; the sense is GRÜSZE (8.18.21".19.26.6). 13 and 10 with two ticks are clearly written
   (work/crops/gruesse.png); the two ticks show the writer meant an umlaut vowel. "Grüße" rests on word sense ("Viele ... von deiner
   Emma"). This is the largest slip on the card.
4. Spelling as written: LIBER (lieber), DEINNER (deiner), WEIST (weißt, used for "weiß"), WURDE (no umlaut mark for "würde"),
   "OB DU KOMMEN KOMMST" (a doubled verb, evidently for "kommen kannst").
5. Line 1: a struck-out number before 7 (FRITZ), probably 26, with the correcting 7 written above; not decoded.
6. Line 9 "23.21": the 2 of 21 is ink-blotted; its shape and URDE make 21 certain enough. Line 15 "23.6.14.14.19": the first digit
   of the second 14 is overwritten (work/crops/wenns.png); 14 (WENNS) partly rests on word sense. Line 4 second 14 (SONNTAG) is under
   a brown stain but legible.
7. Stamp still affixed: any writing under it cannot be checked. No other writing was found on either side.
8. "Emma": first name only; identity unknown. Postmark year illegible.

## Why I believe it is correct

The key is the established Lehmann-family key (four sister cards) and here yields 18 lines of coherent German with a concrete,
locally fitting place name (Hohenposeritz) and a signature. Every number on the card is used in the decode; the few deviations are
isolated single-letter slips that leave the sense unambiguous.

## Response to review 1

Verdict ACCEPT, four minor findings; no reading changed.

1. Geography of Hohenposeritz – fixed. The "between Reichenbach and Schweidnitz" wording is replaced by "a village near Schweidnitz
   (today Pożarzysko, Świdnica County), north-east of the town". The argument from context (a Silesian village within reach of both
   Reichenbach and Schweidnitz) is unchanged; the report uses the hedged wording.
2. Date – agreed. The report keeps the date uncertain (day 26 clear, month probably 6, year illegible) and mentions once that the
   portal file name gives "-03-26".
3. Sister-card status – fixed. At review time hcp-1113, 1134, 1044 and 1045 were REVIEWED1 (ACCEPT); all four now carry FINAL. The
   header no longer says "finished" without qualification.
4. The "+" marks – agreed; the report states that "+" is a sentence-end cross written in plain on the card, rendered as "!", and is
   not an enciphered sign.

Additional check (the human's note on the Jolánka series about steganographic writing under stamps): the Germania stamp on this card
is still affixed, set at a slant, and no writing is visible around its edges or through it (review/work/stamp_pm.png); the picture
side has no handwriting. No steganographic part can be shown, so the type stays MASC; what lies under the stamp is unknown.

Reproduction re-run after the edits (2026-11-03): `python3 -I ciphers/hcp-913/work/decode.py` – four hash checks OK, 18 lines
identical to the literal decode above.
