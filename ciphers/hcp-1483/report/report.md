# HCP 1483 (pc_hcp_164): an English love letter to Colwyn Bay, February 1908

Human solver: Tomáš Pavuk

**Status: deciphered in full (468 of 468 cipher signs mapped by one key); independent review 1 verdict ACCEPT, no change to the decoded letters.** Report dated 2026-10-29.

## Origin and context

The cryptogram is record 1483 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1483), portal name pc_hcp_164, part of the HCPortal collection of cryptographic postcards (private collection). When it was captured on 2026-10-26 the portal listed it as **Not solved**, category Substitution, date 1908-02-11, language Unknown, location Europe, sender Unknown, recipient "J.Willams", with no transcription or solution attached.

The card is a British comic postcard of the "Pictorial Comedy" series. The picture shows a golf scene captioned "Is a caddie always necessary?" and carries no cipher writing. The cipher text fills the message half of the address side. The address is in plain writing and reads, as far as the scan shows, **Miss G. (or J.) Williams, "Baronhill", York Road, Colwyn Bay, N. Wales**. The card bears a green Edwardian halfpenny stamp postmarked **FE 11 08** (11 February 1908). The address side is scanned upside down relative to the message; the working copy below is turned by 180°. The large lettered wheel across the card is the HCPortal watermark, not part of the cipher.

![Address side, turned 180° so that the cipher text reads upright (work/upright.jpg)](../work/upright.jpg)

![Picture side: "Is a caddie always necessary?" (source/picture-large.jpg)](../source/picture-large.jpg)

Two further cards in the portal, HCP 1484 and HCP 1485, have the same addressee and the same kind of signs. They have not yet been solved in this repository, and the key below has not yet been tried on them.

## Method

An OpenAI GPT solver (GPT-6 Astra / GPT-6.1 Sol) downloaded the files on 2026-10-26, made the upright working copy and recorded the metadata; it did not establish a key or plaintext. Claude Opus 5.5 then did the transcription and decipherment (2026-10-29/30).

**Transcription.** The text was read sign by sign from enlarged crops (10x, and 12–16x for doubtful signs) and recorded as feature tokens in `work/transcription.txt`: 468 enciphered letters, including the postscript and the signature. No OCR was used.

**Recognising the system.** There are two classes of sign. Most are a vertical stem with one to three short bars, placed on the left, on the right or crossing the stem, either in the upper part (stem hanging below) or in the lower part (stem rising above). That gives 3 × 3 × 2 = 18 shapes, exactly the number of English consonants from B to W once X and Z are left out. The remaining signs are six closed shapes (circle with a dot, triangle, square and variants): the vowels and Y.

**Cribs.** The card itself gives one in plain writing. The postscript ends with "Does this interest you" in ordinary handwriting, followed by cipher signs and a question mark that fit AT ALL SWEETHEART. The frequent three-sign group ⊥∃Δ fitted THE, and the postscript then read ... HAS BEEN KISSED!!! These few words showed that the consonants are assigned **in alphabetical order** over side × position × number of bars. With this rule every other line decoded on the first pass into continuous English.

**Review.** The reviewer wrote its own decoder, which does not read the key file but rebuilds the key from the stated rule alone, and got the same text on all 20 lines. The key follows from a simple rule and was not tuned sign by sign, so fluent English across the whole card is strong evidence that it is right.

## Key

Monoalphabetic substitution (MASC) with a home-made, systematic alphabet. Words are not separated and ordinary punctuation is kept. A small "2" after a sign doubles the letter.

Consonants (t = bars in the upper part, b = bars in the lower part; 1–3 = number of bars):

| bars | 1t | 2t | 3t | 1b | 2b | 3b |
|---|---|---|---|---|---|---|
| left of stem | B | C | D | F | G | H |
| right of stem | J* | K | L | M | N | P |
| crossing stem | Q | R | S | T | V | W |

Vowels and Y:

| sign | letter |
|---|---|
| circle or oval with central dot | A |
| triangle | E |
| triangle with inner vertical stroke | I |
| square | O |
| square with a diagonal | U |
| square with a Y-shaped pair of strokes | Y |

\* J never occurs on this card; its slot is inferred from the alphabetical rule only. Q is attested twice (QUICK, QUITE), both times consistently. X and Z do not occur and have no sign here. The other 17 consonant signs and all six vowel signs do occur. The most frequent signs are E and O (43 each), T (39) and A (34), as expected for English.

## Plaintext

Literal decode, line by line as on the card (the postscript stands at the top). Words in lower case are in plain writing. `^T` marks a T written above the line with a caret, and `[?]` is an extra sign.

```text
P1   P.S. THES^TAMP ON THIS CARD FAS BEEN KISSED!!!
P2   Does this interest you AT ALL SWEETHEART?
L01  MY OWN CARIAD,THANK YOU SO
L02  MUCH FOR THE CARD.I KNOW YOU WILL
L03  CONSIDER ME AN.UNTHANKFUL BEAST
L04  FOR NOT HAVING EVEN ACKNOWLEDGED
L05  RECEIPT OF THE "MIONEER"! THANK
L06  YOU VERY MUCH FOR YOUR DEAR
L07  THOUGHTFULNESS, DARLING. I LOVE
L08  YOU SWEETHEART MINE, MORE THAN
L09  I DID YESTERDAY BUT NOT SO MUCH
L10  AS I SHALL LOVE YOU TOMOROW!
L11  I AM SO GLAD TO HEAR THAT YOU
L12  ARE STILL GETTING BETTER. BE QUICK
L13  AND GET QUITE ALL RIGHT, DARLING.
L14  MY COLD SEEMS TO HAVE GONE
L15  COM[?]PLETELY. I WOULD NOT SWOL
L16  WITH MISTER KAY FOR
L17  FORTY WORLDS. KISS ME GOONIGHT, DARLING
SIG  a.m. [script capital, R?] "YOUR BOY"
```

**Normalised English** (the letter is already in English, so this is also its translation):

> My own cariad, thank you so much for the card. I know you will consider me an unthankful beast for not having even acknowledged receipt of the "Pioneer"! Thank you very much for your dear thoughtfulness, darling. I love you, sweetheart mine, more than I did yesterday but not so much as I shall love you tomorrow! I am so glad to hear that you are still getting better. Be quick and get quite all right, darling. My cold seems to have gone completely. I would not swop with Mister Kay for forty worlds. Kiss me good night, darling. — a.m. R(?) "Your boy"
>
> P.S. This stamp on this card has been kissed!!! Does this interest you at all, sweetheart?

"Cariad" is Welsh for "darling, love", which fits a card sent to Colwyn Bay in North Wales.

**Slovak translation:**

> Môj vlastný cariad (miláčik), veľmi pekne ďakujem za pohľadnicu. Viem, že ma budeš považovať za nevďačné zviera, lebo som ani nepotvrdil, že mi prišiel „Pioneer“! Veľmi pekne ďakujem za tvoju milú pozornosť, miláčik. Ľúbim ťa, moja zlatá, viac ako včera, ale nie tak veľmi, ako ťa budem ľúbiť zajtra! Som veľmi rád, že počujem, že sa ti stále zlepšuje. Rýchlo sa úplne uzdrav, miláčik. Moja nádcha už asi úplne prešla. Nevymenil by som sa s pánom Kayom ani za štyridsať svetov. Pobozkaj ma na dobrú noc, miláčik. — „Tvoj chlapec“.
>
> P.S. Známka na tejto pohľadnici bola pobozkaná!!! Zaujíma ťa to vôbec, zlatko?

## Reproduction

From the repository root:

```sh
python3 -I ciphers/hcp-1483/work/decode.py
```

The script uses only the Python standard library. It checks the SHA-256 hashes of the three files in `source/`, decodes `work/transcription.txt` with `work/key.json` and stops on any unknown token. It prints the twenty lines above, followed by `-- source hashes OK; 468 enciphered letters decoded, all signs mapped`. It does not read the image: the transcription step is manual and was checked against the scan in review.

## Uncertainties

- **Writer's slips.** The decode keeps these literally and the normalised text corrects them:
  - **THES^TAMP.** The writer first wrote THESTAMP, with one S serving both "this" and "stamp", then squeezed in a T above the line with a caret. The first triangle shows no inner stroke on this scan, so it decodes as E (THES); the intended word is THIS.
  - **FAS** for HAS: a single-bar left sign (F) where three low left bars (H) are expected.
  - **MIONEER** for PIONEER: the sign is clearly M. The same line writes a proper P in RECEIPT, so this is a slip, not a misreading.
  - **TOMOROW** is written with one R, and **GOONIGHT** without D (the sign after OO is clearly N).
  - **SWOL** stands where SWOP ("swap") is expected. The last sign of line 15 is partly covered by the printed margin text; its bars look high (L) rather than low (P).
- **Extra sign in COM[?]PLETELY:** a slanted stem with three crossing bars and an ink blot between M and P, probably a false start.
- **Bar counts.** Each sign is about 10 px high on the 1024-px scan, so two and three bars can look alike. All count-critical signs were rechecked at 12–16x. A few blurred or covered signs (R in CARIAD and DEAR, W in TOMOROW, Y in FORTY, some I triangles under the printed vertical line) were read with help from the word.
- **Signature.** "a.m." and a script capital (perhaps R) are in plain writing. The quoted cipher word is small and cramped: O, B, O and the final Y are clear, while the first Y, the U and the R are probable. "YOUR BOY" is therefore a probable reading.
- **Other marks.** The dot in AN.UNTHANKFUL is a stray dot or separator. The triple underline under "I" (line 15) and the double underline under "MISTER KAY" are emphasis, not cipher.
- **Addressee.** The capital before "Williams" is cut off at the scan edge and may be G or J (the portal gives "J.Willams"). The street is York Road; an early triage note in `source/metadata.md` that says "Oak Road" is a misreading.
- **The J slot** of the key is inferred, not observed (see Key).
- **Identities.** The sender ("your boy"), "Mister Kay" and the "Pioneer" (probably a periodical) are not identified.

## Review summary

Reviewer: a separate Claude Opus 5.5 agent, round 1, verdict **ACCEPT**. The reviewer:

- ran the reproduction command; the output was identical to the claimed plaintext;
- decoded the transcription with its own script, which rebuilds the key from the stated alphabetical rule without reading the key file, and got the same text on all 20 lines;
- checked the postscript, lines 1, 2, 5, 11–13, 15 and 17 and the signature sign by sign on its own 3–7x crops of the scan;
- confirmed the writer's slips (FAS, MIONEER, GOONIGHT), the extra sign in COMPLETELY and the address.

Its four findings were minor, and all were addressed:

1. **Oak Road vs York Road.** The triage note was wrong. This is now recorded in the notes, and York Road is used throughout.
2. **Recipient initial.** The addressee is now given as G. (or J.).
3. **J and Q slots.** The key file and this report now say that J is inferred from the rule and that Q is attested only twice.
4. **THES^TAMP.** Explained above.

No decoded letter changed as a result of the review.

## Sources

- HC Portal record 1483, General, Description and Attachments tabs, captured 2026-10-26: https://crypto.hcportal.eu/dashboard/cryptograms/1483 (source/metadata.md).
- Address side: https://api.hcportal.eu/media/4510/conversions/pc_hcp_164_adr-large.jpg (source/address-large.jpg).
- Picture side: https://api.hcportal.eu/media/4509/conversions/pc_hcp_164_pic-large.jpg (source/picture-large.jpg).
- No published solution of this card was found or used. The AI Decipherment Register (https://ai.hcportal.eu/register/) had no entry for it on 2026-10-29.
