# HCP 1201: a French number-cipher postcard, "Souvenir affectueux" (Parigné-l'Évêque, 1907)

Human solver: Tomáš Pavuk

**Status: deciphered in full (18 of 18 numbers); independent review 1 verdict ACCEPT, no change to the reading.** Report dated 2026-11-03.

## Origin and context

The cryptogram is record 1201 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1201). It is part of the T. Schrödel Collection of cryptographic postcards (private collection). Its portal name is cpc_1901-03-05_DE_Kiel_DE_Zeitz_hedwigzipfel-13. When captured on 2026-11-03 the portal listed it as **Not solved**, language Unknown, sender Unknown, recipient Hedwig Zipfel, with no transcription or solution attached.

**The portal metadata does not match the images.** The name and the recipient describe a card from Kiel to Zeitz to Hedwig Zipfel, dated 1901. The two images attached to the record (both the large conversions and the originals, whose file names carry the same label) show a **French** postcard instead. It is a "Carte postale" for the "régime intérieur" with a green 5 c Type Blanc stamp. The postmarks are PARIGNÉ-L'ÉVÊQUE / SARTHE, 24-6-07 and 25-6-07, i.e. 24 and 25 June 1907. This report deciphers the images as served. The mismatch is probably a mix-up on the portal side.

The address is in plain writing: "Mlle Madeleine Rocheron (or Vacheron), grande-rue, Parigné-l'Évêque, Sarthe". The card was posted and delivered within the same small town. The correspondence field holds two lines of numbers separated by dashes. Below them, in plain script, are "Devine" ("guess [who]") and the initials "A. M".

The address-side stamp is mounted **upside down**. In the period "language of stamps" an inverted stamp was a deliberate signal, usually of affection. That fits the text, but it is not a cipher. The stamp on the picture side is upright. The picture side shows three kittens, a fence and a stag beetle. Neither solver nor reviewer found any writing in the picture, along the edges or in the margins. **Both stamps are still attached, so the area under them could not be inspected.** No ink traces lead under their edges.

![Address side: two number lines, "Devine", "A. M"; inverted 5 c Blanc stamp at top right (../source/address-large.jpg)](../source/address-large.jpg)

![Picture side: kittens and a stag beetle, no writing (../source/picture-large.jpg)](../source/picture-large.jpg)

## Method

The solver (Claude Opus 5.5) read the numbers by hand from enlarged crops of the full-resolution original (work/hires/). No OCR was used. Two places needed care. First, the fifth group in both lines is a looped, descending French "3". It is distinct from the card's 5s, which carry a flat top flag. Second, the "65" in line 2 is written without a dash, but it consists of a normal 6 and a flagged 5. The last group of line 2 is 23, not 29: its second digit has the bulge of a 3, not the straight stem of a 9.

With values from 1 to 23 and small numbers dominating, a direct alphabet count was the obvious first test, and it gave French at once. The script work/decode.py checks the SHA-256 of the images and decodes the transcription.

```
python3 -I ciphers/hcp-1201/work/decode.py
```

The reviewer made its own crops, read all 18 numbers independently (identical to the solver's reading), and decoded them with its own script.

## Key

This is a simple number substitution: each letter is replaced by its position in the alphabet. The count runs over the **25-letter French alphabet without W**, which was the usual school alphabet in 1907. As a result X is 23 rather than 24. All other letters used on the card have their plain A=1 values.

| A | C | E | F | I | N | O | R | S | T | U | V | X |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 3 | 5 | 6 | 9 | 14 | 15 | 18 | 19 | 20 | 21 | 22 | 23 |

## Plaintext

Ciphertext and literal decoding:

```
19-15-21-22-3-14-9-18.        -> S O U V C N I R   (3 written for 5)
1-6-6-5-3-20-21-5-21-23.      -> A F F E C T U E U X
Devine                         (plain)
A. M                           (plain)
```

French: **Souvenir affectueux. Devine. A. M**

English: Affectionate remembrance (fond regards). Guess [who]. A. M.

Slovak: Srdečná spomienka (srdečné pozdravy). Hádaj [kto]. A. M.

"Souvenir affectueux" is a standard French postcard closing formula of the period. "Devine" with only initials is a teasing anonymous signature, which explains why the sender enciphered the text.

## Uncertainties

1. **Line 1, fifth number.** The pen clearly wrote 3 (= C), the same form as the 3 in line 2. The word needs E (= 5), which is used twice correctly in line 2. The reading SOUVENIR is therefore a correction by word sense of a sender's slip. It is not what the digit says.
2. **X = 23** rests on one occurrence. The count without W is the most likely explanation; a counting slip is possible but less likely. The word is AFFECTUEUX either way.
3. **Names (plain text, not cipher).** The recipient's surname is Rocheron or Vacheron, with the first letters uncertain. The first initial of the signature is most likely A; M is less likely.
4. **Under the stamps.** Nothing can be said about what is under the two attached stamps. No hidden writing was seen anywhere on the visible card, so the type is given as MASC, not MASC + Steganography.
5. **Portal metadata.** The metadata (Kiel to Zeitz, 1901, Hedwig Zipfel) does not describe these images.
6. **Published solution.** None is attached on the portal. No wider web search was made.

## Review and what changed

An independent Claude Opus 5.5 reviewer re-ran the command, transcribed all 18 numbers from its own enlargements, decoded them with its own script, and checked both sides of the card. Verdict: **ACCEPT**, with five minor findings:

1. Note the inverted address-side stamp. It has been added to the context and uncertainties.
2. Present X = 23 as the deliberate French count without W rather than as an equal-weight slip. Done.
3. Keep the type MASC and state that nothing under the stamps could be inspected. Done.
4. Give "Rocheron" at least equal weight with "Vacheron". Done.
5. Keep the 3-for-5 slip clearly disclosed. Kept.

None of the findings changed the decoded text.
