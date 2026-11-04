# hcp-1201 — Solution (round 1)

Solver: Claude Opus 5.5, 2026-11-03. No earlier work on this number; no portal transcription or solution; no published solution known (no web search made beyond the portal page, which is Not solved).

## What the card actually is

The portal record is named `cpc_1901-03-05_DE_Kiel_DE_Zeitz_hedwigzipfel-13` with recipient Hedwig Zipfel, but the images attached to it (both the large conversions in source/ and the originals in work/hires/, whose file names carry the same label) show a **French** postcard: "Carte postale" (régime intérieur), 5 c. green Type Blanc stamp, postmarks of Parigné-l'Évêque (Sarthe), 24 and 25 June 1907 (`24-6-07`, `25-6-07`). It is addressed to "Mlle Madeleine Vacheron (first letter uncertain, possibly Rocheron), grande-rue, Parigné-l'Évêque, Sarthe". The portal metadata (date, places, recipient) therefore does not describe these images; the decipherment below is of the images. Language: French.

Picture side: three kittens and a stag beetle; no writing in the picture or along the edges. The stamps on both sides are still attached, so the area under them cannot be inspected.

## Cipher type and key

Simple number substitution (MASC with numbers), A=1, B=2 ... V=22, X=23: the numbering runs over a 25-letter alphabet without W (X is 23 instead of 24). Only X shows the missing W; all other values are the plain A=1 count.

| A | C | E | F | I | N | O | R | S | T | U | V | X |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 3 | 5 | 6 | 9 | 14 | 15 | 18 | 19 | 20 | 21 | 22 | 23 |

## Transcription (work/transcription.txt)

```
19-15-21-22-3-14-9-18.
1-6-6-5-3-20-21-5-21-23.
Devine
A. M
```

In line 2 the third and fourth numbers are written "65" with no dash; the pen forms are a normal 6 followed by the same flagged 5 used in "15" and in "21-5-21", so it is read as 6, 5.

## Command

From the repo root:

```
python3 -I ciphers/hcp-1201/work/decode.py
```

It checks the SHA-256 of all four images and prints `SOUVCNIR`, `AFFECTUEUX` and the final reading.

## Plaintext

French: **Souvenir affectueux. Devine. A. M**

English: Affectionate remembrance (fond regards). Guess [who]. A. M.

Slovak: Srdečná spomienka (srdečné pozdravy). Hádaj [kto]. A. M.

"Devine" ("guess") and the initials "A. M" are written in plain letters. The first initial is a script capital that reads as A (M is possible but less likely).

## Uncertainties

1. Line 1, fifth number: it is written with the same looped, descending French "3" as the 3 (= C) in line 2, so it decodes literally to C ("SOUVCNIR"). The word needs E = 5. I read this as the sender's slip (3 written for 5), not as a different key: E is 5 twice in line 2. The plaintext word SOUVENIR is not in doubt, but the digit on the card is 3.
2. X = 23 (alphabet without W) rests on a single occurrence; it could also be a counting slip. Either way the word is AFFECTUEUX.
3. The recipient's surname (Vacheron / Rocheron) and the first initial of the signature are not part of the cipher and are uncertain only in their first letter.
4. Nothing can be said about the area under the two stamps.
5. Portal metadata mismatch, see above.

## Why I believe it is correct

All 18 numbers are decoded by one key; the two lines give the fixed French postcard formula "Souvenir affectueux", which fits a card from Sarthe in 1907, and "Devine" ("guess who") explains why the sender enciphered it. The only departure is the single 3-for-5 slip, disclosed above.

## Response to review 1

Reviewer verdict: ACCEPT, five minor findings. None of them changes the reading. `python3 -I ciphers/hcp-1201/work/decode.py` was re-run on 2026-11-03: all four SHA-256 checks print OK, and the output is still SOUVCNIR / AFFECTUEUX, giving "Souvenir affectueux. / Devine / A. M".

1. **Inverted stamp on the address side.** Agreed. I checked review/work/stamp.jpg and source/address-large.jpg: "POSTES" and "5c" on the 5 c Blanc are upside down. The picture-side stamp is upright. This is a stamp-language gesture (period "langage des timbres": an inverted stamp usually signals affection). It is not a cipher, and it is consistent with "Souvenir affectueux". It is now in the context section of the report and listed below as uncertainty 6.
2. **X = 23.** Agreed. The 25-letter French alphabet without W was the normal school count in 1907, so X = 23 is most likely intended and is not a slip. Uncertainty 2 is restated: the alphabet without W is the preferred explanation, and a counting slip is the less likely alternative. The word is AFFECTUEUX either way.
3. **Steganography under the stamps.** Agreed: the type stays MASC. The human's note (stamp-area hidden messages are common) refers to the Hungarian Jolánka series. This card is a French card from Sarthe and is not part of that series. Both stamps are still attached. At the stamp edges I see no ink traces leading under them (stamp.jpg). The visible text forms a complete closing formula with a signature. No hidden text could be checked, so none is claimed. The report says explicitly that the area under the stamps was not inspected.
4. **Recipient's surname.** Agreed. The second letter looks more like o than a, so "Rocheron" is now given at least equal weight with "Vacheron" (see uncertainty 3). The surname is not part of the cipher.
5. **3 written for 5 in line 1.** Agreed and unchanged: the digit on the card is 3 (= C), and SOUVENIR is a correction by word sense. The decoder prints this explicitly, and the report states it.

Updated uncertainty list (it replaces items 2, 3 and adds 6):
- 2'. X = 23 is most likely the deliberate count without W. A slip is possible but less likely.
- 3'. Recipient: Mlle Madeleine Rocheron or Vacheron (first letters uncertain). Signature initial: most likely A.
- 6. The address-side stamp is mounted upside down (stamp language). Nothing under either stamp could be inspected.

Decision: ACCEPT with all findings addressed and no change to the reading. Report, register entry (type MASC) and FINAL follow.
