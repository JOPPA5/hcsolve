# HCP 1278 (cpc_1912--27_HU__HU_Jasz Arokszalas_jolanka-103): a consoling card to Jolánka Tóth

Human solver: Tomáš Pavuk

**Status: the message is deciphered in full. Review 1 verdict REVISE; all findings addressed, one letter corrected (it improved the reading), no word of the normalized Hungarian changed. The signature, read as Holes F., is the weakest part.** Report dated 2026-11-01.

## Origin and context

The cryptogram is record 1278 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1278), part of Tobias Schrödel's collection of cryptographic postcards (private collection). When it was captured on 2026-11-01 the portal listed it as **Not solved**, tagged Postcard, T. Schrödel Collection, category Substitution, language Unknown, location Europe, sender Unknown, recipient Tóth Jolánka, with no transcription or solution attached. No published solution of this card was found or used.

The address, in plain writing, reads Szépreményű Tóth Jolánka kisasszonynak, Jász Árokszálás: Miss Jolánka Tóth, at Jászárokszállás in Hungary. A postmark shows ÁROKSZÁ…, 912 and 27, with the month illegible. The portal's file name also gives 1912 and day 27. A second cancellation rings the stamp box, with letters like G and V or Y and a date band; it was seen but not read, so the place of writing is unknown.

The picture side shows a kissing couple with a printed love verse (Hulló falevél … Sárgult falevél … Ajkam ajkadat érintve … Nem szól; csak szivem beszél.). That matters for the text: the writer apologizes for sending such a card in sad days.

The cipher stands in 17 rows of red ink on the left of the address side. The stamp has been lifted, and the stamp box holds a plain, unenciphered greeting that was hidden under it (steganography, checked again on 2026-11-03): Csókolom a távolból ("I kiss you from afar"), whose first letter lies under a pink blot and is restored.

The card belongs to a large family of postcards to Jolánka Tóth in one cipher, several of which are finished in this repository (for example HCP 1212, 1213, 1216, 1217, 1218, 1243, 1301). The key was transferred from those cards, so this is a **known, transferred key**, not a new key recovery. That family work was done by the OpenAI GPT solver and by Claude Opus 5.5.

![Picture side (source/picture-large.jpg)](../source/picture-large.jpg)

![Address side, with the cipher rows and the stamp-box greeting (source/address-large.jpg)](../source/address-large.jpg)

## Method

The transcription is manual: the 17 rows were cropped from the portal's high-resolution address scan, enlarged and read sign by sign into a ledger with one token per written sign. The family key was then applied by a small script. The reading was not blind, since the key and the wording of sister cards were known. Doubtful signs were compared with other occurrences on this card and with the ink profile of the row.

Hungarian word division, accents and spelling are editorial. The cipher writes no spaces, and this writer often uses single for double consonants (keten for ketten, ithon for itthon) and ij for ily.

## Key

Register type: **MASC + Steganography** (changed 2026-11-03). The cipher is a simple monoalphabetic substitution with invented graphic signs, and a plain greeting was hidden under the stamp. Names of signs are conventional descriptions of handwritten shapes.

| sign | letter | sign | letter | sign | letter |
|---|---|---|---|---|---|
| two bars | a | section mark / S / 8 shape | k | F-like | r |
| six | b | wave | l | right bowl | s |
| left bowl, often with a bar | c | three short strokes | m | gamma/corner | t |
| short stroke left + long stroke | d | two short strokes | n | plain cross x | u |
| three bars | e | cursive loop, arched arm | o | chevron | v |
| open C with a tail at the foot | g | tall stroke + tick on the right (high h, low p) | h / p | crossed diagonal | z |
| same loop, straight arm, dot above | i | inverted T | j | C + y joined | gy |

Dots over o and u give ö and ü. No sign for f occurs with certainty. y and cs occur only as parts of gy and as c + s.

## Plaintext

Literal decipherment, row by row. Square brackets mark overwritten or blotted signs, `{blot}` a blot with no letter value, and `{r=F.}` a sign whose keyed value is r but which is read as the initial F.

```text
01 kedvesjolankatuda
02 tomhogyszerencse
03 se{blot}nmegerkeztem.
04 azútelegrövid
05 voltmivelhogy
06 ketenvoltunkhogy
07 telnekmostaniszo
08 morunapjaivig{blot}
09 gasztalodjonedesjo
10 lankamezenmarse
11 giteninemlehet.
12 nezelhogyijszomo
13 runapokbaeztalapot
14 küldökdenincsitho[n]mas
15 [ü][d]vözlömatavolbol
16 [h]oles{r=F.}tisztelemazot
17 maradtakat
```

Row 9 prints edes because the sign was taken as d from word sense; its form is that of h/p.

**Hungarian (normalized).** Kedves Jolánka! Tudatom, hogy szerencsésen megérkeztem. Az út elég rövid volt, mivel hogy ketten voltunk. Hogy telnek mostani szomorú napjai? Vigasztalódjon, édes Jolánkám! Ezen már segíteni nem lehet. Nézze el, hogy ily szomorú napokba[n] ezt a lapot küldöm, de nincs itthon más. Üdvözlöm a távolból. [H]oles [F.] Tisztelem az ott maradtakat.

Stamp box, plain: Csókolom a távolból.

**English.** Dear Jolánka! I am letting you know that I arrived safely. The journey was short enough, since there were two of us. How are your present sad days passing? Be comforted, my sweet Jolánka! This can no longer be helped. Forgive me for sending this card in such sad days, but there is no other in the house. I greet you from afar. [H]oles [F.] My respects to those who stayed there.

In the stamp box: I kiss you from afar.

**Slovak.** Milá Jolánka! Oznamujem Vám, že som šťastne docestoval. Cesta bola dosť krátka, keďže sme boli dvaja. Ako plynú Vaše terajšie smutné dni? Utešte sa, sladká moja Jolánka! Tomu sa už pomôcť nedá. Prepáčte, že v takých smutných dňoch posielam túto pohľadnicu, ale doma nemám inú. Pozdravujem Vás z diaľky. [H]oles [F.] Moju úctu tým, čo tam zostali.

V poli na známku: Bozkávam Vás z diaľky.

## What remains uncertain

- **Signature.** The first sign of row 16 is blotted and could be d, h, p or n, so this card alone gives only `[?]oles`. Holes comes from HCP 1303 (plain Holes Fe…, capital uncertain) and HCP 1309 (holesferi, first letter open), which support each other but are not independent proof. The last sign has the form of r; the family's f is a different sign. Reading it as a Latin initial F. is an interpretation, and a link with the "Feri" of other cards is suggested, not proved.
- **Row 15, üd.** Heavily overinked, but the visible X and strokes match ü + d of row 14, and üdvözlöm is the only word found. Of the two dots over the first ö, one is a free blob and the other looks like the foot of a sign in row 14, so that ö rests on the word.
- **Signs resting on word sense.** The n of itthon (row 14, overwritten, #-like); the d of édes (row 9, h/p shape); the m of mostani (row 7, three strokes and a stray tick); the m of maradtakat (row 17, short third stroke under foxing specks). The h/p split also rests on the word, with the low tick a real tendency on this card.
- **Blots with no letter value.** Rows 3 and 8. The words around them need no letter there. The gy of hogy in row 2 is also blotted, but the word is certain.
- **Editorial normalizations.** nezel → nézze el ("forgive"; nézel, "you look", would break the formal address); ij → ily; napokba → napokba[n]; küldök → küldöm (the k is clear; the object is definite); azot → az ott. The mark over the u of út is probably an accent; many free marks stand on the card.
- **Not resolved.** A heavily overinked group after "bol" at the end of the stamp greeting (taken as a retrace of the ending), two small pen marks in the stamp box, the month, the second postmark, the cause of the "sad days", and who the second traveller in ketten was.

## Why the reading is accepted

The family key, unchanged, turns all 17 rows into natural period Hungarian. Long stretches read with no choice, among them Tudatom, hogy szerencsésen megérkeztem, which also stands on HCP 1243 and 1310. hogy decodes the same way four times and szomorú twice, and a távolból of row 15 repeats the plain greeting in the stamp box. The apology for sending a love-picture card in sad days fits the picture side, which is a check independent of the key.

## Reproduction

From the repository root:

```sh
python3 -I ciphers/hcp-1278/work/decode_opus.py
```

The script checks the SHA-256 of the two source scans and the two high-resolution originals, decodes the manual ledger `work/ledger-opus.txt`, and prints the literal rows and the normalized text. It does not read the image; the transcription step is manual.

## Review summary

Reviewer: a separate Claude Opus 5.5 agent, round 1, verdict **REVISE**. The reviewer ran the command, made its own crops, read the card into its own ledger of 264 signs and decoded it with a separate key table. This was not blind, so it is a check on the pixels and not an independent discovery. Fifteen of 17 rows agreed. Its findings and what changed:

- **Row 13 (major).** The sign after ezt has two bars, not three. It is a, not e, and the solver's note was wrong. The literal row is now …eztalapot, so ezt a lapot stands as written.
- **Signature (minor).** The last sign now shows its keyed value in the literal output, F. is marked as read, the first sign's class is stated as open, and the status line names the signature as the weakest part.
- **Row 15 (minor).** The description now reports the visible strokes instead of calling the place unreadable.
- **Other notes (minor).** Added or corrected: the m of row 17, the blot in row 2, the sentence point of row 11, the dot over row 15's ö, the likely ú, the restored first letter in the stamp box, the second postmark, and a clear separation of küldök (written) from küldöm (editorial).

No word of the normalized Hungarian changed; the only literal letter corrected is the one in row 13. The transcription, decipherment, response to review and this report were made by Claude Opus 5.5.

## Sources

- HC Portal record 1278, all tabs, captured 2026-11-01: https://crypto.hcportal.eu/dashboard/cryptograms/1278 (source/metadata.md).
- Picture side: https://api.hcportal.eu/media/3894/conversions/cpc_1912--27_HU__HU_Jasz-Arokszalas_jolanka-103_pic-large.jpg (source/picture-large.jpg).
- Address side: https://api.hcportal.eu/media/3895/conversions/cpc_1912--27_HU__HU_Jasz-Arokszalas_jolanka-103_adr-large.jpg (source/address-large.jpg).
- High-resolution originals: https://api.hcportal.eu/media/3894/cpc_1912--27_HU__HU_Jasz-Arokszalas_jolanka-103_pic.jpg and https://api.hcportal.eu/media/3895/cpc_1912--27_HU__HU_Jasz-Arokszalas_jolanka-103_adr.jpg (work/hires/).
- Family key and sister cards: ciphers/hcp-1216 and the other Jolánka cards named above in this repository.
- Attachment cited on the portal: https://ecp.ep.liu.se/index.php/histocrypt/article/view/166
