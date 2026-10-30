# HCP 1489 (pc_hcp_170): a null-cipher birthday greeting to Miss A. Stainforth, Hull

Human solver: Tomáš Pavuk

**Status: deciphered (the whole message body; the salutation has one disclosed alternative, and the 22 letters after the last plaintext word are read as nulls); independent review 1 verdict REVISE, disclosure fixed, reading unchanged.** Report dated 2026-10-29.

## Origin and context

The cryptogram is record 1489 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1489), portal name pc_hcp_170, part of the HCPortal collection of cryptographic postcards (private collection). When it was captured on 2026-10-26 the portal listed it as **Not solved**, category Unknown, language Unknown, location Europe, sender Unknown, recipient A. Stainforth, with no transcription or solution attached. No published solution of this card was found.

The picture side is a hand-coloured drawing (signed "Kock") of a young man in Regency dress raising his hat at a garden gate to a lady in a pink crinoline with a parasol; it carries no cipher text.

![Picture side (source/picture-large.jpg)](../source/picture-large.jpg)

The address side is printed "Carte Postale", publisher's line *The "Clifton" Post Cards, E. W. Savory, Ltd., Bristol*. It is addressed in plain handwriting to **Miss A. Stainforth, 61 Hopwood Street, Freehold Street, Hull**, and franked with a ½d Edward VII stamp cancelled by a HULL machine postmark, 8.45 PM, AUG; the year digits are not fully legible, but the stamp dates the card to 1902–1910. On the left half the sender wrote seven lines of printed capitals, signed in cursive (*Jick*) and added printed `LET.` after the signature.

![Address side (source/address-large.jpg)](../source/address-large.jpg)

![The message, turned upright (work/message.jpg)](../work/message.jpg)

Other marks, none of them cipher: the address, the stamp and postmark, the printed headings, small triangle marks with letters and a circled 6 in the corners (most likely collector or dealer annotations), and the HCPortal watermark.

## Method

**Transcription.** The message was read sign by sign from rotated, 5x enlarged crops of every line (work/transcription-v2.json, 144 signs in 7 lines). An earlier transcription by an OpenAI GPT solver (work/transcription.txt) began lines 1, 2 and 3 with an `I`; these are not cipher text (in lines 1 and 2 they are the sideways L and H of the HULL postmark lying over the line starts, in line 3 the end of the printed underline below "Carte Postale") and were dropped. In line 4 the 4th sign is a narrow O and the 13th an overwritten R (GPT had Q for both). The `2` in line 4 is a digit.

**Ruling out the usual systems.** The GPT solver first tried route transpositions (rail fence, grid routes, skips) without result (work/try_routes.py, work/route-results.json). A monoalphabetic hill-climb with English quadgrams gave no English, and the letter frequencies (many V, Y, Q, W, U) look like English diluted with random filler rather than a substitution.

**Null cipher.** The lines contain open English fragments (`BEST`, `AND`, `THUS`, `WI…SH…ES`). Reading them as a null cipher, in which the plaintext letters stand as themselves and in order while meaningless letters are inserted between them, the whole message falls out: the 36 letters WITH LOVE AND BEST WISHES FOR YOUR BIRTHDAY occur in order within 73 consecutive signs, and FROM YOUR within 23. The writer also spaced the line into decoy "words" that cut across the real ones.

**Chance test.** A seeded test (2000 random reorderings of the same 144 signs) asks how often each phrase fits into a window as short as on the card: the long phrase 0/2000, FROM YOUR 0/2000, DEAR 20/2000, NAN 30/2000. The body of the message is therefore not chance.

## Key

There is no substitution alphabet. The key is the set of signal positions (work/key.json): 51 plaintext letters among 144 signs, the other 93 being nulls. Below, CAPITALS are plaintext and lowercase letters are nulls:

| Line | Letters in sequence | Plaintext |
|---|---|---|
| 1 | `sDEolAReuNANvostilar` | DEAR NAN |
| 2 | `ugivWIoTutHvixLOVaiEss` | WITH LOVE |
| 3 | `rANDliBESToviWIroSHdlESoi` | AND BEST WISHES |
| 4 | `vFxOlRzYO2vUReuBjpIRTHus` | FOR YOUR BIRTH- |
| 5 | `oDpArYyyFogROqlMiarn` | -DAY FROM |
| 6 | `wYlyOnnUuvRospioutwtofe` | YOUR |
| 7 | `wriorbbkir` | (nulls) |
| | cursive signature *Jick*; printed `LET.` | signature; `LET.` unexplained |

The card's own spacing (approximate) shows the decoy grouping:

```text
1  S DE OLAR EU NAN VOSTILAR
2  UGIV WI OTU TH VIX LOV AI ESS
3  RAND LI BESTOVI WIROSHDLESOI
4  VFXOLRZYO 2 VUREUBJPIRTHUS
5  ODP ARYYY FOGROQLM IARN
6  WYLY ONNUUVROSPI OUT WTOFE
7  WRIORBB KIR      (signature: Jick)   LET.
```

Where a letter occurs twice in a short span, the key takes the earliest occurrence; this never changes the plaintext.

## Plaintext

English (original): **Dear Nan, with love and best wishes for your birthday, from your Jick.**

Slovak translation: **Milá Nan, s láskou a najlepšími želaniami k narodeninám, tvoj Jick.**

Alternative salutation (see Uncertainties): *Dearest, with love and best wishes for your birthday, from your Jick.* (Slovak: *Najdrahšia, s láskou a najlepšími želaniami k narodeninám, tvoj Jick.*)

"Nan" is the usual pet form of Ann or Annie, matching the addressee Miss A. Stainforth. "Jick" is the cursive signature, written outside the cipher and reported literally.

## Reproduction

From the repository root:

```sh
python3 -I ciphers/hcp-1489/work/decode.py
```

It checks the SHA-256 of the files in source/, applies work/key.json to work/transcription-v2.json, prints each line with plaintext in capitals and nulls in lowercase, asserts that the extracted letters equal the stated words, prints the plaintext and runs the chance test. `python3 -I ciphers/hcp-1489/work/salutation_test.py` runs the comparison of the two salutations.

## Uncertainties

1. **DEAR NAN or DEAREST.** Line 1 `SDEOLAREUNANVOSTILAR` also contains DEAREST (D-E-ol-A-R-E-unanvo-S-T, 7 letters in 15 signs). The two readings exclude each other, since NAN lies between the E and the S-T. In the all-card chance test DEAREST within 15 signs occurs 0/2000 times and NAN within 3 signs 30/2000 times, which favours DEAREST; but that comparison is not like-for-like. A matched test (DEAR kept fixed, the other signs shuffled, looking only at the 9 signs after DEAR, 20000 trials) gives E-S-T in order 1.0 % of the time and N-A-N as an adjacent group 0.04 % of the time. Neither is plausibly chance, so the choice rests on the layout and the address: `NAN` is the writer's own visible group, directly after DEAR, and fits Miss A. Stainforth. DEAR NAN is adopted; DEAREST is a genuine alternative. The rest of the message is the same under both.
2. **The tail.** After FROM YOUR there are 22 more letters (`OSPIOUTWTOFE WRIORBBKIR`) plus printed `LET.` after the signature. No coherent English was found in them (YOURS TRULY does not occur; LOVINGLY occurs only spread over 79 signs). They are read as nulls, with fragments such as OUT, OF, TO probably planted as decoys like THUS and TH. **The words after FROM YOUR are not established**: "from your Jick" assumes the signature completes the sentence. The purpose of `LET.` is unknown.
3. **Signature.** Read *Jick*: a J-form capital with a top loop and long descender, then a clearly dotted i, c, k. The portal record and the earlier GPT notes have "Jack"; the separate dot and the open stroke favour i, but a mis-dotted a cannot be fully excluded, and *Dick* is possible if the writer formed his D this way.
4. **Ambiguous nulls.** Line 1 sign 5 is an L with a stroke (GPT read E); line 4 sign 17 is read J but has a top hook and might be S. Both are nulls either way. Two signal letters in line 4 (O after Y, R after U) are written heavily over other strokes; they are read O and R.
5. **Date.** The postmark year is not fully legible; the ½d Edward VII stamp gives 1902–1910.

## Review summary

An independent reviewer (a separate Claude Opus 5.5 agent) ran the command, decrypted with its own script from its own reading of all seven lines, checked the transcription against 4–7x crops of the scan sign by sign at every signal position, and repeated the chance test with its own seed. It confirmed the body of the message, the dropped postmark letters, the line 4 corrections and the absence of any published solution, and noticed that many signal letters are traced over or written more heavily than the nulls, which supports the choice of positions. Verdict **REVISE**, with one major and four minor findings, all about disclosure:

1. (major) DEAREST was not disclosed as an alternative salutation. Now disclosed, with both statistics and a new like-for-like test (work/salutation_test.py), which shows that the reviewer's comparison overstated the case for DEAREST; DEAR NAN is kept on layout and context.
2. (minor) The dropped `I` at the start of line 3 (the "Carte Postale" underline) was not documented. Now documented.
3. (minor) The signature was "Jack" in the earlier record and *Jick* in the solution without explanation. Now explained.
4. (minor) The status of the tail and `LET.` should be stated plainly. Now stated as not established; the tail count was corrected from 25 to 22.
5. (minor) Cosmetics: a wrong sign count in a script comment and an unclear table header were fixed, and the card's own decoy spacing is now shown.

The plaintext did not change as a result of the review.

## Credit and sources

The card images and portal metadata were captured, a first transcription made and the route-transposition tests run by an OpenAI GPT solver on 2026-10-26 (the exact model version is not recorded in the notes). The revised transcription, the identification of the null cipher, the decipherment and the response to review were done by Claude Opus 5.5 on 2026-10-29/30; the review was done by a separate Claude Opus 5.5 agent. Images: https://api.hcportal.eu/media/4528/conversions/pc_hcp_170_adr-large.jpg and https://api.hcportal.eu/media/4527/conversions/pc_hcp_170_pic-large.jpg (see SOURCES.md).
