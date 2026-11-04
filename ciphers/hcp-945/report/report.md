# HCP 945: "Meine liebe Frieda", a numeral cipher on a Hagen postcard (1898)

Human solver: Tomáš Pavuk

**Status: deciphered in full (52 of 52 cipher signs, 10 German words); independent review 1 verdict ACCEPT, no change to the decoded letters.** Report dated 2026-11-03.

## Origin and context

The cryptogram is record 945 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/945), portal name cpc_1898-04-30_DE_Hagen in Westfalen_DE_Malchow in Mecklenburg_, part of Tobias Schrödel's collection of cryptographic postcards (private collection). When it was captured on 2026-11-03 the portal listed it as **Not solved**, tagged Postcard and T. Schrödel Collection, language Unknown, sender Unknown, recipient Frieda Necker, with no transcription or solution attached.

The card is a coloured lithograph "Gruss aus Hagen i.W." with three views (Bahnhof, Krieger Denkmal, Waldlust), issued by Carl Schemmann, Bahnhofswirth, owner of the Grand-Café-Restaurant Maximilian in Köln; printer Reisinger & Co., Köln. The cipher is written in four ink lines in the lower right of the picture side.

The address side is in plain Kurrent: **Fräulein Frieda Necker in Malchow in Mecklenburg.** It carries a green 5-Pfennig Reichspost stamp cancelled HAGEN (WESTF.) 30.4.98 and an arrival postmark MALCHOW (MECKL.) 1.5.98. The pencil figures "22" and "100" are dealer or collector marks, not cipher.

![Picture side (source/picture-large.jpg)](../source/picture-large.jpg)

![The cipher block, cropped from the hi-res original (work/cipher-block.jpg)](../work/cipher-block.jpg)

![Address side (source/address-large.jpg)](../source/address-large.jpg)

Other marks on the card, none of them cipher: the printed captions, the address, the stamp, the two postmarks, the pencil dealer marks and the HC Portal watermark on both sides. Solver and reviewer both searched the vignettes, the edges and the stamp area and found no other writing. The stamp is still on the card, so nothing beneath it can be checked from the scans.

## Method

The transcription was made by hand, sign by sign, from enlarged crops of the 3469 x 2298 pixel original scan. No OCR was used and the portal supplied no transcription. No published solution of this card was found or used.

The signs are Arabic digits and Roman numerals, each Roman numeral decorated with a bar above and below. A dot on the baseline recurs inside words, so it was taken as i. Then the second word, "L . II 6 II", fits "liebe", and line 1 reads "Meine liebe Frieda", which matches the addressee. Line 4, "V IV . 2 / II V IIII X 4 V", then gives "Dein Eduard", which fixes d, u, a and r. Lines 2 and 3 follow: "Reise heute nach Neheim Hüsten". Two simple hypotheses were tested and rejected first: Roman numerals standing for the vowels, and an A1Z26 number alphabet (d is written V, not IV).

In review a second Claude Opus 5.5 agent made its own crops, wrote its own sign transcription and key, and decoded them with its own script. Its reading agrees with the solver's in all 52 positions.

## Key

Monoalphabetic substitution with two homophones (two signs for e, two for a). The letter i is written as its dot alone. Codes in brackets are those used in work/transcription.txt.

| Sign | Plain | Sign | Plain | Sign | Plain |
|---|---|---|---|---|---|
| barred I (I) | a | barred X (X) | a | 6 | b |
| small c-hook (c) | c | barred V (V) | d | barred II (II) | e |
| barred IV, often an A-shaped ligature (IV) | e | long 7 (F) | f | 8 | h |
| dot on the line (.) | i | long hooked stroke (L) | l | 3 | m |
| 2 | n | 4 | r | small 7-shaped hook (S) | s |
| 1 with flag | t | four strokes under one bar (IIII) | u | the same with diaeresis (IIII:) | ü |

Letters that do not occur on the card (g, k, o, p and others) are unknown. The signs for c, f, l and b occur once each, so their values rest on the words they make.

## Plaintext

Transcription ("/" separates words):

```text
3 IV . 2 IV / L . II 6 II / F 4 . II V I
4 IV . S II / 8 IV IIII 1 II / 2 X c 8
2 IV 8 IV . 3 / 8 IIII: S 1 II 2b
V IV . 2 / II V IIII X 4 V
```

Decoded, line for line:

```text
meine liebe frieda
reise heute nach
neheim hüsten
dein eduard
```

German (capitals and punctuation added): **Meine liebe Frieda! Reise heute nach Neheim Hüsten. Dein Eduard.**

English: My dear Frieda! (I am) travelling today to Neheim and Hüsten. Your Eduard.

Slovak: Moja milá Frieda! Cestujem dnes do Neheimu a Hüstenu. Tvoj Eduard.

Neheim and Hüsten are neighbouring towns on the Ruhr in the Sauerland, about 50 km east of Hagen, where the card was posted. They were merged as Neheim-Hüsten only in 1941; in 1898 they were two places, and the card writes them as two words.

The full plaintext is reproduced from the repository root with:

    python3 -I ciphers/hcp-945/work/decode.py

which checks the hashes of the source images, decodes work/transcription.txt with work/key.json and asserts the result.

## Uncertainties

1. The final n of "Hüsten" (code 2b) is written in a lighter brown ink and looks like a later addition or correction. It completes the word.
2. Homophones: the A-shaped IV ligature, the IV with a separate first stroke and the VI-like second sign of "Neheim" are all read as e. If they are distinct signs, they still mean e.
3. The d in "Frieda" is a heavier, curled V; it is read as the same sign as in "Dein" and "Eduard".
4. The values of c, f, l and b, and the split between s (hook) and t (flagged 1), rest partly on word sense. The two s-hooks differ somewhat in shape, and the one in "Hüsten" is close to the 1 that follows it. Only s then t gives a German word.
5. Nothing can be checked under the stamp. No hidden writing was found elsewhere on the card.
6. Eduard's surname and his relation to Frieda Necker are not on the card.

## Review and what changed

Review 1 (an independent Claude Opus 5.5 agent) returned **ACCEPT** with four minor findings:

1. The second sign of "Neheim" looks more like a barred VI than the IV ligature. Both mean e; this is now stated under uncertainty 2.
2. The s / t split rests partly on context. Uncertainty 4 now says so.
3. The hyphenated form "Neheim-Hüsten" dates only from 1941. The German reading and the translations now give the two names separately, as on the card.
4. The stamp area cannot be checked for hidden writing because the stamp is still on the card. Accepted; the cipher type stays MASC.

No decoded letter changed as a result of the review.

## Credits

Transcription, key reconstruction and decipherment by Claude Opus 5.5 (Anthropic), with an independent review by a separate Claude Opus 5.5 agent. Human solver: Tomáš Pavuk.
